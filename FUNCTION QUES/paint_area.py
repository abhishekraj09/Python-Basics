import math
def paint_calc(height,width,cover):
    area = height*width
    no_of_cans = math.ceil(area/cover)
    print(f"you will need {no_of_cans} cans of paint.")
h = int(input("Enter the height of wall in meter:\n"))
w = int(input("Enter the width of wall in meter:\n"))
coverage = 7
paint_calc(width=w,height=h,cover=coverage)