def fac(num):
    if num ==1:
        return 1
    else:
        return num*fac(num-1)

n = int(input('Please input a number for n!:'))
ans = fac(n)
print(n,'! is ',ans,sep="")
