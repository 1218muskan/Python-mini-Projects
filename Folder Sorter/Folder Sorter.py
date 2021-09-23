import os, shutil

path= input("Enter the path of folder you want to sort: ")
fileList =os.listdir(path)

for files in fileList:
    fname, ext = os.path.splitext(files)
    ext = ext[1:]   #to remove '.' from extension

    if ext== "":
        continue

    if os.path.exists(os.path.join(path,ext)):
        shutil.move(os.path.join(path,files),os.path.join(path,ext))

    else:
        os.makedirs(os.path.join(path,ext))
        shutil.move(os.path.join(path,files),os.path.join(path,ext))

print("File moved Successfully!")

