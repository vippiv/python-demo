# 字符串
str = "hello python"
str2 = 'my name is "tom"'

# 字符串输出
print(str)
print(str[0])
print(str2)
print(str2[0])


# 字符串遍历
print("+" * 100)
for char in str2:
    print(char, end="  ")
print("")


# 字符串长度
print("+" * 100)
print("字符串长度：%d" % len(str))


# 字符串中某个字符出现的次数
print("+" * 100)
print("m在字符串str2中出现的次数：%d" % str2.count("m"))


# 字符串中某个字符出现的位置
print("+" * 100)
print("p在str中出现的位置是：%d" % str.index("p"))
print("hello在str中出现的位置是：%d" % str.index("hello"))


# 判断字符串中是否存在某个字符
print("+" * 100)
isIn = "my" in str2
print("检查my是否在str2中：", end="")
print(isIn)


# 判断字符串中是否只有("注意是只有")空格（\t，\n，\r都可以判断出来）
print("+" * 100)
str3 = "   "
print(str.isspace())
print(str3.isspace())


# 判断字符串中是否只包含数字
"""
下面这三个方法不能判断小数
"""
print("+" * 100)
str4 = "12"
print(str4.isdecimal())  # 只能判断阿拉伯数字
print(str4.isdigit())  # 可以判断unicode字符串，如(1)，\u00b2
print(str4.isnumeric())  # 可以判断unicode字符串，还可以判断中文数字，如“一千零一“


# 判断是否以指定的字符串开始
print("+" * 100)
print(str.startswith("Hello"))


# 判断是否以指定的字符串结束
print("+" * 100)
print(str.endswith("world"))


# 查找指定的字符串
print("+" * 100)
print(str.find("lo"))  # 返回索引位置，和index方法相似，但也有不同，如下
print(str.find("abc"))  # 如果不存在将返回-1，str.index("")则会报错


# 替换指定的字符串
print("+" * 100)
print(str.replace("hello", "fuck"))  # 返回的是新字符串，不修改原字符串
print(str)


# 文本对齐，str.ljust()，str.rjust()，str.center()
print("+" * 100)
poem = [
    "悯农",
    "李白",
    "锄禾日当午",
    "汗滴禾下土",
    "谁知盘中餐",
    "粒粒皆辛苦"
]
for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))
    # print("|%s|" % poem_str.ljust(10, "　"))
    # print("|%s|" % poem_str.rjust(10, "　"))


# 去除空白字符
print("+" * 100)
str5 = " hello china "
print("|%s|" % str5)
print("|%s|" % str5.strip())
print("|%s|" % str5.lstrip())
print("|%s|" % str5.rstrip())


# 字符串拆分和拼接
print("+" * 100)
poem_str1 = "登黄鹤楼\t王之涣\t白日依山尽\t黄河入海流\t欲穷千里目\t更上一层楼"
print(poem_str1.split())
print("，".join(poem_str1.split()))


# 字符串切片
print("+" * 100)
str6 = "0123456789"
print(str6[2:6])  # 截取2-5位
print(str6[2:])  # 截取2到最后一位
print(str6[0:6])  # 截取0-5
print(str6[:6])  # 截取0-5
print(str6[:])  # 截取完整字符串
print(str6[::2])  # 间隔截取
print(str6[1::2])  # 从索引1开始间隔截取
print(str6[2:-1])  # 截取从第二为到倒数第一个字符
print(str6[-2:])  # 截取末尾两个字符
print(str6[-1::-1])  # 字符串逆序
