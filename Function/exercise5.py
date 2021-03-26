''' defining the function '''

def change_list(list1):

    list1.append(20)
    list1.append(30)

    print("list inside the function = ",list1 )

list1 = [10, 34, 39, 40]
change_list(list1)
print("list outside the function = ", list1)


