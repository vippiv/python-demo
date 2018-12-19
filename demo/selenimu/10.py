# 封装（基于登录功能）
from selenium import webdriver
import time
import xlrd
import xlsxwriter


# 测试日志处理类
class Logininfo:
    def __init__(self, path="", mode="w"):
        file_name = path + time.strftime('%Y-%m-%d', time.gmtime())
        self.log = open(path + file_name + ".txt", mode, encoding="UTF-8")

    def log_write(self, msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()


# 读取excel数据类
class XlUserinfo:
    def __init__(self, path=""):
        self.xl = xlrd.open_workbook(path)

    # Excel中读取的数据都会转成浮点型容易造成错误，必须转成字符串
    def float_to_str(self, val):
        if isinstance(val, float):
            val = str(int(val))
        return val

    def get_sheet_info(self):
        listkey = ["username", "pwd"]
        info_list = []
        for row in range(1, len(self.sheet.nrows)):
            info = [self.float_to_str(val) for val in self.sheet.row_values(row)]
            temp = zip(listkey, info)
            info_list.append(dict(temp))
        return info_list

    def get_sheetinfo_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheetinfo_by_index(self, index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()

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


# excel操作函数
def get_webinfo_excel(path):
    xl = xlrd.open_workbook(path)
    table = xl.sheets()[0]  # 获取第一张工作表
    # table = xl.sheet_by_index(0)  # 根据索引获得工作表
    # table = xl.sheet_by_name("一月")  # 根据名称获得工作表
    row = table.row_values(0)  # 获取第一行
    col = table.col_values(0)  # 获取第一列
    print(table.nrows)  # 行数
    print(table.ncols)  # 列数
    print(table.cell(0, 0).value)


def write_excel():
    xl = xlsxwriter.Workbook("ret.xls")  # 创建excel
    table = xl.add_worksheet("测试报告")  # 创建sheet
    table.write_string(0, 0, "first")/("A1", "first")  # 写单元格，两种写法，第一种0,0表示第一行第一列，第二种表示A1单元格,=，最后一个参数表示要写入的值
    table.set_column("C:E", 15)  # 设置单元格宽度
    xl.close()  # 关闭excel



if __name__ == "__main__":
    # module_test()
    # file 从文件读取数据信息（如测试100个网站的登录功能）
    #   get_webinfo(path)  # 读取网站信息
    #   get_userinfo(path)  # 读取登录信息
    print(__name__)
    get_webinfo("webinfo.txt")
    log = Logininfo()
    log.log_write("测试报告")
    log.log_close()



