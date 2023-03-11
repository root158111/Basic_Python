a = []
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
print(a)

b = []
for i in range(1,6):
    b.append(i)
print(b)

b = [x for x in range(1,6)]
print(b)
