""" Question 1: Given a two integer numbers return their product and
 if the product is greater than 1000, then return their sum"""
""" Solution 1"""
num1 = 20
num2 = 30
product = num1 * num2
sum = num1 + num2
if(product > 1000):
    print(product)
else:
    print(sum)

""" Another way to do this program """

def mul_or_sum(num1, num2):
    product = num1 * num2
    sum = num1 + num2
    if(product > 1000):
        return product
    else:
        return sum

print("\n")
result = mul_or_sum(num1, num2)
print("the result is", result)
