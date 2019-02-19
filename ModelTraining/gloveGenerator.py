import glob,os,sys,ast


if not os.path.exists('gloveDataset'):
    os.makedirs('gloveDataset')


i = int(sys.argv[1])
total = i
pathContentVectors=[]
for folderPath in glob.iglob('tokenizedDataset/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    print(folderPath)
    file = open(folderPath +'/text.txt','r')
    #urlfile= open(folderPath+'/url.txt')
    content = file.read()
    content =ast.literal_eval(content)
    pathContentVectors+=[[folderPath,content,[]]]
    if i%5000==0:
        #read through the glove txt and save the documents
        #glove represented
        print('Reading the Common Crawl file. Number of documents processed:')
        print(total -i)
        with open("glove.840B.300d.txt") as infile:
            for line in infile:
                vector =line.split()
                word = vector[0]
                #skip weird cases
                if vector[1] =='name@domain.com':
                    del vector[1]
                if(len(vector) > 301):
                    continue
                #otherwise we turn the 1k documents to wordvecs
                #print(len(pathContentVectors))
                #print(pathContentVectors[1])

                for _,content,vectors in pathContentVectors:
                    if word in content:
                        vectors += [vector]
        #now we save all the wordVectors
        print('Finished reading the file. Creating now new files')
        for path,content,vectors in pathContentVectors:
            newFilePath = path.replace('tokenizedDataset/','gloveDataset/',1)
            if not os.path.exists(newFilePath):
                os.makedirs(newFilePath)
            with open(newFilePath+'/text.txt', 'w') as f:
                f.write(str(vectors))
        #now we remove the documents already processed
        pathContentVectors=[]
