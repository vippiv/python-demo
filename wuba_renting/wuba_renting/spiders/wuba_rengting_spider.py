# -*- coding: utf-8 -*-
import scrapy
from wuba_renting.items import WubaRentingItem


class WubaRengtingSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'wuba_rengting_spider'
    # 允许url
    allowed_domains = ['58.com']
    # 入口url，扔到调度器里去
    start_urls = ['https://su.58.com/chuzu/pn1/']

    # 默认的解析办法
    def parse(self, response):
        # TODO 这里的解析规则尚未经过验证
        renting_list = response.xpath("//ul[@class='listUl']//li")
        for item in renting_list:
            renting_item = WubaRentingItem()
            renting_item["type"] = item.xpath(".//div[@class='des']//h2//a/text()").extract_first()
            renting_item["layout"] = item.xpath(".//div[@class='des']//p[@class='room']/text()").extract_first()
            renting_item["area"] = item.xpath(".//div[@class='des']//p[@class='room']/text()").extract_first()
            renting_item["price"] = item.xpath(".//div[@class='listliright']//div[@class='money']//b[@class='']/text()").extract_first()
            yield renting_item  # 将数据yield到 pipeline里，一定不能少这一步

        next_link = response.xpath("//a[@class='next']/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request(url=next_link, callback=self.parse)
