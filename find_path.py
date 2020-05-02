
import os
def find_files(dir,ext):
    dir=os.path.realpath(dir)
    for root,dirs,files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                print(root + '\\' +file)

path=input("enter the path of folder:: ")
ext=input("enter the extension of files:: ")
find_files(path,ext)