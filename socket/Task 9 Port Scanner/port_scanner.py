import socket

def scan_ports(target, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        sock.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Replace with the target IP address
    ports_to_scan = [22, 80, 443, 8080, 5555]
    scan_ports(target_ip, ports_to_scan)
