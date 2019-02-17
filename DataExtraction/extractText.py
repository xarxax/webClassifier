import glob,os,sys
from bs4 import BeautifulSoup

#gets property property from the soup's meta
#gets property property from the soup's meta
def getMetaContent(soup,property):
    cssQuery='meta[property="og:' + property+'"]'
    #print(cssQuery)
    content = soup.select(cssQuery)
    if len(content)>0 and not(content[0].get('content') is None) :
        return content[0].get('content') + '\n'
    cssQuery='meta[name="' + property+'"]'
    content = soup.select(cssQuery)
    if len(content)>0 and not(content[0].get('content') is None) :
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
        print('Reached limit established')
        break
    i-=1
    print(filePath)
    file = open(filePath,'r')
    #split the 3 important informations
    try:
        [cat,url,htmlDoc] = file.read().split('\n',2)
    except:
        print('Page containing non utf8 characters, will be skipped')
        continue
    soup = BeautifulSoup(htmlDoc, 'html.parser')
    relevantText = addMetas(soup,'')
    #add actual text from the body
    #remove all text of scripts and style
    for script in soup(["script", "style"]):
        script.decompose()    # rip it out

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
    relevantText =relevantText
    with open(newFilePath+'/text.txt', 'w') as f:
        f.write(str(relevantText))
