import os
import re
path = r"D:\_Intern\2_Detec_Windows\Pills_dataset2000\train\annotations"

dirs = os.listdir(path)
name = []

for fname in dirs:
    f = re.search('_(.*)_',fname)
    name.append(f.group(1))


def unique(list1):
    i=0
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        print(x)
        i+=1
    print(i)


unique(name)
