from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/hello":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Hello! This is MY server."}).encode())
        elif self.path == "/api/time":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"now": str(datetime.now())}).encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Route does not exist"}).encode())

print("My first server is running at http://localhost:8000")
HTTPServer(("localhost", 8000), MyHandler).serve_forever()