#!/usr/bin/python3
"""
Wed morning exercise

API Example:
http://ip-api.com/json/24.48.0.1
API Example:
http://ip-api.com/json/24.48.0.1

Write a Python script that accepts an IPv4 address from the user, and returns where that IP address is in the world along with any other
info you'd like

Optional Challenge 01 - Supply a list of IPs via an external file. Have your program look up each one, and write into the file where that IP address is located.
                      - alternative (or also) try passing command line arguments

Optional Challenge 02 - Map the location on a map of the world :p Write the new image out as a stand-alone file (for example, as a .png or .jpg). Alternatively, you can write the program so it runs on a machine with a GUI (say, your local machine).
"""
import argparse
import turtle

import requests

def main():

    # if the user passed in args.ip then set ipToLookup as that value
    if args.ip:
        ipToLookup = args.ip
    else:   # if the user did not pass a value via the --ip flag at the CLI
        ipToLookup = input("What is the IP address to lookup? ")

    zresp = requests.get(f'http://ip-api.com/json/{ipToLookup}')  # this sends an HTTP GET
    print(zresp.json()) # print out the JSON attached to the response zresp

    # try to plot the IP address on a map
    screen = turtle.Screen() # creates screen object
    screen.setup(720, 360) # this is the size of our screen

    screen.setworldcoordinates(-180,-90,180,90)
    screen.bgpic('ip_map.gif')

    iplocation = turtle.Turtle()
    iplocation.penup()
    iplocation.color('yellow')
    iplocation.goto(zresp.json()['lon'],zresp.json()['lat'])
    iplocation.dot(5)

    turtle.mainloop()


# this is ONLY true if you run the script directly (i.e. python3 thisscript.py)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()  # short description of our program avail via help flag --help or -h
    parser.add_argument("--ip", help="The IP address to lookup via the API service")
    args = parser.parse_args()
    main()
