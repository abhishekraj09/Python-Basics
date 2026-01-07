set1 = {'Ram', 'shyam', 'jenny'}
set2 = {'jenny', 'jiya', 'Aakash'}
set3 = {'Abhishek', 'prince','Ram'}
'''print(set1.difference(set2))
print(set1-set2)
print(set1.difference(set2,set3))
set1.difference_update(set2)
print(set1)
print(set1 ^ set2 ^ set3)'''
set2.symmetric_difference_update(set1)
print(set2)
set1.symmetric_difference_update(('mohan','shiva'))
print(set1)

''''The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.'''

