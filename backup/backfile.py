import os
import shutil

source=input("Enter source folder name")
des=input("enter des folder name")

source= source + '/'
des = des + '/'

list_file=os.listdir (source)
for i in list_file:
    shutil.copy((source + i),des)