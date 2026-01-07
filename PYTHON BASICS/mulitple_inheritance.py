class Human:
    def __init__(self,num_heart):
        print("calling init from Human")
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can Eat ")
    def work(self):
        print("i can work")

class Male: 
    def __init__(self,name):
        print("calling init from male")
        self.name = name
    def flirt(self):
        print(" i can  flirt")
    def work(self):
        print("I can code")


class Boy(Human,Male):
    def __init__(self,name, heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name) 
        self.language =language
    def sleep(self):
        print(" i can sleep")
    def work(self):
        print(" i can test")
    def display(self):
        print(f" hi  i am {self.name} and i work on {self.language}")
    pass
boy_1 = Boy("rahul", 1 ,"python")
#boy_1.work()
#Male.work(boy_1)
print(boy_1.num_nose)
print(boy_1.num_heart)
print(boy_1.language)
print(boy_1.display())