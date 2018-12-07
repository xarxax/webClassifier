import sys,os
from random import randint
#print(sys.argv)
currWebs = int(sys.argv[1])
N = int(sys.argv[3])

print('Number total of webs: ' + str(currWebs))
print('Maximum to extract: ' + str(N))

file = open('catAndUrl.txt','r')
outfile=open('catAndUrlChosen.txt','wr')

#creates the folder for our next step
if not os.path.exists('dataset'):
    os.makedirs('dataset')

#if we are asked for more webs than we have we just put them all
if N >= currWebs:
    for line in file:
        print line.replace('\n','')
        outfile.write(line)
    print 'Chose all websites.'    
    sys.exit


#we choose which webs we will evaluate
chosenWebs =[]
for i in range(N):
    pos = randint(0,currWebs-1)
    chosenWebs += [pos]

i= 0
#we write only those that are in our set
#this does not guarantee we will have N
for line in file:
    if i in chosenWebs:
        outfile.write(line)
    i+= 1



