import scrapy


class TodaydealsSpider(scrapy.Spider):
    name = 'todayDeals'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/gp/goldbox']

    def parse(self, response):
        results = response.xpath("//a[@class='a-link-normal  a-color-base a-text-normal']/div/text()").getall()
        for result in results:
            yield{
                #'title' : result.xpath("//div/te").get()
                'title' : results
            }
        
