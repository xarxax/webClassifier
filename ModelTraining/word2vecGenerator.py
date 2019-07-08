import glob,os,sys,ast
import numpy as np
import pandas as pd 
import gensim

DATASETPATH='/datasets/'
FILENAME= 'cleancatwebs.csv'
WEPATH='pretrainedWE/'


def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total

if __name__ == '__main__':
	cwd = os.getcwd()
	print('Loading model')
	model = gensim.models.KeyedVectors.load_word2vec_format(WEPATH + 'GoogleNews-vectors-negative300.bin', binary=True)
	print('Loading dataset')
	dataClean = list(pd.read_csv(cwd+DATASETPATH+FILENAME,sep='\t').iterrows())
	cleany = [y for _,(y,_) in dataClean]
	cleanx =  np.zeros((len(dataClean),300),np.float)#for each document and for each vector

	print('transforming dataset')
	for i,(_,text) in dataClean:
		print(i)
		for word in text.split():
			try:    #vectors+= [[w] + list(model.get_vector(w))]
				cleanx[i]= np.array(list(map(sum,zip(cleanx[i],model.get_vector(word)))))
			except:
		        #print('word \'' + str(w) + '\' not found in word2vec'
				pass


	cleanx=np.array([' '.join(list(map(str,x))) for x in cleanx])
	dataWE = [ '\t'.join([y,x]) for (y,x) in zip(cleany,cleanx)]
	frow= ['CAT\tWE']

	with open(cwd + DATASETPATH+ FILENAME.replace('clean','word2vec'),'w') as f:
		f.write('\n'.join(frow + dataWE))

	exit()

	for folderPath in glob.iglob('tokenizedDataset/*'):
		if i <=0:
		    print('Reached limit established')
		    break
		i-=1
		counter+=1
		if os.path.exists(folderPath.replace('tokenizedDataset/','word2vecDataset/',1)):
		    i+=1#effectively skip the iteration
		    continue
		print(folderPath)
		file = open(folderPath +'/text.txt','r')
		#urlfile= open(folderPath+'/url.txt')
		content = file.read().split()
		#content =ast.literal_eval(content)
		vectors =[]
		#print([['This'] + list(model.get_vector('This'))])
		#print(len(model.wv.word_vec('hello')))
		#break
		for w in content:
		    try:
		        vectors+= [[w] + list(model.get_vector(w))]
		    except:
		        #print('word \'' + str(w) + '\' not found in word2vec')
		        pass
		if len(vectors) < 1:
		    #print('Skipping \"' + str(folderPath) + '\" due to no vectors.')
		    continue
		#vectors = [model[w] for w in content]
		newFilePath = folderPath.replace('tokenizedDataset/','word2vecDataset/',1)
		#if not os.path.exists(newFilePath):
		#    os.makedirs(newFilePath)
		with open(newFilePath, 'w') as f:
		    vectors = [i[1:] for i in vectors]
		    vectors = [[float(i) for i in j] for j in vectors]
		    vectors = [str(sumColumn(vectors,i))for i in range(0,len(vectors[0]))]
		    #print(' '.join(vectors))
		    #exit()
		    f.write(' '.join(vectors))
		#print(str(vectors))


	#print('booya')
