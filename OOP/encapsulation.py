class Student:
    def __init__(self,name,rollno,age): 
        self.name =name #public instance variable
        self._rollno = rollno #protected  instance variable
        self.__age =age #private instance class
    
    def get_age(self):
         return self.__age
    def set_age(self,age):
         if  age>35:
              print("invalid age given.. Age should be less than 35")
         else: 
            self.__age=age
         
         
'''def __display(self):
            print(f"hi  myself {self.name}{self.__age} year old with rollno {self._rollno} from student class")
    
    def displayPrivateData(self):
         self.__display()

class Branch(Student):
     def show(self):
          print(f" My rollno  is {self._rollno}")'''



s1=Student("Rahul" ,23,20)
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())

