from scrapy.cmdline import execute
import os
import sys
if __name__ == '__main__':

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(['scrapy','crawl','quotes', "-O quotes.json"])
    # execute(['scrapy','crawl','quotes_google'])
    # execute(['scrapy','crawl','quotes_pages', "-O quotes_pages.json"])
    execute(['scrapy','crawl','genohub', "-O genohub.json"])
