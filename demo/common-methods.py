# 公共方法，len(item)，del(item)，max(item)，min(item)，cmp(item1, item2)
# 公共方法可用于字符串，列表，元祖，字典
str = "sdfjkldsf4454"
print(len(str))

list_arr = [1, 5, 2, 6, 8, 6]
print(max(list_arr))
print(min(list_arr))


# 切片，适用于字符串，列表，元祖（有索引概念的数据类型就适用于切片方法，字典无索引概念，所以不适用）
list_arr = [0, 1, 2, 3, 4, 5, 6]
print(list_arr[1:3])

tuple_arr = (0, 1, 2, 3, 4, 5, 6)
print(tuple_arr[1:3])


# 运算符，适用于字符串，列表，元祖
print("字符串相加")
s1 = "123"
s2 = "456"
print(s1 + s2)

print("列表相加及列表append，extend对比")
l1 = [1, 2]
l2 = [3, 4]
l3 = [5, 6]
l4 = [7, 8]
print(l1 + l2)
l1.append(l2)
print(l1)
l3.extend(l4)
print(l3)


print("元祖相加")
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# 乘法适用于字符串，列表，元祖
print("列表，元祖乘法")
print(s1 * 2)
print(l1 * 2)
print(t1 * 2)


# in 运算符适用于字符串，列表，元祖，字典
o = {"a": "hi", "b": "hello"}
print("in运算符")
print("1" in s1)
print(1 in l1)
print(1 in t1)
print("a" in o)
print("hi" in o)


# not in 运算符适用于字符串，列表，元祖，字典
print("not in运算符")
print("1" not in s1)
print(1 not in l1)
print(1 not in t1)


# 输出二级制，八进制，十六进制
i = 5
print("二进制 %s" % bin(i))
print("八进制 %s" % oct(i))
print("十六进制 %s" % hex(i))
