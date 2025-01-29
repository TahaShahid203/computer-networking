from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Backend server 2 on port 8082
host = '127.0.0.1'
port = 8082

with TCPServer((host, port), SimpleHTTPRequestHandler) as httpd:
    print(f"Backend Server 2 running on {host}:{port}")
    httpd.serve_forever()
