import http.server
import socketserver
import requests

PORT = 8080

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]  # Remove the leading '/'
        try:
            resp = requests.get(url)
            self.send_response(resp.status_code)
            self.send_header("Content-type", resp.headers["Content-Type"])
            self.end_headers()
            self.wfile.write(resp.content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

with socketserver.TCPServer(("", PORT), ProxyHandler) as httpd:
    print(f"Serving proxy on port {PORT}")
    httpd.serve_forever()
