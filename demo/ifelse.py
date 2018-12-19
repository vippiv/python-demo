# note：python语法if/else后面都要求有冒号，JavaScript则不需要
age = input("请输入年龄：")
if int(age) >= 18:
    print("可以上网")
elif int(age) < 12:
    print("太小了")
else:
    print("再等两年吧")
