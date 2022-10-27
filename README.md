# Subdomain Brute-forcer
Find subdomain using this subdomain brute forcer

to use this using python:

- `pip3 install -r reqirements.txt`

```
python spydomains.py --help
```

output:

```
usage: spydomains.py [-h] [-l WORDLIST] [-t NUM_THREADS] [-o OUTPUT_FILE] domain

Faster Subdomain Scanner using Threads

positional arguments:
  domain                Domain to scan for subdomains without protocol (e.g without 'http://' or 'https://')

options:
  -h, --help            show this help message and exit
  -l WORDLIST, --wordlist WORDLIST
                        File that contains all subdomains to scan, line by line. Default is subdomains.txt  
  -t NUM_THREADS, --num-threads NUM_THREADS
                        Number of threads to use to scan the domain. Default is 10
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Specify the output text file to write discovered subdomains
```

If you want to scan hackthissite.org for subdomains using only 1000 threads with a word list of 20000 subdomains (`/files/subdomains.txt`)

```
python spydomains.py hackthissite.org -l ./files/subdomains.txt -t 1000
```

after sometime, its output:

```
[+] Discovered subdomain: https://mail.hackthissite.org
[+] Discovered subdomain: https://www.hackthissite.org
[+] Discovered subdomain: https://stats.hackthissite.org
[+] Discovered subdomain: https://forums.hackthissite.org
[+] Discovered subdomain: https://mirror.hackthissite.org
[+] Discovered subdomain: https://irc.hackthissite.org
[+] Discovered subdomain: https://MAIL.hackthissite.org
[+] Discovered subdomain: https://hp.hackthissite.org
[+] Discovered subdomain: https://WWW.hackthissite.org
[+] Discovered subdomain: https://legal.hackthissite.org
...
```

If you want to output the discovered URLs to a file:

```
python spydomains.py hackthissite.org -l ./files/subdomains.txt -t 1000 -o discovered_urls.txt
```

This will create a new file `discovered_urls.txt` that includes the discovered subdomains.
