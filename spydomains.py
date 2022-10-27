import requests
from threading import Thread, Lock
from queue import Queue

q = Queue()
list_lock = Lock()
discovered_domains = []
