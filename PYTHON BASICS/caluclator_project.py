import os
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operation_dict  ={
    "+":add,
    "-": subtract,
    "*": multiply,
    "/":divide 
}

def calculator():
    number1 = float(input("Enter first number"))
    for symbol in operation_dict:
        print(symbol)
    
    continue_flag = True
    while continue_flag:
        op_symbol=input("pick an operation:")
        number2= int(input("enter next number"))
        calculator_function=operation_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f" {number1} {op_symbol} {number2}={output}")

        should_continue =input(f"Enter 'Y' to continue calcualation with {output} or 'n' to  start a new calculation or 'x' to exit")#lower()
        if should_continue == 'Y':
            number1 =output
        elif should_continue =='n':
            continue_flag =False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print("bye")
calculator()
