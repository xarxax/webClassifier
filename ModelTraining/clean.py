
import glob,os,sys,re,itertools
from nltk import word_tokenize


if not os.path.exists('tokenizedDataset'):
    os.makedirs('tokenizedDataset')


i = int(sys.argv[1])

for folderPath in glob.iglob('datasetFeatures/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    print(folderPath)
    file = open(folderPath +'/text.txt','r')
    urlfile= open(folderPath+'/url.txt')
    content = file.read()
    content =word_tokenize(content)
    #leave only alfanumerical symbols
    content = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in content]
    content = [x for x in content if x != '' and len(x) > 1 and len(x) < 16]
    content = [re.findall(r'[a-zA-Z][A-Z]*[^A-Z]*',x) for x in content]
    content = sum(content,[])
    content = [x.lower() for x in content]
    #print(content)

    newFilePath = folderPath.replace('datasetFeatures/','tokenizedDataset/',1)
    if not os.path.exists(newFilePath):
        os.makedirs(newFilePath)
    #write text
    with open(newFilePath+'/text.txt', 'w') as f:
        f.write(str(content))
    with open(newFilePath + '/url.txt','w') as f:
        f.write(urlfile.read())
    #we must also write the urls
