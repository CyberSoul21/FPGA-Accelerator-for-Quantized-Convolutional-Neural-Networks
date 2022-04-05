#/**************************************************************************//**
# * @file 00_cnn_mnist_model.py
# *
# *
# * @author:
# * Wilson Javier Almario Rodriguez.
# *
# * @date 06/29/2021
# *
# *
# *****************************************************************************/
#/******************************************************************************
# * Copyright (C) 2021 by Wilson J. Almario R.
# *****************************************************************************/

import matplotlib.pyplot as plt 
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'; # TF debug messages
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed

import sys
np.set_printoptions(threshold=sys.maxsize) # Printing all the weights
import tempfile
import tensorflow as tf
from   tensorflow import keras


#Load data from mnist
mnist = keras.datasets.mnist;
(train_images, train_labels), (test_images, test_labels) = mnist.load_data();
test_images = test_images[0:1000];
test_labels = test_labels[0:1000];

#print(test_images[0]); print(test_images[0].shape); print( type(test_images[0]) ); 
#sys.exit(0);                                              # Finish execution

# Normalize the input image so that each pixel value is between 0 to 1
#train_images = train_images / 255.0;
#test_images  = test_images  / 255.0;


print(" \n ");
print("************************************** ");
print(" Model                                 ");
print("************************************** ");
#Setting up CNN architecture  
model = keras.Sequential( [
  keras.layers.InputLayer( input_shape=(28, 28) ),
  keras.layers.Reshape( target_shape=(28, 28, 1) ),
  keras.layers.Conv2D( filters=3, kernel_size=(3, 3), activation="relu" ),
  #keras.layers.Conv2D( filters=12, kernel_size=(3, 3), activation="relu" ),
  #keras.layers.Conv2D( filters=2, kernel_size=(3, 3), activation="relu" ),
  keras.layers.MaxPooling2D( pool_size=(2, 2) ),
  keras.layers.Flatten( ),
  keras.layers.Dense( 10 )   ] );

# Train the digit classification model
model.compile( optimizer="adam", 
               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
               metrics=["accuracy"] ) ; 
model.summary();

model.fit( train_images, train_labels, epochs=1, validation_split=0.1 );


# Accuracy CNN model
_, model_accuracy = model.evaluate( test_images, test_labels, verbose=0 );
print("Accuracy: ", model_accuracy);

# Save models in  H5 
#------------------------------
model.save("models/cnn_1fil_mnist_fp.h5");                
#model.save("models/cnn_12fil_mnist_fp.h5");                
#model.save("models/cnn_3fil_mnist_fp.h5");
#model.save_weights("models/model_weights.h5");


print("                                      ");
print("**************************************");
print("*              Done!                 *");
print("**************************************");