fin = open('TryAndExcept.txt','rt',encoding ='utf-8')
fout = open('Copy.txt','wt',encoding='utf-8')
line = fin.readline()
while line:
    fout.write(line)
    line = fin.readline()
fin.close()
fout.close()
