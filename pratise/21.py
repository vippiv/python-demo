# 文件批量改名
import os


def batch_rename(entry, base_name):
    """
    批量重命名文件
    :param entry: 入口目录，务必以/结尾
    :param base_name: 重命名的基础名称
    :return:
    """
    try:
        file_list = os.listdir(entry)
        i = 1
        for file in file_list:
            suffix = os.path.splitext(file)[1]
            old_name = entry + file
            new_name = entry + base_name + "_" + str(i) + suffix
            os.rename(old_name, new_name)
            i += 1
    except Exception as result:
        print(result)


batch_rename("D:/Personal/Desktop/img/710-324/", "710-324")
