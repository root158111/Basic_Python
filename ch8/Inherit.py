class Animal():
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def __init__(self,name):
        super().__init__('Puppy'+name)

a = Animal('Aniaml')
d = Dog('Zing')
print(a.name)
print(d.name)
