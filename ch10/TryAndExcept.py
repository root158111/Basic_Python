s = 'This is write with Try and except'
try:
    with open('TryAndExcept.txt','wt',encoding='utf-8') as fout:
        fout.write(s)
except:
    print('Can\'t write in the file!!!')
