##########################################
# This script is designed to back up a set of directories of the format:
# "Dev*", Where * represents anything(usually a number).
# The backup is kept in a folder named AllDev.
##########################################

import shutil
import os
from filecmp import dircmp


all_dirs_list = os.listdir(".")  # list of all directories in the directory that this script is in

# Declaring and initializing a list containing all Dev directories
dev_dirs_list = []
for i in all_dirs_list:
    if (i[0] == "D") and (i[1] == "e") and (i[2] == "v"):
        dev_dirs_list.append(i)

restricted_dir = "./AllDev/"

# This block of code creates AllDev and Dev* directories if absent
for dev_dir in dev_dirs_list:
    if(not os.path.exists(restricted_dir + dev_dir)):
        dirpath = restricted_dir + dev_dir
        os.makedirs(dirpath)
        dirname = os.path.split(dirpath)[1]
        print(dirname + " directory not found")
        print(dirname  + " directory created")
print("\n")  # 2 line gap


# A function that will recursively walk through a directory structure and copy only the new or modified files
def copy_tree(dir1, dir2):
    comparison = dircmp(dir1, dir2)
    for i in comparison.left_only:
        src = dir1 +"/"+ i
        dest = dir2 +"/"+ i
        if(os.path.isdir(src)):
            shutil.copytree(src, dest, dirs_exist_ok=True)
            dirname = os.path.split(src)[1]
            print(dirname+" directory backed up")
        else:
            shutil.copy(src, dest)
            filename = os.path.split(src)[1]
            print(filename+" file backed up")

    for i in comparison.diff_files:
        src = dir1 +"/"+ i
        dest = dir2 
        shutil.copy(src, dest)
        filename = os.path.split(src)[1]
        print(filename+" file updated")

    for i in comparison.common_dirs:
        new_dir1 = dir1 + "/" + i
        new_dir2 = dir2 + "/" + i
        copy_tree(new_dir1, new_dir2)

# calling of copy_tree function
for dev_dir in dev_dirs_list:
    src_path = "./" + dev_dir
    dest_path = restricted_dir + dev_dir
    copy_tree(src_path, dest_path)

# input()  # This function keeps the output window open in the Windows operating system.
