# 私有属性和私有方法，在属性和方法前增加两个下划线就变成了私有属性和方法
# 私有属性在外界不能被直接访问
# 私有属性在对象的方法内部可以访问


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有属性

    # 私有方法
    def __secret(self):
        print("%s的年龄是：%d" % (self.name, self.__age))

    def secret(self):
        self.__secret()


w = Women("小美")
# print(w.__age)  # 这里访问会报错
# w.__secret()  # 这里访问会报错
w.secret()
