class Animal():
    def __init__(self,name):
        self.name = name
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self,name):
        super().__init__('Puppy'+name)
    def sound(self):
        return 'Woof'

d = Dog('Ted')
print(d.name)
print(d.sound())
