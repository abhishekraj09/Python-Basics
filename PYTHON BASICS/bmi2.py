weight = float(input("enter weight in kg"))
height = float(input("enter height in meter"))

bmi = round(weight/height **2)

if bmi< 18.5:
    print(f" your BMI is {bmi} and you are underweight")

elif bmi < 25:
    print(f" your BMI is {bmi} and you have a normal weight")

elif bmi<30:
    print(f"your BMI is {bmi} and you  have a overweight")

elif bmi< 35:
    print(f"your BMI is {bmi} and you have a obesity ")

else:
    print(f" your BMI is {bmi} and you are clinclically  obesity")