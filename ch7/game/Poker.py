from random import choice
def poker():
    a = ['C','H','D','S']
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    return choice(a)+str(choice(b))
