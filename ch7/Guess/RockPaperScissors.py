from Guess import figure_guess
def run():
    computer = figure_guess()
    my = input('Rock、Paper、Scissor(Choice one)')
    print('Computer is ',computer)

    if my =='Paper':
        if computer =='Paper':
            print('Tie')
        elif computer =='Rock':
            print('You Win!')
        else:
            print('Computer Win!')

    elif my =='Rock':
        if computer =='Rock':
            print('Tie')
        elif computer =='Paper':
            print('Computer Win!!')
        else:
            print('You Win!')

    else:
        if computer =='Scissor':
            print('Tie')
        elif computer =='Rock':
            print('Computer Win!!')
        else:
            print('You Win!')
if __name__=='__main__':
    for i in range(10):
        run()
else:
    print('I\'m not independent program')
    
