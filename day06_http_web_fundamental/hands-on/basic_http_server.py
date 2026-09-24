from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello from my Python server!")


server = HTTPServer(("localhost", 8000), MyHandler)

print("Server running at http://localhost:8000")

server.serve_forever()
