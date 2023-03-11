import glob,os
path = "D:\\Python\\ch8"
os.chdir(path)
for file in glob.glob("*.py"):
    print(file)
