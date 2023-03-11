import random

target = random.randint(1,99)
guess = 0
while target != guess:
    guess = int(input('Please input a number between 1 to 99\n'))
    if target<guess:
        print('Lower')
    elif target>guess:
        print('Bigger')
    else:
        print('Bingo')
        break
