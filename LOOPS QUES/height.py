height =input("enter all the height seprated by space")
height_list = height.split() #convert input list to the string
count = 0
for height in height_list:
    count = count+1
print(count)
for i in range(count):
    height_list[i] = int(height_list[i])
#print(height_list)

total = 0
for person in height_list:
    total = total +person
print(sum)
avg = total/count
print(round(avg))