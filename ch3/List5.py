list1 = [1,2,3,4]
list2 = list1
print('list1 = ',list1)
print('list2 = ',list2)

list1[2] = 19
print('list1 = ',list1)
print('list2 = ',list2)

list2[2] = 18
print('list1 = ',list1)
print('list2 = ',list2)

print('list1 id is: ',id(list1))
print('list2 id is: ',id(list2))


list3 = [1,2,3,4]
list4 = list1[:]

list4[2] = 19
print('list3 = ',list3)
print('list4 = ',list4)

list5 = list3.copy()
list5[2] = 19

print('list3 = ',list3)
print('list5 = ',list5)
print('list3 id is: ',id(list3))
print('list5 id is: ',id(list5))

