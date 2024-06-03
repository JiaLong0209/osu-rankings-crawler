# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OsuCrawlerItem(scrapy.Item):

    # Country
    ranking = scrapy.Field()
    country_name = scrapy.Field()
    active_users = scrapy.Field()
    play_count = scrapy.Field()
    ranked_score = scrapy.Field()
    avg_score = scrapy.Field()
    performance = scrapy.Field()
    avg_performance = scrapy.Field()
    mode = scrapy.Field()


