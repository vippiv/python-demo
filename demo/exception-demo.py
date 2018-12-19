try:
    # 不能确定正确执行的代码
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    # 错误的处理代码
    print("除0错误")
# except ValueError:
#     print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("没有异常，执行这里")
finally:
    print("不管是否有异常，这里都会执行")

print("-" * 100)
