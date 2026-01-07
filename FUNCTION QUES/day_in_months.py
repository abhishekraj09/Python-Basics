def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_months(year,month):
    days_in_list =[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year)  & month==2:
        return 29
    else:
        return days_in_list[month-1]
year =int(input("Enter the year:\n"))
month = int(input("Enter the month:\n"))
days = days_in_months(year,month)
print(days)
    


    