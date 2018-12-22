# 把A文件夹里的内容完整的复制到目标文件夹
# 已下做法或碰到无法转换编码的问题，暂时没找到解决办法
import os


def get_all_file(entry, write_dir):
    for item in os.listdir(entry):
        path = os.path.abspath(os.path.join(entry, item))
        target_path = os.path.abspath(os.path.join(write_dir, item))
        if os.path.isdir(path):
            if not os.path.isdir(target_path):
                os.mkdir(target_path)
            get_all_file(path, write_dir)
        else:
            file = open(path, "r", encoding="UTF-8")
            target_file = open(target_path, "w", encoding="UTF-8")
            for line in file.readlines():
                target_file.write(line)
            file.close()
            target_file.close()
        print(path)


get_all_file("D:/文档", "D:/tmp")


# shutil（高级的 文件、文件夹、压缩包 处理模块），模块可以直接进行复制，简单直接

# import shutil
#
#
# if not os.path.exists(dstDir):
#     shutil.copytree(srcDir, dstDir)
