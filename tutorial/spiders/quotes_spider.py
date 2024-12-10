from pathlib import Path

import scrapy
import re



class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        base_url = 'https://pubmed.ncbi.nlm.nih.gov/?term='
        plus = '%2B'
        left_parenthesis = '%28'
        right_parenthesis = '%29'
        and_fu = '+AND+'
        page_size = '&size=200'
        urls = [
            # 'https://pubmed.ncbi.nlm.nih.gov/?term=RNAseq%2Bgenewiz',
            # 'https://pubmed.ncbi.nlm.nih.gov/?term=RNAseq%2Bgenewiz&size=200',
            # 'https://pubmed.ncbi.nlm.nih.gov/?term=RNAseq%2Bgenewiz&size=200',
            '%28globinclear%29+AND+%28RNAseq%29',
            '%28Illumina+Ribo-Zero+Plus%29+AND+%28RNAseq%29',
            '%28whole+blood%29+AND+%28RNAseq%29',
            '%28globinclear%29+AND+%28Genewiz%29',
            '%28globinclear%29+AND+%28Novogen%29',
            '%28Paxgene%29+AND+%28RNAseq%29',
            '%28Tempus%29+AND+%28RNAseq%29',
            '%28Novaseq%29+AND+%28Azenta%29',
            '%28Novaseq%29+AND+%28Novogene%29',
            '%28Novaseq%29+AND+%28Macrogen%29',
            '%28Novaseq%29+AND+%28Genewiz%29',
            '%28Princeton%29+AND+%28RNAseq%29',
            '%28Princeton%29+AND+%28WES++++%29',
            '%28Princeton%29+AND+%28CRISPR%29',
            '%28Princeton%29+AND+%28WGS++%29',
            '%28Princeton%29+AND+%2810X++%29',
            '%28Princeton%29+AND+%28NGS%29'
        ]
        # key_words = ['Abbott']
        # key_words = 
        # for key_word in key_words:
        #     url = base_url + left_parenthesis + key_word + right_parenthesis + and_fu + left_parenthesis + 'Cellranger' + right_parenthesis + page_size
        #     urls.append(url)

        for url in urls:
            for i in range(1, 2):
                for j in range(2000, 2024):
                    url0 = base_url + url + page_size
                    url1 = url0 + "&filter=years."+str(j)+"-"+str(j)    
                    url2 = url1 + "&page=" + str(i)
                    yield scrapy.Request(url=url2, callback=self.parse)

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