import socket
import threading

# Configuration (Change these)
LISTEN_HOST = "0.0.0.0"  # Listen on all interfaces
LISTEN_PORT = 8080        # Incoming port
FORWARD_HOST = "127.0.0.1"  # Destination (can be another machine)
FORWARD_PORT = 5555         # Forward traffic to this port

def handle_client(client_socket):
    """Handles incoming client connections and forwards data."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as forward_socket:
        forward_socket.connect((FORWARD_HOST, FORWARD_PORT))

        # Start forwarding data in both directions
        client_thread = threading.Thread(target=forward_data, args=(client_socket, forward_socket))
        forward_thread = threading.Thread(target=forward_data, args=(forward_socket, client_socket))
        client_thread.start()
        forward_thread.start()
        client_thread.join()
        forward_thread.join()

def forward_data(source, destination):
    """Forwards data between two sockets."""
    try:
        while True:
            data = source.recv(4096)
            if not data:
                break
            destination.sendall(data)
    except:
        pass  # Ignore errors
    finally:
        source.close()
        destination.close()

def start_server():
    """Starts the port forwarding server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((LISTEN_HOST, LISTEN_PORT))
        server.listen(5)
        print(f"Port forwarding started: {LISTEN_HOST}:{LISTEN_PORT} -> {FORWARD_HOST}:{FORWARD_PORT}")

        while True:
            client_socket, addr = server.accept()
            print(f"Connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    start_server()
