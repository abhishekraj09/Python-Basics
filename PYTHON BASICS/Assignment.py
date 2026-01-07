class  University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def display(self):
        print(f"university name is {self.uni_name}")

class Course(University):
    def __init__(self,uni_name,course_name):
        University.__init__(self,uni_name)
        self.course_name = course_name
    def display(self):
        print(f" course name  is {self.course_name}")

class Branch(University):
    def __init__(self,uni_name,branch):
        University.__init__(self,uni_name)
        self.branch = branch
    def display(self):
        print(f"branch  name is {self.branch}")

class Student(Course,Branch):
    def __init__(self,uni_name,course_name,branch):
        Course.__init__(self,uni_name,course_name)
        Branch.__init__(self,uni_name,branch)
    def display(self):
        print("i am student")
class Faculity(Branch):
    def __init__(self,uni_name,branch):
        Branch.__init__(self,uni_name,branch)
    def display(self):
        print(" i am from faculity")  

u1 = University("delhi")
c1 = Course("delhi","BE")
b1 = Branch("delhi","CSE")
f1 = Faculity("Delhi","CSE")
student_1 = Student("delhi","BE","CSE")
student_1.display()
University.display(student_1)
Course.display(student_1)
Branch.display(student_1)
f1.display()
