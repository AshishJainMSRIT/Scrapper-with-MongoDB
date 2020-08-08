import scrapy
from ..items import ScrappermongoItem

class WebsiteSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'https://news.ycombinator.com/'
    ]


    def parse(self, response):

        items = ScrappermongoItem()

        all_title = response.css('.athing')
        all_subtext = response.css('.subtext')

        for i in range(0,len(all_title)-1):
            Title = all_title.css('.storylink::text')[i].extract()
            Url = all_title.css('.storylink::attr(href)')[i].extract()
            Votes = all_subtext.css('.score::text')[i].extract() if all_subtext.css('.score::text')[i] != None else ()

            items['Title'] = Title
            items['Url'] = Url
            items['Votes'] = Votes

            yield items
