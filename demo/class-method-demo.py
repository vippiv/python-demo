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
