import http.server
import json

class APIHandler(http.server.BaseHTTPRequestHandler):
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        elif self.path == "/api/users":
            # TODO: implement user listing
            self.send_response(501)
            self.send_cors_headers()
            self.end_headers()
        else:
            self.send_response(404)
            self.send_cors_headers()
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/users":
            # TODO: implement user creation with validation
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            self.send_response(501)
            self.send_cors_headers()
            self.end_headers()
        else:
            self.send_response(404)
            self.send_cors_headers()
            self.end_headers()

if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", 8080), APIHandler)
    print("Server running on :8080")
    server.serve_forever()

