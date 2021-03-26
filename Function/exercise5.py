''' defining the function '''

def change_list(list1):

    list1.append(20)
    list1.append(30)

    print("list inside the function = ",list1 )

list1 = [10, 34, 39, 40]
change_list(list1)
print("list outside the function = ", list1)

'''exercise 5'''

def pradip(hello):

    print("hello", hello)

pradip('puskar')

''' Passing immutable list'''

def change_name(list2):

    list2.append('Puskar')
    list2.append('pradip')



    print("list2 inside the function = ",list2)

list2 = []

change_name(list2)

'''passing mutable object'''

def change_str(str):

    str = str + "How are you doing"

    print("printing inside the function ", str)

string1 = "Hi, I am puskar karki"

change_str(string1)

print("We are printing outside the function", string1)

''' passing immutable object(list)'''

def my_list(list):

    list.append(20)
    list.append('puskar')
    list.append('Pratima')
    list.append(39)

    print("Printing inside the function", list)

list1 = ['puskar', 'pratima', 'Jiwan']

my_list(list1)
print('printing outside the function', list1)








