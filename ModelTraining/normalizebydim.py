import sys,os,glob


i = int(sys.argv[1])
inputDataset = str(sys.argv[2])
outputDataset = 'normalizedbyvec'+inputDataset

if not os.path.exists(outputDataset):
    os.makedirs(outputDataset)

maxValues = [0.]*300
minValues = [0.]*300

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
    pathWEfile += [['normalizedbyvec'+folderPath, numbers]]

#print(pathWEfile[0])
#print(max(pathWEfile[0]))

for _,numbers in pathWEfile:
    for j,number in enumerate(numbers):
        if maxValues[j]< number:
            maxValues[j]=number
        if minValues[j]> number:
            minValues[j]=number
#print(minValues)
#exit()

for i,_ in enumerate(pathWEfile):
    #print(pathWEfile[i])
    for j,_ in enumerate(pathWEfile[i][1]):
        #print(pathWEfile[i][1])
        if pathWEfile[i][1][j] < 0.:
            #print('boop')
            pathWEfile[i][1][j] /= -minValues[j]
        if pathWEfile[i][1][j]>0.:
            #print('beep')
            pathWEfile[i][1][j]/= maxValues[j]
        pathWEfile[i][1][j] = str(pathWEfile[i][1][j])

#print(pathWEfile[0][1])

#print(max(pathWEfile[0][1]))

for folderPath,numbers in pathWEfile:
    with open(folderPath, 'w') as f:
        f.write(' '.join(numbers))
