from pathlib import Path

import scrapy
import re



class QuotesSpider(scrapy.Spider):
    name = "quotes_google"

    def start_requests(self):
        urls = [
            'https://www.google.com/search?q=Princeton+and+RNAseq&oq=Princeton+and+RNAseq',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        email = response.xpath()
        print(email)
    