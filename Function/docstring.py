def square(n):

    ''' This is a doc string and we are computing the square of  number'''

    square_num = n * n

    return square_num

square(9)
print(square(9))


def hello(name):

    "Hello  Ram, I am learning python programming"

    print("hello, " + name + ", How are you")

print(hello.__doc__)
hello('ram')

''' example 3'''

def greet(name):

    ''' This is a new era of a programming language '''

    print("hello," + name + ", my name is python programming")

print(greet.__doc__)
greet('puskar')


def hi_hello():

    '''Hello Jack, I am learning python programming'''

print(hi_hello.__doc__)


def say_hello(name):

    '''I am  mr sujan dahal '''

    print("Hello, " + name + ", I am new to python programming")
print(say_hello.__doc__)
say_hello('Prajwol')

