class Class3():
    var1 = 0
    var2 = 0
    var3 = 0
obj1 = Class3()
obj1.var1 = 7
obj1.var2 = 4
print(obj1.var1, obj1.var2)
obj1.var3 = obj1.var1 + obj1.var2
print(obj1.var3)

# Read the value from the user dynamically

obj1.var1 = int(input("Enter the first value :"))
obj1.var2 = int(input("Enter the second value: "))
obj1.var3 = obj1.var1 + obj1.var2
print(obj1.var3)