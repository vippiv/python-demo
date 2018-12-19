from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.set_window_position(1000, 0)
browser.get("https://www.baidu.com")
browser.maximize_window()
input = browser.find_element_by_id("kw")
btn = browser.find_element_by_id('su')
input.send_keys("水弹")
btn.click()
input.clear()
print(browser.title)
print(browser.current_url)


time.sleep(3)
browser.close()
