# Simple Network Intrusion Detection System (IDS)

## Project Overview
The Simple Network Intrusion Detection System (IDS) is designed to monitor a network interface for potentially harmful or suspicious activities. This project utilizes Python, Scapy, and logging to capture, analyze, and log network traffic, aiming to enhance network security and provide foundational experience with intrusion detection mechanisms.

The project also features a GUI interface for easier interaction, allowing users to start/stop the IDS, run network scans, and view log files without using the command line. The IDS can identify basic suspicious activities, such as SYN scans and ICMP floods, which are often used as part of cyberattacks.

## Project Structure
The project is organized into the following directory structure:

```
simple_ids_project/
├── src/
│   ├── simple_ids.py           # Main IDS script for monitoring network traffic
│   ├── gui_ids.py              # GUI script for controlling the IDS
│   └── test_data_generator.py  # Script to generate test_data.pcap for testing
├── data/
│   └── test_data.pcap          # Packet capture file with normal and malicious traffic for testing
├── logs/
│   ├── alerts.log              # Logs of detected suspicious activities
│   ├── error.log               # Logs errors encountered by the IDS
│   └── activity.log            # General log of IDS activities
├── project_proposal.md         # Project proposal for the IDS
├── README.md                   # Documentation and instructions for the project
└── venv/                       # (Optional) Virtual environment for managing dependencies
```

## Features
- **Network Monitoring**: The IDS monitors the specified network interface to capture and analyze packets in real-time.
- **Packet Analysis**: Detects suspicious activities, such as TCP SYN scans (common for port scanning) and ICMP packets (ping flood attacks).
- **Logging**:
  - `alerts.log`: Logs detected suspicious activities.
  - `error.log`: Logs any errors encountered by the IDS during execution.
  - `activity.log`: Logs general activities of the IDS, including starting, stopping, and monitoring operations.
- **GUI Interface**: A user-friendly GUI (`gui_ids.py`) built with Tkinter to control the IDS, run scans, and view logs.
- **Test Data Generation**: A script (`test_data_generator.py`) to generate network traffic for testing purposes, including both normal and malicious traffic.

## Prerequisites
- **Python 3.x**
- **Scapy**: For packet capturing and analysis.
  ```bash
  pip install scapy
  ```
- **Tkinter**: For the graphical user interface. Typically comes pre-installed with Python.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd simple_ids_project
   ```

2. **Set Up Virtual Environment (Optional)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install scapy
   ```

## Running the Project

### 1. Generate Test Data
Generate simulated network traffic for testing the IDS.
```bash
python3 src/test_data_generator.py
```
This will create a `.pcap` file in the `data/` directory, which can be used to test IDS detection capabilities.

### 2. Run the IDS
To start the IDS and monitor a network interface:
```bash
cd src
sudo python3 simple_ids.py
```
- You will be prompted to enter the network interface (e.g., `wlan0`, `eth0`). Make sure to run with `sudo` since packet sniffing requires elevated privileges.

### 3. Use the GUI (Optional)
To use the graphical interface to control the IDS:
```bash
python3 src/gui_ids.py
```
- **Start IDS**: Enter the network interface and click "Start IDS".
- **Run SYN Scan**: Enter a target IP to generate a SYN scan.
- **View Logs**: Use the buttons to view `alerts.log`, `error.log`, and `activity.log`.

## Log Files
- **`alerts.log`**: Contains information about suspicious activities detected by the IDS, such as SYN scans or ICMP floods.
- **`error.log`**: Captures errors or exceptions that occur during IDS operation, such as permission issues or packet processing errors.
- **`activity.log`**: Logs general IDS activities, like starting and stopping monitoring, and detection of non-suspicious events (e.g., ICMP pings).

## Important Notes
- **Permissions**: The IDS requires root privileges to sniff network traffic. Always run the IDS script with `sudo`.
- **Testing Environment**: It is recommended to run tests in a controlled environment, such as a local network or using virtual machines, to avoid unintended consequences.
- **Legal and Ethical Use**: Do not scan IP addresses or networks without permission. Unauthorized scanning may have legal implications.

## Future Improvements
- **Add More Detection Rules**: Implement more sophisticated rules to detect a wider variety of network attacks (e.g., ARP spoofing, DNS tunneling).
- **Log Rotation**: Implement log rotation to manage the size of log files over time.
- **Visualization**: Add real-time visualization of network traffic and detected threats using libraries like `matplotlib` or integrating with ELK stack.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes you wish to make.

## License
This project is licensed under the MIT License.

## Acknowledgements
- **Scapy**: For packet capture and analysis.
- **Tkinter**: For building the GUI.

## Contact
For any questions or issues, feel free to reach out via email or open an issue in the repository.
