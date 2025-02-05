import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        sock.close()
        return True
    except:
        return False

def main():
    target_ip = input("Enter IP address to scan: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"Scanning ports {start_port} to {end_port} on {target_ip}...")
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

if __name__ == "__main__":
    main()
