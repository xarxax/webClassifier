# -*- coding: utf-8 -*-
import scrapy



class htmlExtractor(scrapy.Spider):
    name = 'htmlExtractor'

    def start_requests(self):
        input = open('../catAndUrlChosen.txt','r')
        extractionUrls= []
        for i,line in enumerate(input):
            line = line.split(',')
            cat = line[0]
            url = ''.join(line[1:])#rest
            extractionUrls.append((cat,url))
            #if i > 20:
            #    break

        for cat,url in extractionUrls:
            yield scrapy.Request(url=url,callback=self.parse,meta = {'cat':cat})

    def parse(self,response):
        content = response.body
        url = response.url
        cat =  str(response.meta['cat'])
        filename = '../dataset/'+str(cat) + '_' + str(url).replace('/','_')
        with open(filename,'wb') as f:
            f.write(str(cat)+ '\n')
            f.write(str(url)+ '\n')
            f.write(response.body)
