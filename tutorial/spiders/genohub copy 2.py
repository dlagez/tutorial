from pathlib import Path

import scrapy
import re
import json
from scrapy.shell import inspect_response

# 用于测试，只有少数的url

class QuotesSpider(scrapy.Spider):
    name = "genohub2"
    start_urls = ['https://genohub.com/accounts/login/']

    def parse(self, response): # 发送Post请求获取Cookies
            form_data = {
                'login': 'bi_ruo@admerahealth.com',
                'password': 'Bi2022@',
                }
            yield scrapy.FormRequest.from_response(response, formdata=form_data, callback=self.parse_aaa)


    def parse_url(self, response):
        print(response.text)
        re_url = 'https://genohub.com/provider/orders/',
        yield scrapy.Request(url=re_url, callback=self.parse_aaa)

    def parse_aaa(self, response):
        # href = response.xpath("//*[@id='search-results']/section/div[1]/div/article[2]/div[2]/div[1]/a/@href").extract()[0]
        # print(response.text)
        urls_confirm = ['https://genohub.com/provider/project/4661684',
                'https://genohub.com/provider/project/7099733',
                'https://genohub.com/provider/project/7307182',
                'https://genohub.com/provider/project/2155657',
                'https://genohub.com/provider/project/2478086',
                'https://genohub.com/provider/project/4718561',
                'https://genohub.com/provider/project/1959393',
                'https://genohub.com/provider/project/3122972',
                'https://genohub.com/provider/project/8877829',
                'https://genohub.com/provider/project/8557826',
                'https://genohub.com/provider/project/7284238',
                'https://genohub.com/provider/project/1186878',
                'https://genohub.com/provider/project/6090143',
                'https://genohub.com/provider/project/3013187',
                'https://genohub.com/provider/project/5364360',
                'https://genohub.com/provider/project/9464864',
                'https://genohub.com/provider/project/5622885',
                'https://genohub.com/provider/project/4905896',
                'https://genohub.com/provider/project/3349664',
                'https://genohub.com/provider/project/7243328',
                'https://genohub.com/provider/project/8613666',
                'https://genohub.com/provider/project/8174817',
                'https://genohub.com/provider/project/7424984',
                'https://genohub.com/provider/project/5416014',
                'https://genohub.com/provider/project/6795747',
                'https://genohub.com/provider/project/7001964',
                'https://genohub.com/provider/project/1392906',
                'https://genohub.com/provider/project/1568935',
                'https://genohub.com/provider/project/9931284',
                'https://genohub.com/provider/project/9664023',
                'https://genohub.com/provider/project/5787566',
                'https://genohub.com/provider/project/7819015',
                'https://genohub.com/provider/project/1397184',
                'https://genohub.com/provider/project/9383598',
                'https://genohub.com/provider/project/7192388',
                'https://genohub.com/provider/project/2288199',
                'https://genohub.com/provider/project/7417031',
                'https://genohub.com/provider/project/6922271',
                'https://genohub.com/provider/project/8790351',
                'https://genohub.com/provider/project/5898811',
                'https://genohub.com/provider/project/8969387',
                'https://genohub.com/provider/project/2070383',
                'https://genohub.com/provider/project/4567453',
                'https://genohub.com/provider/project/1406808',
                'https://genohub.com/provider/project/4368606',
                'https://genohub.com/provider/project/9239676',
                'https://genohub.com/provider/project/4086735',
                'https://genohub.com/provider/project/5556674',
                'https://genohub.com/provider/project/9235962',
                'https://genohub.com/provider/project/1415052',
                'https://genohub.com/provider/project/3561671',
                'https://genohub.com/provider/project/4650122',
                'https://genohub.com/provider/project/5346014',
                'https://genohub.com/provider/project/4261094',
                'https://genohub.com/provider/project/2637798',
                'https://genohub.com/provider/project/6244797',
                'https://genohub.com/provider/project/2968008',
                'https://genohub.com/provider/project/3074115',
                'https://genohub.com/provider/project/3001419',
                'https://genohub.com/provider/project/7493683',
                'https://genohub.com/provider/project/5427187',
                'https://genohub.com/provider/project/8694626',
                'https://genohub.com/provider/project/4823610',
                'https://genohub.com/provider/project/1749482',
                'https://genohub.com/provider/project/3054617',
                'https://genohub.com/provider/project/1864899',]
        
        urls_unconfirm = ['https://genohub.com/provider/project/1000432',
                'https://genohub.com/provider/project/1622867',
                'https://genohub.com/provider/project/4693089',
                'https://genohub.com/provider/project/8430663',
                'https://genohub.com/provider/project/8885043',
                'https://genohub.com/provider/project/5753534',
                'https://genohub.com/provider/project/4095585',
                'https://genohub.com/provider/project/2681587',
                'https://genohub.com/provider/project/8057055',
                'https://genohub.com/provider/project/7297503',
                'https://genohub.com/provider/project/3342359',
                'https://genohub.com/provider/project/6416100',
                'https://genohub.com/provider/project/2567070',
                'https://genohub.com/provider/project/7219551',
                'https://genohub.com/provider/project/9704176',
                'https://genohub.com/provider/project/9485701',
                'https://genohub.com/provider/project/5257285',
                'https://genohub.com/provider/project/1262876',
                'https://genohub.com/provider/project/9920815',
                'https://genohub.com/provider/project/4702145',
                'https://genohub.com/provider/project/1983623',
                'https://genohub.com/provider/project/1086937',
                'https://genohub.com/provider/project/1785090',
                'https://genohub.com/provider/project/1442275',
                'https://genohub.com/provider/project/7845058',
                'https://genohub.com/provider/project/6298825',
                'https://genohub.com/provider/project/3603380',
                'https://genohub.com/provider/project/9699515',
                'https://genohub.com/provider/project/9566854',
                'https://genohub.com/provider/project/1796102',
                'https://genohub.com/provider/project/4014257',
                'https://genohub.com/provider/project/7282960',
                'https://genohub.com/provider/project/9140705',
                'https://genohub.com/provider/project/7984480',
                'https://genohub.com/provider/project/7803253',
                'https://genohub.com/provider/project/6195832',
                'https://genohub.com/provider/project/2521837',
                'https://genohub.com/provider/project/8596781',
                'https://genohub.com/provider/project/9840509',
                'https://genohub.com/provider/project/1610454',
                'https://genohub.com/provider/project/7756691',
                'https://genohub.com/provider/project/8976044',
                'https://genohub.com/provider/project/6786327',
                'https://genohub.com/provider/project/8358559',
                'https://genohub.com/provider/project/8503055',
                'https://genohub.com/provider/project/4930406',
                'https://genohub.com/provider/project/9546902',
                'https://genohub.com/provider/project/4542005',
                'https://genohub.com/provider/project/5970970',
                'https://genohub.com/provider/project/8768032',
                'https://genohub.com/provider/project/6144519',
                'https://genohub.com/provider/project/6018474',
                'https://genohub.com/provider/project/8666839',
                'https://genohub.com/provider/project/4231180',
                'https://genohub.com/provider/project/3108819',
                'https://genohub.com/provider/project/7082700',
                'https://genohub.com/provider/project/3812782',
                'https://genohub.com/provider/project/3457075',
                'https://genohub.com/provider/project/2728391',
                'https://genohub.com/provider/project/8852866',
                'https://genohub.com/provider/project/4794302',
                'https://genohub.com/provider/project/1743554',
                'https://genohub.com/provider/project/1863877',
                'https://genohub.com/provider/project/2137511',
                'https://genohub.com/provider/project/2808048',
                'https://genohub.com/provider/project/1555931',
                'https://genohub.com/provider/project/3306319',
                'https://genohub.com/provider/project/8792231',
                'https://genohub.com/provider/project/8864934',
                'https://genohub.com/provider/project/7925509',
                'https://genohub.com/provider/project/2500069',
                'https://genohub.com/provider/project/4884541',
                'https://genohub.com/provider/project/1556532',
                'https://genohub.com/provider/project/2852595',
                'https://genohub.com/provider/project/6816473',
                'https://genohub.com/provider/project/1144551',
                'https://genohub.com/provider/project/8355352',
                'https://genohub.com/provider/project/6995241',
                'https://genohub.com/provider/project/8626115',
                'https://genohub.com/provider/project/6911967',
                'https://genohub.com/provider/project/7915356',
                'https://genohub.com/provider/project/3152405',
                'https://genohub.com/provider/project/7025031',
                'https://genohub.com/provider/project/5269272',
                'https://genohub.com/provider/project/5252298',
                'https://genohub.com/provider/project/9601610',
                'https://genohub.com/provider/project/5395952',
                'https://genohub.com/provider/project/7019819',
                'https://genohub.com/provider/project/9715653',
                'https://genohub.com/provider/project/7474628',
                'https://genohub.com/provider/project/6323846',
                'https://genohub.com/provider/project/4274757',
                'https://genohub.com/provider/project/6241365',
                'https://genohub.com/provider/project/8820381',
                'https://genohub.com/provider/project/7046933',
                'https://genohub.com/provider/project/3510540',
                'https://genohub.com/provider/project/9657333',
                'https://genohub.com/provider/project/2159969',
                'https://genohub.com/provider/project/5119056',
                'https://genohub.com/provider/project/7576020',
                'https://genohub.com/provider/project/4641636',
                'https://genohub.com/provider/project/6074527',
                'https://genohub.com/provider/project/3713164',
                'https://genohub.com/provider/project/7466846',
                'https://genohub.com/provider/project/5095409',
                'https://genohub.com/provider/project/9789239',
                'https://genohub.com/provider/project/9666480',
                'https://genohub.com/provider/project/2444428',
                'https://genohub.com/provider/project/1672020',
                'https://genohub.com/provider/project/3881853',
                'https://genohub.com/provider/project/5600806',
                'https://genohub.com/provider/project/1556989',
                'https://genohub.com/provider/project/2737144',
                'https://genohub.com/provider/project/4804986',
                'https://genohub.com/provider/project/6513189',
                'https://genohub.com/provider/project/3316867',
                'https://genohub.com/provider/project/5033015',
                'https://genohub.com/provider/project/6108050',
                'https://genohub.com/provider/project/5487269',
                'https://genohub.com/provider/project/6369694',
                'https://genohub.com/provider/project/6669378',
                'https://genohub.com/provider/project/5308407',
                'https://genohub.com/provider/project/2126066',
                'https://genohub.com/provider/project/9853556',
                'https://genohub.com/provider/project/6133062',
                'https://genohub.com/provider/project/2693933',
                'https://genohub.com/provider/project/7428200',
                'https://genohub.com/provider/project/5562656',
                'https://genohub.com/provider/project/6865252',
                'https://genohub.com/provider/project/9018241',
                'https://genohub.com/provider/project/4347797',
                'https://genohub.com/provider/project/4187692',
                'https://genohub.com/provider/project/9452504',
                'https://genohub.com/provider/project/1921016',
                'https://genohub.com/provider/project/2475451',
                'https://genohub.com/provider/project/3727741',
                'https://genohub.com/provider/project/3037110',
                'https://genohub.com/provider/project/6326796',
                'https://genohub.com/provider/project/3936668',
                'https://genohub.com/provider/project/2690712',
                'https://genohub.com/provider/project/5356338',
                'https://genohub.com/provider/project/8198385',
                'https://genohub.com/provider/project/6815413',
                'https://genohub.com/provider/project/7379930',
                'https://genohub.com/provider/project/2899390',
                'https://genohub.com/provider/project/5632009',
                'https://genohub.com/provider/project/2194303',
                'https://genohub.com/provider/project/6020807',
                'https://genohub.com/provider/project/8641080',
                'https://genohub.com/provider/project/6774084',
                'https://genohub.com/provider/project/4808597',
                'https://genohub.com/provider/project/6497906',
                'https://genohub.com/provider/project/3410794',
                'https://genohub.com/provider/project/5429254',
                'https://genohub.com/provider/project/1117657',
                'https://genohub.com/provider/project/2409053',
                'https://genohub.com/provider/project/6210274',
                'https://genohub.com/provider/project/5703219',
                'https://genohub.com/provider/project/3555392',
                'https://genohub.com/provider/project/2362955',
                'https://genohub.com/provider/project/5658142',
                'https://genohub.com/provider/project/5017210',
                'https://genohub.com/provider/project/7475435',
                'https://genohub.com/provider/project/2808139',
                'https://genohub.com/provider/project/7265980',
                'https://genohub.com/provider/project/6165587',
                'https://genohub.com/provider/project/5839061',
                'https://genohub.com/provider/project/8500250',
                'https://genohub.com/provider/project/8342458',
                'https://genohub.com/provider/project/8249958',
                'https://genohub.com/provider/project/2179131',
                'https://genohub.com/provider/project/4348496',
                'https://genohub.com/provider/project/7053335',
                'https://genohub.com/provider/project/5375857',
                'https://genohub.com/provider/project/2043034',
                'https://genohub.com/provider/project/9382490',
                'https://genohub.com/provider/project/3617599',
                'https://genohub.com/provider/project/8567597',
                'https://genohub.com/provider/project/7145176',
                'https://genohub.com/provider/project/8472514',
                'https://genohub.com/provider/project/4091472',
                'https://genohub.com/provider/project/9333870',
                'https://genohub.com/provider/project/3554721',
                'https://genohub.com/provider/project/8433429',
                'https://genohub.com/provider/project/7404175',
                'https://genohub.com/provider/project/4642403',
                'https://genohub.com/provider/project/2492524',
                'https://genohub.com/provider/project/6601849',
                'https://genohub.com/provider/project/5474974',
                'https://genohub.com/provider/project/1183935',
                'https://genohub.com/provider/project/1995761',
                'https://genohub.com/provider/project/7756363',
                'https://genohub.com/provider/project/9769502',
                'https://genohub.com/provider/project/6795550',
                'https://genohub.com/provider/project/2118913',
                'https://genohub.com/provider/project/3625290',
                'https://genohub.com/provider/project/1324407',
                'https://genohub.com/provider/project/8658488',
                'https://genohub.com/provider/project/4863177',
                'https://genohub.com/provider/project/7068202',
                'https://genohub.com/provider/project/1164429',
                'https://genohub.com/provider/project/7625806',
                'https://genohub.com/provider/project/8941253',
                'https://genohub.com/provider/project/8646457',
                'https://genohub.com/provider/project/6992731',
                'https://genohub.com/provider/project/3870231',
                'https://genohub.com/provider/project/7751266',
                'https://genohub.com/provider/project/9819956',
                'https://genohub.com/provider/project/4655543',
                'https://genohub.com/provider/project/9911688',
                'https://genohub.com/provider/project/2025936',
                'https://genohub.com/provider/project/1559798',
                'https://genohub.com/provider/project/2102553',
                'https://genohub.com/provider/project/2866451',
                'https://genohub.com/provider/project/9736735',
                'https://genohub.com/provider/project/8520970',
                'https://genohub.com/provider/project/4892488',
                'https://genohub.com/provider/project/9137673',
                'https://genohub.com/provider/project/8702742',
                'https://genohub.com/provider/project/1492138',
                'https://genohub.com/provider/project/5041043',
                'https://genohub.com/provider/project/5229187',
                'https://genohub.com/provider/project/1038517',
                'https://genohub.com/provider/project/8845628',
                'https://genohub.com/provider/project/9883251',
                'https://genohub.com/provider/project/7838625',
                'https://genohub.com/provider/project/2916330',
                'https://genohub.com/provider/project/2951797',
                'https://genohub.com/provider/project/3541856',
                'https://genohub.com/provider/project/3779545',
                'https://genohub.com/provider/project/7960597',
                'https://genohub.com/provider/project/7017969',
                'https://genohub.com/provider/project/4049366',
                'https://genohub.com/provider/project/1562804',
                'https://genohub.com/provider/project/6725748',
                'https://genohub.com/provider/project/5972392',
                'https://genohub.com/provider/project/8363017',
                'https://genohub.com/provider/project/1571460',
                'https://genohub.com/provider/project/5465160',
                'https://genohub.com/provider/project/8732146',
                'https://genohub.com/provider/project/6351716',
                'https://genohub.com/provider/project/9170887',
                'https://genohub.com/provider/project/8304867',
                'https://genohub.com/provider/project/9937745',
                'https://genohub.com/provider/project/5928673',
                'https://genohub.com/provider/project/3627663',
                'https://genohub.com/provider/project/2261715',
                'https://genohub.com/provider/project/3460045',
                'https://genohub.com/provider/project/1647003',
                'https://genohub.com/provider/project/2311790',
                'https://genohub.com/provider/project/7767764',
                'https://genohub.com/provider/project/1562793',
                'https://genohub.com/provider/project/9519074',
                'https://genohub.com/provider/project/6044951',
                'https://genohub.com/provider/project/3037848',
                'https://genohub.com/provider/project/3327243',
                'https://genohub.com/provider/project/3929841',
                'https://genohub.com/provider/project/9622867',
                'https://genohub.com/provider/project/2744844',
                'https://genohub.com/provider/project/5071108',
                'https://genohub.com/provider/project/6597927',
                'https://genohub.com/provider/project/1736697',
                'https://genohub.com/provider/project/1367608',
                'https://genohub.com/provider/project/5246124',
                'https://genohub.com/provider/project/1376823',
                'https://genohub.com/provider/project/7709691',]
        
        completed_projects =   ["https://genohub.com/provider/project/9340393/",
                                "https://genohub.com/provider/project/5373661/"]


        # url_dict = {'Unconfirmed Projects': urls_unconfirm, "Confirmed Projects": urls_confirm, "completed": completed_projects}
        url_dict = {"completed": completed_projects}

        
        url_temp = ['https://genohub.com/provider/project/7099733']
             
        # yield scrapy.Request(url='https://genohub.com/provider/project/7099733',
        #                     cookies=response.headers.getlist('Set-Cookie'),
        #                     callback=self.parse_data,
        #                     meta={'project_type': 'Unconfirmed Projects'})
        # for url in urls_confirm:
        #     yield scrapy.Request(url=url,
        #                     cookies=response.headers.getlist('Set-Cookie'),
        #                     callback=self.parse_data_confirm)
        
        # for url in urls_unconfirm:
        #     yield scrapy.Request(url=url,
        #                     cookies=response.headers.getlist('Set-Cookie'),
        #                     callback=self.parse_data_unconfirm)
        # iter url_dict
        for key, value in url_dict.items():
            for url in value:
                yield scrapy.Request(url=url,
                                cookies=response.headers.getlist('Set-Cookie'),
                                callback=self.parse_data,
                                meta={'project_type': key})

    
    def parse_data(self, response):
        aaa = response.xpath('normalize-space(//script[contains(., "window.inits")]/text())').extract_first()
        # inspect_response(response, self)
        base = 'https://genohub.com/api/quotes/'
       
        

        if response.meta['project_type'] == "Unconfirmed Projects":
            category = "Unconfirmed Projects"
        else:
            category = "Confirmed Projects"
            
        try:
            result = json.loads(aaa[15:-1])
            members = result['members']
            members_names = ""
            if members is not None or members.length > 0:
                for member in members:  
                    members_names = members_names + member['firstName'] + " " + member['lastName'] + ","
            status = result['statusText']
            projNumber = result['projNumber']
            data = {
            "Parse Success?": "success!",
            "Category": category,
            "Url": response.url,
            "ProjNumber": projNumber,
            "Title": result['title'],
            "ClientName": result['clientName'],
            "Status": status,
            "Project Notes": result['description'],
            "Members": members_names
            }
            quote_url = base + str(projNumber)
            yield scrapy.Request(url=quote_url, callback=self.parse_quotes_data, meta={'data': data, 'projNumber': projNumber})
        except Exception:
            yield {
            "parse success?": "failed!",
            "Category": "Confirmed Projects",
            "url": response.url,
            "projNumber": None,
            "title": None,
            "clientName": None,
            "status": None,
            "Project Notes": None,
            "members": None
            }

    def parse_quotes_data(self, response):
        data = response.meta['data']
        # inspect_response(response, self)
        response_json = json.loads(response.body)
        quote_accepted = response_json['quotes'][0]
        # convert list(dict) to dict
        projNumber = response.meta['projNumber']
        projNumber = str(projNumber)



        data['items'] = str(quote_accepted['items'])
        data['quotes_description'] = quote_accepted['description']
        data['expiration'] = quote_accepted['expiration']
        data['clientTotal'] = quote_accepted['clientTotal']
        data['location'] = quote_accepted['location']
        data['provider'] = quote_accepted['provider']
        data['Payment status'] = quote_accepted['ppsDisplay']
        data['providerTotal'] = quote_accepted['providerTotal']
        data['serviceFee'] = quote_accepted['serviceFee']

        base_url = 'https://genohub.com/api/refresh-project/?order_number='
        url = base_url + projNumber

        yield scrapy.Request(url=url, callback=self.parse_message_data, meta={'data': data})
    
    def parse_message_data(self, response):
        data = response.meta['data']
        # inspect_response(response, self)
        response_json = json.loads(response.body)
        messages = response_json['messages']
        messages_list = []
        for message in messages:
            data_temp = {'#' + str(message['seqNumber']) + ' ' + message['poster']: message['text']}
            messages_list.append(data_temp)
        # reverse messages_list
        messages_list.reverse()
        data['messages'] = str(messages_list)
        yield data



        
        
        
        
        
        
        




        


        