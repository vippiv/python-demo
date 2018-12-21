"""
二、定义一个字典类：dictclass。完成下面的功能：

dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})
"""


class Dictclass:
    def __init__(self, dict):
        self.dict = dict

    def __key_in_dict(self, key):
        return key in self.dict

    def del_dict(self, key):
        if self.__key_in_dict(key):
            del self.dict[key]

    def get_dict(self, key):
        if self.__key_in_dict(key):
            return self.dict[key]
        else:
            return "not found"

    def get_key(self):
        return self.dict.keys()

    def update_dict(self, new_dict):
        self.dict.update(new_dict)
        return self.dict.values()


dict = {
    "name": "zwl",
    'age': 20
}

dict_instance = Dictclass(dict)
# dict_instance.del_dict("name")
print(dict_instance.get_dict("name"))
ret_list = dict_instance.update_dict({
    "level": "top"
})
print(ret_list)
