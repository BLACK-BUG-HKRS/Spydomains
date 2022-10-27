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




def main(domain, n_threads, subdomains):
    global q

    for subdomain in subdomains:
        q.put(subdomain)

    for t in range(n_threads):
        worker = Thread(target=scan_subdomains, args=(domain,))
        worker.daemon = True
        worker.start()



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Faster Subdomain Scanner using Threads")
    parser.add_argument("domain", help="Domain to scan for subdomains without protocol (e.g without 'http://' or 'https://')")
    parser.add_argument("-l", "--wordlist", help="File that contains all subdomains to scan, line by line. Default is subdomains.txt",
                        default="subdomains.txt")
    parser.add_argument("-t", "--num-threads", help="Number of threads to use to scan the domain. Default is 10", default=10, type=int)
    parser.add_argument("-o", "--output-file", help="Specify the output text file to write discovered subdomains", default="discovered-subdomains.txt")
    
    args = parser.parse_args()