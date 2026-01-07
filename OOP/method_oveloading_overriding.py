#method overloading
class Demo:
    def add(self,a,b,c=0): #using default argument
        return a+b+c
     
d = Demo()
print(d.add(2,3)  )
print(d.add(1,2,3))

#args
class Demo:
    def add(self, *args):
        total = 0
        for i in args:
            total = total +i
        return total
d.Demo()
print(d.add(2,3))
print(d.add(1,2,3))
print(d.add(3,4,5,67,7,8))



#method overriding

class Father:
    def sleep(self):

        print("sleeps from  10:00 PM to  5:00 Am")
    def eat(self):
        print("eating")
class Son(Father):
    def sleep(self):
        print("sleeps from 2:00 AM to 10:00 AM")
        super().sleep()
Ram = Son()
Ram.sleep()