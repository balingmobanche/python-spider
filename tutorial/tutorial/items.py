# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area = scrapy.Field()
    # 普通本科院校(912所)
    # school1 = scrapy.Field()
    # 高职院校(1401所)
    # school2 = scrapy.Field()
    # 独立学院(289所)
    # school3 = scrapy.Field()
    # 成人高等学校（296所）
    # school4 = scrapy.Field()
    school_type = scrapy.Field()
    school_name = scrapy.Field()
    school_url = scrapy.Field()
