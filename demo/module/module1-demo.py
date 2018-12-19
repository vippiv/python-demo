# 模块，一个python文件就是一个模块，每个python都应该是可以导入的
# 导入模块时，python会搜索当前目录指定模块名的文件，如果有直接导入
# 如果没有，再搜索系统目录（由于存在这种行为，如果定义一个和系统模块重名的文件，将导致系统模块无效）

import m1
import m2
import random

m1.say_hello()
m2.say_hello()

c = m1.Cat()
print(c)

d = m2.Dog()
print(d)


print("+" * 100)
print("生成随机数")
print(random.randint(0, 10))
print("当前模块加载路径 %s" % random.__file__)
