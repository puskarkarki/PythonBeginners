class Class1():
    pass

var1 = Class1()
var2 = var1
print(var1)
print(var1)
print(id(var1))
print(type(var2))
print(id(var2))
print(isinstance(var1, Class1))
print(isinstance(var2,Class1))

class Class2():
    var1 = 0
obj1 = Class2()
obj2 = Class2()

