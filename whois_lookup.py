import subprocess
from logger import log_output

def get_whois_info(domain):
    result = f"WHOIS info for {domain}:\n"
    try:
        whois_result = subprocess.run(["whois", domain], capture_output=True, text=True)
        result += whois_result.stdout
        print(whois_result.stdout)
    except Exception as e:
        error_msg = f"[-] Error during WHOIS lookup: {str(e)}"
        print(error_msg)
        result += error_msg
    log_output("WHOIS Lookup", result)