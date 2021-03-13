''' Write a Python program which accepts a sequence of comma-separated numbers from user
 and generate a list and a tuple with those numbers'''
""" """

values = input("Input comma separated by the value: ")
list = values.split(",")
tuple = tuple(list)
print('list', list)
print('Tuple : ', tuple)
