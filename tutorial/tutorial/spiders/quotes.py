# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Selector
from tutorial.items import TutorialItem
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
   # allowed_domains = ['hao123.com/']
    start_urls = ['http://www.hao123.com/edu']

    def parse(self, response):
        body = response.body
        selector = Selector(text=body)
        tr_context = selector.css('.edu-container').xpath(".//tr")
        # 遍历结果
        i = 0
        area = ""
        school_type1 = ""
        school_type2 = ""
        school_type3 = ""
        school_type4 = ""
        for tr_sub in tr_context:
            if i == 0:
                th_text = tr_sub.xpath(".//th/text()").extract()
                print(th_text[0])
                school_type1 = th_text[1]
                school_type2 = th_text[2]
                school_type3 = th_text[3]
                school_type4 = th_text[4]
                i = i + 1
                continue
            else:
                td_text = tr_sub.xpath(".//td")
                area = td_text[0].xpath("text()").extract_first()
                item1 = list()
                item1.append(area)
                item1.append(school_type1)
                school_url1 = td_text[1].xpath(".//a/@href").extract_first()
                yield scrapy.Request(url=school_url1, callback=self.parse_next_0, meta={'message': item1})
                item2 = list()
                item2.append(area)
                item2.append(school_type2)
                school_url2 = td_text[2].xpath(".//a/@href").extract_first()
                yield scrapy.Request(url=school_url2, callback=self.parse_next_0, meta={'message': item2})
                item3 = list()
                item3.append(area)
                item3.append(school_type3)
                school_url3 = td_text[3].xpath(".//a/@href").extract_first()
                yield scrapy.Request(url=school_url3, callback=self.parse_next_0, meta={'message': item3})
                item4 = list()
                item4.append(area)
                item4.append(school_type4)
                school_url4 = td_text[4].xpath(".//a/@href").extract_first()
                yield scrapy.Request(url=school_url4, callback=self.parse_next_0, meta={'message': item4})

    def parse_next_0(self, response):
        item1 = response.meta["message"]

        body0 = response.body.decode(response.encoding)
        selector0 = Selector(text=body0)
        p = selector0.css('.t1').xpath(".//a")
        for a in p:
            item = TutorialItem()
            item["area"] = item1[0]
            item["school_type"] = item1[1]
            name = a.xpath(".//text()").extract_first()
            school_url = a.xpath(".//@href").extract_first()
            item["school_name"] = name
            item["school_url"] = school_url
            yield item









