import os



path = r"D:\_Intern\2_Detec_Windows\Pills_dataset2000\Output"

dirs = os.listdir(path)
list2 = []
#print(dirs)


for i in dirs:
    num = i[:-4]
    list2.append(int(num))


def missing_numbers(num_list):
    original_list = [x for x in range(1,2001)]
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))

print(missing_numbers(list2))
# 2000 1개만 missing