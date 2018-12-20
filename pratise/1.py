# 简述：这里有四个数字，分别是：1、2、3、4
# 提问：能组成多少个互不相同且无重复数字的三位数？各是多少？

list = []   # 定义一个空的列表用来存储生产的数字
for i in range(1, 5):   # 定义百位数
    for j in range(1, 5):   # 定义十位数
        for k in range(1, 5):  # 定义个位数
            if i != j and j != k and i != k:
                num = i*100+j*10+k
                print(num)
                list.append(num)   # 将生成的数字加入到list列表中
                result_num = len(list)   # 统计列表中元素的个数

print("可以组合的个数为%d" % result_num)




