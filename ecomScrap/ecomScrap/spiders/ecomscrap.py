import scrapy


class EcomscrapSpider(scrapy.Spider):
    name = "ecomscrap"
    allowed_domains = ["formation-data.com"]
    start_urls = ["http://formation-data.com/"]

    def parse(self, response):
        pass
