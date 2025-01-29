import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 65433))

    print("Server listening on port 65433...")
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")

if __name__ == "__main__":
    start_server()
