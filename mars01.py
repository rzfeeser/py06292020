#!/usr/bin/python3

import requests

# user should define sol to get photo back
MARS = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?camera=fhaz&api_key=DEMO_KEY"

def main():
    # sol is some kind of nasa scalar, should be investigated more
    thisday = input("Given the rover landed on day 1, which day would you like photos from? ")

    # pass the sol scalar which controls what photos we get
    zresp = requests.get(f"{MARS}&sol={thisday}")

    # strip off json from response
    zjson = zresp.json()

    # loop across each photo returned by response
    for photo in zjson['photos']:
        # dramatically announce that we are downloading photos
        print(f"Downloading... {photo['img_src']}")

        # use requests library to GET the image URL, just as if you were clicking on photos
        # via your web browser
        response = requests.get(photo['img_src'])
        # save each photo to the /home/student/static folder with same name it has when we downloaded it
        with open(f"/home/student/static/{photo['img_src'].split('/')[-1]}", "wb") as nasaphoto:
            # save out photo
            nasaphoto.write(response.content)

if __name__ == "__main__":
    main()
