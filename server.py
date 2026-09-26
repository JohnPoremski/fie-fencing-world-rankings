import http.server
import os

port = int(os.environ.get("PORT", 8000))
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("0.0.0.0", port), handler)
httpd.serve_forever()
