from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get("https://www.taobao.com")
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get("https://www.baidu.com")
browser.close()




# a.add_cookie({"name": 'zwl', "value": "haha"})
# a.get_cookie("name")
# a.current_url
# a.application_cache  # 不清楚用途
# a.back()
# a.capabilities  # 显示实例属性合集
# a.close()
# a.command_executor  # 实例属性，不清楚怎么用
# a.create_options()  # 不清楚用途
# a.create_web_element()  # 创建一个web元素，不清楚用途
# a.current_window_handle
# a.fullscreen_window()
# a.log_types  # log类型，可用于传入get_log()方法
# a.get_log()  # 接受log_types参数，如browser，driver
# a.get_network_conditions()
# a.get_screenshot_as_base64()
# a.get_screenshot_as_file("D:\\python\\screen.png")
# a.get_window_position("current")
# a.get_window_rect()
# a.get_window_size()
# a.implicitly_wait()  # 不清楚用途
# a.launch_app()  # 不清楚用途
# a.maximize_window()  # 最大化
# a.minimize_window()  # 最小化
# a.page_source

