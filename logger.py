import os
from datetime import datetime

LOG_FILE = "logs/output.txt"

def log_output(module_name, content):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- {module_name.upper()} | {datetime.now()} ---\n")
        f.write(content + "\n")