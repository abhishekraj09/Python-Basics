list1 =["hi","hello","welcome"]
names = ["krishna","Ram","Madhav"]
for item in list1:
    for name in names:
        print(item,name)
        if item =="hello" and name =="Ram":
            break
    print("out from inner loop")
print("out from outer loop")