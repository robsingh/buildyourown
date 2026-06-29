# In this step, your goal is to read the provided URL from the command line and print out the protocol text that would be sent for
# a GET request.

import sys

def read_url(url):
    '''we cannot use requests library!'''
      


def main():
    if len(sys.argv) != 2:
        print("Usage: ccurl url")
        sys.exit(1)
    
    url = sys.argv[1]
    print(read_url(url))
    
(main())