import glob
python_files = glob.glob('D:\\Python\\ch10\\*.py')
for file_name in python_files:
    print('File name is: ',file_name)
    with open(file_name) as f:
        for line in f:
            print(line.rstrip())
    print()
