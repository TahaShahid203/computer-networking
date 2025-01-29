from scapy.all import sniff

# Define a callback to process packets


def packet_callback(packet):
    print(packet.summary())  # Print a one-line summary of each packet
    print(packet.show())    # Print detailed packet information


# Start sniffing on the default interface
print("Sniffing packets...")
sniff(count=5, prn=packet_callback)  # Capture 5 packets
