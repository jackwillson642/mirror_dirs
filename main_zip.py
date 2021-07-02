import os
from shutil import make_archive
import zipfile


all_dirs_list = os.listdir(".")  # list of all directories in the directory that this script is in

# Declaring and initializing a list containing all Dev directories
dev_dirs_list = []
for i in all_dirs_list:
    if (i[0] == "D") and (i[1] == "e") and (i[2] == "v"):
        dev_dirs_list.append(i)

restricted_dir = "./AllDev_zip/"

# This block of code creates AllDev and Dev* directories if absent
for dev_dir in dev_dirs_list:
    if(not os.path.exists(restricted_dir + dev_dir)):
        dirpath = restricted_dir + dev_dir
        os.makedirs(dirpath)
        dirname = os.path.split(dirpath)[1]
        print(dirname + " directory not found")
        print(dirname  + " directory created")
print("\n")  # 2 line gap

# Archiving directories
for dev_dir in dev_dirs_list:
    archive_name = dev_dir + ".zip"  # Name of the resulting archived(zip) file
    make_archive(archive_name,
            "zip",
            root_dir = dev_dir,
            base_dir = restricted_dir)
