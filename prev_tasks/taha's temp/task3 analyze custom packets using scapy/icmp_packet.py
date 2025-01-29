from scapy.all import IP, ICMP, sr1

# Define the target IP
target_ip = "8.8.8.8"  # Google DNS

# Craft an ICMP packet (Ping)
packet = IP(dst=target_ip)/ICMP()

# Send the packet and wait for a response
print("Sending ICMP packet to:", target_ip)
response = sr1(packet, timeout=2)  # Sends and waits for 1 response

# Analyze the response
if response:
    print("\n--- Response Received ---")
    print("Source IP:", response.src)
    print("TTL (Time to Live):", response.ttl)
    print("Protocol:", response.proto)
else:
    print("\nNo response received.")
