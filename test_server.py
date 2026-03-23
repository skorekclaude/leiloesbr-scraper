import urllib.request, sys
try:
    r = urllib.request.urlopen("http://localhost:8091/gluchowski.html", timeout=5)
    data = r.read()
    print(f"Status: {r.status}")
    print(f"Size: {len(data)} bytes")
    # Check if obj-images class is in HTML
    html = data.decode("utf-8", errors="replace")
    count = html.count("obj-images")
    print(f"Object image sections: {count}")
except Exception as e:
    print(f"FAIL: {e}")
