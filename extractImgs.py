import glob,os,sys,urllib,requests
from bs4 import BeautifulSoup

#gets property property from the soup's meta
def getMetaContent(soup,property):
    cssQuery='meta ["property"="og:' + property+'"]'
    content = soup.select(cssQuery)
    if len(content)>0 :
        return content[0].get('content')
    return ''

#extracts all metas information from the soup'
#tags obtained from http://ogp.me/
def getMetaImg(soup):
    #title= soup.select('meta ["property"="og:title"]')[0].get('content')
    url =  getMetaContent(soup,'image')
    height = getMetaContent(soup,'image:height')
    width = getMetaContent(soup,'image:width')
    if url:
        return [(url,height,width)]
    url =  getMetaContent(soup,'image:secure_url')
    if url:
        return [(url,height,width)]
    return []


def getSrc(tag):
    if tag.get('src'): return tag.get('src')
    if tag.get('data-src') :return  tag.get('data-src')

def separateImg(tag):
    #print tag
    src= tag.get('src').encode('utf8')
    height= tag.get('height')#.encode('utf8')
    width= tag.get('width')#.encode('utf8')
    return (src,height,width)


def downloadAndSave(img,url,path,filename):
    print '******downloadAndSave******'
    if img[:3] != 'http':
        img=url +img
    print(img)
    print(path)
    try:
        imgWeb= urllib.URLopener()
        content= imgWeb.retrieve(img)
        f =  open(path +str(filename),'w')
        filename +=1
        buf= imgWeb.read()
        f.write(content)
        f.close()
        print '******downloadAndSave******'
    except:
        return filename
    return filename





i = int(sys.argv[1])
filename = 1
i=9
for filePath in glob.iglob('dataset/*'):
    print(filePath)
    if i <=0:
        print 'Reached limit established'
        break
    i-=1
    newFilePath = filePath.replace('dataset/','datasetFeatures/',1)
    if not os.path.exists(newFilePath):
            continue#if we didnt find any text, page is not eligible

    file = open(filePath,'r')
    #split the 3 important informations
    [cat,url,htmlDoc] = file.read().split('\n',2)
    soup = BeautifulSoup(htmlDoc, 'html.parser')#parse html
    relevantImgs = getMetaImg(soup)

    relevantImgs+= map(lambda x: separateImg(x),soup.select('img'))
    relevantImgs= filter( lambda x:x[0].find('googleads')<0,relevantImgs)


    #we create a folder for the images
    newFilePath = newFilePath + '/img/'
    if not os.path.exists(newFilePath):
        os.makedirs(newFilePath)
    for img in relevantImgs:
        filename =downloadAndSave(img[0],url,newFilePath,filename)
    print(i)
