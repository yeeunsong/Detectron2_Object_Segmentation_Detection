import os
import shutil


path = r"D:\_Intern\2_Detec_Windows\Pills_dataset2000\Output"
os.chdir(path)

dirs = os.listdir(path)


#print(dirs)

for i in dirs:
    #print(i)
    #print(type(i))
    dest = i.lstrip("0")
    os.rename(i, dest)

for i in dirs:
    if i.endswith('.txt'):
        shutil.move(r"D:\_Intern\2_Detec_Windows\Pills_dataset2000\Output\\"+i, r"D:\_Intern\2_Detec_Windows\Pills_dataset2000\Output\txt file\\"+i)

dirs = os.listdir(path)
print(dirs)
