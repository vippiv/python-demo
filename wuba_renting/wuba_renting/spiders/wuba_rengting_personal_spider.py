# -*- coding: utf-8 -*-
import scrapy


class WubaRengtingPersonalSpiderSpider(scrapy.Spider):
    name = 'wuba_rengting_personal_spider'
    allowed_domains = ['58.com']
    start_urls = ['http://58.com/']

    def parse(self, response):
        pass
