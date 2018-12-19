# 切换到alert弹窗 switch_to_alert()，返回alert对象
from selenium import webdriver
b = webdriver.Chrome()
b.get("http://alert-demo.com")
ele_alert = b.find_element_by_id("alert")
ele_alert.click()
alert = b.switch_to_alert()  # 获取alert对话框
print(alert.text)
alert.accept()  # 接受，相当于点击确定
alert.dismiss()  # 取消，相当于点击取消
