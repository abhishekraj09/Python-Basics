class A:
    def display(self):
        print("display from A class")

class B(A):
    def display(self):
        print("display from B class")

class C(A):
    def show(self):
        print("hi from C class")

class D(B,C):
    def display(self):
        print("display from D class")

d1= D()
d1.display()
#print(D.mro())
print(D.__mro__) 