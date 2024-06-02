import subprocess
import os 
import time

from osu_crawler.config import *

os.chdir('osu_crawler/')

# command = ["scrapy", "crawl", "country_rankings"]
command = "scrapy crawl country_rankings"

for mode in GAME_MODES:
    try:
        CURRENT_MODE = mode
        print("-" * 40)
        print(f"CURRENT_MODE: {CURRENT_MODE}")

        os.system(command) 
        # subprocess.run(command, check=True)

        print("Command executed successfully")

    except e:
        print(f"Error: {e}")

    time.sleep(5)
