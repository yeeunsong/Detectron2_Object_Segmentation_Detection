import os
import shutil
import re

destination = r"D:\_Intern\2_Detec_Windows\Pills_dataset2000\_train\annotations"


path = r"D:\_Intern\2_Detec_Windows\Pills_dataset2000\scene"
dirs = os.listdir(path)

dirs = [i for i in dirs if i.startswith('scene')]


for i in dirs:
    path_change = path+'\\'+i+'\\Mask'
    files = os.listdir(path_change)
    os.chdir(path_change)

    dirname = int(re.sub('.*_','', i))

    if dirname<=1200:
        for f in files:
            source=path_change+'\\'+f
            #print(source)
            #print(type(source))
            dest = shutil.copy2(source, destination)
            #print(dest)
