set1 ={'ram','shyam','jenny'}
set2 ={'jenny','jiya','Aakash'}

print(set1.isdisjoint(set2))

print(set1.issubset(set2)) #every element of set 1 is in set2 is subset
print(set1<=set2)
print(set1<=set1)

print(set1.issuperset(set2)) #every element of set2 is in set1 superset 
print(set1>=set2)

set2.clear()
print(set2)

#del set2
#print(set2)