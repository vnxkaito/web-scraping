import scrapy

class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']
 
    start_urls = [
        'https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html'
    ]
 
    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']"):
            yield{
                'title': product.xpath(".//").get(),
                'url': product.xpath(".//").get(),
                'discounted_price' : product.xpath(".//").get(),
                'original_price' : product.xpath(".//").get()
            }

        pass