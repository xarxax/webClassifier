import glob,os,sys
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

####MAIN SCRIPT
#we create the folder where we will have our features
#text.txt images and urls.txt
if not os.path.exists('datasetFeatures'):
    os.makedirs('datasetFeatures')

i = int(sys.argv[1])

for filePath in glob.iglob('dataset/*'):
    if i <=0:
        print 'Reached limit established'
        break
    i-=1
    print(filePath)
    file = open(filePath,'r')
    #split the 3 important informations
    [cat,url,htmlDoc] = file.read().split('\n',2)
    soup = BeautifulSoup(htmlDoc, 'html.parser')
    relevantText = addMetas(soup,'')
    #add actual text from the body

    #remove all text of scripts and style
    map(lambda x: x.clear(),soup.select('script'))
    map(lambda x: x.clear(),soup.select('style'))

    if soup.body != None:
        relevantText += soup.body.get_text()

    if relevantText=='':
        print('UNABLE TO EXTRACT ANY TEXT')
        continue
    #saving text now
    #we create a folder for the web features
    newFilePath = filePath.replace('dataset/','datasetFeatures/',1)
    if not os.path.exists(newFilePath):
        os.makedirs(newFilePath)
    #write text
    relevantText =relevantText.encode('utf8')
    with open(newFilePath+'/text.txt', 'w') as f:
        f.write(relevantText)
