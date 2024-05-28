import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from osu_crawler.items import OsuCrawlerItem
from utility.functions import *

# Write a utility.py

class OsuCountrySpider(scrapy.Spider):
    name = "osu_country"
    allowed_domains = ["osu.ppy.sh"]
    start_urls = ["https://osu.ppy.sh/rankings/osu/country"]

    def parse(self, response):
        sel = Selector(response)
        item = OsuCrawlerItem()

        item['ranking'] = replace_space_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[1]/text()').extract())
        item['country_name'] = replace_space_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[2]/div/a/span[2]/text()').extract())
        item['active_users'] = replace_space_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[3]/text()').extract())
        item['play_count'] = replace_space_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[4]/span/text() ').extract())
        item['ranked_score'] = replace_space_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[5]/span/text() ').extract())
        item['avg_score'] = replace_space_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[6]/span/text() ').extract())
        item['performance'] = replace_space_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[7]/span/text() ').extract())
        item['avg_performance'] = replace_space_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[8]/text() ').extract())

        print_dict(item)

        return item

# Xpath: 
    # ranking 
    # //*[@id="scores"]/div/table/tbody//td[1]/text()

    # country
    # //*[@id="scores"]/div/table/tbody/td[2]/div/a/span[2]
    # //*[@id="scores"]/div/table/tbody//td[2]/div/a/span[2]/text()

    # active_users
    # //*[@id="scores"]/div/table/tbody//td[3]/text()

    # play_count
    # //*[@id="scores"]/div/table/tbody//td[4]/span/text()
    # //*[@id="scores"]/div/table/tbody//td[5]/span/text()
    # //*[@id="scores"]/div/table/tbody//td[6]/span/text()
    # //*[@id="scores"]/div/table/tbody//td[7]/span/text()
    # //*[@id="scores"]/div/table/tbody//td[8]/text()




