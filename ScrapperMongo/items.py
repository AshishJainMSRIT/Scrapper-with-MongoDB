# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Field, Item


class ScrappermongoItem(Item):
    # define the fields for your item here like:
    Title = Field()
    Url = Field()
    Votes = Field()


