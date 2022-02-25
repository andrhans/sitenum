import pyfiglet
import requests

welcome_banner=pyfiglet.figlet_format("Directory Discovery")
print(welcome_banner)

target=input("Enter target host: ")
file=input("Enter wordlist location: ")

def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

wordlist=open(file, 'r')
for line in wordlist:
    dir=line.strip()
    long_url=target+"/"+dir
    response=request(long_url)
    if response:
        print("[*] Directory discovered: "+long_url)
