import ast,sys,glob,numpy,os,gc
from keras.models import Sequential,load_model
from keras.layers import Dense
from keras.layers import Dropout
from collections import Counter
from keras.utils import plot_model
import matplotlib.pyplot as plt
from keras import backend as K
from keras.regularizers import l2
from keras import optimizers
from sklearn.model_selection import train_test_split



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
units = int(sys.argv[4])
epochs = int(sys.argv[5])
dropoutval = float(sys.argv[6])

documents = []
categories = []
for folderPath in glob.iglob(inputDataset + '/*'):
    if i <=0:
        print('Reached limit established')
        break
    i-=1
    if (i%10000) == 0:
        print(i)
    #print(folderPath)
    file = open(folderPath ,'r')
    word_representation = file.read().split()
    if word_representation is '':
        print("Empty document, skipping.")
        i+=1
        continue
    #print(folderPath)
    if len(word_representation) == 0:
        print('empty document')
        continue
    #word_representation = [i[1:] for i in word_representation]
    documents = documents + [word_representation]
    categories = categories + [folderPath.split('/')[1].split('_')[0]]

#print(categories)
print(Counter(categories))

all_categories = list(set(categories))

print(all_categories)
#

if not os.path.exists('models'):
    os.makedirs('models')

cur = categories[0]
#print(list(map( lambda x: float(x==cur),all_categories )))
categories = [list(map( lambda x: float(x==i),all_categories )) for i in categories]
#print(categories)
#print(len(documents[0]))
#x_train =[numpy.array(i) for i in documents]
#print(categories)
#x_train =numpy.array(documents)
#print(x_train[0].shape)
#y_train=numpy.array(categories)
#print(y_train)

x_train, x_test, y_train, y_test = train_test_split(documents, categories, test_size=0.1, shuffle= True)
x_train =numpy.array(x_train)
x_test=numpy.array(x_test)
y_train=numpy.array(y_train)
y_test=numpy.array(y_test)
print(y_train)
#exit()

def plotModel(model,history):
    plt.plot(history.history['f1'])
    plt.plot(history.history['val_f1'])
    plt.title('Model F1')
    plt.ylabel('F1')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')

    plt.savefig( 'models/' + inputDataset +'l' +str(layers) +'u'+str(units)+ 'e'+ str(epochs) +'F1.png')

    plt.clf()


    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.savefig( 'models/' + inputDataset + 'l' +str(layers) +'u'+str(units)+ 'e'+ str(epochs)+'Loss.png')
    plt.clf()

    #model.save( 'models/' + inputDataset +'l' +str(layers) +'u'+str(units)+ 'e'+ str(epochs)+ extra +'.h5')  # creates a HDF5 file 'my_model.h5'
    return 0


def createModelL2categ(l2value=0.001,lr=0.01):
    model = Sequential()
    model.add(Dense(units=units, activation='relu', input_dim=300))
    model.add(Dropout(0.3))
    for _ in range(layers):
        model.add(Dense(units=units, activation='relu',kernel_regularizer=l2(l2value)))
        model.add(Dropout(dropoutval))
    model.add(Dense(units=len(all_categories), activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizers.SGD(lr=lr),
                  metrics=[f1])
    print('Training the model.')
    history = model.fit(x_train, y_train,validation_split=0.10, epochs=epochs, batch_size=32)
    return model,history


from sklearn.metrics import classification_report
import numpy as np

curModelData = createModelL2categ(0.001,0.01)

plotModel(curModelData[0],curModelData[1])
y_true= np.argmax(y_test,axis=1)
y_pred = curModelData[0].predict_classes(x_test)
print(classification_report(y_true, y_pred))
with open('models/tables','a') as f:
	f.write(str(inputDataset +'l' +str(layers) +'u'+str(units)+ 'e'+ str(epochs) + '\n'))
	f.write(str(classification_report(y_true, y_pred)))


