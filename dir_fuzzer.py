import requests
from logger import log_output

def dir_fuzz(url):
    wordlist = ["admin", "login", "uploads", "test", "config"]
    result = f"Directory fuzzing results for {url}:\n"
    for word in wordlist:
        full_url = f"{url}/{word}"
        try:
            r = requests.get(full_url)
            if r.status_code == 200:
                line = f"[+] Found: {full_url}"
                print(line)
                result += line + "\n"
            else:
                result += f"[-] {full_url} - {r.status_code}\n"
        except requests.RequestException as e:
            result += f"[!] Error accessing {full_url}: {str(e)}\n"
    log_output("Directory Fuzzer", result)