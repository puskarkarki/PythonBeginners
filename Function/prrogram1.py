
def student(name, roll_no, Nepali, English, Social, Science):

    total = Nepali + English + Social + Science
    return total
    average = (Nepali + English + Social + Science)/4
    return average
    grade = (Nepali + English + Social + Science)/100

    return grade
def power(a, b):
    if b ==1:
        return a

    else:
        return(a * power(a, b-1))

a = int(input("Enter the first number:"))
b = int(input(" Enter the second number: "))
p = power(a, b)

print(a, 'to the power of', b, 'is', p)




