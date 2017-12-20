# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem

class QiubaispiderSpider(scrapy.Spider):
    name = 'qiubaispider'
    allowed_domains = ['qiushibaike.com']
    start_urls = []
    for i in range(1, 4):
        start_urls.append('https://www.qiushibaike.com/8hr/page/' + str(i) + '/')

    def parse(self, response):
        items = []
        divList = response.xpath('//div[@id="content-left"]/div')
        for div in divList:
            item = QiubaiItem()
            if len(div.xpath('div[@class="author clearfix"]/a').extract()) > 0:
                item['author'] = div.xpath('div[@class="author clearfix"]/a[2]/h2/text()').extract()[0].replace('\n', '')
                item['link'] = 'https://www.qiushibaike.com' + div.xpath('div[@class="author clearfix"]/a[2]/@href').extract()[0]
            else:
                item['author'] = div.xpath('div[@class="author clearfix"]/span[2]/h2/text()').extract()[0]
                item['link'] = ''
            article = div.xpath('a[@class="contentHerf"]/div/span[1]').xpath('string(.)').extract()[0].replace('\n', '')
            if len(div.xpath('div[@class="thumb"]').extract()) > 0:
                img = div.xpath('div[@class="thumb"]/a/img/@src').extract()[0].lstrip('/')
                item['content'] = article + '\n图片链接:' + img
            else:
                item['content'] = article
            item['supportNum'] = div.xpath('div[@class="stats"]/span[@class="stats-vote"]/i/text()').extract()[0]
            item['commentNum'] = div.xpath('div[@class="stats"]/span[@class="stats-comments"]/a/i/text()').extract()[0]
            items.append(item)
        return items
