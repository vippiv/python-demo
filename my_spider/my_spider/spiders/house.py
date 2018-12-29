# -*- coding: utf-8 -*-
import scrapy


class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['su.lianjia.com']
    start_urls = ['https://su.lianjia.com/ershoufang/']

    def parse(self, response):
        pass
