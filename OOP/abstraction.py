from  abstract_class  import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color =color
    def start(self):
        print("start with kick")
    def display(self):
        print(f"my color is {self.color}")

class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("self start")
class Car(Vehicle):
    def __init__(self,n,x):
        super().__init(n)
        self.no_of_gears =6
    def start(self):
        print("start with key")