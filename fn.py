import random


def valication_code():
    """
    生成4位验证码，依赖random模块
    :return:
    """
    tmp = ''
    for i in range(0, 4):
        n = random.randrange(0, 2)
        if n == 0:
            num = random.randrange(65, 91)
            tmp += chr(num)
        else:
            k = random.randrange(0, 10)
            tmp += str(k)

    print(tmp)
