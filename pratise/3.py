# 整数顺序排列问题简述：任意个数整数类型，a,b,c....x、y、z
# 提问：要求把这些数，按照由小到大的顺序输出
a = 0
b = 4
c = 8
x = 6
y = 5
z = 9


def sort_num(*args):
    temp = []
    for item in args:
        temp.append(item)
        temp.sort(reverse=False)
    print(temp)


sort_num(a, b, c, x, y, z)
