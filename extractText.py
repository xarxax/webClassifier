import glob
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
def addMetas(soup,text):
    #title= soup.select('meta ["property"="og:title"]')[0].get('content')
    text+=  getMetaContent(soup,'title')
    text+=  getMetaContent(soup,'type')
    text+=  getMetaContent(soup,'description')
    text+=  getMetaContent(soup,'locale')
    text+=  getMetaContent(soup,'locale:alternate')
    text+=  getMetaContent(soup,'site_name')
    text+=  getMetaContent(soup,'image:alt')
    return text

i = 0
for filepath in glob.iglob('dataset/*'):
    print(filepath)
    file = open(filepath,'r')
    #split the 3 important informations
    [cat,url,htmlDoc] = file.read().split('\n',2)
    soup = BeautifulSoup(htmlDoc, 'html.parser')
    relevantText = addMetas(soup,'')
    print(relevantText)
    if i < 1:
        break
    i-=1
