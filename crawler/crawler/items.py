# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VnexpresstrainItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

class VnEconomyItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    
class cafeFItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    
class enternewsItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
