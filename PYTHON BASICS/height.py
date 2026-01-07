height= int(input("enter a number"))

if height>=3:
    print("can ride")
    age =int(input("what is your age?"))
    if age<=18:
        print("please pay 250 rs")
    else:
        print("please pay 500 rs")
else:
    print("can't ride")
print("bye")