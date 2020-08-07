# importing os module 
import os
import re






# print(os.listdir(r"D:\_Intern\2_Detec_Windows\Data93_pycococreater\train"))

dirs = []

path = "D:\\_Intern\\2_Detec_Windows\\Pills_dataset2000\\scene"
dirs = os.listdir(path)

# for files in dirs:
#    print(files)


#print(type(dirs))
#print(len(dirs))


dirs = [i for i in dirs if i.startswith('scene')]
#print(len(dirs))

for i in dirs:
    path_change = path+'\\'+i+'\\Mask'
    image_id = i[6:] # ex> scene_4 --> 4 extracted
    print(image_id)
    files = os.listdir(path_change)
    os.chdir(path_change)
    annotation_id=1
    for f in files:
        name = f[0:3:1]
        os.rename(f, image_id+'_'+name+'_'+str(annotation_id)+'.png')
        annotation_id+=1
        #print(type(name))

print(files)
