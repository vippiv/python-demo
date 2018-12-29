# -*- coding: utf-8 -*-
import scrapy
from my_spider.items import MySpiderItem


class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['su.lianjia.com']
    start_urls = ['https://su.lianjia.com/ershoufang/']

    def parse(self, response):
        print(response)
        lis = response.css(".LOGCLICKDATA")
        for item in lis:
            MySpiderItem["id"] = item.xpath('//div[@class="title"]//a[data-housecode]::text').extract_first()
            MySpiderItem["title"] = item.xpath('//div[@class="title"]').extract_first()
            MySpiderItem["unit_price"] = item.xpath('//div[@class="unitPrice//span"]').extract_first()
            MySpiderItem["total_price"] = item.xpath('//div[@class="totalPrice//span"]').extract_first()
            MySpiderItem["desc"] = item.xpath('//div[@class="houseInfo"]').extract_first()
            MySpiderItem["acreage"] = MySpiderItem["desc"].split("|")[1]

        next_link = response.css(".page-box a:last-child::attr(href)").exact_first()
        url = response.urljoin(next_link)
        yield scrapy.Request(url=url, callback=self.parse)
