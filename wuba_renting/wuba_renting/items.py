# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WubaRentingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # id = scrapy.Field()  # 租房条目id
    type = scrapy.Field()  # 租房类型：整租，单间
    layout = scrapy.Field()  # 房型
    area = scrapy.Field()  # 面积
    price = scrapy.Field()  # 单价
