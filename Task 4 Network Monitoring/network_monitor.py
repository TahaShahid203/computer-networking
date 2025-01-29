import time
from pythonping import ping
import scapy.all as scapy

# Define devices to monitor
devices = {
    "Router": "192.168.1.1",
    "Laptop": "192.168.1.100",
    "Printer": "192.168.1.50"
}

def check_device_status(ip):
    """Ping the device and return True if reachable, else False."""
    response = ping(ip, count=2, timeout=1)
    return response.success()

def scan_network(network_range="192.168.1.1/24"):
    """Scan the network and list active devices."""
    arp_request = scapy.ARP(pdst=network_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    devices_list = []
    for sent, received in answered:
        devices_list.append({"IP": received.psrc, "MAC": received.hwsrc})
    
    return devices_list

if __name__ == "__main__":
    print("Starting network monitoring...")
    
    while True:
        print("\nChecking device status:")
        for name, ip in devices.items():
            status = "Online" if check_device_status(ip) else "Offline"
            print(f"{name} ({ip}) - {status}")

        print("\nScanning network for active devices...")
        active_devices = scan_network()
        for device in active_devices:
            print(f"IP: {device['IP']}, MAC: {device['MAC']}")
            

        print("\nSleeping for 30 seconds before the next scan...\n")
        time.sleep(30)  # Wait 30 seconds before the next check
