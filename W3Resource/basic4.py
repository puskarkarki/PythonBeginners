""" Write a python program to accept a filename from the user and print the extension of that"""

filename = input("Input the file name: ")
f_extns = filename.split(".")
print("The extension of the file name is: " + repr(f_extns[-1]))
