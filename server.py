"""
Serwer WWW do przegladania wynikow scrapera.
Otwierasz w Chrome: http://localhost:8080

Zero dodatkowych instalacji — uzywa wbudowanego Pythona.
"""
import sys
import io
import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime

# Fix kodowania Windows
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from config import SERVER_HOST, SERVER_PORT, WEB_DIR
import re
import uuid
import shutil
from database import (
    get_connection, init_db, get_stats,
    get_collection_objects, get_collection_object_by_id, add_collection_object,
    update_collection_object, delete_collection_object,
    add_object_photo, get_object_photos, delete_object_photo,
    get_object_valuations, add_valuation, get_collection_stats,
)
from config import COLLECTION_IMAGES_DIR


class ArtCollectionHandler(SimpleHTTPRequestHandler):
    """Handler HTTP — serwuje pliki statyczne i API."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # === API ENDPOINTS ===
        if path.startswith("/api/"):
            self._handle_api("GET", path, parse_qs(parsed.query))
            return

        # === COLLECTION IMAGES ===
        if path.startswith("/images/collection/"):
            self._serve_collection_image(path)
            return

        # === STRONA GLOWNA ===
        if path == "/" or path == "":
            self.path = "/index.html"

        # Serwuj pliki statyczne
        super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path.startswith("/api/"):
            self._handle_api("POST", path, parse_qs(parsed.query))
            return
        self._send_json({"error": "Not found"}, 404)

    def do_PUT(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path.startswith("/api/"):
            self._handle_api("PUT", path, parse_qs(parsed.query))
            return
        self._send_json({"error": "Not found"}, 404)

    def do_DELETE(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path.startswith("/api/"):
            self._handle_api("DELETE", path, parse_qs(parsed.query))
            return
        self._send_json({"error": "Not found"}, 404)

    def do_OPTIONS(self):
        """CORS preflight."""
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _serve_collection_image(self, path):
        """Serwuje zdjecia kolekcji z katalogu images/collection/."""
        filename = os.path.basename(path)
        filepath = os.path.join(COLLECTION_IMAGES_DIR, filename)
        if not os.path.exists(filepath):
            self.send_error(404, "Image not found")
            return
        ext = os.path.splitext(filename)[1].lower()
        mime_types = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
                      ".gif": "image/gif", ".webp": "image/webp"}
        mime = mime_types.get(ext, "application/octet-stream")
        with open(filepath, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", len(data))
        self.send_header("Cache-Control", "public, max-age=86400")
        self.end_headers()
        self.wfile.write(data)

    def _read_json_body(self):
        """Odczytuje JSON body z POST/PUT request."""
        content_len = int(self.headers.get("Content-Length", 0))
        if content_len == 0:
            return {}
        raw = self.rfile.read(content_len)
        return json.loads(raw.decode("utf-8"))

    def _read_multipart(self):
        """Odczytuje multipart/form-data (upload zdjec)."""
        content_type = self.headers.get("Content-Type", "")
        if "boundary=" not in content_type:
            return None, {}
        boundary = content_type.split("boundary=")[1].strip()
        content_len = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(content_len)

        # Parse multipart
        parts = raw.split(f"--{boundary}".encode())
        file_data = None
        fields = {}
        for part in parts:
            if b"Content-Disposition" not in part:
                continue
            header_end = part.find(b"\r\n\r\n")
            if header_end < 0:
                continue
            header = part[:header_end].decode("utf-8", errors="replace")
            body = part[header_end + 4:]
            if body.endswith(b"\r\n"):
                body = body[:-2]

            name_match = re.search(r'name="([^"]+)"', header)
            if not name_match:
                continue
            name = name_match.group(1)

            filename_match = re.search(r'filename="([^"]+)"', header)
            if filename_match:
                file_data = {"filename": filename_match.group(1), "data": body}
            else:
                fields[name] = body.decode("utf-8", errors="replace")

        return file_data, fields

    def _handle_api(self, method, path, params):
        """Obsluguje zapytania API."""
        try:
            conn = get_connection()

            # --- Collection endpoints (z ID w URL) ---
            coll_match = re.match(r"^/api/collection/(\d+)$", path)
            coll_photo_match = re.match(r"^/api/collection/(\d+)/photos$", path)
            coll_photo_del = re.match(r"^/api/collection/(\d+)/photos/(\d+)$", path)

            if path == "/api/stats" and method == "GET":
                data = self._api_stats(conn)
            elif path == "/api/auction-items" and method == "GET":
                data = self._api_auction_items(conn, params)
            elif path == "/api/artists" and method == "GET":
                data = self._api_artists(conn, params)
            elif path == "/api/scraper-runs" and method == "GET":
                data = self._api_scraper_runs(conn)

            # --- Collection CRUD ---
            elif path == "/api/collection" and method == "GET":
                data = self._api_collection_list(conn, params)
            elif path == "/api/collection" and method == "POST":
                body = self._read_json_body()
                data = self._api_collection_create(conn, body)
            elif coll_match and method == "GET":
                data = self._api_collection_detail(conn, int(coll_match.group(1)))
            elif coll_match and method == "PUT":
                body = self._read_json_body()
                data = self._api_collection_update(conn, int(coll_match.group(1)), body)
            elif coll_match and method == "DELETE":
                data = self._api_collection_delete(conn, int(coll_match.group(1)))

            # --- Photo upload/delete ---
            elif coll_photo_match and method == "POST":
                data = self._api_photo_upload(conn, int(coll_photo_match.group(1)))
            elif coll_photo_del and method == "DELETE":
                data = self._api_photo_delete(conn, int(coll_photo_del.group(1)), int(coll_photo_del.group(2)))

            else:
                self._send_json({"error": "Unknown endpoint"}, 404)
                conn.close()
                return

            self._send_json(data)
            conn.close()

        except Exception as e:
            self._send_json({"error": str(e)}, 500)

    def _api_stats(self, conn):
        """Statystyki systemu."""
        stats = get_stats(conn)

        # Dodaj rozkład confidence
        rows = conn.execute("""
            SELECT match_confidence, COUNT(*) as c
            FROM auction_items WHERE is_false_positive = 0
            GROUP BY match_confidence
        """).fetchall()
        stats["by_confidence"] = {r["match_confidence"]: r["c"] for r in rows}

        # Ostatni scraping
        row = conn.execute("""
            SELECT * FROM scraper_runs ORDER BY id DESC LIMIT 1
        """).fetchone()
        if row:
            stats["last_run"] = dict(row)
        else:
            stats["last_run"] = None

        # Statystyki kolekcji
        coll_stats = get_collection_stats(conn)
        stats.update(coll_stats)

        return stats

    def _api_auction_items(self, conn, params):
        """Lista znalezisk aukcyjnych z filtrami."""
        query = "SELECT ai.*, a.canonical_name as artist_name FROM auction_items ai LEFT JOIN artists a ON ai.matched_artist_id = a.id WHERE ai.is_false_positive = 0"
        qparams = []

        # Filtr: artysta
        artist_id = params.get("artist_id", [None])[0]
        if artist_id:
            query += " AND ai.matched_artist_id = ?"
            qparams.append(int(artist_id))

        # Filtr: szukaj w tytule
        search = params.get("search", [None])[0]
        if search:
            query += " AND (ai.title LIKE ? OR ai.description LIKE ?)"
            like = f"%{search}%"
            qparams.extend([like, like])

        # Filtr: confidence
        confidence = params.get("confidence", [None])[0]
        if confidence:
            query += " AND ai.match_confidence = ?"
            qparams.append(confidence)

        # Filtr: kategoria artysty
        category = params.get("category", [None])[0]
        if category:
            query += " AND a.category = ?"
            qparams.append(category)

        # Filtr: cena min/max
        price_min = params.get("price_min", [None])[0]
        if price_min:
            query += " AND ai.price_brl >= ?"
            qparams.append(float(price_min))
        price_max = params.get("price_max", [None])[0]
        if price_max:
            query += " AND ai.price_brl <= ?"
            qparams.append(float(price_max))

        # Sortowanie
        sort = params.get("sort", ["newest"])[0]
        sort_map = {
            "newest": "ai.first_seen_at DESC",
            "oldest": "ai.first_seen_at ASC",
            "price_high": "ai.price_brl DESC",
            "price_low": "ai.price_brl ASC",
            "title": "ai.title ASC",
        }
        order = sort_map.get(sort, "ai.first_seen_at DESC")
        query += f" ORDER BY {order}"

        # Paginacja
        page = int(params.get("page", [1])[0])
        per_page = int(params.get("per_page", [50])[0])
        per_page = min(per_page, 200)
        offset = (page - 1) * per_page
        query += f" LIMIT {per_page} OFFSET {offset}"

        rows = conn.execute(query, qparams).fetchall()
        items = [dict(r) for r in rows]

        # Total count
        count_query = query.split("ORDER BY")[0].replace("SELECT ai.*, a.canonical_name as artist_name", "SELECT COUNT(*) as total")
        total = conn.execute(count_query, qparams).fetchone()["total"]

        return {
            "items": items,
            "total": total,
            "page": page,
            "per_page": per_page,
            "pages": (total + per_page - 1) // per_page,
        }

    def _api_artists(self, conn, params):
        """Lista artystow z liczba znalezisk."""
        rows = conn.execute("""
            SELECT a.id, a.canonical_name, a.category, a.birth_year, a.death_year,
                   COUNT(ai.id) as auction_count
            FROM artists a
            LEFT JOIN auction_items ai ON a.id = ai.matched_artist_id AND ai.is_false_positive = 0
            GROUP BY a.id
            ORDER BY auction_count DESC, a.canonical_name
        """).fetchall()
        return {"artists": [dict(r) for r in rows]}

    def _api_scraper_runs(self, conn):
        """Historia uruchomien scrapera."""
        rows = conn.execute("""
            SELECT * FROM scraper_runs ORDER BY id DESC LIMIT 20
        """).fetchall()
        return {"runs": [dict(r) for r in rows]}

    # ================================================================
    # COLLECTION CRUD
    # ================================================================

    def _api_collection_list(self, conn, params):
        """Lista obiektow kolekcji z filtrami i paginacja."""
        category = params.get("category", [None])[0]
        artist_id = params.get("artist_id", [None])[0]
        if artist_id:
            artist_id = int(artist_id)
        search = params.get("search", [None])[0]
        sort_by = params.get("sort", ["title"])[0]
        has_photo = params.get("has_photo", [None])[0]  # "yes" / "no" / None
        page = int(params.get("page", [1])[0])
        per_page = int(params.get("per_page", [48])[0])
        per_page = min(per_page, 200)
        offset = (page - 1) * per_page

        rows = get_collection_objects(conn, category=category, artist_id=artist_id,
                                       search=search, sort_by=sort_by,
                                       limit=per_page, offset=offset,
                                       has_photo=has_photo)
        items = []
        for r in rows:
            obj = dict(r)
            # Dolacz primary photo
            photos = get_object_photos(conn, obj["id"])
            if photos:
                primary = [p for p in photos if p["is_primary"]]
                photo = primary[0] if primary else photos[0]
                obj["primary_photo"] = f"/images/collection/{os.path.basename(photo['file_path'])}"
            else:
                obj["primary_photo"] = None
            obj["photo_count"] = len(photos)
            items.append(obj)

        # Total count (mirror the same filters)
        count_q = "SELECT COUNT(*) as c FROM collection_objects co"
        count_p = []
        if has_photo is not None:
            count_q += " LEFT JOIN (SELECT object_id, COUNT(*) as pc FROM object_photos GROUP BY object_id) ph ON ph.object_id = co.id"
        count_q += " WHERE 1=1"
        if category:
            count_q += " AND co.category = ?"
            count_p.append(category)
        if artist_id:
            count_q += " AND co.artist_id = ?"
            count_p.append(artist_id)
        if search:
            count_q += (" AND (co.title LIKE ? OR co.description LIKE ?"
                         " OR co.artist_name_display LIKE ?"
                         " OR co.inventory_number LIKE ? OR co.notes LIKE ?)")
            like = f"%{search}%"
            count_p.extend([like, like, like, like, like])
        if has_photo == "yes":
            count_q += " AND ph.pc > 0"
        elif has_photo == "no":
            count_q += " AND ph.pc IS NULL"
        total = conn.execute(count_q, count_p).fetchone()["c"]

        return {
            "items": items,
            "total": total,
            "page": page,
            "per_page": per_page,
            "pages": max(1, (total + per_page - 1) // per_page),
        }

    def _api_collection_detail(self, conn, object_id):
        """Szczegoly obiektu + zdjecia + wyceny."""
        obj = get_collection_object_by_id(conn, object_id)
        if not obj:
            return {"error": "Object not found"}
        result = dict(obj)
        photos = get_object_photos(conn, object_id)
        result["photos"] = [dict(p) for p in photos]
        for p in result["photos"]:
            p["url"] = f"/images/collection/{os.path.basename(p['file_path'])}"
        valuations = get_object_valuations(conn, object_id)
        result["valuations"] = [dict(v) for v in valuations]
        return result

    def _api_collection_create(self, conn, body):
        """Dodaje nowy obiekt do kolekcji."""
        if not body.get("title"):
            return {"error": "Title is required"}
        if not body.get("category"):
            body["category"] = "inne"
        obj_id = add_collection_object(conn, body)
        conn.commit()
        return {"id": obj_id, "message": "Object created"}

    def _api_collection_update(self, conn, object_id, body):
        """Aktualizuje obiekt."""
        obj = get_collection_object_by_id(conn, object_id)
        if not obj:
            return {"error": "Object not found"}
        ok = update_collection_object(conn, object_id, body)
        conn.commit()
        return {"id": object_id, "updated": ok}

    def _api_collection_delete(self, conn, object_id):
        """Usuwa obiekt i jego zdjecia."""
        obj = get_collection_object_by_id(conn, object_id)
        if not obj:
            return {"error": "Object not found"}
        # Usun pliki zdjec z dysku
        photos = get_object_photos(conn, object_id)
        for p in photos:
            fpath = p["file_path"]
            if os.path.exists(fpath):
                try:
                    os.remove(fpath)
                except OSError:
                    pass
        delete_collection_object(conn, object_id)
        conn.commit()
        return {"deleted": object_id}

    # ================================================================
    # PHOTO UPLOAD / DELETE
    # ================================================================

    def _api_photo_upload(self, conn, object_id):
        """Upload zdjecia do obiektu (multipart/form-data)."""
        obj = get_collection_object_by_id(conn, object_id)
        if not obj:
            return {"error": "Object not found"}

        file_data, fields = self._read_multipart()
        if not file_data:
            return {"error": "No file uploaded"}

        # Generuj unikalny filename
        ext = os.path.splitext(file_data["filename"])[1].lower() or ".jpg"
        safe_name = f"obj{object_id}_{uuid.uuid4().hex[:8]}{ext}"
        filepath = os.path.join(COLLECTION_IMAGES_DIR, safe_name)

        with open(filepath, "wb") as f:
            f.write(file_data["data"])

        caption = fields.get("caption", "")
        is_primary = int(fields.get("is_primary", "0"))

        # Jesli to pierwszy obraz obiektu — automatycznie primary
        existing = get_object_photos(conn, object_id)
        if not existing:
            is_primary = 1

        photo_id = add_object_photo(conn, object_id, filepath, caption, is_primary)
        conn.commit()

        return {
            "id": photo_id,
            "url": f"/images/collection/{safe_name}",
            "is_primary": is_primary,
        }

    def _api_photo_delete(self, conn, object_id, photo_id):
        """Usuwa zdjecie obiektu."""
        fpath = delete_object_photo(conn, photo_id)
        if fpath and os.path.exists(fpath):
            try:
                os.remove(fpath)
            except OSError:
                pass
        conn.commit()
        return {"deleted": photo_id}

    def _send_json(self, data, status=200):
        """Wysyla odpowiedz JSON."""
        body = json.dumps(data, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        """Cichy log — nie spamuj konsoli."""
        if "/api/" in str(args[0]):
            return  # Nie loguj API calls
        super().log_message(format, *args)


def main():
    init_db()

    server = HTTPServer((SERVER_HOST, SERVER_PORT), ArtCollectionHandler)
    url = f"http://{SERVER_HOST}:{SERVER_PORT}"

    print("=" * 50)
    print("  ART COLLECTION BROWSER")
    print("=" * 50)
    print(f"  Otworz w Chrome: {url}")
    print(f"  Zatrzymaj: Ctrl+C")
    print("=" * 50)

    # Automatycznie otworz przegladarke
    try:
        import webbrowser
        webbrowser.open(url)
    except Exception:
        pass

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
        server.server_close()


if __name__ == "__main__":
    main()
