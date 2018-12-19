# 多继承
# 如果父类之间存在同名方法，应该尽量避免使用多继承
# method resolution order(mro)程序通过mro确定调用顺序
class A:
    def test(self):
        print("A --- test方法")

    def demo(self):
        print("A --- demo方法")


class B:
    def demo(self):
        print("B --- demo方法")

    def test(self):
        print("B --- test方法")


class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()
c.test()
c.demo()


# 确定C类对象调用方法的顺序
print(C.__mro__)



