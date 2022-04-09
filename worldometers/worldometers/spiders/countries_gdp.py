import scrapy
import logging

class CountriesGdpSpider(scrapy.Spider):
    name = 'countries_gdp'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath('//tr')
        for country in countries:
            name = country.xpath('.//td[1]/a/text()').get()
            gdp = country.xpath('.//td[2]/text()').get()
            yield{
            'name' : name,
            'gdp' : gdp
            }
