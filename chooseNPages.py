import sys
from random import randint
currWebs = int(sys.argv[1])
N = int(sys.argv[3])

print(currWebs)
print(N)

file = open('catAndUrl.txt','r')
outfile=open('catAndUrlChosen.txt','wr')



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
