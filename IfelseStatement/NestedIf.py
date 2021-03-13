""" Program to check if the number is postive, negative or Zero """

num = float(input(" Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print(" Number is a positive number")
else:
    print(" Number is a negative number ")