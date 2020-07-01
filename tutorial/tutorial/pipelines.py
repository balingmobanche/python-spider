# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        #这里处理数据存储问题
        print(item["area"], item["school_type"], item["school_name"], item["school_url"], end=',')
        print()
        return item
