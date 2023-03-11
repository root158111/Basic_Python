import os 
path = "D:\\Python\\ch7"
def find_dir(dir):
    fds = os.listdir(dir)
    for fd in fds:
        full_path = os.path.join(dir,fd)
        if os.path.isdir(full_path):
            print('Directory:',full_path)
            find_dir(full_path)
        else:
            print('File:',full_path)
find_dir(path)
