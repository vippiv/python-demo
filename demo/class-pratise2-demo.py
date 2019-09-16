# 类，一个对象的属性可以是另外一个类创建的对象
# is运算符，在python中针对None比较时，建议使用is判断
# is用来判断两个变量引用对象是否相等
# ==用来判断内容是否相等


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了。。。" % self.model)
            return

        self.bullet_count -= 1
        print("[%s] 突突突。。。[%d]" % (self.model, self.bullet_count))


class Solider:
    def __init__(self, name):
        self.name = name
        self.gun = None  # None是关键字，表示空对象，什么都没有

    def fire(self):
        # 1、判断士兵是否有枪
        if self.gun is None:
            print("[%s] 还没有强。。。" % self.name)
            return
        # 2、高喊口号
        print("冲啊。。。[%s]" % self.name)
        # 3、装填子弹
        self.gun.add_bullet(50)
        # 4、发射子弹
        self.gun.shoot()


# 1、创建枪对象
ak47 = Gun("AK47")
# ak47.add_bullet(50)
# ak47.shoot()

# 2、创建许三多
xsd = Solider("许三多")
xsd.gun = ak47
xsd.fire()
print(xsd.gun)
