# 数据类型，集合
# set集合，是一个无序且不重复的元素集合
# 集合对象是一组无序排列的可哈希的值，集合成员可以做字典中的键。
# 集合支持用in和not in操作符检查成员，由len()内建函数得到集合的基数(大小)， 用 for 循环迭代集合的成员。
# 因为集合本身是无序的，不可以为集合创建索引或执行切片(slice)操作，也没有键(keys)可用来获取集合中元素的值。

# 创建集合
s = set()
print(type(s))  # 创建空集合，只能这么写
s1 = {}
print(type(s1))  # 这样写创建的就是字典

a = set('boyn')
b = set(['y', 'b', 'o', 'o', 'h', 'n'])
c = set({"k1": 'v1', 'k2': 'v2'})
d = {'k1', 'k2', 'k2'}
e = {('k1', 'k2', 'k2')}
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

# 集合操作
a1 = set("han")
print(a1)
a1.add("tang")  # add是整个添加成一个成员
print(a1)
a1.update("ming")  # update是打散了去重逐个添加进去
print(a1)
a1.remove("tang")  # 删除某个成员
print(a1)
a.clear()  # 清空集合
print(a)
print("检查元素是否在集合中")
print("o" in a1)


# 集合转换
print(type(list(a1)), list(a1))
print(type(tuple(a1)), tuple(a1))
print(type(str(a1)), str(a1))


# 集合特有功能
print(a1 & b)  # 交集
print(a1 | b)  # 并集
print(a1 - b)  # 差集
print(a1 ^ b)  # 对称差集
print(a1 <= b)  # 子集
print(a1 >= b)  # 子集
