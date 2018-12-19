# from import 从某个模块中导入部分功能
# 如果从不同模块中导入两个同名的功能，后导入的将覆盖前一个
# 语法：from 模块1 import 模块别名，模块别名应该符合大驼峰命名法

from m1 import Cat
from m2 import say_hello as sh1
from m1 import say_hello

tuzi = Cat()
print(tuzi)

sh1()
say_hello()  # 由于后导入的是m1中的功能，因此把m2的覆盖掉了，可以给重名的起个别名
