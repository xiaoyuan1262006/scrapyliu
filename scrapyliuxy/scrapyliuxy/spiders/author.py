# -*- coding: utf-8 -*-
import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    # allowed_domains = ['www.snotr.com']
    start_urls = ['http://quotes.toscrape.com/', ]

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse)

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            '''第一种实现'''
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page,callback=self.parse)
            '''第二种实现'''
            yield response.follow(next_page, callback=self.parse)
        '''第三种'''  # for a in response.css('li.next a'):  #     yield  response.follow(next_page,callback=self.parse)

    def parse_author(self,response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
