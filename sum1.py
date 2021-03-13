"""def sum_num(a,b):

    sum = a + b
    return sum

a = int(input(" Enter the value of a:"))
b = int(input(" Enter the value of b:"))

print(sum_num(a,b))"""

def add_num(num1, num2):

    sum = num1 + num2
    return sum

num1 = float(input(" Enter the first number to be added:"))
num2 = float(input(" Enter the second number to be added:"))
print(add_num(num1, num2))

''' ADD TWO NUMBERS IN PYTHON USING CLASS'''

class sum_num:

    def find_sum(self, num1, num2):

        sum = num1 + num2

        return sum

num1 = int(input(" Enter your first number:"))
num2 = int(input("Enter your second number:"))

obj = sum_num()
sum = obj.find_sum(num1, num2)

print("The sum is:", sum)

''' ADDING OF TWO NUMBERS USING FORMAT METHOD '''

num1 = 23
num2 = 55

sum = num1 + num2

print('The sum of {0} and {1} is {2}:'.format(num1, num2, sum))