# 抓取指定页面内容并解析出需要的内容（抓取异步数据）
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html  requests模块官方文档
import requests
import re
import os
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
    # print(data.text)  # 返回的是Unicode型的数据，可能乱码
    # print(data.content)  # 返回的是bytes型的数据
    htmlPage = data.text
    prog = re.compile(r'app\.page\["pins"\].*')
    appPins = prog.findall(htmlPage)
    true = "true"
    null = None
    result = eval(appPins[0][19:-1])
    images = []
    if not os.path.exists('imgs'):
        os.mkdir("imgs")
    for i in result:
        info = {}
        info['id'] = str(i['pin_id'])
        info['url'] = "http://img.hb.aicdn.com/" + i["file"]["key"] + "_fw658"
        info['type'] = i["file"]["type"][6:]
        images.append(info)
    for image in images:
        req = requests.get(image["url"])
        imageName = image["id"] + "." + image["type"]
        with open("imgs/" + imageName, 'wb') as fp:
            fp.write(req.content)


def make_ajax_url(No):
    """ 返回ajax请求的url """
    return "http://huaban.com/favorite/beauty/?i5p998kw&max=" + No + "&limit=20&wfl=1"


get_ajax_data(r'http://huaban.com/favorite/beauty/')
