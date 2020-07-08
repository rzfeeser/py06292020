#!/usr/bin/python3

# this is what we want to TRY to do
try:
    # print("Enter a file name: ")
    name = input("Enter a file name: ")

    # try to open the file defined by var name
    with open(name, "w") as myfile:
        myfile.write("No problems with that file name.")
    
    #break

except FileNotFoundError:
    print("Problem with that file name! Try again!!")

except:
    print("I do not know exactly what you are trying to do, but you cannot do that.")
