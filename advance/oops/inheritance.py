# single inh.
# class  A:
#     def a(self):
#         print("I am from class A")

# class  B(A):
#     def b(self):
#         print("I am from class B")

# obj = B()
# obj.a()
# obj.b()

# mutli-level inh.

# class  A:
#     def a(self):
#         print("I am from class A")

# class  B(A):
#     def b(self):
#         print("I am from class B")

# class  C(B):
#     def c(self):
#         print("I am from class C")

# obj = C()

# obj.a()
# obj.b()
# obj.c()

# multiple inheritance
# class  A:
#     def a(self):
#         print("I am from class A")

# class  B:
#     def b(self):
#         print("I am from class B")

# class  C(A,B):
#     def c(self):
#         print("I am from class C")

# obj = C()

# obj.a()
# obj.b()
# obj.c()

# herarchical inh.

class Shape:
    def shape(self):
        print("From Shape class")

class Shape2D(Shape):
    def shape2d(self):
        print("From Shape2d class")

class Circle(Shape2D):
    def circle(self):
        print("From Circle class")

class Square(Shape2D):
    def square(self):
        print("From Square class")

class Shape3D(Shape):
    def shape3d(self):
        print("From Shape3d class")

class Cube(Shape3D):
    def cube(self):
        print("From Cube class")

obj = Cube()
obj.shape()
obj.shape3d()
obj.cube()