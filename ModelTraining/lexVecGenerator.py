import glob,os,sys,ast


if not os.path.exists('lexVecDataset'):
    os.makedirs('lexVecDataset')


i = int(sys.argv[1])
total = i
pathContentVectors=[]
counter=0
for folderPath in glob.iglob('tokenizedDataset/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1

    counter +=1
    if os.path.exists(folderPath.replace('tokenizedDataset/','lexVecDataset/',1)):
        i+=1#effectively skip the iteration
        continue
    print(folderPath)
    file = open(folderPath +'/text.txt','r')
    #urlfile= open(folderPath+'/url.txt')
    content = file.read()
    content =ast.literal_eval(content)
    pathContentVectors+=[[folderPath,content,[]]]
    if (total-i)%5000==0:#more than 10k files make python just stop when opening the big file
        #read through the glove txt and save the documents
        #glove represented
        print('Reading the Common Crawl file. Number of documents processed:')
        print(total -i)
        with open("lexVec58Bvectors300.txt") as infile:
            #print('begin getting words')

            for line in infile:
                vector =line.split()
                #word = vector[0]
                #skip weird cases
                print('word:'+str(vector[0]))
                if vector[1] =='name@domain.com':
                    del vector[1]
                if(len(vector) > 301):
                    continue
                #otherwise we turn the 1k documents to wordvecs
                #print(pathContentVectors[1])
                #print('adding content:')
                for _,content,vectors in pathContentVectors:
                    #print('Adding:'+str(word))
                    if vector[0] in content:
                        vectors += [vector]
        #now we save all the wordVectors
        print('Finished reading the file. Creating now new files')
        for path,content,vectors in pathContentVectors:
            newFilePath = path.replace('tokenizedDataset/','lexVecDataset/',1)
            if not os.path.exists(newFilePath):
                os.makedirs(newFilePath)
            with open(newFilePath+'/text.txt', 'w') as f:
                f.write(str(vectors))
        #now we remove the documents already processed
        #should probably close files
        pathContentVectors=[]
###
print('Final write. Length of files to be written:')
print(len(pathContentVectors))
print('Reading the Common Crawl file. Number of documents processed:')
print(total -i)
with open("lexVec58Bvectors300.txt") as infile:
    for line in infile:
        vector =line.split()
        #word = vector[0]
        #skip weird cases
        print('word:'+str(vector[0]))

        if vector[1] =='name@domain.com':
            del vector[1]
        if(len(vector) > 301):
            continue
        #otherwise we turn the 1k documents to wordvecs
        #print(len(pathContentVectors))
        #print(pathContentVectors[1])
        for _,content,vectors in pathContentVectors:
            if vector[0] in content:
                vectors += [vector]
#now we save all the wordVectors
print('Finished reading the file. Creating now new files')
for path,content,vectors in pathContentVectors:
    newFilePath = path.replace('tokenizedDataset/','lexVecDataset/',1)
    if not os.path.exists(newFilePath):
        os.makedirs(newFilePath)
    with open(newFilePath+'/text.txt', 'w') as f:
        f.write(str(vectors))
