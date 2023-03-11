import os
os.chdir('D:\\')
print(os.getcwd())
fds = os.listdir('D:\\')
for fd in fds:
    if os.path.isdir(fd):
        print('Directory:',fd)
    else:
        print('File:',fd)
