import socket
import threading

# Server settings
SERVER_HOST = '127.0.0.1'  # The server's IP address
SERVER_PORT = 12345        # The server's port

def receive_messages(client_socket):
    """Listen for messages from the server and display them."""
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"\n{message.decode()}")
            else:
                break
        except:
            break

def start_client():
    """Starts the client, connects to the server, and sends messages."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        # Start a thread to listen for messages from the server
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        # Enter username
        username = input("Enter your username: ")
        client_socket.send(username.encode())

        print("Connected to the server. Type your messages:")
        while True:
            message = input()  # Take input from the user
            if message.lower() == 'exit':
                print("Disconnecting...")
                break
            elif message.startswith("/private"):
                # Send private message
                client_socket.send(message.encode())
            else:
                # Send general message
                client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()
