#/**************************************************************************//**
# * @file 00_cnn_model_3filter_np_float.py
# *
# *
# * @author:
# * Wilson Javier Almario Rodriguez.
# *
# * @date 04/05/2022
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
import tensorflow as tf
from tensorflow    import keras
from mes_fonctions import *


def eva_model(img_test, verbose):
	print(" \n ");
	print("************************************** ");
	print(" Convolution                           ");
	print("************************************** ");
	data_input = img_test;	

	conv_w0= \
	[[0.10431633, 0.077673465, -0.103833474], 
	 [-0.017027456, -0.10956009, 0.103353985], 
	 [0.06311326, -0.08357252, -0.015568181]];
	con_w0 = np.asarray(con_w0);                    # filter 0 conv2d
	con_b0 = -0.22855271;                           # bias   0 conv2d  

	con_w1 = \
	[[-0.26532573, -0.04313986, -0.29961488], 
	 [-0.07563897, -0.1185793, 0.18638213], 
	 [0.080050394, 0.19344968, -0.21536113]];
	con_w1 = np.asarray(con_w1);                    # filter 1 conv2d
	con_b1 = -0.06542021;                           # bias   1 conv2d  

	con_w2 = \
	[[-0.16771996, -0.24295896, 0.2502175], 
	 [0.044923585, -0.032837007, -0.29113683], 
	 [-0.14363475, -0.05524177, -0.09120469]];
	con_w2 = np.asarray(con_w2);                    # filtre 2 conv2d
	con_b2 = -0.03916147;                           # bias   1 conv2d
