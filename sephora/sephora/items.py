# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SephoraItem(scrapy.Item):
    # this is an item for each product:
    brand = scrapy.Field()
    item = scrapy.Field()
    price = scrapy.Field()
    num_reviews = scrapy.Field()
    overall_rating = scrapy.Field()
    num_loves = scrapy.Field()
    solutions_for = scrapy.Field()
    ingredient_1 = scrapy.Field()
    ingredient_2 = scrapy.Field()
    ingredient_3 = scrapy.Field()
    ingredient_4 = scrapy.Field()
    ingredient_5 = scrapy.Field()
    ingredient_6 = scrapy.Field()
    ingredient_7 = scrapy.Field()
    ingredient_8 = scrapy.Field()
    ingredient_9 = scrapy.Field()
    ingredient_10 = scrapy.Field()

class SephoraReview(scrapy.Item):
    # this is an item for each review:
    # will get this info from api
    brand = scrapy.Field()
    item = scrapy.Field()
    reviewer = scrapy.Field()
    stars = scrapy.Field()
    age = scrapy.Field()
    eye = scrapy.Field()
    hair = scrapy.Field()
    skin_tone = scrapy.Field()
    skin_type = scrapy.Field()
    skin_concerns = scrapy.Field()
    recommends = scrapy.Field() # boolean
    date = scrapy.Field()




    'https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId%3A 29383 &Sort=Helpfulness%3Adesc&Limit=100&Offset=0&Include=Products%2CComments&Stats=Reviews&passkey=rwbw526r2e7spptqd2qzbkp7&apiversion=5.4'
