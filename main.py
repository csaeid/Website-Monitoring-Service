import os
import time

from Monitoring.cpu_percent import get_cpu_percent
from Monitoring.virtual_memory import get_ram_percent
from Monitoring.disk_usage import get_disk_usage
from Monitoring.website_checker import check_website    

url = input("Enter a website URL to check (or 'CTRL + C' to quit): ")
print("Checking website...")

if url.strip() == "":
    url = "https://www.google.com"

try:
    while True:
        website_status = check_website(url)
        cpu_percent = get_cpu_percent()
        ram_percent = get_ram_percent()
        disk_usage = get_disk_usage()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"➤  Website: {website_status['url']}")
        print(f"➤  Status: {'🟢 UP' if website_status['is_up'] else '🔴 DOWN'} (HTTP {website_status['status']})")
        print(f"➤  Ping: {website_status['ping_sec']} seconds")
        print("──────────────────────────────────────────────────────────────────────────────────")
        print(f"• CPU: {cpu_percent}% | • RAM: {ram_percent}% | • Disk: {disk_usage}%")
        time.sleep(1) 

except KeyboardInterrupt:
    print("\nExiting...")
    os.system('cls' if os.name == 'nt' else 'clear')


