# /XXX 选取根节点XXX
# /XXX/yyy 根据绝对路径选择元素
# //XXX 整个文档扫描，找到所有XXX元素
# //XXX/yyy 所有父元素为XXX的yyy元素
# . 选取当前节点的父元素节点
# .. 选取父元素地址
# //XXX[@id] 选取所有XXX元素中有id属性的元素
# //XXX[@id=yyy] 选取所有XXX元素id属性为yyy的元素

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.set_window_position(1000, 0)
browser.get("https://www.sina.com")
text_link = browser.find_element_by_xpath("//form//input")  # 通过xpath来查找
text_link.send_keys("美女")
text_link.send_keys("美女")
# print(text_link.text)

print(browser.title)
print(browser.current_url)


time.sleep(3)
browser.close()
