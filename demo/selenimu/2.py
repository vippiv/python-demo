from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.set_window_position(1000, 0)
browser.get("https://www.sina.com")
# text_link = browser.find_element_by_link_text("军事")
# text_link = browser.find_element_by_partial_link_text("女")  # 通过部分文字来查找
# text_link = browser.find_element_by_css_selector('a[title="军事"]')  # 通过css来查找
text_link = browser.find_element_by_css_selector('a[title="军事"]')  # 通过xpath来查找

text_link.click()
print(browser.title)
print(browser.current_url)


time.sleep(3)
browser.close()
