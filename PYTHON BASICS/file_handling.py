'''f1 = open("file_1.txt","w+")
print(f1.tell())
f1.write("hi Welcome")
print(f1.tell())
f1.write("this is python course")
print(f1.tell())
f1.seek(0)
data = f1.read()
print(data)
print(f1.tell())
f1.close()'''

f1 = open("C:\python\file_2.txt", "a+")
print(f1.tell())
f1.seek(0)
#f1.write("hello guys ")
print(f1.read())
f1.write("jenny lecture")


