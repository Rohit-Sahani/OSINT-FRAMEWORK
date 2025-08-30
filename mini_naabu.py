# This code is default ip scanner like (Nabbu) no fancy state management just an script that takes an IP and checks ports


import socket

def scan(ip):
    # Full port range from 1 to 65535
    ports_to_scan = range(1, 65536)  
    print(f"Scanning {ip} on ports: 1–65535\n")

    for port in ports_to_scan:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)  # short timeout for faster scan
            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target = input("Enter IP to scan: ").strip()
    scan(target)
