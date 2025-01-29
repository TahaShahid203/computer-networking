from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Backend server 1 on port 8081
host = '127.0.0.1'
port = 8081

with TCPServer((host, port), SimpleHTTPRequestHandler) as httpd:
    print(f"Backend Server 1 running on {host}:{port}")
    httpd.serve_forever()
