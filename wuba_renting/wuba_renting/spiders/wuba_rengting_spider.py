# -*- coding: utf-8 -*-
import scrapy


class WubaRengtingSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'wuba_rengting_spider'
    # 允许url
    allowed_domains = ['58.com']
    # 入口url，扔到调度器里去
    start_urls = ['https://su.58.com/chuzu/pn1/']

    def parse(self, response):
        print(response.text)
