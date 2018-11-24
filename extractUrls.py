import glob,os
from bs4 import BeautifulSoup

#gets property property from the soup's meta
def getMetaContent(soup,property):
    cssQuery='meta ["property"="og:' + property+'"]'
    content = soup.select(cssQuery)
    if len(content)>0 :
        return content[0].get('content') + '\n'
    return ''

#extracts all metas information from the soup'
#tags obtained from http://ogp.me/
def addMetas(soup,urls):
    #title= soup.select('meta ["property"="og:title"]')[0].get('content')
    urls+=  [getMetaContent(soup,'url')]
    urls+=  [getMetaContent(soup,'image')]
    urls+=  [getMetaContent(soup,'image:secure_url')]
    urls+=  [getMetaContent(soup,'video')]
    urls+=  [getMetaContent(soup,'video:secure_url')]
    urls+=  [getMetaContent(soup,'video')]
    urls+=  [getMetaContent(soup,'video')]

    return urls






i = 1000

for filePath in glob.iglob('dataset/*'):
    print(filePath)
    file = open(filePath,'r')
    #split the 3 important informations
    [cat,url,htmlDoc] = file.read().split('\n',2)
    soup = BeautifulSoup(htmlDoc, 'html.parser')
    relevantText = addMetas(soup,[url])
    #add actual text from the body

    #remove all text of scripts and style
    map(lambda x: x.clear(),soup.select('script'))
    map(lambda x: x.clear(),soup.select('style'))



    if relevantText=='':
        print('UNABLE TO EXTRACT ANY TEXT')
        continue
    #saving urls now

    #we open the folder at dataset features
    newFilePath = filePath.replace('dataset/','datasetFeatures/',1)
    if not os.path.exists(newFilePath):
        continue#if we didnt find any text, page is not eligible
    #write text
    relevantText =relevantText.encode('utf8')
    with open(newFilePath+'/ur.txt', 'w') as f:
        f.write(relevantText)
        
    if i <=0:
        break
    i-=1
