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


2. **Run the Script**
   ```bash
   python3 port_scanner.py
   ```
   
   - When prompted, enter the target IP address (e.g., `192.168.1.27`).
   - Then provide the starting and ending port numbers (e.g., `20` to `25`).

3. **Observe the Output**  
   The script will print whether each port in the specified range is **OPEN** or **CLOSED**.

---

## Screenshots

1. **"ip addr show" command:** Verifies the target machine's IP address.  
   ![Target Host IP](screenshots/ipaddrshow.png)

2. **Ping command:** Verifies the connection between host and target machines.  
   ![Ping Command Output](screenshots/pingcommand.png)

3. **Python script:** The port scanner script.  
   ![Port Scanner Script](screenshots/portscannerpythonscript.png)
   
4. **First run output:** The script's output on the first run.  
   ![First Run and Output](screenshots/portscanneroutput1.png)

5. **SSH startup:** Opening port 22 via SSH.  
   ![Open Port 22 / SSH](screenshots/startsshonkali.png)

6. **Second run output:** The script's output on the second run.  
   ![Second Run and Output](screenshots/portscanneroutput2.png)

---

## Notes

- **Ethical Use Only:** Please use this tool responsibly. Scanning ports without permission may violate laws or terms of service.
- You can experiment further by enabling various network services on your target machine (e.g., SSH, FTP, HTTP) and observing the scanner’s output.
- Enhancements to the script can include multithreading for faster scans, banner grabbing to identify running services, and command-line arguments for increased flexibility.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. Please see the LICENSE file for more details.

---

## Contact

**Author:** Chet Flowers  
**GitHub:** [chetflowers](https://github.com/chetflowers)
```
