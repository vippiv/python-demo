# demo
list_arr = [1, 2, 3, 4, 5, 6]
search_num = 2
for k in list_arr:
    print(k)
    if k == search_num:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else下方的代码就不会被执行
    print("碰到break,调到这里了")

print("循环结束")


print("+" * 100)
# 常见应用，for-else语法重点是不能少了break
list_dict = [
    {
        "name": "zwl",
        "age": 20,
        "math": 95
    }, {
        "name": "han",
        "age": 20,
        "math": 93
    }, {
        "name": "mei",
        "age": 20,
        "math": 99
    }
]
find_name = "dc"
for item in list_dict:
    if item["name"] == find_name:
        print("找到了，%s，数学成绩是：%d，年龄： %d岁" % (find_name, item["math"], item["age"]))
        break
else:
    print("没有找到 %s" % find_name)
