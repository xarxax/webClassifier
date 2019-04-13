# -*- coding: utf-8 -*-
import scrapy,os,sys,glob
from scrapy_splash import SplashRequest
from selenium import webdriver



class htmlExtractor(scrapy.Spider):
    name = 'htmlExtractor'
    custom_settings = {
        'CONCURRENT_REQUESTS' :30,
        'REACTOR_THREADPOOL_MAXSIZE' : 20,
        'LOG_LEVEL' : 'CRITICAL',
        'COOKIES_ENABLED' : True,
        'AJAXCRAWL_ENABLED' : True,
        'AUTOTHROTTLE_ENABLED':True,
        'HTTPCACHE_ENABLED': True,
        'CLOSESPIDER_TIMEOUT': 7200#number of seconds in 4 hours
    }
    def start_requests(self):
        print('beginning crawling')
        self.driver = webdriver.PhantomJS('../phantomjs')
        #print('geese')
        #print(self.parameter)
        print(self.parameter)
        if not os.path.exists('../../tempfiles'):
            os.makedirs('../../tempfiles')
        if not os.path.exists('../../tempfiles/HTML'):
            os.makedirs('../../tempfiles/HTML')
        input = open('../../'+ self.parameter ,'r')
        extractionUrls= []
        for line in input:
            extractionUrls+= [line]
        print(extractionUrls)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in extractionUrls:
            #print('aaaaaaaa')
            yield SplashRequest(url=url,callback=self.parse, headers=headers)

    def parse(self,response):
        #print('bbbbbbb')
        #print(response.url)
        self.driver.get(response.url)
        content = response.replace(body=self.driver.page_source)
        #print(content)
        url = response.url
        filename = '../../tempfiles/HTML/'+ str(url[:70]).replace('/','_')
        with open(filename,'w') as f:
            f.write(str(response.body))
