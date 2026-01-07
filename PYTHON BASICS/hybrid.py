class A:
    def display(self):
        print("display from A class")

class B(A):
    def display(self):
        print("display from B class")
    
class C:
    def show(self): 
        print("hi from c  class")

class D(B,C):
    def display(self):
        super().display()
        print("display from D class")

d1 = D()
d1.display()
print(D.mro())
    