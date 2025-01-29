import socket

def client_request():
    # Connect to the load balancer (which listens on port 5000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))
    
    # Send a request to the load balancer
    client_socket.sendall(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')

    # Receive the response
    response = client_socket.recv(1024)
    print(f"Response from Load Balancer: {response.decode()}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    client_request()
