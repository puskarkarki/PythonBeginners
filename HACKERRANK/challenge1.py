n = 3
if n  in range(2,5):
    print("Weird")
else:
    print("Not Weird")

''' Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps.
 She decided to count the total number of distinct country stamps in her collection. 
 She asked for your help. You pick the stamps one by one from a stack of  country stamps.
'''
'''n = int(input())
s = set()
for i in range(n):
    string = input()
    s.add(string)
print(len(s))'''

stamps = set()
for _ in range(int(input())):
    stamps.add(input().strip())
print(len(stamps))