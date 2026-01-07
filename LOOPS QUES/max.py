numbers = input("Enter list of number:")
#34 45 12 -8 89 67
numbers_list =  numbers.split()
print(numbers_list)
count =0
for number in numbers_list:
    count= count+1
print(count)
for i in range(count):
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)
maximum_number =numbers_list[0]
for number in numbers_list:
    if number > maximum_number:
        maximum_number=number
print(maximum_number)