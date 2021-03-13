i = 20;
if (i < 18):
    print("I is smaller than 18")
    print(" I am in if block and my condition will be executed if I would be true")
else:
    print(" I is  greater than 18")
    print(" I will be executed if my condition will be true")

""" Ask the user to enter the marks of a student in a subject. If the
marks entered are greater than 40 then print “pass,” if they are lower print “fail """

a = int(input("Enter the percentage obtained in the exam:  "))
if(a >= 40):
    print("congratulations you have passed the exam")
else:
    print("Sorry! you have failed the exam ")

""" Write a program to find the greatest of the three numbers
entered by the user."""

num1 = int(input(" Enter the value of num1: "))
num2 = int(input("Enter the vlue of num2: "))
num3 = int(input("Enter the value of num3: "))
if num1 > num2:
    if num1 > num3:
        print("num1 is the greatest number")
    else:
        print("num3 is the greatest number")
else:
    if num2 >num3:
        print("num2 is the  greatest number")
    else:
        print("num3 is the greatest number")

""" Find the greatest of the three number entered by the user """
a = int(input(" Enter the first number : "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

big = (a if (a>c) else c) if (a>b) else(b if (b > c)else c)
print('Thee greatest of the three numbers is '+ str(big))

'''THE GET CONSTRUCT
<dictionary name>.get('<value to be searched>', 'default
value>')'''

movies = {'Inception': 2018, 'Intersteller':2020, 'peacefulwarrior': 2012}
print(movies.get('Inception', 'not found'))
print(movies.get('2012', 'not found'))
print(movies.get('peacefulwarrior', 'not found'))






