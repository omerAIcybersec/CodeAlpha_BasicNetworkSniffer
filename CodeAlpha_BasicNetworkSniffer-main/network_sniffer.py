from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        print("\n--- Packet Captured ---")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

print("Starting Network Sniffer...")
print("Press Ctrl + C to stop.\n")

sniff(prn=packet_callback, store=False)