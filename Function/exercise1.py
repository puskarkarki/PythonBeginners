''' example1'''

def greet(name):

    ''''This function greets to the person passed in as parameter'''


    print("HELLO, " + name + ", Good morning!" )

greet('puskar')


'''This is a example 2 about python function '''

def sum():

    a = 10

    b = 20

    c = a + b

    return c

print("The sum of a and b is", sum())

''' EXAMPLE 3'''

def sum_num(a, b):

    sum = a + b

    return sum
print("The sum of  a and b is", sum_num(12, 20))

'''A simple python function to check whether x is even or odd '''

def evenOdd(x):

    if (x%2 ==0):
        print('This is an even number ')

    else:
        print('This is an odd number')

evenOdd(2)
evenOdd(89)

