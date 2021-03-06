# -*- coding: utf-8 -*-
"""Clasificador.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lAX0tTEWhvgFVtNbZjUf9PSADU4uez5k
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import math
import matplotlib.image as mpimg
import numpy as np
dataTrain = "/content/drive/My Drive/SIGNED-LANGUAGE/imagenes"
dataValidation= "/content/drive/My Drive/SIGNED-LANGUAGE/imagenes"

directory_train = os.path.join(dataTrain, 'Train')
directory_validation = os.path.join(dataValidation, 'Validation')

"""Datos Entrenamiento

"""

def get_data(list_data, directory):
    arr = []
    for caracter_ima in list_data :
      nombre_caracter = caracter_ima
      #print(nombre_caracter)
      arr.append(mpimg.imread(directory_train+"/"+nombre_caracter))

    arr=np.array(arr)
    print(arr.shape)
    return arr

list_train = os.listdir(directory_train) # dir is your directory path
number_files = len(list_train)
train_arr= get_data(list_train, directory_train)
train_arr= train_arr.reshape(7290,64,64,1) #Especificar nuevo tamaño de la matriz, el 1 significa volverle a especificar que las imagenes son de un solo canal.

print(train_arr)

Letters=[ 0, 1 , 2 ,3, 4, 5 , 6, 7 , 8 , 9 , 10 , 11, 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26]
size=7290/len(Letters)
labels_t=[]
for i in range(7290):
  aux=math.floor(i/size)
  labels_t.append(Letters[aux])

labels_t= np.array(labels_t)
labels_t=labels_t.reshape(7290,1)

labels_t.shape
print(labels_t)

"""Datos Validación

"""

def get_dataV(list_data, directory):
    arr = []
    for caracter_ima in list_data :
      nombre_caracter = caracter_ima
      #print(nombre_caracter)
      arr.append(mpimg.imread(directory_validation+"/"+nombre_caracter))

    arr=np.array(arr)
    print(arr.shape)
    return arr

list_v = os.listdir(directory_validation) # dir is your directory path
number_filesV = len(list_v)
valid_arr= get_dataV(list_v, directory_validation)
valid_arr= valid_arr.reshape(2700,64,64,1)

LettersV=[ 0, 1 , 2 ,3, 4, 5 , 6, 7 , 8 , 9 , 10 , 11, 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26]
sizeV=2700/len(LettersV)
labels_v=[]
for i in range(2700):
  aux=math.floor(i/sizeV)
  labels_v.append(LettersV[aux])

labels_v= np.array(labels_v)
labels_v=labels_v.reshape(2700,1)

labels_v.shape
print(labels_v)
#categories = Y.shape[1] //Justo esta es laparte que no entiendo

"""Creación de la Red Neuronal

"""

import sys
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation, BatchNormalization
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D

epochs= 100      #Número de veces a iterar sobre todo el set de datos en el entrenamiento 
batch_size= 100        #Número de imagénes a procesar en cada uno de los pasos  
steps= 300       #Número de veces que se va a procesar la información por cada época
steps_validation= 100
filtersConv1= 16
filtersConv2= 32 
filtersConv3= 64
filtersConv4=128
size_filter1= (5,5)
size_filter2= (5,5)
size_filter3= (5,5)
classes= 2
lr= 0.005              #Learning rate

optimizer = tf.keras.optimizers.Adam(lr = 0.001, beta_1 = 0.9, beta_2 = 0.999)

#Creación de la red Neuronal

import tensorflow as tf

from tensorflow import keras
#from keras.models import Sequential # to create a cnn model
#from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
#from keras.optimizers import RMSprop,Adam
#from keras.preprocessing.image import ImageDataGenerator
#from keras.callbacks import ReduceLROnPlateau

cnn= Sequential()

cnn.add(Convolution2D(64, kernel_size=(3,3), activation = 'relu', input_shape=(64,64 ,1) ))
cnn.add(MaxPooling2D(pool_size = (2, 2)))

cnn.add(Convolution2D(64, kernel_size = (3, 3), activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (2, 2)))

cnn.add(Convolution2D(64, kernel_size = (3, 3), activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (2, 2)))

cnn.add(Flatten())
cnn.add(Dense(128, activation = 'relu'))
cnn.add(Dropout(0.20))
cnn.add(Dense(27, activation='softmax'))     #Tercera capa fully conected con funcion de activación softmax

cnn.compile(loss= 'sparse_categorical_crossentropy', optimizer= optimizer)
, metrics=['accuracy'])



cnn.summary()


#Agregar capa de normalización// antes de los maxpooling

cnn.fit(train_arr, labels_t , epochs=epochs, batch_size=batch_size, validation_split= 0.3)



test_loss, test_acc= cnn.evaluate(valid_arr,labels_v)
print(test_acc)