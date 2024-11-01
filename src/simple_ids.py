import logging
import os
from scapy.all import sniff, IP, TCP, ICMP

# Set up logging directories and configuration
log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Alerts logger for suspicious activities
alerts_logger = logging.getLogger('alerts_logger')
alerts_handler = logging.FileHandler(os.path.join(log_dir, 'alerts.log'))
alerts_logger.addHandler(alerts_handler)
alerts_logger.setLevel(logging.WARNING)

# Activity logger for general events
activity_logger = logging.getLogger('activity_logger')
activity_handler = logging.FileHandler(os.path.join(log_dir, 'activity.log'))
activity_logger.addHandler(activity_handler)
activity_logger.setLevel(logging.INFO)

# Error logger for errors during packet analysis
error_logger = logging.getLogger('error_logger')
error_handler = logging.FileHandler(os.path.join(log_dir, 'error.log'))
error_logger.addHandler(error_handler)
error_logger.setLevel(logging.ERROR)

# Log the starting of the IDS
activity_logger.info('Starting the IDS...')

# Define a packet analysis function to detect malicious activities
def analyze_packet(packet):
    try:
        if packet.haslayer(TCP):
            # Example: Detecting potential port scan (TCP SYN scan)
            if packet[TCP].flags == 'S':
                alerts_logger.warning(f"Suspicious activity detected: Possible SYN scan from IP {packet[IP].src}")
        
        elif packet.haslayer(ICMP):
            # Detect ICMP Ping requests (ICMP Echo Requests)
            if packet[ICMP].type == 8:  # Type 8 is Echo Request (Ping)
                alerts_logger.warning(f"ICMP Ping request detected from IP {packet[IP].src}")
                activity_logger.info(f"ICMP packet detected from {packet[IP].src}")

    except Exception as e:
        error_logger.error(f"Error analyzing packet: {str(e)}")

# Sniff packets on the network interface (e.g., eth0)
try:
    interface = input("Enter the network interface to monitor (e.g., eth0, wlan0): ").strip()
    if not interface:
        raise ValueError("No network interface provided.")

    # Log the interface being used
    activity_logger.info(f"Monitoring network interface: {interface}")

    print(f"Starting packet capture on {interface}... (Press CTRL+C to stop)")

    # Start sniffing
    sniff(iface=interface, prn=analyze_packet, store=False)

except KeyboardInterrupt:
    print("\nStopping the IDS...")
    activity_logger.info('Stopping the IDS...')

except PermissionError:
    print("Error: Permission denied. Please run the script with elevated privileges (e.g., using 'sudo').")
    error_logger.error('Permission denied. Please run the script with elevated privileges.')

except Exception as e:
    print(f"Error during packet capture: {str(e)}")
    error_logger.error(f"Error during packet capture: {str(e)}")
