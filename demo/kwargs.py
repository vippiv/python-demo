# 测试kwargs解构
def test_kwargs(**kwargs):
    for item in kwargs:
        print(item)


dict = {
    "name": "zwl",
    "age": 20,
    "college": 'universal'
}

test_kwargs(**dict)
# test_kwargs(dict)  # 这样调用就是错误的，必须用对应的**进行解构
