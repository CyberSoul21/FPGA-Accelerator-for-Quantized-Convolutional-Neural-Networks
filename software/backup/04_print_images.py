import matplotlib as mpl


import matplotlib.pyplot as plt
import numpy as np
#np.set_printoptions(threshold=sys.maxsize) # Printing all the weights

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3';                  # TF debug messages
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed

import sys
import tensorflow as tf
from tensorflow import keras

from ctypes import *
from mes_fonctions import *


lst = [3,5,1,18,4,8,11,17,84,7];
# Load MNIST data set 
mnist = keras.datasets.mnist;
(train_images, train_labels), (test_images, test_labels) = mnist.load_data();

img_test = test_images[7];
print(test_images[5]);
img_test = np.asarray(img_test);                           # Convertir données à tableau numpy


# Imprimer quelques images
fig = plt.figure(figsize=(3,3)); 
plt.imshow(img_test, cmap="gray", interpolation=None);
plt.title(r"$~5~$");
plt.tight_layout();
plt.show();
print(img_test);

print(" \n ");
print("************************************** ");
print(" Quantization de l'image               ");
print("************************************** ");
scale = 0.04896376;  zero_point = -6;
img_test = quant_np(img_test, scale, zero_point, verbose=1);
print(img_test);
#sys.exit(0); 

'''
img_lst = [];
for x in img_test:
	print('[',end=" ");
	for y in x:
		print(str(y)+',',end=" ");		 
	print('],')	
'''

img_lst = [];
for x in img_test:
	for y in x:
		print(str(int(y))+',',end=" ");		 
	

