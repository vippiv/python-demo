# 静态方法
# 既不访问对象属性也不访问对象方法同时也不访问类属性和类方法的方法就是静态方法
# 调用静态方法不需要创建对象，直接通过类名.调用静态方法
# 静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。可以理解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。


class Dog:
    # 定义静态方法
    @staticmethod
    def run():
        print("小狗要跑。。。")


# 通过类名.调用静态方法
Dog.run()

dog = Dog()
dog.run()

print("+" * 100)


class Game:

    # 历史最高分
    top_score = 0

    def __init__(self, player):
        self.player = player

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_scrore(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏了。。。" % self.player)


# 1、查看游戏的帮助信息
Game.show_help()

# 2、查看历史最高分
Game.show_top_scrore()

# 3、创建游戏对象
game = Game("头号玩家")
game.start_game()
