# 字典，在JavaScript中叫对象
person = {
    "name": 'zwl',
    "age": 20,
    "gender": "male",
    "home": "suzhou"
}

# 字典键值获取
print("+" * 100)
print(person.keys())
print(person.values())
print(person.items())


# 字典遍历
print("+" * 100)
for item in person:
    print(item, end="：")
    print(person[item])


# 字典取值
print("+" * 100)
print("姓名： %s" % person["name"])  # 取不存在的值会报错


# 字典修改
print("+" * 100)
person["name"] = "张三"
print("修改后的名字是：%s" % person["name"])

# 字典增加
print("+" * 100)
person["nickname"] = "kiki"
print("小名是： %s" % person["nickname"])

# 字典删除
print("+" * 100)
person.pop("age")  # 方法一
del person["name"]  # 方法二
print(person)


# 字典长度
print("+" * 100)
print("字典长度：%d" % len(person))


# 字典合并
print("+" * 100)
family = {
    "father": "haha",
    "mother": "fafa"
}
person.update(family)
print("字典合并，如果有同名的key，则会覆盖原有的键值")
print(person)

# 字典清空
print("+" * 100)
print("字典清空")
person.clear()
print(person)


# 字典列表综合应用
print("+" * 100)
print("字典列表综合应用")
students = [
    {
        "name": "zwl",
        "age": 12,
        "gender": "male"
    }, {
        "name": "meimei",
        "age": 13,
        "gender": "female"
    }, {
        "name": "suncoo",
        "age": 11,
        "gender": "female"
    }
]
for item in students:
    print("姓名：%s，年龄：%d，性别：%s" % (item["name"], item["age"], item["gender"]), end="\t")
    print("")


# fromkeys 将列表中的值转换成字典
li = ["a", "b", "c", "d"]
dict = {}
print(dict.fromkeys(li))
