def multiply(*args):
    c=1
    for i in args:
        c=c*i
    print(f"The multiplication of the given numbers is {c}")
multiply(2,3,-6,8)
multiply(2,5,8,9,0,6) 