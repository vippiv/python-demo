# 继承（子类拥有父类所有的方法和属性），Animal是大类，Dog是子类，子类需要继承大类
# 继承具有传递性，子类可以继承父类的方法和属性也可以继承父类的父类的方法和属性
# 类的私有属性和方法，子类无法访问


class Animal:

    def __init__(self):
        self.fuck = "fuck"

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")

    def __belong(self):
        print("动物的私有方法")

    def belong(self):
        self.__belong()


class Dog(Animal):
    # 可以通过重写方法实现对父类方法的覆盖
    def eat(self):
        print("吃肉and吃鱼")

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("这条狗会飞")

    def bark(self):
        # 1、针对子类特有的需求编写代码
        print("神一样的叫法。。。")

        # 2、使用super()，调用原本在父类中封装的代码
        super().bark()

        # 增加其他子类代码
        print("sf&&8Jh")


# 创建一个对象 - 狗对象
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
# wangcai.__belong()  # 这里无法直接访问父类的私有属性
wangcai.belong()  # 这里就可以调用了
print(wangcai.fuck)


print("+" * 100)
xtq = XiaoTianQuan()
xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()
xtq.bark()
xtq.fly()
