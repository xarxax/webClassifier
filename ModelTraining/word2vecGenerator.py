import glob,os,sys,ast,gensim

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

if not os.path.exists('word2vecDataset'):
    os.makedirs('word2vecDataset')

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
    #vectors = [model[w] for w in content]
    newFilePath = folderPath.replace('tokenizedDataset/','word2vecDataset/',1)
    if not os.path.exists(newFilePath):
        os.makedirs(newFilePath)
    with open(newFilePath+'/text.txt', 'w') as f:
        f.write(str(vectors))
    #print(str(vectors))


print('booya')
