# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。


def calc_sum():
    num = input("请输入整数：")
    size = int(input("请输入相加的次数："))
    out = ""
    sum = 0
    for i in range(1, size + 1):
        if i == size:
            out += num*i
            print(out)
        else:
            out += (num*i + "+")
        sum += int(num*i)
    # print(eval(out))  # 这种做法一样可以得到结果，eval功能很强大
    print(sum)


calc_sum()
