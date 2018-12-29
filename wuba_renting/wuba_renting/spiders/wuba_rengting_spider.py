# -*- coding: utf-8 -*-
import scrapy


class WubaRengtingSpiderSpider(scrapy.Spider):
    name = 'wuba_rengting_spider'
    allowed_domains = ['58.com']
    start_urls = ['http://58.com/']

    def parse(self, response):
        pass
