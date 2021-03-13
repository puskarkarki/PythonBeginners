def add_sum(num1, num2):

    sum = num1 + num2



    return sum

print(add_sum(2, 3))


# *args

# We need to pass list/tuple

def f11(*nums):
    sum = 0
    for n in nums:
        sum += n
    print(sum)

f11(30,20)
f11(30,20,78,9)
f11(30,6,7,8,3,4,5,6)

def f12(** data):

    for key, value in data.items():
        print('{} = {}'.format(key, value))

f12(pid= 1, name = 'krishna')
print()

f12(pid=1, name ='krishna')
print()

f12(pid=2, name = "raj", address= 'Bhaktapur')

