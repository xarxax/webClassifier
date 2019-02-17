import glob,os,sys,ast


if not os.path.exists('gloveDataset'):
    os.makedirs('gloveDataset')


i = int(sys.argv[1])

for folderPath in glob.iglob('tokenizedDataset/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    print(folderPath)
    file = open(folderPath +'/text.txt','r')
    urlfile= open(folderPath+'/url.txt')
    content = file.read()
    content =ast.literal_eval(content)
    wordVectors = []
    with open("glove.840B.300d.txt") as infile:
        for line in infile:
            vector =line.split()
            word = vector[0]
            if vector[1] =='name@domain.com':
                del vector[1]

            if(len(vector) > 301):
                #print('weird shit happened')
                #print(vector)
                continue
            if word in content:
                wordVectors += [vector]
            #print(line.split())
            #print(len(line.split()))
            #break
    #print(wordVectors)
    #break
    newFilePath = folderPath.replace('tokenizedDataset/','gloveDataset/',1)
    if not os.path.exists(newFilePath):
        os.makedirs(newFilePath)
    #write text
    with open(newFilePath+'/text.txt', 'w') as f:
        f.write(str(wordVectors))
    with open(newFilePath + '/url.txt','w') as f:
        f.write(urlfile.read())
    #we must also write the urls
