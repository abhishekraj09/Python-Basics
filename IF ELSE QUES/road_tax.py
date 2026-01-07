prc = int(input("enter the price of  road"))
tax=0
if prc>100000:
    tax=15/100*prc
elif prc>50000:
    tax=10/100*prc
else:
    tax=5/100*prc
print(tax) 