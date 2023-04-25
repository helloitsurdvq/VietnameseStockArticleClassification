import scrapy
import time
from ..items import cafeFItem
# from scrapy_splash import SplashRequest 
# from scrapy_selenium import SeleniumRequest
# from selenium import webdriver

class CafefSpider(scrapy.Spider):
    name = "cafeF"
    start_urls = ["https://cafef.vn/thi-truong-chung-khoan.chn"]

    def parse(self, response):
        all_div_articles = response.css('div.tlitem.box-category-item') #more update asap
        for article in all_div_articles:
            link = article.css('a::attr(href)').extract_first() #more updated asap
            yield scrapy.Request(response.urljoin(link), callback=self.parse_article)
    
    def parse_article(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        
        item = cafeFItem()
        
        title = response.css('h1.title::text').extract_first()
        # title = [c.strip() for c in title if c.strip()]
        content = response.css('p::text').extract()
        content = [c.strip() for c in content if c.strip()]
        item['title'] = title
        item['content'] = content
        
        if content:
            yield item