# 设置超时等待
from selenium import webdriver
from selenium.webdriver.common.ui import WebDriverWait


def get_ele_times(driver, times, fn):
    return WebDriverWait(driver, times).until(fn)


b = webdriver.Chrome()
b.get("http://www.qizuang.com")
# b.implicitly_wait(5)  # 设置查询时间，单位秒
ele_login = get_ele_times(b, 10, lambda x: x.find_element_by_id("login"))

ele = b.find_element_by_id("kw")  # 如果找到直接返回，如果找不到则查够5秒
