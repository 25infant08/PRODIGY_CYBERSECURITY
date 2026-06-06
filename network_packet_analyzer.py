from scapy.all import sniff, IP, TCP, UDP, ICMP
def packet_analyzer(packet):
    try:
        if packet.haslayer(IP):
            source_ip = packet[IP].src
            destination_ip = packet[IP].dst
            print("========== PACKET CAPTURED ==========")
            print("Source IP Address      :", source_ip)
            print("Destination IP Address :", destination_ip)
            if packet.haslayer(TCP):
                print("Protocol               : TCP")
            elif packet.haslayer(UDP):
                print("Protocol               : UDP")
            elif packet.haslayer(ICMP):
                print("Protocol               : ICMP")
            else:
                print("Protocol               : Other")
            print("Packet Size            :", len(packet), "bytes")
            print("=====================================")
    except Exception as error:
        print("Error while analyzing packet :", error)
print("=====================================")
print("     NETWORK PACKET ANALYZER")
print("=====================================")
print("Monitoring Network Traffic...")
print("Press CTRL + C to Stop")
try:
    sniff(prn=packet_analyzer, store=False)
except KeyboardInterrupt:
    print("Packet Analyzer Stopped.")
except Exception as error:
    print("An Error Occurred :", error)