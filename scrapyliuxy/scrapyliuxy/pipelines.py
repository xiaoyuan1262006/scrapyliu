# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import numpy as np
import pymongo


class ScrapyliuxyPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    collection_name = 'scrapy_items'

    def __init__(self):
        self.mongo_uri = '127.0.0.1'
        self.mongo_db = 'scrapyliu'
        self.port = 27017

    # @classmethod
    # def from_clawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DB')
    #     )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_uri, port=self.port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # print('-----', json.dumps(item._value()))
        # item.
        # a = item.__str__()
        item_dict = dict(item)
        print('item_dict=', item_dict)
        # jsondateye = json.dumps(item_dict)
        # print('jsondateye=', jsondateye)
        self.db[self.collection_name].insert_one(item_dict).inserted_id
        return item


