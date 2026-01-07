class Duck:
    def swim(self):
        print("I am duck and i can swim")
    def speaks(self):
        print("Quack Quack")
    
class Dog:
    def swim(self):
        
        print("I am duck and i can swim")
    def speaks(self):
        print("Quack Quack")
        
class person:
    def speaks(self):
        print("blah blah blah")

def display(obj):
    obj.swim()
    obj.speaks()
    print("Information Displayed")
d = Duck()
dog = Dog()
p = person()
display(d)
display(dog)
display(p)


    
    