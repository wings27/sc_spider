# -*- coding: utf-8 -*-
import os

import scrapy

from sc_spider.items import SongCiItem
from sc_spider.spiders.spider_utils import page_name_from_url


class SongSanSpider(scrapy.Spider):
    name = "songsan"
    allowed_domains = ["gushiwen.org"]
    start_urls = (
        'http://www.gushiwen.org/gushi/songsan.aspx',
    )

    STORAGE_PATH = './out/'

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        if not os.path.exists(self.STORAGE_PATH):
            os.makedirs(self.STORAGE_PATH)

    def parse(self, response):
        filename = self.STORAGE_PATH + page_name_from_url(response.url)
        with open(filename, 'wb') as f:
            self.logger.debug('saving page: %s', filename)
            f.write(response.body)
            self.logger.info('page save: %s', filename)

        cont2s = response.xpath('//div[@class="guwencont2"]')
        for cont2 in cont2s:
            links = cont2.xpath('a')
            for link in links:
                yield self._parse_item(link)

    @staticmethod
    def _parse_item(link):
        item = SongCiItem()
        item['url'] = link.xpath('@href').extract_first()
        title_author = link.xpath('text()').re('(.+)\((.+)\)')
        if title_author:
            item['title'] = title_author[0]
            item['author'] = title_author[1]
        else:
            item['title'] = link.xpath('text()').extract_first()

        return item
