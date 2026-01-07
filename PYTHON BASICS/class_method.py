class Instructor:
    follower =0 # class object variable
    def __init__(self,name,address):
        self.name= name
        self.address = address
    def display(self,subject_name):
        print(f"hi , I am {self.name} and I teach {subject_name}")
    def update_follower(self,follower_name):
        self.follower +=1

instructor_1 = Instructor("manish", "noida")
print(instructor_1.name)
instructor_2 = Instructor("rahul","delhi")
print(instructor_2.name)
instructor_1.display("python")
instructor_1.update_follower("mohan")
print(instructor_1.follower)
#print(instructor_1.follower)

