# Determine novel/trending skincare ingredients
# sephora web scraping Spider

from scrapy import Spider, Request
from sephora.items import SephoraItem, SephoraReview
import re
import json
import time


class SephoraSpider(Spider):
    # inherets from scrapy Spider class
    name = 'sephora_spider'
    allowed_urls = ["https://www.sephora.com", "https://api.bazaarvoice.com"]
    # get best-selling skin care
    start_urls = ["https://www.sephora.com/best-selling-skin-care"]

    # collect all the links to the products
    def parse_skincare(self, response):
        # time.sleep(0.5)
        # this scapes all the products on the best selling skin care page as a json
        raw_info = response.xpath('//div[@id="main"]/div[1]/span').extract()[0].replace(r"&quot;", "\"")
        #data = re.findall('"sku_list":\[(.*?)\]', raw_info)[0]
        raw_info = raw_info.replace('" class="u-hide"></span>', ']')
        raw_info = raw_info.replace('<span seph-json-to-js="skugrid" data-json="', '[')
        data = json.loads(raw_info)
        print("Gathered Data")
        print("="*50)
        print(data)
