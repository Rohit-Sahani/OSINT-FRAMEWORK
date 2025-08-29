# This code is default ip scanner like (Nabbu) no fancy state management just an script that takes an IP and checks ports


import socket

def scan(ip):
    ports_to_scan = [22, 21, 80, 443, 8080]  # only 5 ports for faster scanning
    print(f"Scanning {ip} on ports: {ports_to_scan}\n")

    for port in ports_to_scan:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)  # short timeout for faster scan
            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")

            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")


if __name__ == "__main__":
    target = input("Enter IP to scan: ").strip()
    scan(target)












































# import socket

# def scan(ip):
#     print(f"Scanning {ip} (all , 65,535)")

#     for port in range(1 , 65536): # all port ranges
#         try:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             sock.settimeout(0.3)
#             result = sock.connect_ex((ip , port))

#             if result == 0:
#                 print(f"Port {port} is OPEN")
#             sock.close()
#         except:
#             pass



# if __name__ == "__main__":
#     target = input("Enter Ip to scan : ")
#     scan(target)