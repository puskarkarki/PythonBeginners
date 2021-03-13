
"""def people_names():
    return people_names()

def f1():
    print("Helo python")
    print("Hello world")
    print("Thank you")

for i in range(10):
    f1()
    print()

def f2(str1):
    print(str1)


str2 = "Kathmandu, Nepal"
str3  = "Balaju, Kathmandu"
f2(str2)
f3(str3)"""

def f3(var1, var2):

    print(var1,var2)

f3("value1", 25)


def f4():
    return("Helllo")

var1 = f4()
print(var1)

def f5(var1):
    return("hello:" + str(var1))

def sum(num1, num2):

    sum = num1 + num2

    return sum

print(sum(2, 4))

def f2(num1, num2):

    print(num1 + num2)


f2(20, 32)

def f3(num1, num2):

    return(num1 + num2)

result = f3(78, 54)
print(result)



"""" Ask the user to enter the values of a and b and calculate a to the power of b using recursion"""

def power(a, b):
    if b ==1:
        return a

    else:
        return(a * power(a, b+1))

a = int(input("Enter the first number:"))
b = int(input(" Enter the second number: "))
p = power(a, b)

print(a, 'to the power of', b, 'is', p)

