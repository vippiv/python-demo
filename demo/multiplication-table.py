# 九九乘法表
i = 1
j = 1
while(j<=9):
    i = 1
    while(i<=j):
        print("%d * %d = %d" % (i, j, i*j), end="\t")
        i += 1
    print("")
    j += 1

