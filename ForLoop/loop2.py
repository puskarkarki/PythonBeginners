""" Write a program to find the sum of all numbers stored in a list"""

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:

    sum = sum + val

    print(sum)

print('The sum of all the numbers sorted in a list', sum)

'''for loop iteration in a list'''

print("For loop iteration in a list using python")
L = ['Python', 'programming', 'for', 'beginnners']
for i in L:
    print(i)

''' Write a python program to show the iteration through tuple using for loop '''

print('\tIterating through the tuple using python')
t = ('Iterating', 'through', 'tuple')
for i in t:
    print(i)


'''Write a program to show the iteration through strings using for loop'''


print("Iterating through strings using for loop")
s=("pythonprogramming is the best")
for i in s:
    print(i)

'''Iterating through the dictionary in python '''

dictionary = {'name':'puskar','height':'5.9','age':'26'}

for value in dictionary:
    print(value)


dictionary_name = {'name': 'Anusha', 'age':'18', 'caste':'bista'}


for key in dictionary_name:
    print(key, '->', dictionary_name[key])

''' Another program to iterate dictionary using for loop that can print the items in a dcitionary name'''

movie = {'name':'shawshank redemption', 'rating':'8/10', 'year':'1998'}

for item in movie.items():
    print(item)

'''peogram to iterate through a list using indexing:'''

genre = ['rock', 'pop', 'blues']

for i in genre:
    print("I love", i, "music")

name = ['ram', 'shyam', 'gopal', 'hari']

for i in name:
    print("My name is ", i)

'''' FOR LOOP WITH ELSE: '''

digits = [0,1,2,4,5]

for i in digits:
    print(i)
else:
    print("No items left")

''''''
student_name = 'ram'
marks = {'james': '78', 'suraj':'98', 'puskar':'97'}
for student in marks:

    if student == student_name:
        print(marks[student])
        break
    else:
        print('No list found')

''''''


