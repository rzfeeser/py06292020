#!/usr/bin/python3
"""
Author: RZFeeser
Learning to parse log files with python
"""

def main():

   totalfail = 0
   # parse keystone.common.wsgi and return number of failed login attempts
   loginfail = 0 # counter for fails
   listOfailedIPs = [] # store the failed IPs in here

   # open the file for reading
   with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as keystone_file:
       # loop over the list of lines
       for line in keystone_file:
           if "-] Authorization failed" in line:
               totalfail += 1
           # if this 'fail pattern' appears in the line...
           if "- - - - -] Authorization failed" in line:
               loginfail += 1 # this is the same as loginfail = loginfail + 1
               listOfailedIPs.append(line.split(" ")[-1])
   
   ## display the results
   print("The number of failed log in attempts is", loginfail)
   print("The number of successful log in attempts was", totalfail - loginfail)
   print("BAN the following IPs:")
   for ip in listOfailedIPs:
       print(ip.rstrip("\n"), end=" ")
   print()

if __name__ == "__main__":
    main()
