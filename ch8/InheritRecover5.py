class Leg():
    def __init__(self,num,look):
        self.num = num
        self.look = look

class Animal():
    def __init__(self,name,leg):
        self.__name = name
        self.leg = leg
    def show_name(self):
        return self.__name
    def show(self):
        print(self.show_name(),' has ',self.leg.num,self.leg.look,' legs ')
leg = Leg(4,'shortly')
a =Animal('Puppy' ,leg)
a.show()
