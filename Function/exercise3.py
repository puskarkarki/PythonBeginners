'''' Python function examples '''


def square_num(num):
    ''' This is a doc strring and we are calcultaing the square of a number'''

    return num**2

print(square_num(5))
print(square_num(-6))
print(square_num.__doc__)

def cub_num(num):

    return num**3

print(cub_num(3))