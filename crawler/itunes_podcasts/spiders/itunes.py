# -*- coding: utf-8 -*-
import scrapy


class ItunesSpider(scrapy.Spider):
    name = 'itunes'
    allowed_domains = ['itunes.apple.com']
    start_urls = ['https://itunes.apple.com/us/genre/podcasts-arts/id1301?mt=2']

    def parse(self, response):
        print(response.text)
