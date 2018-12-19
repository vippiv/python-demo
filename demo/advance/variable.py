# 变量的引用
# a = 1
# print(id(a))  # id()返回数据存放的地址
# print(id(1))

# b = a
# print(id(b))


# b = 2
# print(a)
# print(b)


def test(num):
    # print("调用函数后的内存地址 %d" % id(num))

    # 1、定义一个字符串变量
    result = "hello"
    print("函数要返回数据的内存地址是 %d" % id(result))
    # 2、将字符串变量返回，返回的是数据的引用，而不是数据本身
    return result


a = 10
# print("未调用函数的内存地址 %d" % id(a))
# python本质上是值传递，传递的是地址
# 注意：如果函数有返回值，但没有定义变量接收
# 程序不会报错，但无法获得返回结果
# r = test(a)
# print("%s 的内存地址是 %d" % (r, id(r)))


# 不可比那数据类型，数字类型（int,long,bool,float,complex），字符串类型，元祖
# 可变类型， 列表，字段


# 内存地址不会发生变化（字典也一样）
list_arr = [1, 2, 3]
# print(id(list_arr))
list_arr.append(30)
# print(id(list_arr))
# 执行下面语句，内存地址会发生变化
list_arr = [4, 5, 6]
# print(id(list_arr))


# 哈希函数（只能接受不可变类型的数据），只要值相同，hash值就相同
# 在设置字典key时，python会先对key进行hash，以决定如何在内存中保存字典的数据，以方便后续对字典的操作：增。删，改，查
print(hash(0))
print(hash(0.1))
print(hash("hello"))
print(hash((0, 1, 2, 3)))
