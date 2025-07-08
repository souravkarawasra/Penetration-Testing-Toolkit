from port_scanner import scan_ports
from brute_forcer import ftp_brute_force
from dir_fuzzer import dir_fuzz
from banner_grabber import grab_banner
from whois_lookup import get_whois_info

def menu():
    print("""
    PENETRATION TESTING TOOLKIT
    ---------------------------
    1. Port Scanner
    2. FTP Brute Forcer
    3. Directory Fuzzer
    4. Banner Grabber
    5. WHOIS Lookup
    0. Exit
    """)

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose a module: ")

        if choice == "1":
            ip = input("Enter target IP: ")
            scan_ports(ip)
        elif choice == "2":
            ip = input("Enter target FTP server: ")
            ftp_brute_force(ip)
        elif choice == "3":
            url = input("Enter target URL (e.g., http://example.com): ")
            dir_fuzz(url)
        elif choice == "4":
            ip = input("Enter target IP: ")
            port = int(input("Enter port: "))
            grab_banner(ip, port)
        elif choice == "5":
            domain = input("Enter domain: ")
            get_whois_info(domain)
        elif choice == "0":
            print("Exiting toolkit.")
            break
        else:
            print("Invalid option. Try again.")