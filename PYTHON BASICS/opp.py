class Instructor:
    def __init__(self,instructor_name,address):
        self.name = instructor_name
        self.address = address
        self.follower=0

    
instructor_1 =Instructor("abhishek", "bangalore")
print(instructor_1.name)
print(instructor_1.address)
print(instructor_1.follower)
#instructor_2 = Instructor("prince", "delhi")
#print(instructor_2.address)
