# 简述：要求输入某年某月某日
# 提问：求判断输入日期是当年中的第几天？


def get_days():

    year = int(input("请输入年："))
    month = int(input("请输入月："))
    day = int(input("请输入日："))

    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if 0 < month <= 12:
        sum = months[month - 1]
    else:
        print("月份错误")

    sum += day

    leap = 0

    if (year % 400 == 0) or (year % 4 == 0) or (year % 100 != 0):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1

    print("%s-%s-%s是第%s天" % (year, month, day, sum))


try:
    get_days()
except ValueError:
    print("数据类型错误")
except Exception as result:
    print("未知错误 %s" % result)
