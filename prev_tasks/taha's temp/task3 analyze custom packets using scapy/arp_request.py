from scapy.all import ARP, Ether, srp

# Define the target network
target_ip = "192.168.1.1/24"  # Replace with your network range

# Craft an ARP request
arp_request = ARP(pdst=target_ip)
ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast frame
packet = ether_frame/arp_request

# Send the packet and capture responses
print("Sending ARP request...")
responses, _ = srp(packet, timeout=2, verbose=False)

# Analyze responses
print("\n--- Devices Found ---")
for sent, received in responses:
    print("IP Address:", received.psrc)
    print("MAC Address:", received.hwsrc)
