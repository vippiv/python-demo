# 类练习
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1.0

    def __str__(self):
        return "%s 爱跑步，目前的体重是 %.2f 公斤" % (self.name, self.weight)


xm = Person("小明", 75.0)
xm.run()
xm.eat()
print(xm)

print("=" * 50)
xmei = Person("小美", 45)
xmei.run()
xmei.eat()
print(xmei)
