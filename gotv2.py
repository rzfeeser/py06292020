#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import sys

import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters"

def main():
    ## Ask user for input
    got_charToLookup = input("What is the name of the character we should lookup? " )

    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + "?name=" + got_charToLookup)

    ## ensure that a valid HTTP response was returned
    if gotresp.status_code != 200:
        sys.exit("A non 200 HTTP response was returned. Exiting.")

    ## ensure json is present
    if gotresp.json():
        got_dj = gotresp.json()
    else:
        sys.exit("There was no JSON on the 200 response. Exiting.")

    ##print(got_dj)
    print(f"\n\nThe character {got_charToLookup} has the URL: {got_dj[0]['url']}")

    ## determine if the character has any allegiances
    if got_dj[0]['allegiances']: #if allegiances is an empty list, this tests FALSE
        print(f"\n\n{got_charToLookup}'s allegiance is to the following house(s):")
        for allegiance in got_dj[0]['allegiances']:    # loop through the list of allegiances
            house = requests.get(allegiance)
            print(house.json()['name'])

if __name__ == "__main__":
    main()
