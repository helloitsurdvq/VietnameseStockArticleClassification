import scrapy
# from scrapy_splash import SplashRequest 
# from scrapy_selenium import SeleniumRequest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
from ..items import VnEconomyItem

class VnecoSpider(scrapy.Spider):
    name = "vnEco"
    start_urls = ['https://vneconomy.vn/chung-khoan.htm']
    page_num = 2
    # title_script = """
#         function main(splash)
#             local num_scrolls = 20
#             local scroll_delay = 0.5
#             local num_clicks = 4
#             local click_delay = 1
#             local scroll_to = splash:jsfunc("window.scrollTo")
#             local get_body_height = splash:jsfunc(
#                 "function() {return document.body.scrollHeight;}"
#             )
#             local url = splash.args.url
#             assert(splash:go(url))
#             splash:wait(splash.args.wait)        
#             end        
#             return {
#                 html = splash:html(),
#                 url = splash:url()
#                 }             
#         end

    def parse(self, response):
        all_div_articles = response.css('article.story.story--featured.story--timeline')
        for article in all_div_articles:
            link = article.css('a::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(link), callback=self.parse_article)
        
        next_page = 'https://vneconomy.vn/chung-khoan.htm?trang=' + str(VnecoSpider.page_num)
        if VnecoSpider.page_num <= 301: # 300 pages crawled
            VnecoSpider.page_num += 1
            # next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        # yield SplashRequest(
        #     url=url,
        #     callback=self.parse,
        #     endpoint='execute',
        #     args={'lua_source': lua_script, 'wait': 24}
        # )
        # yield SeleniumRequest(
        #     url=url,
        #     callback=self.parse,
        #     wait_time=3,
        #     script=sele_script, 
        # )

    def parse_article(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        
        item = VnEconomyItem()
        title = response.css('h1.detail__title::text').extract_first()
        content = response.css('div.detail__content p::text').extract()
        
        item['title'] = title
        item['content'] = content
        if title and content:
            yield item