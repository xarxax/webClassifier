import glob,os,sys,ast,gc

if not os.path.exists('gloveDataset'):
    os.makedirs('gloveDataset')


def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total

print('Reading WE')
WE = ''
WEvectors=[]
with open("glove.840B.300d.txt") as infile:
    breakcount=0
    for line in infile:
        if len(line.split()[0])< 16:
            WEvectors += [line.split()]
            breakcount+=1
            if (breakcount%10000)==0:
                print('Flushing memory')
                breakcount=0
                gc.collect()
        #print(WEvectors)
        #break
print('File loaded and with vectors')

exit()
i = int(sys.argv[1])
total = i
pathContentVectors=[]
counter = 0
for folderPath in glob.iglob('tokenizedDataset/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1

    #print(folderPath + '\n' + 'folder number:' +  str(counter))
    counter +=1
    if os.path.exists(folderPath.replace('tokenizedDataset/','gloveDataset/',1)):
        i+=1#effectively skip the iteration
        continue
    file = open(folderPath +'/text.txt','r')
    #urlfile= open(folderPath+'/url.txt')
    content = file.read()
    content =ast.literal_eval(content)
    pathContentVectors+=[[folderPath,content,[]]]
    if (total-i)%10000==0:#more than 10k files make python just stop when opening the big file
        #read through the glove txt and save the documents
        #glove represented
        print('Length of files to be written:')
        print(len(pathContentVectors))
        print('Reading the Common Crawl file. Number of documents processed:')
        print(total -i)

        with open("glove.840B.300d.txt") as infile:
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
                #print(len(pathContentVectors))
                #print(pathContentVectors[1])
                #print('adding content:')
                for _,content,vectors in pathContentVectors:
                    #print('Adding:'+str(word))
                    if vector[0] in content:
                        vectors += [vector]
        #now we save all the wordVectors
        print('Finished reading the file. Creating now new files')
        for path,content,vectors in pathContentVectors:
            if len(vectors) < 1:
                print('Skipping \"' + str(path) + '\" due to no vectors.')
                continue
            #print(len(vectors[0]))
            #print(vectors[0])
            newFilePath = path.replace('tokenizedDataset/','gloveDataset/',1)
            if not os.path.exists(newFilePath):
                os.makedirs(newFilePath)
            with open(newFilePath+'/text.txt', 'w') as f:
                vectors = [i[1:] for i in vectors]
                vectors = [[float(i) for i in j] for j in vectors]
                vectors = [sumColumn(vectors,i)for i in range(0,len(vectors[0]))]
                f.write(str(vectors))
        #now we remove the documents already processed
        #should probably close files
        pathContentVectors=[]
###

print('Final write. Length of files to be written:')
print(len(pathContentVectors))
print('Reading the Common Crawl file. Number of documents processed:')
print(total -i)
with open("glove.840B.300d.txt") as infile:
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
                #print(len(vector))
                vectors += [vector]
#now we save all the wordVectors
print('Finished reading the file. Creating now new files')
for path,content,vectors in pathContentVectors:
    if len(vectors) < 1:
        print('Skipping \"' + str(path) + '\" due to no vectors.')
        continue
    #print(len(vectors[0]))
    #print(vectors[0])
    newFilePath = path.replace('tokenizedDataset/','gloveDataset/',1)
    if not os.path.exists(newFilePath):
        os.makedirs(newFilePath)
    with open(newFilePath+'/text.txt', 'w') as f:
        vectors = [i[1:] for i in vectors]
        vectors = [[float(i) for i in j] for j in vectors]
        #print(range(0,len(vectors[0])))
        vectors = [sumColumn(vectors,i)for i in range(0,len(vectors[0]))]
        print(len(vectors))

        f.write(str(vectors))
