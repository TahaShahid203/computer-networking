import socket
import threading

# Server settings
SERVER_HOST = '0.0.0.0'  # Listen on all available interfaces
SERVER_PORT = 12345       # Port to listen on

clients = {}  # Dictionary to store clients' usernames and sockets

def handle_client(client_socket, client_address):
    """Handles messages from a client."""
    # Request and set username
    client_socket.send("Enter your username:".encode())
    username = client_socket.recv(1024).decode()
    
    clients[username] = client_socket
    print(f"User {username} connected from {client_address}")
    
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024)
            if not message:
                break

            # Check if it's a private message
            if message.decode().startswith("/private"):
                # Private message format: /private <username> <message>
                parts = message.decode().split(" ", 2)
                if len(parts) > 2 and parts[1] in clients:
                    private_message = parts[2]
                    clients[parts[1]].send(f"Private message from {username}: {private_message}".encode())
                else:
                    client_socket.send(f"User {parts[1]} not found.".encode())
            else:
                # Broadcast the message to all other clients
                broadcast(f"{username}: {message.decode()}", client_socket)
        except:
            break

    # Remove the client when they disconnect
    del clients[username]
    client_socket.close()

def broadcast(message, sender_socket):
    """Broadcast the message to all connected clients."""
    for client_socket in clients.values():
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except:
                pass

def start_server():
    """Starts the chat server to listen for incoming connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(5)
        print(f"Chat server running on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            # Accept incoming client connections
            client_socket, client_address = server_socket.accept()
            
            # Handle the client in a new thread
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()

if __name__ == "__main__":
    start_server()
