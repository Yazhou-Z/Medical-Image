import os

path = 'DTI_p2/012/dti/'
filename_list = os.listdir(path)
a = 0

for i in filename_list:
    used_name = path + filename_list[a]
    new_name = path + "ZhangSan_" + used_name[33:]
    os.rename(used_name,new_name)
    print("New name is %s" %(used_name,new_name))
    a += 1

