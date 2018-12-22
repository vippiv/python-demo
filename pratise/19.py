# 语法上建议except后加个原因，但这样写也没错
try:
    num = int(input("请输入数字："))
except:
    print("数据类型错误")
