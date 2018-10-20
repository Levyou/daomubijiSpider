# -*- coding: utf-8 -*-
from scrapy import Spider, Request

from daomubiji.items import DaomubijiItem


class DaomuspiderSpider(Spider):
    name = 'daomuspider'

    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1',
                  'http://www.daomubiji.com/dao-mu-bi-ji-2',
                  'http://www.daomubiji.com/dao-mu-bi-ji-3',
                  'http://www.daomubiji.com/dao-mu-bi-ji-4',
                  'http://www.daomubiji.com/dao-mu-bi-ji-5',
                  'http://www.daomubiji.com/dao-mu-bi-ji-6',
                  'http://www.daomubiji.com/dao-mu-bi-ji-7',
                  'http://www.daomubiji.com/dao-mu-bi-ji-8',
                  'http://www.daomubiji.com/dao-mu-bi-ji-2015',
                  'http://www.daomubiji.com/sha-hai',
                  'http://www.daomubiji.com/zang-hai-hua']

    # def parse(self, response):
    #     urls = response.css('.article-content a::attr(href)').extract()
    #     for url in urls:
    #         yield Request(url=url, callback=self.parse_a)

    def parse(self, response):
        first_url = response.css('.excerpt.excerpt-c3 a::attr(href)').extract_first()
        yield Request(url=first_url, callback=self.parse_b)

    def parse_b(self, response):
        item = DaomubijiItem()
        book_name = response.css('.item.item-3 a::text').extract()
        piece = response.css('.article-content p::text').extract()
        content = "\n".join(piece)
        chapter_name = response.css('.article-header h1::text').extract_first()
        item['book_name'] = book_name
        item['content'] = content
        item['chapter_name'] = chapter_name
        yield item

        next_url = response.css('.article-nav-next a::attr(href)').extract_first()
        if next_url:
            yield Request(url=next_url, callback=self.parse_b)
        else:
            print('end')






# class DaomuspiderSpider(Spider):
#     name = 'daomuspider'
#
#     start_urls = ['http://www.daomubiji.com/qi-xing-lu-wang-01.html']
#
#     def parse(self, response):
#         item = DaomubijiItem()
#         piece = response.css('.article-content p::text').extract()
#         content = "\n".join(piece)
#         chapter_name = response.css('.article-header h1::text').extract_first()
#         item['content'] = content
#         item['chapter_name'] = chapter_name
#         yield item
#
#         next_url = response.css('.article-nav-next a::attr(href)').extract_first()
#         if next_url:
#             yield Request(url=next_url, callback=self.parse)
#         else:
#             print('end')
