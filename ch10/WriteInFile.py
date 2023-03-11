s = '987654321'
with open('WriteInFile.txt','wt',encoding='utf-8') as fout:
    print(s,file=fout)
    fout.write(s)
