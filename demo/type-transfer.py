# 类型转换
i = "123"
print(type(i))
print(type(int(i)))
print(type(float(i)))


# 案例
priceStr = input("请输入苹果单价：")
weightStr = input("请输入苹果重量：")
money = float(priceStr) * float(weightStr)
print("苹果的单价：%s" % priceStr)
print("苹果的重量：%s" % weightStr)
print("苹果的总价：%f" % money)
print("苹果的单价：%s 元/kg，苹果的重量：%s kg，苹果的总价：%f 元，输出一个%%要用%%%%" % (priceStr, weightStr, money))
