
import glob,os,sys,re,itertools,random
import nltk
import pandas as pd 
from math import isnan



DATAFOLDER= '/datasets/'
FILENAME= 'catwebs.csv'
STOPWORDS = set(nltk.corpus.stopwords.words('english'))
STOPWORDS.add("n\'t")




cwd = os.getcwd()
data = pd.read_csv(cwd+DATAFOLDER + FILENAME,sep='\t')
cleanData=[]

for _,(cat,text) in data.iterrows():
	#print(cat)	
	if type(text) != type('pancake'):
		continue
	#exit()
	text =' '.join([w for w in nltk.word_tokenize(text.lower()) if w not in STOPWORDS])
    #content = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in content]
    #content = [x for x in content if x != '' and len(x) > 1 and len(x) < 16]
    #content = [re.findall(r'[a-zA-Z][A-Z]*[^A-Z]*',x) for x in content]
	if text == '':
		print('skipped nan')
		continue
	
	cleanData+=[cat + '\t'+ text]


frow= ['CAT\tTEXT']
with open(cwd + DATAFOLDER+ 'clean'+FILENAME,'w') as f:
	f.write('\n'.join(frow + cleanData))

