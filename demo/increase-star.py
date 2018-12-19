# 递增的星星

# 第一种写法
i = 1
while(i <= 5):
    print("*" * i)
    i += 1

print("+" * 100)

# 第二种写法
r = 1
j = 1
while(r <= 5):
    j = 1
    while(j<=r):
        if j < r:
            print("*", end="")
        else:
            print("*")
        j += 1
    r += 1
