'''count = 5
while count>=0:
    print(count)
    count = count-1
print("out from the loop")'''

total =0
number = int(input("enter a number(0 to quit)"))
while number!=0:
    total = total +number
    number = int(input("enter a number(0 to quit):"))
print(total)

