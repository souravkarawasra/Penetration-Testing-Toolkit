import socket
from logger import log_output

def scan_ports(target):
    print(f"[+] Scanning ports on {target}")
    result = f"Scanning ports on {target}\n"
    for port in range(1, 1024):
        try:
            sock = socket.socket()
            sock.settimeout(0.3)
            sock.connect((target, port))
            line = f"[+] Port {port} is OPEN"
            print(line)
            result += line + "\n"
            sock.close()
        except:
            continue
    log_output("Port Scanner", result)