import shutil
import os
from filecmp import dircmp


all_dirs_list = os.listdir(".")  # list of all directories in the directory that this script is in

# Declaring and initializing a list containing all Dev directories
dev_dirs_list = []
for i in all_dirs_list:
    if (i[0] == "D") and (i[1] == "e") and (i[2] == "v"):
        dev_dirs_list.append(i)

for dev_dir in dev_dirs_list:
    if(not os.path.exists("./AllDev/" + dev_dir)):
        os.makedirs("./AllDev/" + dev_dir)
    print("AllDev directory not found\nAllDev directory created")


# A function that will recursively walk through a directory structure and copy only the new or modified files
def copy_tree(dir1, dir2):
    comparison = dircmp(dir1, dir2)
    for i in comparison.left_only:
        src = dir1 +"/"+ i
        dest = dir2 +"/"+ i
        if(os.path.isdir(src)):
            shutil.copytree(src, dest, dirs_exist_ok=True)
            print(src+" Copied to "+dest)
        else:
            shutil.copy(src, dest)
            print(src+" copied To "+dest)

    for i in comparison.diff_files:
        src = dir1 +"/"+ i
        dest = dir2 
        shutil.copy(src, dest)
        print(src+"copied to"+dest)

#     for i in comparison.common_dirs:
        new_dir1 = dir1 + "/" + i
        new_dir2 = dir2 + "/" + i
        copy_tree(new_dir1, new_dir2)

# calling of copy_tree function
for dev_dir in dev_dirs_list:
    src_path = "./" + dev_dir
    dest_path = "./AllDev/" + dev_dir
    copy_tree(src_path, dest_path)
