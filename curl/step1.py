import argparse
from urllib.parse import urlparse

'''
In this step your goal is to read the provided URL from the command line and print out the protocol text that would be sent for a GET request. 
'''
def read_url(url):
    parsed = urlparse(url)
    host = parsed.hostname
    path = parsed.path or "/"
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    protocol = parsed.scheme
    if parsed.query:
        path += "?" + parsed.query

    print(f"Connecting to {host}")
    print(f"Protocol: {protocol}")
    print(f"Sending request GET {path} HTTP/1.1")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print("Accept: */*")


def main():
    parser = argparse.ArgumentParser(prog='cccurl', description="A custom implementation of the 'curl' command.")
    parser.add_argument("cccurl", type=str, help="command to call curl")
    parser.add_argument("url",help="The target URL to process." )
    args = parser.parse_args()

    read_url(args.url)

if __name__ == "__main__":
    main()
