# Penetration Testing Toolkit

A modular Python toolkit for beginners and cybersecurity learners to practice penetration testing. Includes tools for scanning, brute forcing, directory fuzzing, and gathering network information. Logs all results to `logs/output.txt`.

---

## Modules Included

| Module             | Purpose                                |
|--------------------|----------------------------------------|
| 1. Port Scanner     | Scan for open ports on a target IP     |
| 2. FTP Brute Forcer | Attempt weak login credentials on FTP  |
| 3. Directory Fuzzer | Discover hidden paths on web servers   |
| 4. Banner Grabber   | Capture service banners for analysis   |
| 5. WHOIS Lookup     | Fetch domain registration information  |

---

## Module Explanations

### 1. **Port Scanner**
- **What it does:** Tries connecting to a range of ports on a target IP.
- **Goal:** Identify open ports (e.g., 22 for SSH, 80 for HTTP).
- **Code logic:** Uses `socket.connect()` with timeout.
- **Use:** Network mapping.

### 2. **FTP Brute Forcer**
- **What it does:** Attempts logins on FTP using a small username/password list.
- **Goal:** Identify weak or default credentials.
- **Code logic:** Uses `ftplib.FTP()` to try logging in.
- **Use:** Password vulnerability testing.

### 3. **Directory Fuzzer**
- **What it does:** Tries accessing common web directories like `/admin`, `/uploads`.
- **Goal:** Reveal hidden pages or unsecured endpoints.
- **Code logic:** Sends `GET` requests using `requests`.
- **Use:** Web app enumeration.

### 4. **Banner Grabber**
- **What it does:** Connects to a port and captures banner text (e.g., FTP welcome message).
- **Goal:** Identify software/version running on a port.
- **Code logic:** Uses `socket.recv()` after connecting.
- **Use:** Service fingerprinting.

### 5. **WHOIS Lookup**
- **What it does:** Queries WHOIS servers for domain info.
- **Goal:** Find domain owner, registrar, creation/expiry.
- **Code logic:** Uses `subprocess.run()` to call system `whois`.
- **Use:** OSINT (Open Source Intelligence).

---

## What you will see after runing the code:

1. Port Scanner
2. FTP Brute Forcer
3. Directory Fuzzer
4. Banner Grabber
5. WHOIS Lookup
0. Exit

Choose a module:

---

## Sample Outputs

### Port Scanner:

[+] Port 21 is OPEN
[+] Port 80 is OPEN

### FTP Brute Force:

[+] Success: admin:admin

### Directory Fuzzer:

[+] Found: http://localhost/admin

### Banner Grabber:

220 FileZilla Server 1.6 ready

### WHOIS Lookup:

Registrar: GoDaddy.com
Creation Date: 2021-05-01

