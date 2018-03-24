# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class IspMinerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    IP = Field()
    Domain = Field()
    Country = Field()
    Region = Field()
    City = Field()
    ISP = Field()
    ASN = Field()
