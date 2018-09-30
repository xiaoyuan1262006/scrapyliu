# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.loader import ItemLoader


class QuotesItem(scrapy.Item):
    # def __str__(self):
    #     return '['+'text:'+self.text+','+'author:'+self.text+','+'tags:'+self.tags+']'
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class ExampleSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/
    # def start_requests(self):
    #     urls = ['http://quotes.toscrape.com/page/1/',
    #             'http://quotes.toscrape.com/page/2/',
    #             ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    start_urls = ['http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
                  ]

    def parse(self, response):
        # page = response.url.split("/")[-2]  #         # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        # print('===============================')
        # text = response.xpath("//div[@class='quote']//span[1]/text()").extract_first(default='not-found')
        # author = response.xpath("//div[@class='quote']//small[1]/text()").extract_first(default='not-found')
        # tags = response.xpath("//div[@class='quote']//div[@class='tags']//a[@class='tag']/text()").extract()
        # print('xx==', text)
        # ll = QuotesItem(text=text, author=author, tags=tags)
        # print('Quotes=', ll.items())
        #ItemLoader(item=, response=response)
        # ll.add_css('text', quote.css('span.text::text').extract_first())
        # ll.add_css('author', quote.css('small.author::text').extract_first())
        # ll.add_css('tags', quote.css('div.tags a.tag::text').extract_first())
        # ll.load_item()

        # print('111111', response.body_as_unicode())
        # print('text===', ll['text'])
        # la  = ItemLoader(item=QuotesItem, response=response)
        # la.add_xpath('',)
        # sitedate = json.loads(response.body_as_unicode())
        # jsonresponse = json.loads(response.body_as_unicode())



        for quote in response.css('div.quote'):
            # for i in range(1, 5):
            # text = quote.css('span.text::text').extract_first()#response.xpath("//span[1]/text()").extract_first(default='not-found')
            author = quote.css('small.author::text').extract_first()#response.xpath("//small[1]/text()").extract_first(default='not-found')
            tags = quote.css('div.tags a.tag::text').extract()#response.xpath("//div[@class='tags']/a[@class='tag']/text()").extract()
            # print('xx==', text)
            ll = QuotesItem()
            # ll['text'] = text
            ll['author'] = author
            ll['tags'] = tags

            # print('Quotes=', ll.items())
            yield ll
            #     {
            #     'text': quote.css('span.text::text').extract_first(),
            #     'author': quote.css('small.author::text').extract_first(),
            #     'tags': quote.css('div.tags a.tag::text').extract(),
            # }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            '''第一种实现'''
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page,callback=self.parse)
            '''第二种实现'''
            yield response.follow(next_page,callback=self.parse)
        '''第三种'''
        # for a in response.css('li.next a'):
        #     yield  response.follow(next_page,callback=self.parse)
