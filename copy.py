import shutil
import os

def copy_file(old_path, new_path):
    print(old_path)
    print(new_path)
    filelist = os.listdir(old_path)
    print(filelist)
    for file in filelist:
        src = os.path.join(old_path, file)
        dst = os.path.join(new_path, file)
        print('src:', src)
        print('dst:', dst)
        if os.path.splitext(src)[1] == '.xml':
            shutil.copy(src, new_path)

path = 'T1_seg/'
files00x = os.listdir(path)
for file00 in files00x:
    old = os.path.join(path, file00)
    oold = os.path.join(old, 'label')
    copy_file(oold, 'labelsForTest')