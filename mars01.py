#!/usr/bin/python3

import requests

# user should define sol to get photo back
MARS = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?camera=fhaz&api_key=DEMO_KEY"

def main():
    thisday = input("Given the rover landed on day 1, which day would you like photos from? ")

    zresp = requests.get(f"{MARS}&sol={thisday}")

    zjson = zresp.json()

    for photo in zjson['photos']:
        print(photo['img_src'])
        print()


if __name__ == "__main__":
    main()
