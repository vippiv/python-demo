# 打开百度，搜索关键字并进入相关网站
from selenium import webdriver

b = webdriver.Chrome()
b.get("https://www.baidu.com")

input = b.find_element_by_id("kw")
btn = b.find_element_by_id("su")
input.clear()
input.send_keys("齐装网")
btn.click()
target = b.find_element_by_partial_link_text("齐装网")
target.click()
