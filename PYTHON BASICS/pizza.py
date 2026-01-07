size = input("what size pizza you want S/M/L")
bill = 0

if size == "S" or size=='s':
    bill =  bill + 100
    print("small pizza price is 100 rs")

elif size == "M" or size=='m':
    bill = bill + 200
    print("medium pizza price is 200 rs ")

else:
    bill = bill + 300
    print("large pizaa price is 300rs")

add_pepproni = input("do you want pepproni(Y/N)")
if add_pepproni == 'y' or add_pepproni == 'Y':
    if size == 'S' or size == 's':
        bill = bill + 30
    else:
        bill = bill + 50

extra_cheese = input("Do you want to take extra cheese (Y/N)")
if extra_cheese  == 'y' or extra_cheese == 'Y':
    bill= bill + 20
print(f"your  final bill is {bill}")  






