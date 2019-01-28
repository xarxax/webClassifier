import glob,os,sys
from bs4 import BeautifulSoup

# gets property property from the soup's meta


def getMetaContent(soup, property):
    cssQuery = 'meta ["property"="og:' + property + '"]'
    content = soup.select(cssQuery)
    #print(content)
    if len(content) > 0:
        return content[0].get('content')#.encode('utf8')
    return ''

# extracts all metas information from the soup'
# tags obtained from http://ogp.me/


def addMetas(soup, urls):
    #title= soup.select('meta ["property"="og:title"]')[0].get('content')
    urls += [getMetaContent(soup, 'url')]
    urls += [getMetaContent(soup, 'image')]
    urls += [getMetaContent(soup, 'image:secure_url')]
    urls += [getMetaContent(soup, 'video')]
    urls += [getMetaContent(soup, 'video:secure_url')]
    urls += [getMetaContent(soup, 'video')]
    urls += [getMetaContent(soup, 'video')]

    return urls


i = int(sys.argv[1])

for filePath in glob.iglob('dataset/*'):
    if i <= 0:
        print('Reached limit established')
        break
    i -= 1
    print(filePath)

    file = open(filePath, 'r')
    # split the 3 important informations
    try:
        [cat,url,htmlDoc] = file.read().split('\n',2)
    except:
        print('Page containing non utf8 characters, will be skipped')
        continue
    soup = BeautifulSoup(htmlDoc, 'html.parser')  # parse html
    relevantUrls = addMetas(soup, [url])

    # links will not be included in the encode
    # mainly contain  urls for styles, fonts
    #print 'links:'
    #print map(lambda x: x.get('href').encode('utf8'),soup.select('link[href]'))
    # obtain all urls from a's in the page
    relevantUrls += map(lambda x: x.get('href'),#.encode('utf8'),
                        soup.select('a[href]'))#.decode('utf-8')

    #relevantUrls = map(lambda x:x.decode('utf-8'),relevantUrls)
    relevantUrls = list(map(lambda x: x.replace(url,''),relevantUrls))  # unify all pages in domain

    relevantUrls[0] = url  # we want the original url still
    #print(relevantUrls)

    # remove first and last / if there are
    relevantUrls = map(lambda x: x[1:] if len(
        x) > 0 and x[0] == '/' else x, relevantUrls)
    relevantUrls = map(lambda x: x[:-1] if len(x)
                       > 0 and x[-1] == '/' else x, relevantUrls)
    # print(relevantUrls)

    # remove these
    # they were originally the page url in the html
    relevantUrls = filter(lambda x: x != '#', relevantUrls)
    relevantUrls = list(filter(lambda x: x != '', relevantUrls))
    # remove duplicates
    relevantUrls = [ii for n, ii in enumerate(
        relevantUrls) if ii not in relevantUrls[:n]]
    # saving urls now
    # print(relevantUrls)

    # we open the folder at dataset features
    newFilePath = filePath.replace('dataset/', 'datasetFeatures/', 1)
    if not os.path.exists(newFilePath):
        continue  # if we didnt find any text, page is not eligible
    # write text
    with open(newFilePath + '/url.txt', 'w') as f:
        for url in relevantUrls:
            f.write(url + '\n')

