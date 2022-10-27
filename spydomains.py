import requests
from threading import Thread, Lock
from queue import Queue

q = Queue()
list_lock = Lock()
discovered_domains = []


def scan_subdomains(domain):
    global q
    while True:
        
        subdomain = q.get()
        
        url = f"https://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain:", url)
            
            with list_lock:
                discovered_domains.append(url)

        
        q.task_done()
