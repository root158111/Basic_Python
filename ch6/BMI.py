def BMI(w,h):
    return w/(h*h)
w = float(input("Please input your weight(Kilogram): "))
h = float(input("Please input your high(Meter):"))

bmi = BMI(w,h)
print("Your bmi is: ",bmi)

if(bmi < 18):
    print("Too light")
elif(bmi < 24):
    print("Good")
elif(bmi < 27):
    print("Too Heavy")
else:
    print("Too fat")
