import csv
from scapy.all import *

def csv_to_pcap(csv_file, pcap_file):
    # Create a packet list
    packets = []
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create an IP packet based on CSV row
            packet = IP(src=row['src_ip'], dst=row['dst_ip']) / TCP() / row['payload']
            packets.append(packet)
    
    # Write the packets to a pcap file
    wrpcap(pcap_file, packets)

csv_to_pcap('your_file.csv', 'output.pcap')
