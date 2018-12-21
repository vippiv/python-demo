# 静态方法和类方法即可以通过实例调用也可以直接通过类名调用
class Animal:

    info = "父类只能通过类调用的属性"

    def __init__(self):
        pass

    def instance_method(self):
        print("父类实例方式")

    @staticmethod
    def static_method():
        print("父类静态方法")

    @classmethod
    def class_method(cls):
        print(cls.info)
        print("父类类方法")


class Dog(Animal):
    def __init__(self):
        pass

    def instance_method(self):
        print("子类实例方法")

    @staticmethod
    def static_method():
        Animal.static_method()
        print("子类静态方法")

    @classmethod
    def class_method(cls):
        Animal.class_method()
        print("子类类方法")


dog = Dog()
dog.instance_method()
dog.static_method()
dog.class_method()
