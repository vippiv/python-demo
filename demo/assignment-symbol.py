# 赋值运算符，等于（=），加等于（+=），减等于（-=），乘等于（*=），除等于（/=），取整除等于（//=），取余等于（%=），交集（&），并集（|），差集（-）
i = 10
j = 25
i += j
print(i)

i -= j
print(i)

i *= j
print(i)

i /= j
print(i)

i //= j
print(i)

i %= j
print(i)


x = set('runoob')
y = set('google')
print(set(x))  # set可去重
print(set(y))
print(x & y)  # 求交集
print(x | y)  # 求并集
print(x - y)  # 求差集
