# 格式化字符串的函数 str.format()，增强了字符串格式化的功能，通过 {} 和 : 来代替以前的 %
print("{} {}".format("hello", "world"))
print("{} {} {}".format("world", "war", 2))

# 设置顺序
print("{1} {0}".format("hello", "world"))
print("{1} {0} {1}".format("hello", "world"))


# 设置参数
print("姓名：{name}，年龄：{age}".format(name="林子", age=25))


# 传入对象，传入字典无效
class AssignValue(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Scool:
    def __init__(self, level):
        self.level = level


dict_o = AssignValue('lin', 22)
dict_s = Scool('三年级')
print("姓名：{0.name}，年龄：{0.age}，年级：{1.level}".format(dict_o, dict_s))


# 传入列表
list_arr_one = ['百度', 'https://www.baidu.com']
list_arr_two = ['新浪', 'http://www.sina.com']
print("网站名：{0[0]}, 地址：{0[1]}\n网站名：{1[0]}，地址：{1[1]}".format(list_arr_one, list_arr_two))  # "0" 是必须的


# 数字格式化
print("{:.2f}".format(1.23622))
print('{:d}'.format(12361))
