#!/usr/bin/python3

import requests

def main():
    zresp = requests.get("https://google.com")
    print(zresp)

if __name__ == "__main__":
    main()
