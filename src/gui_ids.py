import os
import subprocess
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Function to run commands with subprocess
def run_command(command):
    try:
        output = subprocess.run(command, shell=True, text=True, capture_output=True)
        return output.stdout
    except Exception as e:
        return str(e)

# Function to start IDS
def start_ids():
    interface = entry_interface.get()
    if not interface:
        messagebox.showerror("Error", "Please enter a network interface")
        return
    command = f"sudo python3 simple_ids.py"
    subprocess.Popen(command, shell=True)
    text_area.insert(tk.END, f"Started IDS on interface: {interface}\n")

# Function to run Nmap SYN scan
def run_syn_scan():
    target_ip = entry_ip.get()
    if not target_ip:
        messagebox.showerror("Error", "Please enter a target IP")
        return
    command = f"sudo nmap -sS {target_ip}"
    output = run_command(command)
    text_area.insert(tk.END, f"Nmap SYN Scan Output:\n{output}\n")

# Function to view log files
def view_logs(log_file):
    try:
        with open(log_file, 'r') as file:
            content = file.read()
            text_area.insert(tk.END, f"Contents of {log_file}:\n{content}\n")
    except FileNotFoundError:
        messagebox.showerror("Error", f"Log file {log_file} not found")

# Creating the GUI window
window = tk.Tk()
window.title("Simple Network IDS GUI")
window.geometry("700x600")

# Interface Entry
label_interface = tk.Label(window, text="Enter Network Interface (e.g., wlan0):")
label_interface.pack(pady=5)
entry_interface = tk.Entry(window, width=50)
entry_interface.pack(pady=5)

# Start IDS Button
btn_start_ids = tk.Button(window, text="Start IDS", command=start_ids, width=20, bg='green', fg='white')
btn_start_ids.pack(pady=10)

# Target IP Entry
label_ip = tk.Label(window, text="Enter Target IP for SYN Scan:")
label_ip.pack(pady=5)
entry_ip = tk.Entry(window, width=50)
entry_ip.pack(pady=5)

# Run Nmap SYN Scan Button
btn_syn_scan = tk.Button(window, text="Run Nmap SYN Scan", command=run_syn_scan, width=20, bg='blue', fg='white')
btn_syn_scan.pack(pady=10)

# Log File Buttons
btn_alerts_log = tk.Button(window, text="View Alerts Log", command=lambda: view_logs('../logs/alerts.log'), width=20)
btn_alerts_log.pack(pady=5)
btn_error_log = tk.Button(window, text="View Error Log", command=lambda: view_logs('../logs/error.log'), width=20)
btn_error_log.pack(pady=5)
btn_activity_log = tk.Button(window, text="View Activity Log", command=lambda: view_logs('../logs/activity.log'), width=20)
btn_activity_log.pack(pady=5)

# Output Text Area
text_area = scrolledtext.ScrolledText(window, width=80, height=20)
text_area.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()


