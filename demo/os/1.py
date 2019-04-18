import os
# print(os.listdir())  # 列出当前目录下所有文件/文件夹
# print(os.path.exists('1.py'))  # 检测某个文件/文件夹是否存在

# if not os.path.exists('os'):
#     os.mkdir("os")  # 创建目录

# print(os.path.dirname(os.path.abspath(__file__)))  # 返回当前文件所在的目录
# print(os.path.abspath(__file__))  # 返回当前文件的绝对路径并把顺斜杠转换成反斜杠
# print(__file__)  # 当前文件的绝对路径

# print(os.path.split("D:/python/demo/os"))  # 把路径切割成元祖，以最后一级为切割依据
# print(os.path.isfile("D:/python/demo/os/1.py"))  # 判断指定路径是否是文件，只有文件真实存在才返回True
# print(os.path.isdir("D:/python/demo/os/ad/"))  # 判断指定路径是否是目录，只有，目录真实存在才返回True
# print(os.path.realpath("2/4"))  # 返回指定路径的真实绝对路径

# os.chdir('os')
# print(os.getcwd())

os.mkdir('mkdir')
