height=int(input("what is your height"))
bill = 0

if height>=3:
    print("can ride")
    age = int(input("what is your age"))
    if age<12:
        bill =150 
        print("pay 150 rs") 
    elif age<=18:
        bill =250   
        print("ticket price is 250 rs")
    else:  
        bill = 500
        print("ticket price is  500 rs")
    
    want_photo =  input("do you want to take photo(Y/N)?")
    if want_photo == 'y' or want_photo == 'Y':
        bill = bill + 50
    print(f"your total bill is {bill}")

else:
    print("can't ride")
print("Thank you enjoy the ride")    
