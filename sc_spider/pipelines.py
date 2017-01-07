# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


class MongoDBPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB', 'songci'),
        )

    def open_spider(self, spider):
        spider.logger.info('Opened spider: %s.', spider)
        spider.logger.info('Using mongo address: %s', self.client.address)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        self.save_item(collection, item)
        return item

    @staticmethod
    def save_item(collection, item):
        try:
            collection.update({'url': item['url']}, dict(item), upsert=True)
        except ServerSelectionTimeoutError as e:
            logging.error('Fail to connect to mongodb. %s', e)
