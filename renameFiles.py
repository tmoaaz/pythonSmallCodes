# this code to organize photos in prank folder by rename it and delete integer
import os
import string
def rename_files():
    keep_files = os.listdir(r"C:\Users\moaaz\Desktop\prank")
    print (keep_files)
    table = str.maketrans(dict.fromkeys('0123456789'))
    os.chdir(r"C:\Users\moaaz\Desktop\prank")
    print(os.getcwd())
    for file_name in keep_files:
        os.rename(file_name,file_name.translate(table))

rename_files()
