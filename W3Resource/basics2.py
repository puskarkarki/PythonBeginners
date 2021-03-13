from datetime import date
from datetime import datetime
today = date.today()
print("The current datetime is", today)
now = datetime.now()
print(now)

''' Write a Python program which accepts the radius of a circle from the user and compute the area '''

import math
from math import pi

r = float(input("Enter the radius of the circle: "))
area = pi*r**2
print(area)


''' Write a Python program which accepts the user's first and last name and 
print them in reverse order with a space between them '''

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
print("Hello " + lastname + "" + firstname)
print(lastname + "" +  firstname)

