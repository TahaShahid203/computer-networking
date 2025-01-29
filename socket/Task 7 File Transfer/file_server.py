import socket
import os

# Server settings
SERVER_HOST = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 12345       # Port to listen on
SERVER_DIR = 'shared_files'  # Directory to serve files from

# Ensure the shared directory exists
if not os.path.exists(SERVER_DIR):
    os.makedirs(SERVER_DIR)

def handle_client(client_socket):
    """Handle the incoming client request and send the requested file."""
    try:
        # Receive the file request from the client
        requested_file = client_socket.recv(1024).decode()

        # Check if the file exists
        file_path = os.path.join(SERVER_DIR, requested_file)
        if os.path.isfile(file_path):
            # Send file content to the client
            with open(file_path, 'rb') as file:
                data = file.read()
                client_socket.sendall(data)
                print(f"Sent {requested_file} to the client.")
        else:
            # Send an error message if the file is not found
            client_socket.send("ERROR: File not found.".encode())
    except Exception as e:
        print(f"Error: {e}")
        client_socket.send("ERROR: An unexpected error occurred.".encode())
    finally:
        client_socket.close()

def start_server():
    """Start the file server and listen for incoming requests."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(1)
        print(f"File server running on {SERVER_HOST}:{SERVER_PORT}. Serving files from '{SERVER_DIR}'.")

        while True:
            client_socket, _ = server_socket.accept()
            print("Client connected.")
            handle_client(client_socket)

if __name__ == "__main__":
    start_server()
