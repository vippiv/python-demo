# 模拟鼠标悬浮
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get("http://www.qizuang.com")
ele = browser.find_element_by_link_text("装修效果图")
ActionChains(browser).move_to_element(ele).perform()
sub_ele = browser.find_element_by_link_text("家装效果")
sub_ele.click()

time.sleep(3)
browser.close()
