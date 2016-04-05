# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YhdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    price=scrapy.Field()
    link=scrapy.Field()
    category=scrapy.Field()
    product_id=scrapy.Field()
    img_link=scrapy.Field()
    pass


class PriceItem(scrapy.Item):
      price_url=scrapy.Field()
      price_info=scrapy.Field()
      pass
