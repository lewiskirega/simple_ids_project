from scapy.all import IP, TCP, ICMP, UDP, wrpcap

# List to hold all packets
packets = []

# 1. Normal Traffic: HTTP Request Simulation (TCP packets)
# Simulate an HTTP SYN packet to port 80 of a web server
packets.append(IP(dst='192.168.1.10') / TCP(dport=80, sport=12345, flags='S'))

# 2. Normal Traffic: DNS Query (UDP packet)
# Simulate a DNS query to port 53
packets.append(IP(dst='192.168.1.11') / UDP(dport=53, sport=23456))

# 3. Malicious Traffic: SYN Scan Simulation
# Generate multiple SYN packets to simulate a port scanning attack
for port in range(20, 30):
    packets.append(IP(dst='192.168.1.20') / TCP(dport=port, sport=34567, flags='S'))

# 4. Malicious Traffic: ICMP Flood Simulation
# Simulate an ICMP (ping) flood
for i in range(5):
    packets.append(IP(dst='192.168.1.30') / ICMP())

# 5. Malicious Traffic: Brute-Force Login Attempt Simulation
# Simulate multiple failed connection attempts to represent brute-force attempts
for i in range(3):
    packets.append(IP(dst='192.168.1.40') / TCP(dport=22, sport=45678 + i, flags='S'))

# Write all the packets to a pcap file
wrpcap('../data/test_data.pcap', packets)
