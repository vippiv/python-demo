# 键盘事件
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
ele = browser.find_element_by_id("kw")
ele.send_keys("python1")
time.sleep(1)
ele.clear()
ele.send_keys("锦明8")
time.sleep(1)
ele.send_keys(Keys.BACKSPACE)  # 逐个删除字符
time.sleep(1)
ele.send_keys(Keys.CONTROL, 'a')  # 全选
time.sleep(1)
ele.send_keys(Keys.CONTROL, 'x')  # 复制
time.sleep(1)
ele.send_keys(Keys.CONTROL, 'v')  # 粘贴


time.sleep(3)
browser.close()
