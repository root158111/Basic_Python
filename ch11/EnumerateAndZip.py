days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
p = enumerate(days,start=1)
for c,day in p:
    print(c,day)
do = ['Work','Swim','Run','Baseball','Football','Workout','Snap','Eat']
week  =zip(days,do)
for day,sport in week:
    print(day,sport)
