import socket
from logger import log_output

def grab_banner(ip, port):
    result = f"Banner grabbing result for {ip}:{port}\n"
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        result += f"[+] Banner: {banner}\n"
        print(result)
    except:
        result += "[-] Could not grab banner\n"
        print("[-] Could not grab banner")
    log_output("Banner Grabber", result)