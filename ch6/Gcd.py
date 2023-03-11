def gcd(m,n):
    if m == 0:
        return n
    else:
        return gcd(n % m , m )

m  = int(input("Please input a number for m: "))
n  = int(input("Please input a number for n: "))

ans = gcd(m,n)

print("The GCD with ",m," and ",n," is ",ans,sep="")
