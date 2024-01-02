import scrapy


class EcomscrapSpider(scrapy.Spider):
    name = "ecomscrap"
    allowed_domains = ["formation-data.com"]
    start_urls = ["http://formation-data.com/?product_cat=women"]

    def parse(self, response):
        parent_container = response.xpath("//div[@id='primary']/ul/li")
        
        for children in parent_container : 
            link = children.xpath('.//div[1]/a/@href').get()
            
            yield response.follow(link, callback=self.new_fun)
            
        
        next_btn = response.xpath('//*[@id="primary"]/nav/ul/li[4]/a/@href').get()
        if next_btn : 
            new_url = response.urljoin(next_btn)
            yield scrapy.Request(url=new_url , callback=self.parse)
            
            
    def new_fun(self , response) :
        
        yield {
            'title' : response.xpath("//div[@id='primary']/div/div[@class='summary entry-summary']/h1/text()").get(),
            'price' : float(response.xpath("//div[@class='summary entry-summary']/p[@class='price']/span[@class='woocommerce-Price-amount amount']/bdi/text()").get()),
            'SKU' : response.xpath("//div[@class='product_meta']/span[@class='sku_wrapper']/span[@class='sku']/text()").get(),
            'Categories' : response.xpath("//div[@class='product_meta']/span[@class='posted_in']/a/text()").getall(),
            'Tags' : response.xpath("//div[@class='product_meta']/span[@class='tagged_as']/a/text()").getall(),
        }