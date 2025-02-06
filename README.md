# Port Scanner Project with Kali and Python

A beginner-friendly Python script for scanning ports on a specified IP address.  
This project demonstrates basic cybersecurity and network concepts, such as TCP connections and port discovery.

---

## Description

This **port scanner** allows you to:
- Input a target IP or hostname.
- Specify a range of ports to scan.
- Determine which ports are open or closed by attempting TCP connections on each port.

**Why is this useful?**  
Port scanning is a fundamental step in network reconnaissance for both ethical hacking and security assessments. By knowing which ports are open on a system, you can identify potential attack vectors or services running on those ports.

---

## Requirements

- **Python 3.x** installed on your system.
- A basic understanding of networking concepts is helpful but not mandatory.

---

## How to Use

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/chetflowers/Port-Scanner-Project-with-Kali-and-Python.git
   cd Port-Scanner-Project-with-Kali-and-Python
   ```

2.	**Run the Script**

   ```bash
   python3 port_scanner.py
   ```

- When prompted, enter the target IP address (e.g., 192.168.1.27).
- Then provide the starting and ending port numbers (e.g., 20 to 25).

3.	**Observe the Output**
- The script will print whether each port in the specified range is OPEN or CLOSED.

## Screenshots

1.	The “ip addr show” command to verify the target machine’s IP address.
2.	The ping command verifying the connection between host and target machines.
3.	Port scanner Python script.
4.	First run and output of script.
5.	Starting SSH to open port 22.
6.	Second run and output of script.

## Notes
- Ethical Use Only: Please use this tool responsibly. Scanning ports without permission may violate laws or terms of service.
- You can experiment further by enabling various network services on your target machine (e.g., SSH, FTP, HTTP) and observing the scanner’s output.
- Enhancements to the script can include multithreading for faster scans, banner grabbing to identify running services, and command-line arguments for flexibility.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. Please see the LICENSE file for more details.
