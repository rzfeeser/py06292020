#!/usr/bin/python3
"""
Author: RZFeeser
PART A Pull timestamp of now (format is up to you)
PART B Pull the IP address of your current system
PART C Read in a list of servers from a file called, myservers.txt (you'll need to make this)
PART D format the data in the following manner: {"json": "time: <<PART A>>, ip: <<PARTB>>, mysvrs: [ <<PARTC>> ]"}
PART E Validate your JSON with a POST
"""

ZURL = "jsontest.com"

# send HTTP primatives
import requests

def main():

    # part a - pull timestamp of now
    ts = requests.get(f"http://date.{ZURL}")
    ts = ts.json()
    ts = ts['date']

    # part b - pull ip
    ip = requests.get(f"http://ip.{ZURL}")
    ip = ip.json()
    ip = ip['ip']

    # part c - read in file
    with open("myservers.txt", "r") as zf:
        zsrv = zf.readlines() # read in a list of lines from file called myservers

    # part d - format the data
    mydata = {"json": f"{{'time': {ts}, 'ip': {ip}, 'mysvrs': {zsrv}}}"}
    print(mydata)

    # part e - use requests library to send an HTTP POST
    resp = requests.post(f"http://validate.{ZURL}", data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()

