# 封装（基于登录功能）
from selenium import webdriver


# 打开浏览器
def open_browser():
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle


# 打开网址
def open_url(driver, url):
    driver.open(url)
    driver.maximize_window()


# 查找元素
def find_ele(driver, **kwargs):
    """
    :param driver:
    :param kwargs: text_id(登录文字), user_id, pwd_id, login_id
    :return:
    """
    if text_id in kwargs:
        ele_login = driver.find_element_by_id(kwargs[text_id])
        ele_login.click()
    user_input = driver.find_element_by_id(kwargs[user_id])
    pass_input = driver.find_element_by_id(kwargs[pwd_id])
    login_btn = driver.find_element_by_id(kwargs[login_id])
    return ele_login, user_input, pass_input, login_btn


# 发送数据
def send_values(ele_tuple, **kwargs):
    """
    :param ele_tuple: 元素字典
    :param kwargs: 账号字典
    :return:
    """
    list_key = ["uname", "pwd"]
    i = 0
    for key in list_key:
        ele_tuple[i].clear()
        ele_tuple.send_keys(kwargs[key])
        i += 1
    ele_tuple[2].click()


# 检查结果
def check_result(driver, text):
    try:
        driver.find_element_link_text(text)
        print("账号不正确")
    except Exception as result:
        print("未知错误 %s" % result)


def module_test(url):
    b = open_browser()
    open_url(b, url)
    ele_dict = {
        "text_id": "login_text",
        "user_id": "account",
        "pwd_id": "password",
        "login_id": "login"
    }
    account_dict = {
        "username": "admin",
        "pwd": "123456"
    }
    tu = find_ele(b, **ele_dict)
    send_values(tu, **account_dict)
    check_result(b, "该账号格式不正确")


# 从文件中读取数据
def get_webinfo(path):
    files = open(path, "r", encoding="UTF-8")
    dict = {}
    for file in files.readlines():
        temp = file.split("=")
        dict[temp[0].strip()] = temp[1].replace("\n", "").strip()

    return dict


if __name__ == "__main__":
    # module_test()
    # file 从文件读取数据信息（如测试100个网站的登录功能）
    #   get_webinfo(path)  # 读取网站信息
    #   get_userinfo(path)  # 读取登录信息
    print(__name__)
    get_webinfo("webinfo.txt")
