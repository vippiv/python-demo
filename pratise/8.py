# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

def calc_sum():
    num = input("请输入整数：")
    size = int(input("请输入相加的次数："))
    sum = 0
    for i in range(size):
        sum += int(num*i)

calc_sum()
