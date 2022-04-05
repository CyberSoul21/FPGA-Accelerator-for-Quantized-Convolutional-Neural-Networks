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
import sys
import tempfile
import tensorflow as tf
from   tensorflow import keras

model = tf.keras.models.load_model("cnn_3fil_mnist_fp.h5");
model.summary();

print(" ");

for layer in model.layers:
	print( "--> Layer: ", layer ); 
	print( "--> Layer architecture: ", layer.get_config() ); 
	print( "--> Parameter of layer: ", layer.get_weights() );
	print(" ");

conv = model.layers[1].get_weights()
dense = model.layers[4].get_weights()

conv_w = conv[0]
conv_w0=[]
temp0=[]
conv_w1=[]
temp1=[]
conv_w2=[]
temp2=[]

for x in conv_w:
	for y in x:
		temp0.append(y[0][0])
		temp1.append(y[0][1])
		temp2.append(y[0][2])
	conv_w0.append(temp0)
	conv_w1.append(temp1)
	conv_w2.append(temp2)
	temp0=[]
	temp1=[]
	temp2=[]

print("**************************************");
print("**************************************");
print("conv_w0=")
print(conv_w0)
print("**************************************");
print("**************************************");
print("conv_w1=")
print(conv_w1)
print("**************************************");
print("**************************************");
print("conv_w2=")
print(conv_w2)
print("conv_bias=")
print(conv[1])


dense_w = dense[0]
dense_w0 = []
dense_w1 = []
dense_w2 = []
dense_w3 = []
dense_w4 = []
dense_w5 = []
dense_w6 = []
dense_w7 = []
dense_w8 = []
dense_w9 = []
for x in dense_w:
	dense_w0.append(x[0])
	dense_w1.append(x[1])
	dense_w2.append(x[2])
	dense_w3.append(x[3])
	dense_w4.append(x[4])
	dense_w5.append(x[5])
	dense_w6.append(x[6])
	dense_w7.append(x[7])
	dense_w8.append(x[8])
	dense_w9.append(x[9])

print("**************************************");
print("**************************************");
print("dense_w0=")
print(dense_w0)
print("**************************************");
print("**************************************");
print("dense_w1=")
print(dense_w1)
print("**************************************");
print("**************************************");
print("dense_w2=")
print(dense_w2)
print("**************************************");
print("**************************************");
print("dense_w3=")
print(dense_w3)
print("**************************************");
print("**************************************");
print("dense_w4=")
print(dense_w4)
print("**************************************");
print("**************************************");
print("dense_w5=")
print(dense_w5)
print("**************************************");
print("**************************************");
print("dense_w6=")
print(dense_w6)
print("**************************************");
print("**************************************");
print("dense_w7=")
print(dense_w7)
print("**************************************");
print("**************************************");
print("dense_w8=")
print(dense_w8)
print("**************************************");
print("**************************************");
print("dense_w9=")
print(dense_w9)



print("**************************************");
print("**************************************");
print(len(dense_w9))


