import os,sys
import numpy as np
import pandas as pd 


DATASETPATH='/datasets/'
FILENAME= 'cleancatwebs.csv'
WEPATH='/pretrainedWE/'


if __name__ == '__main__':
	i=0
	cwd = os.getcwd()
	print('loading dataset')
	dataClean = list(pd.read_csv(cwd+DATASETPATH+FILENAME,sep='\t').iterrows())
	cleany = [y for _,(y,_) in dataClean]
	print('loading WE')
	WE = dict()
	WEname='lexVec58Bvectors300.txt'
	WEid='lexvec'
	if sys.argv[1] == 'glove':
		WEname='glove.840B.300d.txt' 
		WEid='glove'	
	with open(cwd + WEPATH + WEname,'r') as f:
		if WEname == 'lexVec58Bvectors300.txt':
			f.readline()
		for line in f:
			#print(line)
			#exit()
			line = line.split()
			word_spaces= (len(line)-300)
			i+=1
			if (i % 100000) == 0:
			#	break
				print(i)
			word = ' '.join(line[:word_spaces])
			WE[word]= np.array([np.float(i) for i in line[word_spaces:]])


	cleanx =  np.zeros((len(dataClean),300),np.float)#for each document and for each vector


	print('transforming dataset')
	for i,(_,text) in dataClean:
		print(i)
		#if i==200:
		#	break
		for word in text.split():
			if word in WE:
				cleanx[i]= np.array(list(map(sum,zip(cleanx[i],WE[word]))))

	cleanx=np.array([' '.join(list(map(str,x))) for x in cleanx])
	dataWE = [ '\t'.join([y,x]) for (y,x) in zip(cleany,cleanx)]
	frow= ['CAT\tWE']

	with open(cwd + DATASETPATH+ FILENAME.replace('clean',WEid),'w') as f:
		f.write('\n'.join(frow + dataWE))


