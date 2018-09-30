# -*- coding: utf-8 -*-
import scrapy


class QuoteswithtagsSpider(scrapy.Spider):
    name = 'quoteswithtags'
    # allowed_domains = ['http://quotes.toscrape.com/']
    # start_urls = ['http://http://quotes.toscrape.com//']

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        '''scrapy crawl 爬虫名字  -a tag=humor 
            接受参数tag值'''
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)