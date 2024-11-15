#Python Firewall PT2.
#DOS: attacker aims to disrupt your network or computer by flooding the system with data packets
#Scapy: allows professionals to review network packets

import os #interact with operating system
import sys #handles system specific operations (exiting script)
import time #time intervals
from collections import defaultdict #manage and store packet counts for each IP address
from scapy.all import sniff, IP #monitor network traffic

#Variable representing the threshold for a DOS attack
THRESHOLD = 40
print(f"THRESHOLD:  {THRESHOLD}")

def packet_callback(packet):
    src_ip = packet[IP].src
    packet_count[src_ip] += 1
    current_time = time.time()
    time_interval = current_time - start_time[0]

    if time_interval >= 1:
        for ip, count in packet_count.items():
            packet_rate = count / time_interval
            if packet_rate > THRESHOLD and ip not in blocked_ips:
                print(f"Blocking IP: {ip}, packet rate: {packet_rate}")
                os.system(f"iptables -A INPUT -s {ip} -j DROP")
                blocked_ips.add(ip)
                
        packet_count.clear()
        start_time[0] = current_time
    

if __name__ == "__main__":
    if os.getuid() != 0:
        print("This script requires root priveleges.")
        sys.exit(1)
    packet_count = defaultdict(int)
    start_time = [time.time()]
    blocked_ips = set()

    print("Monitoring network traffic")
    sniff(filter="ip", prn=packet_callback)