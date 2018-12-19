print("数字型变量之间可以直接计算，数字甚至可以和布尔型直接计算")
print("变量为bool型，True对应数字1，False对应数字0")
i = 10
f = 10.5
b = True
b1 = False
print(i + f)
print(i + b)
print(f + b)
print(i + b1)
print(f + b1)
print(i * b1)
print(f * b1)

print("+" * 100)
print("字符串拼接，用+号拼接，用*号表示将运算符前面的字符串重复n倍")
first_name = "赵"
last_name = "四"
print(first_name + last_name)

print("+" * 100)
print("数字变量和字符串变量之间不能进行任何计算，但数字和字符串之间可以直接计算")
print(first_name * 10)
print(first_name + i)  # 报错
print(first_name * i)  # 报错

