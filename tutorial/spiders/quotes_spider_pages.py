from pathlib import Path

import scrapy
import re
import os
os.environ['SCRAPY_REACTOR'] = 'twisted.internet.selectreactor.SelectReactor'


class QuotesSpider(scrapy.Spider):
    name = "quotes_pages"

    def start_requests(self):
        
        urls = [
            'https://pubmed.ncbi.nlm.nih.gov/?term=novogene&page='
        ]

        for url in urls:
            for page_index in range(1, 42):
                url1 = url + str(page_index)
                yield scrapy.Request(url=url1, callback=self.parse)

    def parse(self, response):
        # href = response.xpath("//*[@id='search-results']/section/div[1]/div/article[2]/div[2]/div[1]/a/@href").extract()[0]
        # href_list = response.xpath("//*[@id='search-results']/section/div[1]/div/article/div[2]/div[1]/a/@href")
        href_list = response.xpath('//a[@class="docsum-title"]/@href').extract()
        if len(href_list) > 0:
            for href_name in href_list:
                # root = href_name.root
                href_link = "https://pubmed.ncbi.nlm.nih.gov" + href_name

                self.logger.info(f"Extracted URL: {href_link}")

                yield scrapy.Request(
                    url=href_link,
                    callback=self.parse_email,
                )
         
    
    def parse_email(self, response):
        email=re.compile(r'[a-z0-9\-\.]+@[0-9a-z\-\.]+')
        title = response.xpath("//*[@class='heading-title']/text()").extract()[0].rstrip().lstrip()
        # affiliation_list = response.xpath("//*[@id='full-view-expanded-authors']/div/ul/li/text()")
        #affiliation_list_content = response.xpath("//*[@id='full-view-expanded-authors']/div/ul/li/text()").extract()
        # for affiliation in affiliation_list:
            # affiliation_content = affiliation.root
        # author_name = response.xpath("//*[@class='authors-list']/span/a/text()").extract()
        
        # yield {
        #     "title": title,
        #     "affiliation_list": affiliation_list_content
        # }
        
        authors = []
        author_item = response.xpath("//*[@class='authors-list-item ']")
        for item in author_item:

            author_email_map = dict()
            author = item.xpath("a/text()").extract()[0]
            affiliationSupList = item.xpath("sup/a/@title").extract()
            
            if len(affiliationSupList) > 0:
                affiliation = affiliationSupList[0]
                emailList = email.findall(affiliation)
                
                if len(emailList) > 0:
                    author_email_map["author"] = author
                    # Collect all emails for this author
                    author_email_map["emails"] = emailList  # List of emails
                    authors.append(author_email_map)
            

        if len(authors) > 0:
            yield {
                "title": title,
                "author": authors,
                # "author": author_email_map["author"],
                # "emails": author_email_map["emails"],  # List of emails
                "url(Click url to access page)": response.url,
            }
        else:
            yield {
                "title": title,
                "author": "no find authors",
                # "author": author_email_map["author"],
                # "emails": author_email_map["emails"],  # List of emails
                "url(Click url to access page)": response.url,
            }


    def emailre(testStr):
        email=re.compile(r'([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)')
        emailset=set()  #列表
        for em in email.findall(testStr):
            emailset.add(em)
        return emailset
    
    def removeDot(emailStr):
        char = emailStr[-1]
        if char == ".":
            return emailStr[0: -1]
        else:
            return emailStr