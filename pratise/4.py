# 提问：将一个列表的数据复制到另一个列表中。
# 请仔细看要求，这里要求的是复制数据到一个新的列表中。

li = ["a", "b", "c", "d"]
copy_list = []

# copy_list = li  # 这种复制只是将copy_list的在指针指向了li并未实现真正的复制

copy_list = li[:]

copy_list[0] = "G"

print(li)
print(copy_list)



