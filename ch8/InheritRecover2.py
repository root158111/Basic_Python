class Animal():
    def __init__(self,name):
        self.name = name
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self,name,leg):
        super().__init__('Puppy'+name)
        self.leg = leg
    def sound(self):
        return 'Woof'

d = Dog('Ted',4)
print(d.name,'has ',d.leg,' legs')
print(d.sound())
