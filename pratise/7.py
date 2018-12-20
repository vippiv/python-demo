# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


def calc_char():
    str = input("请输入任意字符：")
    char_size = 0
    space_size = 0
    num_size = 0
    other_size = 0
    for i in str:
        if i.isspace():
            space_size += 1
        elif i.isdigit():
            num_size += 1
        elif i.isalpha():
            char_size += 1
        else:
            other_size += 1

    print("英文字母的个数是：%s，空格个数是：%s，数字个数是：%s，其他字符个数是：%s" % (char_size, space_size, num_size, other_size))


calc_char()
