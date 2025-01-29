import socket
import threading

# List of backend servers (IPs and ports)
backend_servers = [
    ('127.0.0.1', 5001),
    ('127.0.0.1', 5002),
    ('127.0.0.1', 5003)
]

current_server = 0

# Round-robin load balancing
def load_balancer(client_socket, address):
    global current_server
    backend_ip, backend_port = backend_servers[current_server]
    current_server = (current_server + 1) % len(backend_servers)

    # Connect to the selected backend server
    backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    backend_socket.connect((backend_ip, backend_port))

    # Receive the request from the client
    request = client_socket.recv(1024)

    # Forward request to backend server
    backend_socket.sendall(request)

    # Get the response from the backend server
    response = backend_socket.recv(1024)

    # Send the response back to the client
    client_socket.sendall(response)

    # Close the connections
    backend_socket.close()
    client_socket.close()

# Server to accept client requests
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(5)

    print("Load Balancer is running on port 5000...")

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=load_balancer, args=(client_socket, client_address)).start()

# Run the load balancer
if __name__ == "__main__":
    server()
