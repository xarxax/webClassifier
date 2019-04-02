import sys,os,glob


i = int(sys.argv[1])
inputDataset = str(sys.argv[2])
outputDataset = 'normalized'+inputDataset

if not os.path.exists(outputDataset):
    os.makedirs(outputDataset)

maxValue = 0.
minValue = 0.

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
    pathWEfile += [['normalized'+folderPath, numbers]]

#print(pathWEfile[0])
#print(max(pathWEfile[0]))

for _,numbers in pathWEfile:
    for number in numbers:
        if maxValue< number:
            maxValue=number
        if minValue> number:
            minValue=number
print(minValue)
print(maxValue)

for i,_ in enumerate(pathWEfile):
    #print(pathWEfile[i])
    for j,_ in enumerate(pathWEfile[i][1]):
        #print(pathWEfile[i][1])
        if pathWEfile[i][1][j] < 0.:
            #print('boop')
            pathWEfile[i][1][j] /= -minValue
        if pathWEfile[i][1][j]>0.:
            #print('beep')
            pathWEfile[i][1][j]/= maxValue
        pathWEfile[i][1][j] = str(pathWEfile[i][1][j])

#print(pathWEfile[0][1])

#print(max(pathWEfile[0][1]))

for folderPath,numbers in pathWEfile:
    with open(folderPath, 'w') as f:
        f.write(' '.join(numbers))
