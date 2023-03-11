nums = [i for i in range(1,10)]
num2 = filter(lambda x:x%2,nums)
print(list(num2))

num2 = filter(lambda x:x%2==0,nums)
print(list(num2))

