from scapy.all import IP, TCP, sr

# Define the target
target_ip = "8.8.8.8"
target_port = 80  # HTTP port

# Craft a TCP SYN packet
packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

# Send the packet and capture the response
print("Sending TCP SYN packet to:", target_ip)
response, _ = sr(packet, timeout=2)  # Send and receive packets

# Analyze the response
if response:
    print("\n--- Response Received ---")
    for sent, received in response:
        print("Source IP:", received.src)
        print("Flags:", received[TCP].flags)
        print("TTL:", received.ttl)
else:
    print("\nNo response received.")
