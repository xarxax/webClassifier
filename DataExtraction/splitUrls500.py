import sys,glob,os



file = open('catAndUrl.txt','r')

name= 'catAndUrl'
filenum=0


if not os.path.exists('urlSplit'):
    os.makedirs('urlSplit')

outfile = open('urlSplit/catAndUrl'+str(filenum) + '.txt','wr')
i=0
for i,line in enumerate(file):
    if i % 5000 == 0:
        outfile.close()
        outfile = open('urlSplit/catAndUrl'+str(filenum) + '.txt','wr')
        filenum = filenum+1
    outfile.write(line)
