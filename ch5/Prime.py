num = int(input('Please input a number: '))
j = 2
prime = True
while j < num:
    if(num%j==0):
        prime = False
        break
    j+=1
if prime:
    print(num,'is odd')
else:
    print(num,'is even')
