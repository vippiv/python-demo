# 格式化字符
# %s 字符串
# %d 十进制整数，%06d表示输出的整数显示位数，不足的地方使用0补全
# %f 浮点数，%.02f表示先书店只显示两位，不足的地方用0补全
# %%输出%

# 字符串和数字一起格式化输出
priceStr = input("请输入苹果单价：")
weightStr = input("请输入苹果重量：")
money = float(priceStr) * float(weightStr)
print("苹果的单价：%s" % priceStr)
print("苹果的重量：%s" % weightStr)
print("苹果的总价：%f" % money)
print("苹果的单价：%s 元/kg，苹果的重量：%s kg，苹果的总价：%f 元，输出一个%%要用%%%%" % (priceStr, weightStr, money))

# 控制数字输出的位数
i = 1
i1 = 123
f = 12.10255122
print("输出整数：%d" % i)
print("控制整数的输出位数：%06d，位数不足用0补，位数充足无影响，原来什么样输出还是什么样" % i1)
print("控制浮点数的输出位数：%.4f，会四舍五入，位数不够用0补足" % f)
print("控制浮点数的输出位数：%.12f，会四舍五入，位数不够用0补足" % f)
