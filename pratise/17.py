# 随机整数生成类。要求： 可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数。
import random


class RandomInt:

    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    def get_int(self):
        i = 0
        while i <= self.count:
            num = random.randint(self.start, self.end)
            print(num)
            i += 1


random_int = RandomInt(0, 11, 6)
random_int.get_int()
