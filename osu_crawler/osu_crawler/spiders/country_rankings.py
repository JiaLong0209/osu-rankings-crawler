import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from osu_crawler.items import OsuCrawlerItem
from utility.functions import *

# Write a utility.py

class OsuCountrySpider(scrapy.Spider):
    name = "country_rankings"
    allowed_domains = ["osu.ppy.sh"]
    # https://osu.ppy.sh/rankings/osu/country?page=1#scores
    start_urls = [f"https://osu.ppy.sh/rankings/osu/country?page={i}#scores" for i in range(1, 3)]


    def parse(self, response):
        sel = Selector(response)
        item = OsuCrawlerItem()

        item['ranking'] = str_preprocess_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[1]/text()').extract())
        item['country_name'] = str_preprocess_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[2]/div/a/span[2]/text()').extract())
        item['active_users'] = str_preprocess_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[3]/text()').extract())

        item['play_count'] = str_preprocess_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[4]/span/text()').extract())
        item['ranked_score'] = str_preprocess_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[5]/span/text()').extract())
        item['avg_score'] = str_preprocess_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[6]/span/text()').extract())
        item['performance'] = str_preprocess_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[7]/span/text()').extract())

        item['avg_performance'] = str_preprocess_in_list(sel.xpath('//*[@id="scores"]/div/table/tbody//td[8]/text()').extract())

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

    # ranked_score
    # //*[@id="scores"]/div/table/tbody//td[5]/span/text()

    # avg_score
    # //*[@id="scores"]/div/table/tbody//td[6]/span/text()

    # performance
    # //*[@id="scores"]/div/table/tbody//td[7]/span/text()

    # avg_performance
    # //*[@id="scores"]/div/table/tbody//td[8]/text()



