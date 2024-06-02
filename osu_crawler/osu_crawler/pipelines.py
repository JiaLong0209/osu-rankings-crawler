# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import sqlite3
from utility import *

import config


prefix_path = "../"
db_path = "osu.db"

class OsuCrawlerPipeline:

    def open_spider(self, spider):
        self.conn = sqlite3.connect(prefix_path + db_path)
        self.cursor = self.conn.cursor()
        self.mode = config.CURRENT_MODE
        self.table_name = config.TABLES[self.mode]
        self.schema = "schema/" + config.SCHEMAS[self.mode]
        print("~" * 50)
        print(f"\n\n\n\nmode: {self.mode}")

        # create table
        # with open(self.shcema) as f:
        #     exe = f.read()
        #     self.conn.executescript(exe)
        # self.conn.commit()


    def close_spider(self, spider):
        self.conn.commit()
        print(f"Item commit to {config.DATABASE}")
        self.conn.close()

    def process_item(self, item, spider):
                
        for i in range(len(item['ranking'])):
            self.cursor.execute(f'''
                INSERT OR REPLACE INTO {self.table_name} (ranking, country_name, active_users, play_count, avg_score, performance, avg_performance) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                int(item.get('ranking', None)[i]),
                item.get('country_name', None)[i],
                int(item.get('active_users', None)[i]),
                int(item.get('play_count', None)[i]),
                int(item.get('avg_score', None)[i]),
                int(item.get('performance', None)[i]),
                int(item.get('avg_performance', None)[i])
            ))

        return item
