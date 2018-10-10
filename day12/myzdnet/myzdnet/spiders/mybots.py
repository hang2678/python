# -*- coding: utf-8 -*-
import scrapy


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['www.zdnet.co.kr/news/news_keyword.asp?keyword=%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8&lo=z26']
    start_urls = ['http://www.zdnet.co.kr/news/news_keyword.asp?keyword=%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8&lo=z26/']

    def parse(self, response):
        pass
