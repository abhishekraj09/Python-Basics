from abc import ABC,abstractmethod  

class Vehicle:
    def __init__(self,n):
        self.no_of_tyres = n
    @abstractmethod # decorator  to make abstract method
    def start(self):
        pass
    def display(self):
        print("hi i am calling from vehicle class")
        
