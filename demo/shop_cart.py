# 功能要求：
# 要求用户输入总资产，例如： 2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]


def calc_price(good):
    for item in goods:
        if item["name"] == good:
            return item
    return ""


cart = []
total_asset = int(input("请输入总资产："))
print("-" * 100)
free_asset = total_asset

while True:
    print("可选购的商品：")
    for item in goods:
        print("商品： %s，价格：%s" % (item["name"], item["price"]))
    print("-" * 100)
    choose = input("请输入选购的商品：")
    choose_good_info = calc_price(choose)
    if not choose_good_info:
        print("您选购的商品不存在，请重新选择")
        print("-" * 100)
        continue
    size = int(input("请输入选购商品的数量："))
    if free_asset > choose_good_info["price"] * size:
        choose_good_info["size"] = size
        cart.append(choose_good_info)
        free_asset -= choose_good_info["price"]
        print("选购成功，当前购物车中有如下商品：")
        print(cart)
        print("-" * 100)
    else:
        print("当前余额不足以购买当前商品请重新选择")

    print("目前还剩 %s 元" % free_asset)
    is_go_on = int(input("是否继续选购商品："))
    # 0 表示退出 1 表示继续
    if is_go_on == 0:
        break
