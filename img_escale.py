# -*- coding: utf-8 -*-
"""img_escale.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12-61rhcjbjaPqEH_EVBe2KDgkP6Inanu
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io
from skimage.transform import resize

from google.colab import drive
drive.mount('/content/drive')

#Ruta donde estan las imagenes que voy a cambiar de escala
data = ("/content/drive/My Drive/SIGNED-LANGUAGE/Dataset/Validation/")
#data = ("/content/drive/My Drive/SIGNED-LANGUAGE/Dataset/Train")

print(data+"/0")


#Imagen de prueba 
test_ima = mpimg.imread(data + "/Y/Letra_Y_325.png")

plotima = plt.imshow(test_ima)
print(test_ima.shape)# se puede ver que todas las imagenes estan en3 canales

#este es el cambio que se le va hacer a todas las imagenes 
newima = resize(test_ima, (64,64)).mean(axis=2)
#newima = test_ima
#io.imsave('Nfasdfa.png', arr = newima)
#print(newima.shape)


io.imshow(newima)
print(newima.shape)
#newima = plt.imshow(newima, cmap = plt.cm.Greys_r)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/C")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/C/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/D")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/D/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/E")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/E/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/F")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/F/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/I")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/I/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/K")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/K/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/L")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/L/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/M")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/M/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/N")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/N/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/O")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/O/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/P")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/P/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/Q")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/Q/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/R")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/R/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/T")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/T/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/U")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/U/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/V")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/V/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/W")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/W/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/X")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/X/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/Y")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/Y/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/0")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/0/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/1")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/1/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/2")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/2/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/3")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/3/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/4")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/4/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)

# Se construye estructura que recorre todos los archivos de la carpeta  a la que se estetratando
import os
os.chdir("/content/drive/My Drive/SIGNED-LANGUAGE/imgs/Validation")
print('Directorio en el que me encuentro',os.getcwd ())
lista_caracter = os.listdir (data+"/5")
print(lista_caracter)

for caracter_ima in lista_caracter :
  nombre_caracter = caracter_ima
  #print(nombre_caracter)
  caracter_ima = mpimg.imread(data + "/5/"+caracter_ima)#Esta es la imagen
  caracter_ima = resize(caracter_ima, (64,64)).mean(axis=2)
  io.imsave(nombre_caracter, arr = caracter_ima)
  #print(caracter_ima)
  #plotima = plt.imshow(caracter_ima)