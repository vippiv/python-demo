"""
定义一个集合的操作类：Setinfo

包括的方法:

1 集合元素添加: add_setinfo(keyname) [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
set_info = Setinfo(你要操作的集合)
"""


class Setinfo:
    def __init__(self, my_set):
        self.sett = my_set

    def add_setinfo(self, keyname):
        if isinstance(keyname, (str, int)):
            self.sett.add(keyname)
            return self.sett

    def get_intersection(self, unioninfo):
        if isinstance(unioninfo, set):
            a = self.sett & (unioninfo)
            return a

    def get_union(self, unioninfo):
        if isinstance(unioninfo, set):
            a = self.sett | (unioninfo)
            return a

    def del_difference(self, unioninfo):
        if isinstance(unioninfo, set):
            a = self.sett - (unioninfo)
            return a


a = Setinfo({1, "a", 2, "b", 3, "c"})
print(a.add_setinfo(4))
print(a.get_intersection({1, 2, "a"}))
print(a.get_union({2, 3, 4, "c", "d"}))
print(a.del_difference({1, 2, 3, 4}))
