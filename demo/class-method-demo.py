# 原则上，类方法是将类本身作为对象进行操作的方法。假设有个方法，且这个方法在逻辑上采用类本身作为对象来调用更合理，那么这个方法就可以定义为类方法。另外，如果需要继承，也可以定义为类方法。

# 类方法
class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print('工具对象的数量 %d' % cls.count)


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool('榔头')



# 调用类方法
Tool.show_tool_count()
