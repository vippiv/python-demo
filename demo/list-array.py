# 列表，在其他语言中叫数组
list_arr = ["zs", "ls", "ww", "zs"]

# 列表取值，超出索引会报错
# print(list_arr[0])

# 根据内容取索引，如果找不到则报错
# print(list_arr.index("ww"))

# 修改指定位置的数据，
# list_arr[0] = "赵文林"
# list_arr[3] = "小明"  # 超出索引会报错
# print(list_arr)

# 列表新增，在末尾增加
# list_arr.append("zwl")
# print(list_arr)

# 列表新增，在指定位置插入
# list_arr.insert(1, "hello")
# print(list_arr)

# 列表新增,直接增加数组
# tmp = ["swk", "zbj", "ss"]
# list_arr.extend(tmp)  # 调用extend会对参数进行迭代，拆出单个元素，如果参数无法迭代调用extend就会报错
# print(list_arr)

# 列表删除，参数是元素，不能是索引，不存在则报错
# list_arr.remove("zs") # 删除列表中第一次出现的数据
# print(list_arr)

# 列表删除，不给参数默认删除最后一个，给定索引，则删除索引位置的数据
# list_arr.pop(1)
# print(list_arr)

# 列表删除，clear表示删光
# list_arr.clear()
# print(list_arr)

# 列表删除，用del关键字删除，一般不建议这么用
# del本质上用来把一个变量从内存中删除
# del list_arr[0]
# print(list_arr)

# 列表统计
# print(len(list_arr))  # 查列表元素的数量
# print(list_arr.count("zs"))  # 查列表中某个元素出现的数量

# 列表排序
# num_arr = [0, 2, 5, 8, 4, 3, 3, 5, 4, 1, 7, 0]
# num_arr.sort()  # 按升序排列
# num_arr.sort(reverse=True)  # 按降序排列
# num_arr.reverse()  # 顺序翻转
# print(num_arr)


# 列表循环
for item in list_arr:
    print(item)


# keys 把字典中的key转换成列表
dict = {
    "name": "zwl",
    "age": 20,
    "gender": "male",
    "collage": "sz unival"
}
li = dict.keys()
print(li)
