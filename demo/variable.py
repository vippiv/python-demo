print("+" * 100)
print("变量学习")
print("1、python定义变量时不需要指定类型，解析器会自动根据右边的值推导变量类型")
print("+" * 100)

print("python语法层面没有变量定义标识符")
qqNum = "123456"
qqPass = "asjkfjsdf"
print("QQ账号：" + qqNum)
print("QQ密码：" + qqPass)


print("+" * 100)
print("超时买苹果案例")
price = 8.5
weight = 4
money = price * weight
print("单价：")
print(price)
print("购买份量：")
print(weight)
print("总价：")
print(money)


print("+" * 100)
print("个人信息案例")
name = "小明"
print(name)
age = 20
print(age)
# True 或者 False 首字母必须大写，否则会报变量未定义
gender = True
print(gender)
pHeight = 1.75
print(pHeight)
pWeight = "65kg"
print(pWeight)

print("+" * 100)
print("type函数")
print(type(name))
print(type(age))
print(type(gender))
print(type(pHeight))

print("+" * 100)
print("python2.0中有整形和长整型，python3.0中不分")
print(type(2**32))
print(type(2**64))
