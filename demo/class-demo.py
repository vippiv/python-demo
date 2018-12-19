# 类

# 类名的定义采用大驼峰写法（所有单词首字母全部大写）
class Cat:
    # 对象初始化时自动调用
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 喜欢吃鱼" % self.name)

    def drink(self):
        print("%s 想要喝水" % self.name)

    # 自定义输出内容及格式，必须有返回值
    def __str__(self):
        return "这只猫的名字叫 %s" % self.name

    # 对象销毁前自动调用
    def __del__(self):
        print("%s 被销毁了" % self.name)


tom = Cat("tom")
print(tom)
tom.eat()
tom.drink()
del tom

print("+" * 100)
tuzi = Cat("tuzi")
print(tuzi)
tuzi.eat()
tuzi.drink()
del tuzi

print("+" * 100)
print(dir(Cat))  # dir可以查询对象方法列表，其中有自带的也有自定义的


print("+" * 100)
print("采用十进制输出类Cat的内存地址 %d" % id(Cat))  # %d是采用十进制输出
print("采用十六进制输出类Cat的内存地址 %x" % id(Cat))  # %x采用十六进制输出
