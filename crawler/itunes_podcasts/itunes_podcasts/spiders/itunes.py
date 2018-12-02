# -*- coding: utf-8 -*-
import scrapy


class ItunesSpider(scrapy.Spider):
    name = 'itunes'
    allowed_domains = ['https://itunes.apple.com/us/genre/podcasts/id26?mt=2']
    start_urls = ['http://https://itunes.apple.com/us/genre/podcasts/id26?mt=2/']

    def parse(self, response):
        pass
