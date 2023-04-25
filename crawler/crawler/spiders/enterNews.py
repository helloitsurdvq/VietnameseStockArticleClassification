import scrapy
import time
from ..items import enternewsItem

lua_script = """
        function main(splash)
            local num_scrolls = 100
            local scroll_delay = 30
            local num_clicks = 4
            local click_delay = 0.5
            local scroll_to = splash:jsfunc("window.scrollTo")
            local get_body_height = splash:jsfunc(
                "function() {return document.body.scrollHeight;}"
            )
            local url = splash.args.url
            assert(splash:go(url))
            splash:wait(splash.args.wait)
            for _ = 1, num_scrolls do
                scroll_to(0, get_body_height())
                splash:wait(scroll_delay)            
            end        
            return {
                html = splash:html(),
                url = splash:url()
                }    
        end
"""

class EnternewsSpider(scrapy.Spider):
    name = "enterNews"
    start_urls = ["https://diendandoanhnghiep.vn/dau-tu-chung-khoan-c124"]
    page_num = 2
    
    # for i in range(num_scrolls):
    #         driver.execute_script("window.scrollBy(0,9000)","")
    #         time.sleep(0.5)   
    
    def parse(self, response):
        all_articles = response.css('li.item.blv2-item')
        for article in all_articles:
            link = article.css('a::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(link), callback=self.parse_article)
            
        nextPage = 'https://diendandoanhnghiep.vn/dau-tu-chung-khoan-c124/page-' + str(EnternewsSpider.page_num) + '.html'
        if EnternewsSpider.page_num <= 151:
            EnternewsSpider.page_num += 1
            yield scrapy.Request(nextPage, callback=self.parse)
        
    def parse_article(self, response):
        title = response.css('h1.post-title.main-title::text').extract_first()
        content = response.css('div.post-content p::text').extract()
        if title and content:
            yield{
                'title': title,
                'content': content
            }