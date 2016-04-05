from scrapy import Spider
from yhd.items import YhdItem
from yhd.items import PriceItem
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor as le
from scrapy.http import Request
import requests
import json
class YHDSpider(CrawlSpider):
      name='yhd'
      allowed_domains=['yhd.com']
      start_urls=[
          'http://www.yhd.com/marketing/allproduct.html'
      ]

      rules=[
        Rule(le(allow=('http://www.yhd.com/marketing/allproduct.html')),follow=True),
        Rule(le(allow=('^http://list.yhd.com/c.*//$')),follow=True),
        Rule(le(allow=('^http://list.yhd.com/c.*/b/a\d*-s1-v4-p\d+-price-d0-f0d-m1-rt0-pid-mid0-k/$')),follow=True),
        Rule(le(allow=('^http://item.yhd.com/item/\d+$')),callback='parse_product')
      ]
      
      def parse_product(self,response):
          item=YhdItem()
          item['title']=response.xpath('//h1[@id="productMainName"]/text()').extract()
          price_str=response.xpath('//a[@class="ico_sina"]/@href').extract()[0]
          item['price']=price_str
          item['link']=response.url
          pmld = response.url.split('/')[-1]
          price_url='http://gps.yhd.com/restful/detail?mcsite=1&provinceId=12&pmId='+pmld
          item['category']=response.xpath('//div[@class="crumb clearfix"]/a[contains(@onclick,"detail_BreadcrumbNav_cat")]/text()').extract()
          item['product_id']=response.xpath('//p[@id="pro_code"]/text()').extract()
          item['img_link']=response.xpath('//img[@id="J_prodImg"]/@src').extract()[0]
          request = Request(price_url,callback=self.parse_price)
          request.meta['item']=item
          yield request
      
      def parse_price(self,response):
          item = response.meta['item']
          item['price']=response.body
          return item
          

      def _process_request(self,request):
          return request     
