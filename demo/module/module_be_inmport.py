print("不知道谁开发的")


def say_hello():
    print("你好，你好")

# 如果直接执行模块，__name__值永远是__main__
print(__name__)

if __name__ == "__main__":
    say_hello()
