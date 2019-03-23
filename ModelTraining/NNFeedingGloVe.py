import ast,sys,glob,numpy
from keras.models import Sequential,load_model
from keras.layers import Dense
from collections import Counter
from keras.utils import plot_model
import matplotlib.pyplot as plt

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
    print(folderPath)
    file = open(folderPath +'/text.txt','r')
    if file.read() is '':
        print("Empty document, skipping.")
        i+=1
        continue
    word_representation = ast.literal_eval(file.read())
    #urlfile= open(folderPath+'/url.txt')
    #print(folderPath)
    if len(word_representation) == 0:
        #print('empty document')
        continue
    #word_representation = [i[1:] for i in word_representation]
    #word_representation = [[float(i) for i in j] for j in word_representation]
    #wordCount= len(word_representation)
    #vectors= len(word_representation[0])
    #print('words:' + str(wordCount))
    #print('vectors:' + str(vectors))
    #print(sumColumn(word_representation,0))
    #word_representation = [sumColumn(word_representation,i)for i in range(0,vectors)]
    documents = documents + [word_representation]
    categories = categories + [folderPath.split('/')[1].split('_')[0]]

print(categories)
print(Counter(categories))

all_categories = ['Arts' ,'Business','Computers','Games','Health','Home','News','Recreation'
,'Reference','Science','Shopping','Society','Sports']
cur = categories[0]
#print(list(map( lambda x: float(x==cur),all_categories )))
categories = [list(map( lambda x: float(x==i),all_categories )) for i in categories]
#print(categories)
#print(len(documents[0]))
#x_train =[numpy.array(i) for i in documents]
x_train =numpy.array(documents)
#print(x_train[0].shape)
y_train=numpy.array(categories)
#print(y_train)

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=300))
model.add(Dense(units=13, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
print('Training the model.')
history = model.fit(x_train, y_train,validation_split=0.25, epochs=20, batch_size=32)
model.save('gloVe.h5')  # creates a HDF5 file 'my_model.h5'


plot_model(model, to_file='modelGloVe.png')


# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
