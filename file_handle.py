import shutil
import os 
folder_path = "\image"
dest_folder = "\paperimage"
dest = os.getcwd() + str(dest_folder)
src = os.getcwd() + str(folder_path)
print(src)



file_list = os.listdir(src)

for i in file_list:
    exte = os.path.splitext(i)[1]
    if exte == '.png':
        s=os.path.join(src,i)
        shutil.move(s,dest)