# 抓取指定页面内容并解析出需要的内容（抓取异步数据）
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html  requests模块官方文档
import requests
from requests.exceptions import RequestException
from urllib import request
from lxml import etree  # lxml模块不是自带的，需要安装
import json
import time


def get_ajax_data(url, handler=''):
    """
    抓取异步加载的数据（图片等）
    :param url: 页面地址
    :param handler: 处理函数
    :return:
    """
    data = requests.get(url)
    print(data.text)
    # print(data.content)
    # for item in data:
    #     print(item, end="\n")


get_ajax_data(r'http://huaban.com/favorite/home/')
