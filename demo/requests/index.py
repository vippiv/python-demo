import requests
import os

r = requests.get("http://docs.python-requests.org/zh_CN/latest/user/quickstart.html")

file = open("text.html", "w", encoding='utf-8')

file.write(r.text)
file.close()
