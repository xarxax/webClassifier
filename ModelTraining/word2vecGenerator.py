import glob,os,sys,ast,gensim

def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total


print('Loading model')


model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

if not os.path.exists('word2vecDataset'):
    os.makedirs('word2vecDataset')

i = int(sys.argv[1])
total = i
pathContentVectors=[]
counter=0
for folderPath in glob.iglob('tokenizedDataset/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    counter+=1
    if os.path.exists(folderPath.replace('tokenizedDataset/','word2vecDataset/',1)):
        i+=1#effectively skip the iteration
        continue
    #print(folderPath)
    file = open(folderPath +'/text.txt','r')
    #urlfile= open(folderPath+'/url.txt')
    content = file.read()
    content =ast.literal_eval(content)
    vectors =[]
    #print([['This'] + list(model.get_vector('This'))])
    #print(len(model.wv.word_vec('hello')))
    #break
    for w in content:
        try:
            vectors+= [[w] + list(model.get_vector(w))]
        except:
            print('word \'' + str(w) + '\' not found in word2vec')
            pass
    if len(vectors) < 1:
        print('Skipping \"' + str(folderPath) + '\" due to no vectors.')
        continue
    #vectors = [model[w] for w in content]
    newFilePath = folderPath.replace('tokenizedDataset/','word2vecDataset/',1)
    if not os.path.exists(newFilePath):
        os.makedirs(newFilePath)
    with open(newFilePath+'/text.txt', 'w') as f:
        vectors = [i[1:] for i in vectors]
        vectors = [[float(i) for i in j] for j in vectors]
        vectors = [sumColumn(vectors,i)for i in range(0,len(vectors[0]))]
        f.write(str(vectors))
    #print(str(vectors))


print('booya')
