import sys,os,glob,math


i = int(sys.argv[1])
inputDataset = str(sys.argv[2])
outputDataset = 'unitized'+inputDataset

if not os.path.exists(outputDataset):
    os.makedirs(outputDataset)

def unitize(orig):
    modul=0.
    #print(orig)
    for i in orig:
        modul+= i**2
    modul=math.sqrt(modul)
    modified=[]
    for i in orig:
        if i==0.:
            modified+=['0.']
        else :
            modified+=[str(i/modul)]
    return modified


pathWEfile = []
for folderPath in glob.iglob(inputDataset + '/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    print(folderPath)
    file = open(folderPath ,'r')
    numbers = [float(i) for i in file.read().split()]
    file.close()
    pathWEfile += [['unitized'+folderPath, numbers]]


for i,_ in enumerate(pathWEfile):
        pathWEfile[i][1] =unitize(pathWEfile[i][1])

#print('beeep')
#print(pathWEfile[0][1])

#print(max(pathWEfile[0][1]))

for folderPath,numbers in pathWEfile:
    with open(folderPath, 'w') as f:
        f.write(' '.join(numbers))
