# 定义一个扑克类，属性是颜色，数字。
# 定义一个手类，属性是扑克牌得颜色数字
# 定义一个人类，属性是左手，右手。类里定义一些方法，比如交换，展示


class Poker:
    def __init__(self, num, color):
        self.num = num
        self.color = color


class Hand:
    def __init__(self, poker):
        self.poker = poker


class Person:
    def __init__(self, left_h, right_h):
        self.left_hand = left_h
        self.right_hand = right_h

    def exchange(self):
        self.left_hand, self.right_hand = self.right_hand, self.left_hand

    def show(self):
        print("左手扑克颜色：%s，数字：%s" % (self.left_hand.poker.color, self.left_hand.poker.num))
        print("右手扑克颜色：%s，数字：%s" % (self.right_hand.poker.color, self.right_hand.poker.num))


poker_one = Poker(10, "梅花")
poker_two = Poker(9, "方块")
left_hand = Hand(poker_one)
right_hand = Hand(poker_two)
person = Person(left_hand, right_hand)
person.show()
print('*****左右手交换牌******')
person.exchange()
person.show()
