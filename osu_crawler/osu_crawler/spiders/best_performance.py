import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from osu_crawler.items import OsuCrawlerItem
from utility.functions import *
from config import *
import re


class BestPerformanceSpider(scrapy.Spider):
    name = "best_performance"
    allowed_domains = ["osu.ppy.sh"]
    start_urls = ["https://osu.ppy.sh/rankings/osu/performance"]

    # pages = [i for i in range(START_PAGE, END_PAGE+1)] 
    # start_urls = [f"https://osu.ppy.sh/rankings/{mode}/performance?page={i}#scores" for i in pages for mode in GAME_MODES] 

    def parse(self, response):
        sel = Selector(response)
        item = OsuCrawlerItem()

        return item
