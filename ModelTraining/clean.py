
import glob,os,sys,re,itertools
from nltk import word_tokenize


if not os.path.exists('tokenizedDataset'):
    os.makedirs('tokenizedDataset')


i = int(sys.argv[1])
total =i
counter=0
skipped =0
for folderPath in glob.iglob('datasetFeatures/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    print(folderPath)
    file = open(folderPath +'/text.txt','r')
    if os.path.exists(folderPath.replace('datasetFeatures/','tokenizedDataset/',1)):
        #i+=1#effectively skip the iteration
        print('Skipped.')
        continue
    #urlfile= open(folderPath+'/url.txt')
    content = file.read()
    print('File read')
    content =word_tokenize(content)
    print('Tokenize')
    #leave only alfanumerical symbols
    content = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in content]
    print('Substringed')
    content = [x for x in content if x != '' and len(x) > 1 and len(x) < 16]
    content = [re.findall(r'[a-zA-Z][A-Z]*[^A-Z]*',x) for x in content]
    content = sum(content,[])
    #content = [x.lower() for x in content]
    #print(content)

    newFilePath = folderPath.replace('datasetFeatures/','tokenizedDataset/',1)
    if not os.path.exists(newFilePath):
        counter+=1
        os.makedirs(newFilePath)
    #write text
    with open(newFilePath+'/text.txt', 'w') as f:
        f.write(str(content))
    #with open(newFilePath + '/url.txt','w') as f:
    #    f.write(urlfile.read())
    #we must also write the urls
print('Total websites:' + str(total-i) )
print(str(counter) + ' documents generated' )
