# 类属性
class Tools:

    # 这是类属性，专门用来记录类相关特征
    count = 0

    def __init__(self, name):
        self.name = name
        print("创建了一个工具, %s" % self.name)
        Tools.count += 1

    # @classmethod 开头的是类方法，在内部用cls表示
    @classmethod
    def add_count(cls):
        cls.count = 100
        print("类方法")


Tools.read()
tool1 = Tools("锤子")
tool2 = Tools("斧子")
tool3 = Tools("剪刀")

print("创建了 %d 件工具" % Tools.count)
# print(tool1.count)  # 不推荐这种方式，因为count可能存在被赋值的情况
