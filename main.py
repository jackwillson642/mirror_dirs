import shutil
import os

all_dirs_list = os.listdir(".")
dev_dirs_list = []

for i in all_dirs_list:
    if (i[0] == "D") and (i[1] == "e") and (i[2] == "v"):
        dev_dirs_list.append(i)
        print(i)

for i in dev_dirs_list:
    src_path = "./" + i
    dest_path = "./restricted/" + i
    shutil.copytree(src_path, dest_path, copy_function=shutil.copy, dirs_exist_ok=True)
