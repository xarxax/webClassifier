import ast,sys,glob,numpy
from keras.models import Sequential
from keras.layers import Dense

def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total



i = int(sys.argv[1])

documents = []
categories = []
for folderPath in glob.iglob('gloveDataset/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    with open(folderPath +'/text.txt','r') as file:
        word_representation = ast.literal_eval(file.read())
    urlfile= open(folderPath+'/url.txt')
    print(folderPath)
    if len(word_representation) == 0:
        print('empty document')
        continue
    word_representation = [i[1:] for i in word_representation]
    word_representation = [[float(i) for i in j] for j in word_representation]
    wordCount= len(word_representation)
    vectors= len(word_representation[0])
    print('words:' + str(wordCount))
    print('vectors:' + str(vectors))
    #print(sumColumn(word_representation,0))
    word_representation = [sumColumn(word_representation,i)for i in range(0,vectors)]
    documents = documents + [word_representation]
    categories = categories + [folderPath.split('/')[1].split('_')[0]]

print(categories)

all_categories = ['Arts' ,'Business','Computers','Games','Health','Home','News','Recreation'
,'Reference','Science','Shopping','Society','Sports']
cur = categories[0]
#print(list(map( lambda x: float(x==cur),all_categories )))
categories = [list(map( lambda x: float(x==i),all_categories )) for i in categories]
#print(categories)
print(len(documents[0]))
#x_train =[numpy.array(i) for i in documents]
x_train =numpy.array(documents)
print(x_train[0].shape)
y_train=numpy.array(categories)
print(y_train)

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=300))
model.add(Dense(units=13, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=32)
