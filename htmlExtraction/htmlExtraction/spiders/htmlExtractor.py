# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest



class htmlExtractor(scrapy.Spider):
    name = 'htmlExtractor'
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS' :10000,
        'REACTOR_THREADPOOL_MAXSIZE' : 20,
        'LOG_LEVEL' : 'INFO',
        'COOKIES_ENABLED' : False,
        'AJAXCRAWL_ENABLED' : True
    }
    def start_requests(self):

        input = open('../catAndUrlChosen.txt','r')
        extractionUrls= []
        for i,line in enumerate(input):
            line = line.split(',')
            cat = line[0]
            url = ''.join(line[1:]).replace('\n','')#rest
            print(url)
            extractionUrls.append((cat,url))
            #if i > 20:
            #    br
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for cat,url in extractionUrls:
            yield SplashRequest(url=url,callback=self.parse,meta = {'cat':cat},
            headers=headers,args={'wait': '1'})

    def parse(self,response):
        content = response.body
        url = response.url
        cat =  str(response.meta['cat'])
        filename = '../dataset/'+str(cat) + '_' + str(url[:70]).replace('/','_')
        with open(filename,'wb') as f:
            f.write(str(cat)+ '\n')
            f.write(str(url)+ '\n')
            f.write(response.body)
