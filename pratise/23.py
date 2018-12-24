# 抓取指定页面内容并解析出需要的内容
from urllib import request
from lxml import etree  # lxml模块不是自带的，需要安装


def get_html(url, handler):
    """
    获取指定url页面的内容
    :param url: 页面地址
    :param handler: 处理函数
    :return:
    """
    try:
        headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Connection': 'keep-alive'
        }
        req = request.Request(url, headers=headers)
        html = request.urlopen(req).read()
        # 处理编码
        html = html.decode('utf-8')
        handler(html)
    except Exception as result:
        print(result)


def parse_detail_html(html_str):
    """
    解析html（解析的是详情页数据）
    从html中解析出需要的文本
    :param html_str: html字符串
    :return:
    """
    selector = etree.HTML(html_str)
    title = selector.xpath('//h1[@class="main-title"]/text()')[0].replace('\r\n', '')
    desc = selector.xpath('//div[@class="new_style_article"]/p')[0].xpath('string(.)').replace('\r\n', '')
    content = selector.xpath('//div[@class="article"]')[0].xpath('string(.)').replace('\r\n', '')
    imgs = selector.xpath('//div[@class="article"]//img/@src')  # 这种方法只能抓取到同步加载的图片
    print(title)
    print(desc)
    print(content)
    print(imgs)


def parse_list_html(html_str):
    """
    解析html（解析的是列表页数据）
    从html中解析出需要的文本
    :param html_str:
    :return:
    """
    selector = etree.HTML(html_str)
    data = selector.xpath('//ul[@class="list_14"]//li')
    for item in data:
        print(item[0].xpath('string(.)'))


# get_html(r'https://finance.sina.com.cn/chanjing/gsnews/2018-12-24/doc-ihmutuee2060813.shtml', parse_detail_html)

# get_html(r'https://news.sina.com.cn/', parse_list_html)
