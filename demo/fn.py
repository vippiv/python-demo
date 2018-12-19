# 函数定义文件，一个py文件也是一个模块，模块名（文件名）也是一个标识符（必须遵守标识符定义规范，如while.py就是非法的）

def multiple_table():
    """九九乘法表，官方建议函数文档注释写在这里，用三地引号包起来"""
    i = 1
    j = 1
    while (j <= 9):
        i = 1
        while (i <= j):
            print("%d * %d = %d" % (i, j, i * j), end="\t")
            i += 1
        print("")
        j += 1


def say_hello():
    print("hello")


# python必须先定义再调用，没有函数提升的说法
# say_hello()


def sum(n1, n2):
    """求和"""
    print("%d + %d = %d" % (n1, n2, (n1 + n2)))


# sum(10, 15)


def minus(n1, n2):
    return n1 - n2


# print(minus(30, 11))


def out_fn():
    print("top")
    inner_fn()
    print("bottom")


def inner_fn():
    print("middle")


# out_fn()


def print_line(char, time):
    print(char * time)


def print_lines(char, size, time):
    """
    打印多行分割线
    :param char: 分割字符
    :param size: 一行显示次数
    :param time: 显示行数
    :return: 无返回值
    """
    row = 0
    while(row<=time):
        print_line(char, size)
        row += 1


# print_lines("*", 50, 5)


def measure():
    """测量温度和湿度，返回元祖"""
    print("开始测量。。。")
    temp = 39
    wetness = 50
    print("测量结束")

    # 返回元祖
    # return (temp, wetness)
    # 如果是元祖，可以去掉小括号
    return temp, wetness


# print(measure())
# gl_temp, gl_wetness = measure()  # 可以这样写，相当于参数解构，元祖的值会分别赋值给对应的变量（定义变量个数必须和元祖元素个数一样，否则报错）
# print(gl_temp)
# print(gl_wetness)


def changeable_var(list_arr):
    # list_arr[0] = 100  # 由于列表是可变数据，所以直接修改成员会导致全局变量（列表）发生改变
    list_arr = [4, 5, 6]  # 如果是这样就不会改变全局变量（列表）
    # list_arr += list_arr  # 该操作本质上回调用列表的extend方法


gl_list_arr = [0, 1, 2]
print(gl_list_arr)
changeable_var(gl_list_arr)
print(gl_list_arr)


def print_info(name, gender=True):
    """
    缺省值
    :param name:
    :param gender:
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


print_info("小明")
print_info("小美", False)


def mutiple_args(num, *args, **kwargs):
    """
    一个星号代表接受元祖
    两个星号代表字典
    :param num:
    :param args: 元祖
    :param kwargs: 字典
    :return:
    """
    print(num)
    print(args)
    print(kwargs)


mutiple_args(1, 2, 3, 4, name="小明", age=20)


def sum_numbers(*args):
    """
    利用元祖多参数求和
    :param args:
    :return:
    """
    num = 0
    for k in args:
        num += k

    return num


print(sum_numbers(1, 2, 3, 4))


def unpacking_demo(*args, **kwargs):
    print(args)
    print(kwargs)


unpacking_list = [0, 1, 2, 3]
unpacking_dict = {
    "name": "zwl",
    'age': 20
}
unpacking_demo(unpacking_list, unpacking_dict)  # 直接这样调用，参数整体会被当做元祖传入第一个参数
unpacking_demo(*unpacking_list, **unpacking_dict)  # 采用拆包方式传递参数才对


def recursion_demo(num):
    if num > 0:
        recursion_demo(num - 1)
    print(num)


recursion_demo(3)
