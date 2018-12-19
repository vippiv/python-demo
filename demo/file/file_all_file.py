# 递归遍历文件夹中所有文件
import os


def all_file(sp):
    files_list = os.listdir(sp)
    for lists in files_list:
        path = os.path.join(sp, lists)
        print(path)
        if os.path.isdir(path):
            all_file(path)


all_file("D:\\python")
