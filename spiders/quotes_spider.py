from pathlib import Path

import scrapy
import re



class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            # 'https://pubmed.ncbi.nlm.nih.gov/?term=RNAseq%2Bgenewiz',
            'https://pubmed.ncbi.nlm.nih.gov/?term=RNAseq%2Bgenewiz&size=200',
        ]
        for url in urls:
            for i in range(1, 2):
                for j in range(2000, 2023):
                    url1 = url + "&filter=years."+str(j)+"-"+str(j)    
                    url2 = url1 + "&page=" + str(i)
                    yield scrapy.Request(url=url2, callback=self.parse)

    def parse(self, response):
        href = response.xpath("//*[@id='search-results']/section/div[1]/div/article[2]/div[2]/div[1]/a/@href").extract()[0]
        href_list = response.xpath("//*[@id='search-results']/section/div[1]/div/article/div[2]/div[1]/a/@href")
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