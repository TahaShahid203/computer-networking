import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))  # Bind to port 5555
server.listen(1)
print("Waiting for a connection...")

conn, addr = server.accept()
print(f"Connected by {addr}")
conn.sendall(b"Hello, client!")
conn.close()
