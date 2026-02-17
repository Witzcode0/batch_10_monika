# syntax:

# class className:
    # data member [attribute or property]

    # member function [method or behavior]

# syntax of object

# obj_name = className()

class person:
    # data member [attribute or property]
    def __init__(self, name, age):
        self.n = name
        self.a = age

    # member function [method or behavior]
    def info(self):
        print("My name is %s. and my age is %d" % (self.n, self.a))

p1 =  person("Brijesh", 29)
print(p1.a)
print(p1.n)
p1.info()
p2 =  person("MONICA", 24)
print(p2.a)
print(p2.n)
p2.info()