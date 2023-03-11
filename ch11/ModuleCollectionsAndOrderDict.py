import collections

days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
do = ['Work','Swim','Run','Baseball','Football','Workout','Snap','Eat']
week  =zip(days,do)
d1 = dict(week)
print(d1)
week = zip(days,do)
d2 = collections.OrderedDict(week)
print(d2)
