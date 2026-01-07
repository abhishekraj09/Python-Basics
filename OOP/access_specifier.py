class Student:
    def __init__(self,name,rollno,age): 
        self.name =name #public instance variable
        self._rollno = rollno #protected  instance variable
        self.__age =age #private instance class
         
    def __display(self):
            print(f"hi  myself {self.name}{self.__age} year old with rollno {self._rollno} from student class")
    
    def displayPrivateData(self):
         self.__display()

class Branch(Student):
     def show(self):
          print(f" My rollno  is {self._rollno}")

#b1 = Branch("Nisha", 45,23)
#b1.show()

''''def showData():
    b1 = Branch("nishu", 23, 20)
    print(b1.name)'''

#print(b1._rollno)
#showData()
s1=Student("Rahul" ,23,20)
#s1.name ="Raunak"
#s1._rollno =45
#print(s1.__age)
#print(s1.name)
print(s1._Student__age)
s1._Student__display()
#s1.display()
