""" A simple example of for loop """
"""
numbers = [2,4,5,6,7,6,8,9,10]

sum = 0

for val in numbers:

    sum = sum + val

print("The sum is", sum)

# The range function 

print(range(10))
print(list(range(10)))
print(list(range(2,8)))
print(list(range(2,20, 3)))

genre = ['rock', 'jazzz', 'pop']

for i in range(len(genre)):

    print(" I like ", genre[i])

#  for loop with else

name = ['Rajesh', 'puskar', 'Binay']

for i in name:
    print(i)
else:
    print("No names left")

# " for loop with else

film = ['Fast & furious', ' Slumdog millioaire']

for i in film:
    print(i)
else:
    print("No name found")

#  program to display students mark from record

student_name = 'Puskar'
marks  = { 'Binay': 89, 'Puskar': 63, 'Rajesh': 67}

for student in marks:
    if student == student_name:

        print(marks[student])
        break
else:
    print("No name found ")

 Program to display personal character from the record
"""
    
People_name = 'Binay'
character = {'Suraj': 'Honest', 'Binay': 'shy', 'Rajesh':'inocent'}
for key in character.keys():
    if key  == People_name:
        print(character[key])
        break
else:
    print(' Your input doesnot match our record, please try again later ')







