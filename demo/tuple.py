# 元祖
# 定义元祖用一对小括号，列表用中括号（列表通常用来存储相同类型的数据，元祖则不同）
# 元祖变量一旦定义完成就不能修改（无法增删改）
info_tuple = ("小明", 18, 1.75)
# info_tuple[0] = "lis"  # 无法修改，一旦修改就报错
print(type(info_tuple))
print(info_tuple[0])  # 查找数据


# 定义一个只包含一个元素的元祖（元素后面必须有一个逗号）
print("+" * 100)
single_tuple = (5)
single_tuple_two = (5,)
print(type(single_tuple))  # int，如果没有逗号，解析器会忽略括号
print(type(single_tuple_two))  # tuple

# 常用操作
print("+" * 100)
print(info_tuple.count(18))  # 查某个元素的数量
print(info_tuple.index(18))  # 查某个元素的位置
print(len(info_tuple))  # 查元祖的长度

# 元祖遍历
print("+" * 100)
for info in info_tuple:
    # 由于元祖数据类型不一定一直，所以格式化输出很不方便，因此元祖的遍历不太常用
    print(info)


# 元祖的应用
print("+" * 100)
print("%s 的年龄是 %d，身高是 %.2f" % info_tuple)
info_str = "%s 的年龄是 %d，身高是 %.2f" % info_tuple
print(info_str)


# 元祖和列表之间的相互转换
print("+" * 100)
print(type(list(info_tuple)))
print(type(tuple(info_tuple)))


# 利用元祖实现交换变量（不借助第三个变量）
print("+" * 100)
a = 6
b = 100
print("交换前，a = %d，b = %d" % (a, b))
a, b = b, a
print("交换后，a = %d，b = %d" % (a, b))
