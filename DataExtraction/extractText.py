import glob,os,sys
from bs4 import BeautifulSoup
import pandas as pd 



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
if not os.path.exists('datasets'):
    os.makedirs('datasets')




i = int(sys.argv[1])
cwd = os.getcwd()
catAndText= []



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


    relevantText = (' '.join(relevantText.replace('\n',' ').replace('\\n',' ').replace('\\t',' ').replace('\\r',' ').replace('\t','').split())).encode('utf-16','surrogatepass').decode('utf-16')
        #print(relevantText)
    catAndText+=[cat + '\t'+str(relevantText)]


frow= ['CAT\tTEXT']
with open(cwd + '/datasets/catwebs.csv','w') as f:
	f.write('\n'.join(frow + catAndText))







