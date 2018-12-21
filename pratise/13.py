"""
定义一个列表的操作类：Listinfo

包括的方法:

1 列表元素添加: add_key(keyname) [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	[list:列表类型]
4 删除并且返回最后一个元素：del_key()

a = Listinfo([44,222,111,333,454,'sss','333'])
"""


class Listinfo:
    def __init__(self):
        self.list = []

    def add_key(self, keyname):
        self.list.append(keyname)

    def get_key(self, num):
        if num < 0 or num > len(self.list):
            return "not found"
        return self.list[num]

    def update_list(self, list):
        self.list.extend(list)

    def del_key(self):
        ele = self.list[len(self.list) - 1]
        del self.list[-1:]
        return ele

    def show_list(self):
        print(self.list)


list = Listinfo()
list.add_key(100)
print(list.get_key(0))
list.update_list(["dsf", 5])
list.show_list()
print(list.del_key())
list.show_list()
