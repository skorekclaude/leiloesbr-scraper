#!/usr/bin/env python3
"""
PAI System Monitor — Real-time dashboard for Personal AI Assistant.

Shows: PM2 processes, smart-checkins state, recent logs, agent sessions,
memory stats, cron jobs, and system health.

Usage:
    python pai_monitor.py              # start on port 8090
    python pai_monitor.py --port 9000  # custom port
"""

import os
import sys
import json
import subprocess
import argparse
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

# Fix encoding
import io
if sys.stdout and sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============================================================
# CONFIG
# ============================================================
PM2_LOGS_DIR = os.path.expanduser("~/.pm2/logs")
CHECKINS_STATE = os.path.expanduser("~/.claude-relay/checkins-state.json")
SESSION_FILE = os.path.expanduser("~/.claude-relay/session.json")
MEMORY_DIR = os.path.expanduser("~/.pai/memory")
CHECKINS_HEALTH_URL = "http://127.0.0.1:3001/health"
NPX_CMD = "npx"

# ============================================================
# DATA COLLECTION
# ============================================================

def get_pm2_processes():
    """Get PM2 process info from pid files + single tasklist call (fast)."""
    pm2_pids_dir = os.path.expanduser("~/.pm2/pids")
    processes = []
    if not os.path.exists(pm2_pids_dir):
        return [{"error": "No PM2 pids directory"}]

    # Collect all PIDs first
    pid_entries = []
    for fname in os.listdir(pm2_pids_dir):
        if not fname.endswith(".pid"):
            continue
        name = fname.rsplit("-", 1)[0]
        pid_path = os.path.join(pm2_pids_dir, fname)
        try:
            with open(pid_path, "r") as f:
                pid = int(f.read().strip())
            pid_entries.append((name, pid, pid_path))
        except:
            processes.append({"name": name, "pid": 0, "status": "unknown", "cpu": 0, "memory_mb": 0, "restarts": 0, "uptime_ms": 0})

    if not pid_entries:
        return processes or [{"error": "No PM2 pid files found"}]

    # Single tasklist call to check all processes at once
    running_pids = {}  # pid -> memory_mb
    needed_pids = {pid for _, pid, _ in pid_entries}
    try:
        result = subprocess.run(
            ["tasklist", "/FO", "CSV", "/NH"],
            capture_output=True, timeout=5, encoding="utf-8", errors="replace"
        )
        import re
        for line in result.stdout.strip().split("\n"):
            parts = line.split('"')
            if len(parts) >= 10:
                try:
                    line_pid = int(parts[3].strip())
                except:
                    continue
                if line_pid not in needed_pids:
                    continue
                # Memory is in parts[9]: e.g. "206\xa0736 K" or "164 804 K"
                mem_str = parts[9] if len(parts) > 9 else ""
                # Remove all non-digit characters except for "K" marker
                mem_digits = re.sub(r'[^\d]', '', mem_str)
                mem_mb = 0
                if mem_digits:
                    try:
                        mem_mb = round(int(mem_digits) / 1024, 1)
                    except:
                        pass
                running_pids[line_pid] = mem_mb
    except:
        pass

    for name, pid, pid_path in pid_entries:
        status = "online" if pid in running_pids else "stopped"
        memory_mb = running_pids.get(pid, 0)

        # Get uptime from pid file mtime
        try:
            mtime = os.path.getmtime(pid_path)
            uptime_ms = (datetime.now().timestamp() - mtime) * 1000
        except:
            uptime_ms = 0

        processes.append({
            "name": name,
            "pid": pid,
            "status": status,
            "cpu": 0,
            "memory_mb": memory_mb,
            "restarts": 0,
            "uptime_ms": uptime_ms,
        })

    return processes


def get_checkins_state():
    """Read smart-checkins state file."""
    try:
        with open(CHECKINS_STATE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"error": "Cannot read checkins state"}


def get_checkins_health():
    """Query smart-checkins /health endpoint (fast, 2s timeout)."""
    import urllib.request
    try:
        req = urllib.request.urlopen(CHECKINS_HEALTH_URL, timeout=2)
        return json.loads(req.read().decode())
    except Exception:
        return {"status": "unreachable"}


def get_session():
    """Read Claude Code session state."""
    try:
        with open(SESSION_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"error": "Cannot read session"}


def get_logs(service, lines=40):
    """Get last N lines from PM2 logs."""
    log_file = os.path.join(PM2_LOGS_DIR, f"{service}-out.log")
    err_file = os.path.join(PM2_LOGS_DIR, f"{service}-error.log")
    result = {"out": [], "err": []}

    for key, path in [("out", log_file), ("err", err_file)]:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                all_lines = f.readlines()
                result[key] = [l.rstrip() for l in all_lines[-lines:]]
        except:
            result[key] = []
    return result


def get_memory_stats():
    """Get PAI memory file stats."""
    stats = {}
    for fname in ["MEMORY.md", "GOALS.md"]:
        path = os.path.join(MEMORY_DIR, fname)
        if os.path.exists(path):
            size = os.path.getsize(path)
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            line_count = content.count("\n")
            stats[fname] = {"size_bytes": size, "lines": line_count}
        else:
            stats[fname] = {"size_bytes": 0, "lines": 0}

    # Daily log — check today (Warsaw time = UTC+1) and yesterday
    import time
    utc_offset = 1  # CET (or 2 for CEST)
    local_hour = (datetime.utcnow().hour + utc_offset) % 24
    today = datetime.now().strftime("%Y-%m-%d")
    daily_path = os.path.join(MEMORY_DIR, "daily", f"{today}.md")
    if not os.path.exists(daily_path):
        # Try yesterday (might be just past midnight UTC but still same day in Warsaw)
        from datetime import timedelta
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        alt_path = os.path.join(MEMORY_DIR, "daily", f"{yesterday}.md")
        if os.path.exists(alt_path):
            daily_path = alt_path
            today = yesterday

    if os.path.exists(daily_path):
        size = os.path.getsize(daily_path)
        with open(daily_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
            entries = content.count("\n- ")
        stats["daily_log"] = {"size_bytes": size, "entries": entries, "date": today}
    else:
        stats["daily_log"] = {"size_bytes": 0, "entries": 0, "date": today}

    return stats


_ram_cache = {"data": None, "ts": 0}

def get_system_ram():
    """Get system RAM: total, used, free, top consumers. Cached for 10s."""
    import re, time
    now = time.time()

    # Cache for 10 seconds (PowerShell calls are slow)
    if _ram_cache["data"] and (now - _ram_cache["ts"]) < 10:
        return _ram_cache["data"]

    ram = {"total_mb": 0, "used_mb": 0, "free_mb": 0, "percent": 0, "top_processes": []}

    # Get total/free RAM via PowerShell (one call, faster)
    try:
        r = subprocess.run(
            ["powershell", "-NoProfile", "-Command",
             "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory.ToString() + '|' + (Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory.ToString()"],
            capture_output=True, timeout=10, encoding="utf-8", errors="replace"
        )
        parts = r.stdout.strip().split("|")
        if len(parts) == 2 and parts[0].strip() and parts[1].strip():
            total_bytes = int(re.sub(r'[^\d]', '', parts[0]))
            free_kb = int(re.sub(r'[^\d]', '', parts[1]))
            ram["total_mb"] = round(total_bytes / (1024 * 1024))
            ram["free_mb"] = round(free_kb / 1024)
            ram["used_mb"] = ram["total_mb"] - ram["free_mb"]
            if ram["total_mb"] > 0:
                ram["percent"] = round(ram["used_mb"] / ram["total_mb"] * 100, 1)
    except Exception as e:
        print(f"[RAM] PowerShell error: {e}")

    # Top memory consumers from tasklist
    try:
        result = subprocess.run(
            ["tasklist", "/FO", "CSV", "/NH"],
            capture_output=True, timeout=5, encoding="utf-8", errors="replace"
        )
        proc_mem = {}  # name -> total_kb
        for line in result.stdout.strip().split("\n"):
            parts = line.split('"')
            if len(parts) >= 10:
                name = parts[1].strip() if len(parts) > 1 else ""
                mem_str = parts[9] if len(parts) > 9 else ""
                mem_digits = re.sub(r'[^\d]', '', mem_str)
                if mem_digits and name:
                    kb = int(mem_digits)
                    proc_mem[name] = proc_mem.get(name, 0) + kb

        # Sort by memory desc, take top 8
        top = sorted(proc_mem.items(), key=lambda x: x[1], reverse=True)[:8]
        ram["top_processes"] = [
            {"name": name, "memory_mb": round(kb / 1024, 1)}
            for name, kb in top
        ]
    except Exception as e:
        print(f"[RAM] tasklist error: {e}")

    _ram_cache["data"] = ram
    _ram_cache["ts"] = now
    return ram


def get_daily_entries(max_entries=20):
    """Get last N daily log entries."""
    import time
    today = datetime.now().strftime("%Y-%m-%d")
    daily_path = os.path.join(MEMORY_DIR, "daily", f"{today}.md")
    if not os.path.exists(daily_path):
        from datetime import timedelta
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        daily_path = os.path.join(MEMORY_DIR, "daily", f"{yesterday}.md")

    if not os.path.exists(daily_path):
        return []

    try:
        with open(daily_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        entries = [l.rstrip() for l in lines if l.startswith("- ")]
        return entries[-max_entries:]
    except:
        return []


# ============================================================
# HTTP SERVER
# ============================================================

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PAI Monitor — System Dashboard</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace; background: #0a0e14; color: #c5c8c6; min-height: 100vh; }

.header { background: #0d1117; border-bottom: 1px solid #21262d; padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; }
.header h1 { font-size: 16px; color: #58a6ff; font-weight: 600; }
.header h1 .emoji { font-family: sans-serif; }
.header .status { font-size: 12px; display: flex; gap: 12px; align-items: center; }
.header .dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; }
.dot.green { background: #3fb950; box-shadow: 0 0 6px #3fb950; }
.dot.red { background: #f85149; box-shadow: 0 0 6px #f85149; }
.dot.yellow { background: #d29922; box-shadow: 0 0 6px #d29922; }
.refresh-info { color: #484f58; font-size: 11px; }

.grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; padding: 16px; }
@media (max-width: 1200px) { .grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 800px) { .grid { grid-template-columns: 1fr; } }

.card { background: #0d1117; border: 1px solid #21262d; border-radius: 8px; padding: 14px; overflow: hidden; }
.card h2 { font-size: 12px; text-transform: uppercase; color: #484f58; letter-spacing: 1.5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
.card h2 .emoji { font-family: sans-serif; font-size: 14px; }

.process { display: flex; align-items: center; gap: 10px; padding: 8px 0; border-bottom: 1px solid #161b22; }
.process:last-child { border-bottom: none; }
.process .name { font-weight: 600; color: #c9d1d9; font-size: 13px; flex: 1; }
.process .meta { font-size: 11px; color: #484f58; }
.process .badge { padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 700; text-transform: uppercase; }
.badge.online { background: #0d3b1a; color: #3fb950; }
.badge.stopped { background: #3b1010; color: #f85149; }
.badge.errored { background: #3b2510; color: #d29922; }

.metric { display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid #161b22; font-size: 12px; }
.metric:last-child { border-bottom: none; }
.metric .label { color: #8b949e; }
.metric .value { color: #c9d1d9; font-weight: 600; }
.metric .value.ok { color: #3fb950; }
.metric .value.warn { color: #d29922; }
.metric .value.err { color: #f85149; }

.timeline { max-height: 200px; overflow-y: auto; }
.timeline .event { padding: 6px 0; border-bottom: 1px solid #161b22; font-size: 11px; }
.timeline .event:last-child { border-bottom: none; }
.timeline .time { color: #58a6ff; font-weight: 600; }
.timeline .type { padding: 1px 6px; border-radius: 3px; font-size: 10px; font-weight: 700; margin-left: 6px; }
.type.briefing { background: #0d3b1a; color: #3fb950; }
.type.checkin { background: #0d2748; color: #58a6ff; }
.type.psycho { background: #2d1054; color: #bc8cff; }
.timeline .msg { color: #8b949e; margin-top: 2px; display: block; }

.log-box { max-height: 280px; overflow-y: auto; font-size: 10px; line-height: 1.5; background: #010409; border-radius: 4px; padding: 8px; }
.log-box .line { white-space: pre-wrap; word-break: break-all; }
.log-box .line.tool { color: #d29922; }
.log-box .line.session { color: #58a6ff; }
.log-box .line.router { color: #3fb950; }
.log-box .line.error { color: #f85149; }
.log-box .line.cron { color: #bc8cff; }
.log-box .line.message { color: #c9d1d9; }

.agent-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }
.agent { padding: 6px 8px; background: #161b22; border-radius: 4px; font-size: 11px; }
.agent .name { font-weight: 700; }
.agent.active { border-left: 3px solid #58a6ff; background: #0d2748; }
.agent .sid { color: #484f58; font-size: 9px; word-break: break-all; }

.card.wide { grid-column: span 2; }
.card.full { grid-column: 1 / -1; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0d1117; }
::-webkit-scrollbar-thumb { background: #21262d; border-radius: 2px; }
</style>
</head>
<body>

<div class="header">
    <h1><span class="emoji">🤖</span> PAI System Monitor</h1>
    <div class="status">
        <span id="liveStatus"></span>
        <span class="refresh-info" id="refreshInfo">Loading...</span>
    </div>
</div>

<div class="grid" id="dashboard"></div>

<script>
let refreshInterval = 5000; // 5 sec
let lastData = null;

function formatUptime(ms) {
    const s = Math.floor(ms / 1000);
    if (s < 60) return s + 's';
    const m = Math.floor(s / 60);
    if (m < 60) return m + 'm';
    const h = Math.floor(m / 60);
    if (h < 24) return h + 'h ' + (m % 60) + 'm';
    const d = Math.floor(h / 24);
    return d + 'd ' + (h % 24) + 'h';
}

function classifyLine(line) {
    if (line.includes('[ClaudeCode] Tool call')) return 'tool';
    if (line.includes('[ClaudeCode] Session')) return 'session';
    if (line.includes('[Router]')) return 'router';
    if (line.includes('[Cron]')) return 'cron';
    if (line.includes('Message:')) return 'message';
    if (line.includes('error') || line.includes('Error')) return 'error';
    return '';
}

function renderDashboard(data) {
    const d = document.getElementById('dashboard');
    const procs = data.processes || [];
    const state = data.checkins_state || {};
    const health = data.checkins_health || {};
    const session = data.session || {};
    const memory = data.memory || {};
    const relayLogs = data.relay_logs || {};
    const checkinLogs = data.checkin_logs || {};

    const allOnline = procs.every(p => p.status === 'online');
    document.getElementById('liveStatus').innerHTML = `<span class="dot ${allOnline ? 'green' : 'red'}"></span> ${allOnline ? 'All systems online' : 'Issues detected'}`;

    let html = '';

    // === PROCESSES ===
    html += `<div class="card">
        <h2><span class="emoji">⚙️</span> PM2 Processes</h2>`;
    for (const p of procs) {
        if (p.error) { html += `<div class="process"><span class="meta">${p.error}</span></div>`; continue; }
        const statusClass = p.status === 'online' ? 'online' : (p.status === 'errored' ? 'errored' : 'stopped');
        html += `<div class="process">
            <span class="dot ${p.status === 'online' ? 'green' : 'red'}"></span>
            <span class="name">${p.name}</span>
            <span class="badge ${statusClass}">${p.status}</span>
        </div>
        <div style="display:flex;gap:16px;font-size:11px;color:#484f58;padding:0 0 6px 18px;">
            <span>PID: ${p.pid}</span>
            <span>CPU: ${p.cpu}%</span>
            <span>RAM: ${p.memory_mb}MB</span>
            <span>↻ ${p.restarts}</span>
            <span>Up: ${formatUptime(p.uptime_ms)}</span>
        </div>`;
    }
    html += '</div>';

    // === SYSTEM RAM ===
    const ram = data.system_ram || {};
    if (ram.total_mb) {
        const pct = ram.percent || 0;
        const barColor = pct > 85 ? '#f85149' : pct > 70 ? '#d29922' : '#3fb950';
        const totalGB = (ram.total_mb / 1024).toFixed(1);
        const usedGB = (ram.used_mb / 1024).toFixed(1);
        const freeGB = (ram.free_mb / 1024).toFixed(1);
        html += `<div class="card">
            <h2><span class="emoji">💾</span> System RAM</h2>
            <div style="margin-bottom:10px;">
                <div style="display:flex;justify-content:space-between;font-size:11px;color:#8b949e;margin-bottom:4px;">
                    <span>${usedGB} GB used</span>
                    <span>${freeGB} GB free</span>
                </div>
                <div style="background:#161b22;border-radius:4px;height:18px;overflow:hidden;position:relative;">
                    <div style="background:${barColor};height:100%;width:${pct}%;border-radius:4px;transition:width 0.5s;"></div>
                    <span style="position:absolute;top:1px;left:50%;transform:translateX(-50%);font-size:10px;font-weight:700;color:#c9d1d9;">${pct}% of ${totalGB} GB</span>
                </div>
            </div>`;
        const topProcs = ram.top_processes || [];
        if (topProcs.length > 0) {
            html += '<div style="font-size:10px;color:#484f58;margin-bottom:4px;">Top consumers:</div>';
            for (const tp of topProcs) {
                const w = ram.total_mb > 0 ? Math.min((tp.memory_mb / ram.total_mb) * 100 * 3, 100) : 0;
                html += `<div style="display:flex;align-items:center;gap:6px;padding:2px 0;font-size:11px;">
                    <span style="color:#8b949e;width:140px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${tp.name}</span>
                    <div style="flex:1;background:#161b22;border-radius:2px;height:10px;overflow:hidden;">
                        <div style="background:#21262d;height:100%;width:${w.toFixed(1)}%;border-radius:2px;"></div>
                    </div>
                    <span style="color:#c9d1d9;font-weight:600;width:60px;text-align:right;">${tp.memory_mb > 1024 ? (tp.memory_mb/1024).toFixed(1) + ' GB' : tp.memory_mb + ' MB'}</span>
                </div>`;
            }
        }
        html += '</div>';
    }

    // === CHECKINS STATUS ===
    html += `<div class="card">
        <h2><span class="emoji">📋</span> Smart Check-ins</h2>`;
    const checks = [
        ['Morning Briefing', state.morningBriefingSentDate === new Date().toISOString().split('T')[0]],
        ['Psycho Morning', state.psychoMorningSentDate === new Date().toISOString().split('T')[0]],
        ['Psycho Evening', state.psychoEveningSentDate === new Date().toISOString().split('T')[0]],
        ['Evening Recap', state.eveningRecapSentDate === new Date().toISOString().split('T')[0]],
    ];
    for (const [label, done] of checks) {
        html += `<div class="metric"><span class="label">${label}</span><span class="value ${done ? 'ok' : ''}">${done ? '✅' : '—'}</span></div>`;
    }
    html += `<div class="metric"><span class="label">Notifications today</span><span class="value ${(state.notificationsToday||0) > 6 ? 'warn' : ''}">${state.notificationsToday || 0} / 8</span></div>`;
    html += `<div class="metric"><span class="label">Google Auth</span><span class="value ${health.googleAuthorized ? 'ok' : 'err'}">${health.googleAuthorized ? '✅ OK' : '❌'}</span></div>`;
    html += `<div class="metric"><span class="label">Claude Code</span><span class="value ${health.claudeCodeEnabled ? 'ok' : 'warn'}">${health.claudeCodeEnabled ? '✅ OK' : '⚠️ OFF'}</span></div>`;
    html += '</div>';

    // === AGENT SESSIONS ===
    html += `<div class="card">
        <h2><span class="emoji">👑</span> Agent Sessions</h2>`;
    const agents = {'general': '👑', 'strategy': '🎯', 'psycho': '🧠', 'research': '🔬', 'content': '✍️', 'finance': '💰', 'critic': '😈'};
    const activeSessions = session.agentSessionIds || {};
    html += '<div class="agent-grid">';
    for (const [name, emoji] of Object.entries(agents)) {
        const sid = activeSessions[name];
        const isActive = !!sid;
        html += `<div class="agent ${isActive ? 'active' : ''}">
            <span class="name">${emoji} ${name}</span>
            ${sid ? `<div class="sid">${sid.substring(0,8)}</div>` : '<div class="sid" style="color:#21262d">no session</div>'}
        </div>`;
    }
    html += '</div>';
    html += `<div class="metric" style="margin-top:8px"><span class="label">Last activity</span><span class="value">${session.lastActivity ? new Date(session.lastActivity).toLocaleTimeString('pl') : '—'}</span></div>`;
    html += '</div>';

    // === MEMORY ===
    html += `<div class="card">
        <h2><span class="emoji">🧠</span> Memory</h2>`;
    if (memory['MEMORY.md']) {
        html += `<div class="metric"><span class="label">MEMORY.md</span><span class="value">${memory['MEMORY.md'].lines} lines / ${(memory['MEMORY.md'].size_bytes/1024).toFixed(1)}KB</span></div>`;
    }
    if (memory['GOALS.md']) {
        html += `<div class="metric"><span class="label">GOALS.md</span><span class="value">${memory['GOALS.md'].lines} lines / ${(memory['GOALS.md'].size_bytes/1024).toFixed(1)}KB</span></div>`;
    }
    if (memory.daily_log) {
        html += `<div class="metric"><span class="label">Daily log (${memory.daily_log.date})</span><span class="value">${memory.daily_log.entries} entries</span></div>`;
    }
    html += '</div>';

    // === NOTIFICATION TIMELINE ===
    html += `<div class="card">
        <h2><span class="emoji">🔔</span> Today's Notifications</h2>
        <div class="timeline">`;
    const notifications = (state.recentNotifications || []).slice().reverse();
    for (const n of notifications) {
        const typeClass = n.type || 'checkin';
        const timeStr = n.time || '';
        const msg = n.message || '';
        html += `<div class="event">
            <span class="time">${timeStr}</span>
            <span class="type ${typeClass}">${typeClass}</span>
            <span class="msg">${msg.length > 120 ? msg.substring(0,120) + '...' : msg}</span>
        </div>`;
    }
    if (notifications.length === 0) html += '<div style="color:#484f58;font-size:11px;">No notifications yet</div>';
    html += '</div></div>';

    // === DAILY ACTIVITY ===
    const dailyEntries = data.daily_entries || [];
    if (dailyEntries.length > 0) {
        html += `<div class="card">
            <h2><span class="emoji">📅</span> Daily Activity Log</h2>
            <div class="timeline">`;
        for (const entry of dailyEntries.slice().reverse()) {
            const text = entry.replace(/^- /, '');
            let cls = '';
            if (text.includes('Agent switched')) cls = 'session';
            else if (text.includes('Mode switched')) cls = 'router';
            else if (text.includes('Tool call') || text.includes('tool_call')) cls = 'tool';
            else if (text.includes('Session reset')) cls = 'cron';
            else if (text.includes('Zapamiętano') || text.includes('Dodano')) cls = 'message';
            html += `<div class="event"><span class="msg" style="color:${cls === 'session' ? '#58a6ff' : cls === 'router' ? '#3fb950' : cls === 'tool' ? '#d29922' : cls === 'cron' ? '#bc8cff' : '#8b949e'}">${escHtml(text)}</span></div>`;
        }
        html += '</div></div>';
    }

    // === RELAY LOGS (wide) ===
    html += `<div class="card wide">
        <h2><span class="emoji">📡</span> Relay Logs (claude-telegram-relay)</h2>
        <div class="log-box">`;
    for (const line of (relayLogs.out || []).slice(-30)) {
        const cls = classifyLine(line);
        html += `<div class="line ${cls}">${escHtml(line)}</div>`;
    }
    html += '</div></div>';

    // === CHECKINS LOGS ===
    const cLogs = checkinLogs.out || [];
    if (cLogs.length > 0) {
        html += `<div class="card">
            <h2><span class="emoji">⏰</span> Smart-Checkins Logs</h2>
            <div class="log-box">`;
        for (const line of cLogs.slice(-20)) {
            let cls = '';
            if (line.includes('[Cron]') || line.includes('cron')) cls = 'cron';
            else if (line.includes('notification') || line.includes('Sending')) cls = 'session';
            else if (line.includes('error') || line.includes('Error')) cls = 'error';
            html += `<div class="line ${cls}">${escHtml(line)}</div>`;
        }
        html += '</div></div>';
    }

    // === ERRORS ===
    const allErrors = [...(relayLogs.err || []), ...(checkinLogs.err || [])].filter(l => l.trim());
    if (allErrors.length > 0) {
        html += `<div class="card full">
            <h2><span class="emoji">🔴</span> Errors</h2>
            <div class="log-box">`;
        for (const line of allErrors.slice(-20)) {
            html += `<div class="line error">${escHtml(line)}</div>`;
        }
        html += '</div></div>';
    }

    d.innerHTML = html;
}

function escHtml(str) {
    if (!str) return '';
    return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

async function refresh() {
    try {
        const resp = await fetch('/api/monitor');
        const data = await resp.json();
        lastData = data;
        renderDashboard(data);
        document.getElementById('refreshInfo').textContent = 'Updated: ' + new Date().toLocaleTimeString('pl');
    } catch (e) {
        document.getElementById('refreshInfo').textContent = 'Error: ' + e.message;
    }
}

refresh();
setInterval(refresh, refreshInterval);
</script>
</body>
</html>"""


class MonitorHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Quiet

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/" or parsed.path == "/monitor":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(DASHBOARD_HTML.encode("utf-8"))

        elif parsed.path == "/api/monitor":
            # Build RAM data safely (PowerShell can be slow/fail)
            try:
                ram_data = get_system_ram()
            except Exception as e:
                print(f"[API] system_ram error: {e}")
                ram_data = {"total_mb": 0, "used_mb": 0, "free_mb": 0, "percent": 0, "top_processes": [], "error": str(e)}

            data = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "processes": get_pm2_processes(),
                "checkins_state": get_checkins_state(),
                "checkins_health": get_checkins_health(),
                "session": get_session(),
                "memory": get_memory_stats(),
                "system_ram": ram_data,
                "relay_logs": get_logs("claude-telegram-relay", 40),
                "checkin_logs": get_logs("smart-checkins", 20),
                "daily_entries": get_daily_entries(20),
            }
            body = json.dumps(data, ensure_ascii=False, default=str)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()


def main():
    parser = argparse.ArgumentParser(description="PAI System Monitor")
    parser.add_argument("--port", type=int, default=8090, help="Port (default: 8090)")
    args = parser.parse_args()

    server = HTTPServer(("0.0.0.0", args.port), MonitorHandler)
    print(f"🤖 PAI Monitor running at http://localhost:{args.port}")
    print(f"   Dashboard: http://localhost:{args.port}/")
    print(f"   API:       http://localhost:{args.port}/api/monitor")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()


if __name__ == "__main__":
    main()
