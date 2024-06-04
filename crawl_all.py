import subprocess
import os 
import time

from osu_crawler.config import *

os.chdir('osu_crawler/')

from config import * 

command = f"scrapy crawl {CRAWLER_NAME}"

for mode in GAME_MODES:
    try:
        change_current_mode(mode)
        print("-" * 40)
        print(f"current mode: {CURRENT_MODE}")

        os.system(command) 

        print("Command executed successfully")

    except e:
        print(f"Error: {e}")

