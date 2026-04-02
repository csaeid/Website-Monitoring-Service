# Website Monitoring Service

This is an interactive and professional Python tool that allows you to monitor website health and local computer system resources simultaneously in real-time from a single terminal screen.

Designed with a "Command Center" aesthetic, this project notifies the user of connection errors while automatically logging them in the background.

## ⭐ Key Features

- **Live Website Monitoring:** Checks the status code (HTTP 200, 404, 403, etc.) and Ping (latency in seconds) of any given URL.
- **System Resource Tracking:** Displays real-time local computer CPU, RAM, and Disk usage in percentages (%).
- **Secret Logging:** The moment a monitored site goes DOWN, the program automatically generates a `log.txt` file and records the exact time, date, and status code of the error.
- **"Armored" Architecture (`try-except`):** Built to be crash-proof. Even if the internet drops suddenly or a network error occurs, the program handles the exception seamlessly and continues monitoring.
- **Bot Protection Bypass:** Utilizes a custom `User-Agent` (Mac OS/Chrome mask) to bypass bot-blocking mechanisms on secure sites (e.g., Cloudflare).
- **Clean Terminal UI:** A sleek, compact user interface that refreshes dynamically and clears old data for a smooth monitoring experience.

## ⭐ Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/csaeid/Website-Monitoring-Service.git
   cd cyber-monitor
   ```

2. Install the required dependencies (requests and psutil):
    ```bash
    pip install requests psutil
    ```

3. Usage
    ```bash
    python main.py
    ```

The program will prompt you for the URL you wish to monitor. You can type a full link (e.g., https://github.com) or simply press Enter to monitor Google by default. To stop the monitor and exit safely, use the CTRL + C keyboard shortcut.

## ⭐ Terminal Preview
    ```
    Checking website...

Website: [https://www.google.com](https://www.google.com)
Status:  🟢 UP (HTTP 200)
Ping:    1.23 seconds
--------------------------------------------------
CPU Usage: 8.8%  |  RAM Usage: 52.1%  |  Disk Usage: 28.1%
```

## 📂 Project Structure
```
Cyber-Monitor/
│
├── main.py                    # Main execution script and UI layout
├── log.txt                    # (Auto-generated) Hidden error log history
│
└── Monitoring/                # Modular logic folder
    ├── cpu_percent.py         # Fetches CPU usage
    ├── virtual_memory.py      # Fetches RAM usage
    ├── disk_usage.py          # Fetches Disk usage
    └── website_checker.py     # Handles HTTP requests, masking, and ping logic
```
