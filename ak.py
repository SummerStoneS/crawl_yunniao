# -*- coding: utf-8 -*-
import scrapy


class AkSpider(scrapy.Spider):
    name = "ak"
    allowed_domains = ["ak"]
    start_urls = ['http://ak/']

    def parse(self, response):
        pass
