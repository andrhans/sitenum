import pyfiglet
import requests
import sys
from datetime import datetime

welcome_banner=pyfiglet.figlet_format("Directory Enumeration")
print(welcome_banner)

url=sys.argv[1]

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

print("*" * 50)
print("Scan started...")
print("Start time: " + str(datetime.now()))
print("Scanning host: " +url)
print("*" * 50)

if len(sys.argv) == 3:
    wordlist=open(sys.argv[2], 'r')
    for line in wordlist:
        directory = line.strip()
        response=request(url+"/"+directory)
        if response:
            print("\n[*] Discovered directory: "+directory)
        else:
            continue
else:
    print("Missing argument(s). \nEspecify the host and the path of the wordlist. \n\nFor example:\npython dir-enum.py http://10.10.10.10 wordlist.txt")
