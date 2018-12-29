# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # 房产id
    title = scrapy.Field()  # 房产名称
    # address = scrapy.Field()  # 房产地址
    unit_price = scrapy.Field()  # 房产单价
    total_price = scrapy.Field()  # 房产总价
    acreage = scrapy.Field()  # 房产面积
    desc = scrapy.Field()  # 房产简介
