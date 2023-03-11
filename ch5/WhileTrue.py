while True:
    account = input('Account:')
    password = input('Password:')
    if(account=='abc' and password=='123'):
        print('Correct!')
        break
    else:
        print('Fail')
