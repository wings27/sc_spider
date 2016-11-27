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
                url = link.xpath('@href').extract_first()
                if url is not None:
                    next_url = response.urljoin(url)
                    yield scrapy.Request(next_url, callback=SongSanSpider.parse_songci)

    @staticmethod
    def parse_songci(response):
        item = SongCiItem()
        item['url'] = response.url
        item['title'] = response.css('div.son1>h1::text').extract_first()
        son2 = response.css('div.son2>p')
        for p in son2:
            for name, field in {'朝代': 'dynasty', '作者': 'author'}.items():
                if name in p.css('::text').extract_first():
                    item[field] = p.css('::text').extract()[1]
        item['content'] = ''.join(response.css('div.son2::text').extract()).strip()
        yield item
