from pathlib import Path

import scrapy
import re



class QuotesSpider(scrapy.Spider):
    name = "quotes_pages"

    def start_requests(self):
        
        urls = [
            'https://pubmed.ncbi.nlm.nih.gov/?term=princeton.edu&page='
        ]

        for url in urls:
            for page_index in range(1, 470):
                url1 = url + str(page_index)
                yield scrapy.Request(url=url1, callback=self.parse)

    def parse(self, response):
        # href = response.xpath("//*[@id='search-results']/section/div[1]/div/article[2]/div[2]/div[1]/a/@href").extract()[0]
        href_list = response.xpath("//*[@id='search-results']/section/div[1]/div/article/div[2]/div[1]/a/@href")
        if len(href_list) > 0:
            for href_name in href_list:
                root = href_name.root
                href_link = "https://pubmed.ncbi.nlm.nih.gov" + root
                yield scrapy.Request(
                    url=href_link,
                    callback=self.parse_email,
                )
         
    
    def parse_email(self, response):
        email=re.compile(r'[a-z0-9\-\.]+@[0-9a-z\-\.]+')
        title = response.xpath("//*[@class='heading-title']/text()").extract()[0].rstrip().lstrip()
        affiliation_list = response.xpath("//*[@id='full-view-expanded-authors']/div/ul/li/text()")
        #affiliation_list_content = response.xpath("//*[@id='full-view-expanded-authors']/div/ul/li/text()").extract()
        # for affiliation in affiliation_list:
            # affiliation_content = affiliation.root
        # author_name = response.xpath("//*[@class='authors-list']/span/a/text()").extract()
        
        # yield {
        #     "title": title,
        #     "affiliation_list": affiliation_list_content
        # }
        author_email_map = dict()
        author_item = response.xpath("//*[@class='authors-list-item ']")
        for item in author_item:
            author = item.xpath("a/text()").extract()[0]
            affiliationSupList = item.xpath("sup/a/@title").extract()
            if len(affiliationSupList) > 0:
                affiliation = item.xpath("sup/a/@title").extract()[0]
                #emailSet=set()
                emailList = email.findall(affiliation)
                if len(emailList) > 0:
                    em = emailList[0]
                    char = em[-1]
                    if (char == "."):
                        em = em[0: -1]
                    author_email_map["author"] = author
                    author_email_map["email"] = em

        if len(author_email_map) > 0:
            yield {
                "title": title,
                "author": author_email_map,
                "url(Click url to access page)": response.url,
            }
        # else:
        #     author_email_map["author"] = ""
        #     author_email_map["email"] = "can't find any email in this page"
        #     yield {
        #         "title": title,
        #         "author": author_email_map,
        #         "url(Click url to access page)": response.url,
        #     }

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