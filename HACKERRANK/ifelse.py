""" An example to manipulate if else statement """

"""Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2  to 5, print Not Weird
If n  is even and in the inclusive range of 6 to 20 , print Weird
If n  is even and greater than 20, print Not Weird """

import os
import math
import random
import re
import sys

n = int(input().strip())
if n%2 ==1:
    print("Weird")
elif n%2==0 and (n>=2 and n<6):
    print("Not Weird")
elif n%2==0 and (n>=6 and n<21):
    print("Weird")
else:
    print("Not Weird")




