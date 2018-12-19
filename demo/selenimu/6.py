# 多tab也切换
from selenium import webdriver
import time

b = webdriver.Chrome()
b.get("http://meitu.qizuang.com/list/")
b.execute_script("window.open()")
b.switch_to_window(b.window_handles[1])
b.get("https://www.baidu.com")

time.sleep(10)

# for i in range(len(b.window_handles)):
#     b.switch_to_window(b.window_handles[i])
#     b.close()
