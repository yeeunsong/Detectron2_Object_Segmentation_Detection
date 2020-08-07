import os

sizes = []
dirs = []

path = r"D:\_Intern\2_Detec_Windows\Pills_dataset2000\scene\\"
dirs = os.listdir(path)
dirs = [i for i in dirs if i.startswith('scene')]

for i in dirs:
    path_change = path + '\\' + i + '\\Mask'
    os.chdir(path_change)

    subdirs=[]
    subdirs = os.listdir(path_change)
    for j in subdirs:
        size = os.path.getsize(j)
        if size==994:
            os.remove(j)


