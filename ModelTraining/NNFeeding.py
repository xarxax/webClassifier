import ast,sys,glob,numpy,os
from keras.models import Sequential,load_model
from keras.layers import Dense
from collections import Counter
from keras.utils import plot_model
import matplotlib.pyplot as plt
from keras import backend as K



def f1(y_true, y_pred):
    def recall(y_true, y_pred):
        """Recall metric.

        Only computes a batch-wise average of recall.

        Computes the recall, a metric for multi-label classification of
        how many relevant items are selected.
        """
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

    def precision(y_true, y_pred):
        """Precision metric.

        Only computes a batch-wise average of precision.

        Computes the precision, a metric for multi-label classification of
        how many selected items are relevant.
        """
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision
    precision = precision(y_true, y_pred)
    recall = recall(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))



i = int(sys.argv[1])
inputDataset = str(sys.argv[2])
layers = int(sys.argv[3])
width = int(sys.argv[4])
epochs = int(sys.argv[5])

print('loading all the documents')

documents = []
categories = []
for folderPath in glob.iglob(inputDataset + '/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    #print(folderPath)
    file = open(folderPath ,'r')
    word_representation = file.read().split()
    if word_representation is '':
        print("Empty document, skipping.")
        i+=1
        continue
    #urlfile= open(folderPath+'/url.txt')
    #print(folderPath)
    if len(word_representation) == 0:
        print('empty document')
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

#print(categories)

print('loaded all the documents')
print(Counter(categories))

all_categories = ['Arts' ,'Business','Computers','Games','Health','Home','News','Recreation'
,'Reference','Science','Shopping','Society','Sports']

print(all_categories)


if not os.path.exists('models'):
    os.makedirs('models')

cur = categories[0]
#print(list(map( lambda x: float(x==cur),all_categories )))
categories = [list(map( lambda x: float(x==i),all_categories )) for i in categories]
#print(categories)
#print(len(documents[0]))
#x_train =[numpy.array(i) for i in documents]
#print(categories)
x_train =numpy.array(documents)
#print(x_train[0].shape)
y_train=numpy.array(categories)
#print(y_train)

#exit()


print('NN training all the documents')

model = Sequential()
model.add(Dense(units=width, activation='relu', input_dim=300))
for _ in range(layers):
    model.add(Dense(units=width, activation='relu'))
model.add(Dense(units=13, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['acc'])
print('Training the model.')
history = model.fit(x_train, y_train,validation_split=0.25, epochs=epochs, batch_size=32)
model.save( 'models/' + inputDataset + '.h5')  # creates a HDF5 file 'my_model.h5'


plot_model(model, to_file=  'models/' + inputDataset + '.png')

metric = 'acc' 

# Plot training & validation accuracy values
plt.plot(history.history[metric])
plt.plot(history.history['val_' +metric])
plt.title('Model '+metric)
plt.ylabel(metric)
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
#plt.show()
plt.savefig( 'models/' + inputDataset + metric +'.png')



# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
#plt.show()
plt.savefig( 'models/' + inputDataset + 'Loss.png')
