import socket

# Server settings
SERVER_HOST = '127.0.0.1'  # Server IP
SERVER_PORT = 12345        # Server port

def request_file():
    """Request a file from the server."""
    # Connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        # Request file name from the user
        file_name = input("Enter the name of the file you want to download: ")

        # Send the file name to the server
        client_socket.send(file_name.encode())

        # Receive the file content from the server
        data = client_socket.recv(1024)
        
        # Check if the server sent an error message
        if data.startswith(b"ERROR"):
            print(data.decode())
        else:
            # Save the received file content to the current directory
            with open(file_name, 'wb') as file:
                while data:
                    file.write(data)
                    data = client_socket.recv(1024)
                print(f"File '{file_name}' downloaded successfully.")

if __name__ == "__main__":
    request_file()
