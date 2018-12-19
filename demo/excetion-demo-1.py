def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


try:
    # 异常具有传递性，可以在主程序中捕获异常
    print(demo2())
except ValueError:
    print("请输入正确的值")
except Exception as result:
    print("未知错误 %s" % result)
