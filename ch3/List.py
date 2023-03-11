shoplist = ['Milk','Egg','Coffee Bean','Watermelon','Pineapple']

print('shoplist[0] is ',shoplist[0])

shoplist[0] = 'Tea'
print('shoplist = ',shoplist)

index = shoplist.index('Coffee Bean')
print('index = ',index)


shoplist.append('Bread')
print('shoplist = ',shoplist)

shoplist.insert(4,'Apple')
print('shoplist =',shoplist)

shoplist.remove('Egg')
print('shoplist = ',shoplist)

del shoplist[0]
print('shoplist = ',shoplist)

shoplist.sort()
print('shoplist = ',shoplist)

for item in shoplist:
    print(item)



list = [1,2.0,3,'Python']
print(list)


