num = int(input("enter the number:"))
last_digit = num%3
if last_digit%3==0:
    print("divisible by 3")
else:
    print("not divisible by 3") 