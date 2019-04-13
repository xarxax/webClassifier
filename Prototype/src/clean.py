
import glob,os,sys,re,itertools
from nltk import word_tokenize


if not os.path.exists('tempfiles/tokenizedText/'):
    os.makedirs('tempfiles/tokenizedText/')



for filePath in glob.iglob('tempfiles/rawText/*'):
    print(filePath)
    file = open(filePath,'r')
    content = file.read()
    content =word_tokenize(content)
    #leave only alfanumerical symbols
    content = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in content]
    content = [x for x in content if x != '' and len(x) > 1 and len(x) < 16]
    content = [re.findall(r'[a-zA-Z][A-Z]*[^A-Z]*',x) for x in content]
    content = sum(content,[])
    #print(content)

    newFilePath = filePath.replace('rawText/','tokenizedText/',1)
    #write text
    with open(newFilePath, 'w') as f:
        for word in content:
            f.write(str(word) + ' ')

