# 多态

class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person():
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1、创建一个狗对象
# wangcai = Dog("wangcai")
wangcai = XiaoTianDog("飞天旺财")

# 2、创建一个人对象
xm = Person("小明")

# 3、让人调用和狗玩的方法
xm.game_with_dog(wangcai)
