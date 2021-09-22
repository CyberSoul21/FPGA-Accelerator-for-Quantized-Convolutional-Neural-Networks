import matplotlib as mpl
mpl.rcParams['legend.fontsize'] = 12;
mpl.rcParams['axes.labelsize']  = 12; 
mpl.rcParams['xtick.labelsize'] = 12; 
mpl.rcParams['ytick.labelsize'] = 12;
mpl.rcParams['text.usetex'] = True;
mpl.rcParams['font.family'] = 'sans-serif';
mpl.rcParams['mathtext.fontset']    = 'dejavusans';
mpl.rcParams['text.latex.preamble'] = [r'\usepackage{mathrsfs}'];
mpl.rcParams.update({'font.size': 12});

import matplotlib.pyplot as plt
import numpy as np
#np.set_printoptions(threshold=sys.maxsize) # Printing all the weights

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'; # TF debug messages
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed

import sys
import tensorflow as tf
from tensorflow import keras

from ctypes import *
from mes_fonctions import *


print(" \n ");
print("************************************** ");
print(" Testing fonctions en CPP avec ctypes  ");
print("************************************** ");
monbib = CDLL("mes_fon_CPP/monbib.so");                    # Bibliothèque CPP
print(monbib); monbib.print_cpp();


def eva_model(img_test, verbose):
  ''' Cette fonction fait evaluation de l'inference 
      d'un modèle CNN avec 12 filtres pour classifer
      la base de données Mnist. Il rendre le valeur
      estimée de la clasification (i.e. la prediction).
      img_test: tableau Numpy de entrée (uint8).
      predict:  Prediction avec le modèle.                 '''
   
  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize);

  print(" \n ");
  print("************************************** ");
  print(" Quantization de l'image               ");
  print("************************************** ");
  scale = 0.04896376;  zero_point = -6;                    # sequential/quantize_layer
  img_test = quant_np(img_test, scale, zero_point, verbose=1);
  #print(img_test);
  #sys.exit(0);                                            # Terminer l'execution

  print(" \n ");
  print("************************************** ");
  print(" Convolution                           ");
  print("************************************** ");
  entree = img_test;
  scale = 0.04697853699326515;                             # quant_conv2d/BiasAdd  
  offset_ent =  6;                                         # input_offset  =  -zero_point de l'entrée  quant_reshape/Reshape
  offset_sor = -1;                                         # output_offset =   zero_point de la sortie quant_conv2d/Relu

  con_f0 = \
   [[  70,  45, -91],
    [ -62, -27,  19],
    [ -11,-110,-126]]; con_f0 = np.asarray(con_f0);        # filtre 0 conv2d
  con_b0 = -2165;                                          # bias   0 conv2d  
  M_b0   = 3.9030474e-05 / scale;                          # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/BiasAdd)--> (S1*S2)/S3 --> Sbias/SBiasAdd
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b0), byref(M0), byref(shift) );
  #print("M_b0= ", M_b0, "M0= ", M0.value, "shift= ", shift.value);
  mc_0 = conv_np(entree, con_f0, con_b0, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_0);

  con_f1 = \
   [[ -18,  59,  43],
    [ -45, -15,  16],
    [   0,-127,-110]]; con_f1 = np.asarray(con_f1);        # filtre 1 conv2d
  con_b1 = -477;                                           # bias   1 conv2d  
  M_b1   = 8.6878958e-05 / scale;                          # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b1), byref(M0), byref(shift) );
  #print("M_b1= ", M_b1, "M0= ", M0.value, "shift= ", shift.value);
  mc_1 = conv_np(entree, con_f1, con_b1, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_1);

  con_f2 = \
   [[-112,-127,  43],
    [  68,  47,   7],
    [ -82, -88,  21]]; con_f2 = np.asarray(con_f2);        # filtre 2 conv2d
  con_b2 = -1847;                                          # bias   2 conv2d  
  M_b2   = 9.1588015e-05 / scale;                          # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b2), byref(M0), byref(shift) );
  #print("M_b2= ", M_b2, "M0= ", M0.value, "shift= ", shift.value);
  mc_2 = conv_np(entree, con_f2, con_b2, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_2);

  con_f3 = \
   [[  38,-127,   4],
    [-103,  -2,  35],
    [ -13, -16,  14]]; con_f3 = np.asarray(con_f3);        # filtre 3 conv2d
  con_b3 = -718;                                           # bias   3 conv2d  
  M_b3   = 8.9985377e-05 / scale;                          # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b3), byref(M0), byref(shift) );
  #print("M_b3= ", M_b3, "M0= ", M0.value, "shift= ", shift.value);
  mc_3 = conv_np(entree, con_f3, con_b3, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_3);

  con_f4 = \
   [[ -11,   6,  43],
    [ -34,-127,  10],
    [  43,  -4, -77]]; con_f4 = np.asarray(con_f4);        # filtre 4 conv2d
  con_b4 = -2396;                                          # bias   4 conv2d  
  M_b4   = 7.2162838e-05 / scale;                          # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b4), byref(M0), byref(shift) );
  #print("M_b4= ", M_b4, "M0= ", M0.value, "shift= ", shift.value);
  mc_4 = conv_np(entree, con_f4, con_b4, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_4);

  con_f5 = \
   [[-103, -91,-127],
    [ -14,  23, -89],
    [  39,116,  -88]]; con_f5 = np.asarray(con_f5);        # filtre 5 conv2d
  con_b5 = 135;                                            # bias   5 conv2d  
  M_b5   = 6.3372834e-05 / scale;                          # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b5), byref(M0), byref(shift) );
  #print("M_b5= ", M_b5, "M0= ", M0.value, "shift= ", shift.value);
  mc_5 = conv_np(entree, con_f5, con_b5, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_5);
 
  con_f6 = \
   [[-108,-123,-127],
    [  83, -36,  24],
    [ -87,  76,  10]]; con_f6 = np.asarray(con_f6);        # filtre 6 conv2d
  con_b6 = -1679;                                          # bias   6 conv2d  
  M_b6   =  6.4356493e-05 / scale;                         # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b6), byref(M0), byref(shift) );
  #print("M_b6= ", M_b6, "M0= ", M0.value, "shift= ", shift.value);
  mc_6 = conv_np(entree, con_f6, con_b6, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_6);

  con_f7 = \
   [[  35,   4,-126],
    [  52, -30, -72],
    [ -54,   9,  32]]; con_f7 = np.asarray(con_f7);        # filtre 7 conv2d
  con_b7 = -2866;                                          # bias   7 conv2d  
  M_b7   = 7.6763994e-05 / scale;                          # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b7), byref(M0), byref(shift) );
  #print("M_b7= ", M_b7, "M0= ", M0.value, "shift= ", shift.value);
  mc_7 = conv_np(entree, con_f7, con_b7, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_7);

  con_f8 = \
   [[ -39,  56,  24],
    [  13,  28,-126],
    [  89, -43,  66]]; con_f8 = np.asarray(con_f8);        # filtre 8 conv2d
  con_b8 = -4977;                                          # bias   8 conv2d  
  M_b8   = 3.7042475e-05 / scale;                          # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b8), byref(M0), byref(shift) );
  #print("M_b8= ", M_b8, "M0= ", M0.value, "shift= ", shift.value);
  mc_8 = conv_np(entree, con_f8, con_b8, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_8);

  con_f9 = \
   [[ -56,-127,   6],
    [ -67,  83,  14],
    [  52, -10, -51]]; con_f9 = np.asarray(con_f9);        # filtre 9 conv2d
  con_b9 = -1650;                                          # bias   9 conv2d  
  M_b9   =  8.3447310e-05 / scale;                         # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b9), byref(M0), byref(shift) );
  #print("M_b9= ", M_b9, "M0= ", M0.value, "shift= ", shift.value);
  mc_9 = conv_np(entree, con_f9, con_b9, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_9);

  con_f10 = \
   [[  74, -30,   4],
    [ -37, -54, -28],
    [ -34,   7,-126]]; con_f10 = np.asarray(con_f10);      # filtre 10 conv2d
  con_b10 = -1001;                                         # bias   10 conv2d  
  M_b10   = 5.6461951e-05 / scale;                         # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b10), byref(M0), byref(shift) );
  #print("M_b10= ", M_b10, "M0= ", M0.value, "shift= ", shift.value);
  mc_10 = conv_np(entree, con_f10, con_b10, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_10);

  con_f11 = \
   [[  45, -48, -52],
    [-104,  54,-124],
    [-127,  49,  54]]; con_f11 = np.asarray(con_f11);      # filtre 11 conv2d
  con_b11 = -2810;                                         # bias   11 conv2d  
  M_b11   = 6.9674665e-05 / scale;                         # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/Relu)--> (S1*S2)/S3 --> Sbias/Srelu
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_b11), byref(M0), byref(shift) );
  #print("M_b11= ", M_b11, "M0= ", M0.value, "shift= ", shift.value);
  mc_11 = conv_np(entree, con_f11, con_b11, M0.value, shift.value, offset_ent, offset_sor, verbose=1); # print(mc_11);

  # Map des caractéristiques 
  #print("mc_0:",  mc_0, "\n");  print("mc_1:",  mc_1, "\n");  print("mc_2:", mc_2, "\n");  print("mc_3:", mc_3, "\n");  print("mc_4:", mc_4, "\n");
  #print("mc_5:",  mc_5, "\n");  print("mc_6:",  mc_6, "\n");  print("mc_7:", mc_7, "\n");  print("mc_8:", mc_8, "\n");  print("mc_9:", mc_9, "\n");
  #print("mc_10:",mc_10, "\n");  print("mc_11:", mc_11, "\n");

  con_aux0  = np.zeros([26, 12]); con_aux1  = np.zeros([26, 12]); con_aux2  = np.zeros([26, 12]); con_aux3  = np.zeros([26, 12]);
  con_aux4  = np.zeros([26, 12]); con_aux5  = np.zeros([26, 12]); con_aux6  = np.zeros([26, 12]); con_aux7  = np.zeros([26, 12]);
  con_aux8  = np.zeros([26, 12]); con_aux9  = np.zeros([26, 12]); con_aux10 = np.zeros([26, 12]); con_aux11 = np.zeros([26, 12]);
  con_aux12 = np.zeros([26, 12]); con_aux13 = np.zeros([26, 12]); con_aux14 = np.zeros([26, 12]); con_aux15 = np.zeros([26, 12]);
  con_aux16 = np.zeros([26, 12]); con_aux17 = np.zeros([26, 12]); con_aux18 = np.zeros([26, 12]); con_aux19 = np.zeros([26, 12]);
  con_aux20 = np.zeros([26, 12]); con_aux21 = np.zeros([26, 12]); con_aux22 = np.zeros([26, 12]); con_aux23 = np.zeros([26, 12]);
  con_aux24 = np.zeros([26, 12]); con_aux25 = np.zeros([26, 12]);

  # con_aux
  con_aux0[:, 0] = mc_0[0,:]; con_aux0[:, 1] = mc_1[0,:]; con_aux0[:, 2] = mc_2[0,:]; con_aux0[:, 3] = mc_3[0,:]; con_aux0[:, 4] = mc_4[0, :]; con_aux0[:, 5] = mc_5[0, :]; 
  con_aux0[:, 6] = mc_6[0,:]; con_aux0[:, 7] = mc_7[0,:]; con_aux0[:, 8] = mc_8[0,:]; con_aux0[:, 9] = mc_9[0,:]; con_aux0[:,10] = mc_10[0,:]; con_aux0[:,11] = mc_11[0,:]; 

  con_aux1[:, 0] = mc_0[1,:]; con_aux1[:, 1] = mc_1[1,:]; con_aux1[:, 2] = mc_2[1,:]; con_aux1[:, 3] = mc_3[1,:]; con_aux1[:, 4] = mc_4[1, :]; con_aux1[:, 5] = mc_5[1, :]; 
  con_aux1[:, 6] = mc_6[1,:]; con_aux1[:, 7] = mc_7[1,:]; con_aux1[:, 8] = mc_8[1,:]; con_aux1[:, 9] = mc_9[1,:]; con_aux1[:,10] = mc_10[1,:]; con_aux1[:,11] = mc_11[1,:]; 

  con_aux2[:, 0] = mc_0[2,:]; con_aux2[:, 1] = mc_1[2,:]; con_aux2[:, 2] = mc_2[2,:]; con_aux2[:, 3] = mc_3[2,:]; con_aux2[:, 4] = mc_4[2, :]; con_aux2[:, 5] = mc_5[2, :]; 
  con_aux2[:, 6] = mc_6[2,:]; con_aux2[:, 7] = mc_7[2,:]; con_aux2[:, 8] = mc_8[2,:]; con_aux2[:, 9] = mc_9[2,:]; con_aux2[:,10] = mc_10[2,:]; con_aux2[:,11] = mc_11[2,:]; 

  con_aux3[:, 0] = mc_0[3,:]; con_aux3[:, 1] = mc_1[3,:]; con_aux3[:, 2] = mc_2[3,:]; con_aux3[:, 3] = mc_3[3,:]; con_aux3[:, 4] = mc_4[3, :]; con_aux3[:, 5] = mc_5[3, :]; 
  con_aux3[:, 6] = mc_6[3,:]; con_aux3[:, 7] = mc_7[3,:]; con_aux3[:, 8] = mc_8[3,:]; con_aux3[:, 9] = mc_9[3,:]; con_aux3[:,10] = mc_10[3,:]; con_aux3[:,11] = mc_11[3,:]; 

  con_aux4[:, 0] = mc_0[4,:]; con_aux4[:, 1] = mc_1[4,:]; con_aux4[:, 2] = mc_2[4,:]; con_aux4[:, 3] = mc_3[4,:]; con_aux4[:, 4] = mc_4[4, :]; con_aux4[:, 5] = mc_5[4, :]; 
  con_aux4[:, 6] = mc_6[4,:]; con_aux4[:, 7] = mc_7[4,:]; con_aux4[:, 8] = mc_8[4,:]; con_aux4[:, 9] = mc_9[4,:]; con_aux4[:,10] = mc_10[4,:]; con_aux4[:,11] = mc_11[4,:]; 

  con_aux5[:, 0] = mc_0[5,:]; con_aux5[:, 1] = mc_1[5,:]; con_aux5[:, 2] = mc_2[5,:]; con_aux5[:, 3] = mc_3[5,:]; con_aux5[:, 4] = mc_4[5, :]; con_aux5[:, 5] = mc_5[5, :]; 
  con_aux5[:, 6] = mc_6[5,:]; con_aux5[:, 7] = mc_7[5,:]; con_aux5[:, 8] = mc_8[5,:]; con_aux5[:, 9] = mc_9[5,:]; con_aux5[:,10] = mc_10[5,:]; con_aux5[:,11] = mc_11[5,:]; 

  con_aux6[:, 0] = mc_0[6,:]; con_aux6[:, 1] = mc_1[6,:]; con_aux6[:, 2] = mc_2[6,:]; con_aux6[:, 3] = mc_3[6,:]; con_aux6[:, 4] = mc_4[6, :]; con_aux6[:, 5] = mc_5[6, :]; 
  con_aux6[:, 6] = mc_6[6,:]; con_aux6[:, 7] = mc_7[6,:]; con_aux6[:, 8] = mc_8[6,:]; con_aux6[:, 9] = mc_9[6,:]; con_aux6[:,10] = mc_10[6,:]; con_aux6[:,11] = mc_11[6,:]; 

  con_aux7[:, 0] = mc_0[7,:]; con_aux7[:, 1] = mc_1[7,:]; con_aux7[:, 2] = mc_2[7,:]; con_aux7[:, 3] = mc_3[7,:]; con_aux7[:, 4] = mc_4[7, :]; con_aux7[:, 5] = mc_5[7, :]; 
  con_aux7[:, 6] = mc_6[7,:]; con_aux7[:, 7] = mc_7[7,:]; con_aux7[:, 8] = mc_8[7,:]; con_aux7[:, 9] = mc_9[7,:]; con_aux7[:,10] = mc_10[7,:]; con_aux7[:,11] = mc_11[7,:]; 

  con_aux8[:, 0] = mc_0[8,:]; con_aux8[:, 1] = mc_1[8,:]; con_aux8[:, 2] = mc_2[8,:]; con_aux8[:, 3] = mc_3[8,:]; con_aux8[:, 4] = mc_4[8, :]; con_aux8[:, 5] = mc_5[8, :]; 
  con_aux8[:, 6] = mc_6[8,:]; con_aux8[:, 7] = mc_7[8,:]; con_aux8[:, 8] = mc_8[8,:]; con_aux8[:, 9] = mc_9[8,:]; con_aux8[:,10] = mc_10[8,:]; con_aux8[:,11] = mc_11[8,:]; 

  con_aux9[:, 0] = mc_0[9,:]; con_aux9[:, 1] = mc_1[9,:]; con_aux9[:, 2] = mc_2[9,:]; con_aux9[:, 3] = mc_3[9,:]; con_aux9[:, 4] = mc_4[9, :]; con_aux9[:, 5] = mc_5[9, :]; 
  con_aux9[:, 6] = mc_6[9,:]; con_aux9[:, 7] = mc_7[9,:]; con_aux9[:, 8] = mc_8[9,:]; con_aux9[:, 9] = mc_9[9,:]; con_aux9[:,10] = mc_10[9,:]; con_aux9[:,11] = mc_11[9,:]; 

  con_aux10[:, 0] = mc_0[10,:]; con_aux10[:, 1] = mc_1[10,:]; con_aux10[:, 2] = mc_2[10,:]; con_aux10[:, 3] = mc_3[10,:]; con_aux10[:, 4] = mc_4[10, :]; con_aux10[:, 5] = mc_5[10, :]; 
  con_aux10[:, 6] = mc_6[10,:]; con_aux10[:, 7] = mc_7[10,:]; con_aux10[:, 8] = mc_8[10,:]; con_aux10[:, 9] = mc_9[10,:]; con_aux10[:,10] = mc_10[10,:]; con_aux10[:,11] = mc_11[10,:]; 

  con_aux11[:, 0] = mc_0[11,:]; con_aux11[:, 1] = mc_1[11,:]; con_aux11[:, 2] = mc_2[11,:]; con_aux11[:, 3] = mc_3[11,:]; con_aux11[:, 4] = mc_4[11, :]; con_aux11[:, 5] = mc_5[11, :]; 
  con_aux11[:, 6] = mc_6[11,:]; con_aux11[:, 7] = mc_7[11,:]; con_aux11[:, 8] = mc_8[11,:]; con_aux11[:, 9] = mc_9[11,:]; con_aux11[:,10] = mc_10[11,:]; con_aux11[:,11] = mc_11[11,:]; 

  con_aux12[:, 0] = mc_0[12,:]; con_aux12[:, 1] = mc_1[12,:]; con_aux12[:, 2] = mc_2[12,:]; con_aux12[:, 3] = mc_3[12,:]; con_aux12[:, 4] = mc_4[12, :]; con_aux12[:, 5] = mc_5[12, :]; 
  con_aux12[:, 6] = mc_6[12,:]; con_aux12[:, 7] = mc_7[12,:]; con_aux12[:, 8] = mc_8[12,:]; con_aux12[:, 9] = mc_9[12,:]; con_aux12[:,10] = mc_10[12,:]; con_aux12[:,11] = mc_11[12,:]; 

  con_aux13[:, 0] = mc_0[13,:]; con_aux13[:, 1] = mc_1[13,:]; con_aux13[:, 2] = mc_2[13,:]; con_aux13[:, 3] = mc_3[13,:]; con_aux13[:, 4] = mc_4[13, :]; con_aux13[:, 5] = mc_5[13, :]; 
  con_aux13[:, 6] = mc_6[13,:]; con_aux13[:, 7] = mc_7[13,:]; con_aux13[:, 8] = mc_8[13,:]; con_aux13[:, 9] = mc_9[13,:]; con_aux13[:,10] = mc_10[13,:]; con_aux13[:,11] = mc_11[13,:]; 

  con_aux14[:, 0] = mc_0[14,:]; con_aux14[:, 1] = mc_1[14,:]; con_aux14[:, 2] = mc_2[14,:]; con_aux14[:, 3] = mc_3[14,:]; con_aux14[:, 4] = mc_4[14, :]; con_aux14[:, 5] = mc_5[14, :]; 
  con_aux14[:, 6] = mc_6[14,:]; con_aux14[:, 7] = mc_7[14,:]; con_aux14[:, 8] = mc_8[14,:]; con_aux14[:, 9] = mc_9[14,:]; con_aux14[:,10] = mc_10[14,:]; con_aux14[:,11] = mc_11[14,:]; 

  con_aux15[:, 0] = mc_0[15,:]; con_aux15[:, 1] = mc_1[15,:]; con_aux15[:, 2] = mc_2[15,:]; con_aux15[:, 3] = mc_3[15,:]; con_aux15[:, 4] = mc_4[15, :]; con_aux15[:, 5] = mc_5[15, :]; 
  con_aux15[:, 6] = mc_6[15,:]; con_aux15[:, 7] = mc_7[15,:]; con_aux15[:, 8] = mc_8[15,:]; con_aux15[:, 9] = mc_9[15,:]; con_aux15[:,10] = mc_10[15,:]; con_aux15[:,11] = mc_11[15,:]; 

  con_aux16[:, 0] = mc_0[16,:]; con_aux16[:, 1] = mc_1[16,:]; con_aux16[:, 2] = mc_2[16,:]; con_aux16[:, 3] = mc_3[16,:]; con_aux16[:, 4] = mc_4[16, :]; con_aux16[:, 5] = mc_5[16, :]; 
  con_aux16[:, 6] = mc_6[16,:]; con_aux16[:, 7] = mc_7[16,:]; con_aux16[:, 8] = mc_8[16,:]; con_aux16[:, 9] = mc_9[16,:]; con_aux16[:,10] = mc_10[16,:]; con_aux16[:,11] = mc_11[16,:]; 

  con_aux17[:, 0] = mc_0[17,:]; con_aux17[:, 1] = mc_1[17,:]; con_aux17[:, 2] = mc_2[17,:]; con_aux17[:, 3] = mc_3[17,:]; con_aux17[:, 4] = mc_4[17, :]; con_aux17[:, 5] = mc_5[17, :]; 
  con_aux17[:, 6] = mc_6[17,:]; con_aux17[:, 7] = mc_7[17,:]; con_aux17[:, 8] = mc_8[17,:]; con_aux17[:, 9] = mc_9[17,:]; con_aux17[:,10] = mc_10[17,:]; con_aux17[:,11] = mc_11[17,:]; 

  con_aux18[:, 0] = mc_0[18,:]; con_aux18[:, 1] = mc_1[18,:]; con_aux18[:, 2] = mc_2[18,:]; con_aux18[:, 3] = mc_3[18,:]; con_aux18[:, 4] = mc_4[18, :]; con_aux18[:, 5] = mc_5[18, :]; 
  con_aux18[:, 6] = mc_6[18,:]; con_aux18[:, 7] = mc_7[18,:]; con_aux18[:, 8] = mc_8[18,:]; con_aux18[:, 9] = mc_9[18,:]; con_aux18[:,10] = mc_10[18,:]; con_aux18[:,11] = mc_11[18,:]; 

  con_aux19[:, 0] = mc_0[19,:]; con_aux19[:, 1] = mc_1[19,:]; con_aux19[:, 2] = mc_2[19,:]; con_aux19[:, 3] = mc_3[19,:]; con_aux19[:, 4] = mc_4[19, :]; con_aux19[:, 5] = mc_5[19, :]; 
  con_aux19[:, 6] = mc_6[19,:]; con_aux19[:, 7] = mc_7[19,:]; con_aux19[:, 8] = mc_8[19,:]; con_aux19[:, 9] = mc_9[19,:]; con_aux19[:,10] = mc_10[19,:]; con_aux19[:,11] = mc_11[19,:]; 

  con_aux20[:, 0] = mc_0[20,:]; con_aux20[:, 1] = mc_1[20,:]; con_aux20[:, 2] = mc_2[20,:]; con_aux20[:, 3] = mc_3[20,:]; con_aux20[:, 4] = mc_4[20, :]; con_aux20[:, 5] = mc_5[20, :]; 
  con_aux20[:, 6] = mc_6[20,:]; con_aux20[:, 7] = mc_7[20,:]; con_aux20[:, 8] = mc_8[20,:]; con_aux20[:, 9] = mc_9[20,:]; con_aux20[:,10] = mc_10[20,:]; con_aux20[:,11] = mc_11[20,:]; 

  con_aux21[:, 0] = mc_0[21,:]; con_aux21[:, 1] = mc_1[21,:]; con_aux21[:, 2] = mc_2[21,:]; con_aux21[:, 3] = mc_3[21,:]; con_aux14[:, 4] = mc_4[21, :]; con_aux21[:, 5] = mc_5[21, :]; 
  con_aux21[:, 6] = mc_6[21,:]; con_aux21[:, 7] = mc_7[21,:]; con_aux21[:, 8] = mc_8[21,:]; con_aux21[:, 9] = mc_9[21,:]; con_aux14[:,10] = mc_10[21,:]; con_aux21[:,11] = mc_11[21,:]; 

  con_aux22[:, 0] = mc_0[22,:]; con_aux22[:, 1] = mc_1[22,:]; con_aux22[:, 2] = mc_2[22,:]; con_aux22[:, 3] = mc_3[22,:]; con_aux22[:, 4] = mc_4[22, :]; con_aux22[:, 5] = mc_5[22, :]; 
  con_aux22[:, 6] = mc_6[22,:]; con_aux22[:, 7] = mc_7[22,:]; con_aux22[:, 8] = mc_8[22,:]; con_aux22[:, 9] = mc_9[22,:]; con_aux22[:,10] = mc_10[22,:]; con_aux22[:,11] = mc_11[22,:]; 

  con_aux23[:, 0] = mc_0[23,:]; con_aux23[:, 1] = mc_1[23,:]; con_aux23[:, 2] = mc_2[23,:]; con_aux23[:, 3] = mc_3[23,:]; con_aux23[:, 4] = mc_4[23, :]; con_aux23[:, 5] = mc_5[23, :]; 
  con_aux23[:, 6] = mc_6[23,:]; con_aux23[:, 7] = mc_7[23,:]; con_aux23[:, 8] = mc_8[23,:]; con_aux23[:, 9] = mc_9[23,:]; con_aux23[:,10] = mc_10[23,:]; con_aux23[:,11] = mc_11[23,:]; 

  con_aux24[:, 0] = mc_0[24,:]; con_aux24[:, 1] = mc_1[24,:]; con_aux24[:, 2] = mc_2[24,:]; con_aux24[:, 3] = mc_3[24,:]; con_aux24[:, 4] = mc_4[24, :]; con_aux24[:, 5] = mc_5[24, :]; 
  con_aux24[:, 6] = mc_6[24,:]; con_aux24[:, 7] = mc_7[24,:]; con_aux24[:, 8] = mc_8[24,:]; con_aux24[:, 9] = mc_9[24,:]; con_aux24[:,10] = mc_10[24,:]; con_aux24[:,11] = mc_11[24,:]; 

  con_aux25[:, 0] = mc_0[25,:]; con_aux25[:, 1] = mc_1[25,:]; con_aux25[:, 2] = mc_2[25,:]; con_aux25[:, 3] = mc_3[25,:]; con_aux25[:, 4] = mc_4[25, :]; con_aux25[:, 5] = mc_5[25, :]; 
  con_aux25[:, 6] = mc_6[25,:]; con_aux25[:, 7] = mc_7[25,:]; con_aux25[:, 8] = mc_8[25,:]; con_aux25[:, 9] = mc_9[25,:]; con_aux25[:,10] = mc_10[25,:]; con_aux25[:,11] = mc_11[25,:]; 

  print("con_aux0:  \n", con_aux0);  print("con_aux1:  \n", con_aux1);  print("con_aux2:  \n", con_aux2);  print("con_aux3: \n", con_aux3);
  print("con_aux4:  \n", con_aux4);  print("con_aux5:  \n", con_aux5);  print("con_aux6:  \n", con_aux6);  print("con_aux7: \n", con_aux7);
  print("con_aux8:  \n", con_aux8);  print("con_aux9:  \n", con_aux9);  print("con_aux10: \n", con_aux10); print("con_aux11: \n", con_aux11);
  print("con_aux12: \n", con_aux12); print("con_aux13: \n", con_aux13); print("con_aux14: \n", con_aux14); print("con_aux15: \n", con_aux15);
  print("con_aux16: \n", con_aux16); print("con_aux17: \n", con_aux17); print("con_aux18: \n", con_aux18); print("con_aux19: \n", con_aux19);
  print("con_aux20: \n", con_aux20); print("con_aux21: \n", con_aux21); print("con_aux22: \n", con_aux22); print("con_aux23: \n", con_aux23);
  print("con_aux24: \n", con_aux24); print("con_aux25: \n", con_aux25); 
  #sys.exit(0);                                              # Terminer l'execution


  print(" \n ");
  print("************************************** ");
  print(" MaxPooling (2,2)                      ");
  print("************************************** ");
  mp_0   = maxpool_np(mc_0,   verbose=1);
  mp_1   = maxpool_np(mc_1,   verbose=1);
  mp_2   = maxpool_np(mc_2,   verbose=1);
  mp_3   = maxpool_np(mc_3,   verbose=1);
  mp_4   = maxpool_np(mc_4,   verbose=1);
  mp_5   = maxpool_np(mc_5,   verbose=1);
  mp_6   = maxpool_np(mc_6,   verbose=1);
  mp_7   = maxpool_np(mc_7,   verbose=1);
  mp_8   = maxpool_np(mc_8,   verbose=1);
  mp_9   = maxpool_np(mc_9,   verbose=1);
  mp_10  = maxpool_np(mc_10,  verbose=1);
  mp_11  = maxpool_np(mc_11,  verbose=1);

  '''print(mp_0);  print(mp_1);  print(mp_2);  print(mp_3);  print(mp_4);
  print(mp_5);  print(mp_6);  print(mp_7);  print(mp_8);  print(mp_9); 
  print(mp_10); print(mp_11); '''

  con_aux0  = np.zeros([13, 12]); con_aux1  = np.zeros([13, 12]); con_aux2  = np.zeros([13, 12]); con_aux3  = np.zeros([13, 12]);
  con_aux4  = np.zeros([13, 12]); con_aux5  = np.zeros([13, 12]); con_aux6  = np.zeros([13, 12]); con_aux7  = np.zeros([13, 12]);
  con_aux8  = np.zeros([13, 12]); con_aux9  = np.zeros([13, 12]); con_aux10 = np.zeros([13, 12]); con_aux11 = np.zeros([13, 12]);
  con_aux12 = np.zeros([13, 12]); 

  # con_aux
  con_aux0[:, 0] = mp_0[0,:]; con_aux0[:, 1] = mp_1[0,:]; con_aux0[:, 2] = mp_2[0,:]; con_aux0[:, 3] = mp_3[0,:]; con_aux0[:, 4] = mp_4[0, :]; con_aux0[:, 5] = mp_5[0, :]; 
  con_aux0[:, 6] = mp_6[0,:]; con_aux0[:, 7] = mp_7[0,:]; con_aux0[:, 8] = mp_8[0,:]; con_aux0[:, 9] = mp_9[0,:]; con_aux0[:,10] = mp_10[0,:]; con_aux0[:,11] = mp_11[0,:]; 

  con_aux1[:, 0] = mp_0[1,:]; con_aux1[:, 1] = mp_1[1,:]; con_aux1[:, 2] = mp_2[1,:]; con_aux1[:, 3] = mp_3[1,:]; con_aux1[:, 4] = mp_4[1, :]; con_aux1[:, 5] = mp_5[1, :]; 
  con_aux1[:, 6] = mp_6[1,:]; con_aux1[:, 7] = mp_7[1,:]; con_aux1[:, 8] = mp_8[1,:]; con_aux1[:, 9] = mp_9[1,:]; con_aux1[:,10] = mp_10[1,:]; con_aux1[:,11] = mp_11[1,:]; 

  con_aux2[:, 0] = mp_0[2,:]; con_aux2[:, 1] = mp_1[2,:]; con_aux2[:, 2] = mp_2[2,:]; con_aux2[:, 3] = mp_3[2,:]; con_aux2[:, 4] = mp_4[2, :]; con_aux2[:, 5] = mp_5[2, :]; 
  con_aux2[:, 6] = mp_6[2,:]; con_aux2[:, 7] = mp_7[2,:]; con_aux2[:, 8] = mp_8[2,:]; con_aux2[:, 9] = mp_9[2,:]; con_aux2[:,10] = mp_10[2,:]; con_aux2[:,11] = mp_11[2,:]; 

  con_aux3[:, 0] = mp_0[3,:]; con_aux3[:, 1] = mp_1[3,:]; con_aux3[:, 2] = mp_2[3,:]; con_aux3[:, 3] = mp_3[3,:]; con_aux3[:, 4] = mp_4[3, :]; con_aux3[:, 5] = mp_5[3, :]; 
  con_aux3[:, 6] = mp_6[3,:]; con_aux3[:, 7] = mp_7[3,:]; con_aux3[:, 8] = mp_8[3,:]; con_aux3[:, 9] = mp_9[3,:]; con_aux3[:,10] = mp_10[3,:]; con_aux3[:,11] = mp_11[3,:]; 

  con_aux4[:, 0] = mp_0[4,:]; con_aux4[:, 1] = mp_1[4,:]; con_aux4[:, 2] = mp_2[4,:]; con_aux4[:, 3] = mp_3[4,:]; con_aux4[:, 4] = mp_4[4, :]; con_aux4[:, 5] = mp_5[4, :]; 
  con_aux4[:, 6] = mp_6[4,:]; con_aux4[:, 7] = mp_7[4,:]; con_aux4[:, 8] = mp_8[4,:]; con_aux4[:, 9] = mp_9[4,:]; con_aux4[:,10] = mp_10[4,:]; con_aux4[:,11] = mp_11[4,:]; 

  con_aux5[:, 0] = mp_0[5,:]; con_aux5[:, 1] = mp_1[5,:]; con_aux5[:, 2] = mp_2[5,:]; con_aux5[:, 3] = mp_3[5,:]; con_aux5[:, 4] = mp_4[5, :]; con_aux5[:, 5] = mp_5[5, :]; 
  con_aux5[:, 6] = mp_6[5,:]; con_aux5[:, 7] = mp_7[5,:]; con_aux5[:, 8] = mp_8[5,:]; con_aux5[:, 9] = mp_9[5,:]; con_aux5[:,10] = mp_10[5,:]; con_aux5[:,11] = mp_11[5,:]; 

  con_aux6[:, 0] = mp_0[6,:]; con_aux6[:, 1] = mp_1[6,:]; con_aux6[:, 2] = mp_2[6,:]; con_aux6[:, 3] = mp_3[6,:]; con_aux6[:, 4] = mp_4[6, :]; con_aux6[:, 5] = mp_5[6, :]; 
  con_aux6[:, 6] = mp_6[6,:]; con_aux6[:, 7] = mp_7[6,:]; con_aux6[:, 8] = mp_8[6,:]; con_aux6[:, 9] = mp_9[6,:]; con_aux6[:,10] = mp_10[6,:]; con_aux6[:,11] = mp_11[6,:]; 

  con_aux7[:, 0] = mp_0[7,:]; con_aux7[:, 1] = mp_1[7,:]; con_aux7[:, 2] = mp_2[7,:]; con_aux7[:, 3] = mp_3[7,:]; con_aux7[:, 4] = mp_4[7, :]; con_aux7[:, 5] = mp_5[7, :]; 
  con_aux7[:, 6] = mp_6[7,:]; con_aux7[:, 7] = mp_7[7,:]; con_aux7[:, 8] = mp_8[7,:]; con_aux7[:, 9] = mp_9[7,:]; con_aux7[:,10] = mp_10[7,:]; con_aux7[:,11] = mp_11[7,:]; 

  con_aux8[:, 0] = mp_0[8,:]; con_aux8[:, 1] = mp_1[8,:]; con_aux8[:, 2] = mp_2[8,:]; con_aux8[:, 3] = mp_3[8,:]; con_aux8[:, 4] = mp_4[8, :]; con_aux8[:, 5] = mp_5[8, :]; 
  con_aux8[:, 6] = mp_6[8,:]; con_aux8[:, 7] = mp_7[8,:]; con_aux8[:, 8] = mp_8[8,:]; con_aux8[:, 9] = mp_9[8,:]; con_aux8[:,10] = mp_10[8,:]; con_aux8[:,11] = mp_11[8,:]; 

  con_aux9[:, 0] = mp_0[9,:]; con_aux9[:, 1] = mp_1[9,:]; con_aux9[:, 2] = mp_2[9,:]; con_aux9[:, 3] = mp_3[9,:]; con_aux9[:, 4] = mp_4[9, :]; con_aux9[:, 5] = mp_5[9, :]; 
  con_aux9[:, 6] = mp_6[9,:]; con_aux9[:, 7] = mp_7[9,:]; con_aux9[:, 8] = mp_8[9,:]; con_aux9[:, 9] = mp_9[9,:]; con_aux9[:,10] = mp_10[9,:]; con_aux9[:,11] = mp_11[9,:]; 

  con_aux10[:, 0] = mp_0[10,:]; con_aux10[:, 1] = mp_1[10,:]; con_aux10[:, 2] = mp_2[10,:]; con_aux10[:, 3] = mp_3[10,:]; con_aux10[:, 4] = mp_4[10, :]; con_aux10[:, 5] = mp_5[10, :]; 
  con_aux10[:, 6] = mp_6[10,:]; con_aux10[:, 7] = mp_7[10,:]; con_aux10[:, 8] = mp_8[10,:]; con_aux10[:, 9] = mp_9[10,:]; con_aux10[:,10] = mp_10[10,:]; con_aux10[:,11] = mp_11[10,:]; 

  con_aux11[:, 0] = mp_0[11,:]; con_aux11[:, 1] = mp_1[11,:]; con_aux11[:, 2] = mp_2[11,:]; con_aux11[:, 3] = mp_3[11,:]; con_aux11[:, 4] = mp_4[11, :]; con_aux11[:, 5] = mp_5[11, :]; 
  con_aux11[:, 6] = mp_6[11,:]; con_aux11[:, 7] = mp_7[11,:]; con_aux11[:, 8] = mp_8[11,:]; con_aux11[:, 9] = mp_9[11,:]; con_aux11[:,10] = mp_10[11,:]; con_aux11[:,11] = mp_11[11,:]; 

  con_aux12[:, 0] = mp_0[12,:]; con_aux12[:, 1] = mp_1[12,:]; con_aux12[:, 2] = mp_2[12,:]; con_aux12[:, 3] = mp_3[12,:]; con_aux12[:, 4] = mp_4[12, :]; con_aux12[:, 5] = mp_5[12, :]; 
  con_aux12[:, 6] = mp_6[12,:]; con_aux12[:, 7] = mp_7[12,:]; con_aux12[:, 8] = mp_8[12,:]; con_aux12[:, 9] = mp_9[12,:]; con_aux12[:,10] = mp_10[12,:]; con_aux12[:,11] = mp_11[12,:]; 

  print("con_aux0:  \n", con_aux0);  print("con_aux1:  \n", con_aux1);  print("con_aux2:  \n", con_aux2);   print("con_aux3: \n", con_aux3);
  print("con_aux4:  \n", con_aux4);  print("con_aux5:  \n", con_aux5);  print("con_aux6:  \n", con_aux6);   print("con_aux7: \n", con_aux7);
  print("con_aux4:  \n", con_aux8);  print("con_aux5:  \n", con_aux9);  print("con_aux6:  \n", con_aux10);  print("con_aux7: \n", con_aux11);
  print("con_aux12: \n", con_aux12); 
  #sys.exit(0);                                              # Terminer l'execution


  print(" \n ");
  print("************************************** ");
  print(" Flatten                               ");
  print("************************************** ");
  flatten_aux = np.append(con_aux0, con_aux1); 
  flatten_aux = np.append(flatten_aux, con_aux2);  flatten_aux = np.append(flatten_aux, con_aux3);  flatten_aux = np.append(flatten_aux, con_aux4); 
  flatten_aux = np.append(flatten_aux, con_aux5);  flatten_aux = np.append(flatten_aux, con_aux6);  flatten_aux = np.append(flatten_aux, con_aux7); 
  flatten_aux = np.append(flatten_aux, con_aux8);  flatten_aux = np.append(flatten_aux, con_aux9);  flatten_aux = np.append(flatten_aux, con_aux10); 
  flatten_aux = np.append(flatten_aux, con_aux11); flatten_aux = np.append(flatten_aux, con_aux12); #print(flatten_aux);  
  flatten_aux = np.expand_dims(flatten_aux, axis=0); print(flatten_aux); 
  #sys.exit(0);                                              # Terminer l'execution


  print(" \n ");
  print("************************************** ");
  print(" Full connected                        ");
  print("************************************** ");

  fc_w0 = \
    [[   37,   52,   36,   -1,  -16,  -31,    3,  -27,   19,  -10,   29,
         66,   37,   17,  -93,  -32,   58,   28,   46,  -67,   17,  -27,
        -51,  -20,  -15,   79,  -67,  -40,   64,   12, -108, -127,  -28,
         52,   36, -124,  -25,   50,   32,  -77,   -5,   65,  -42,   32,
        -37,  -79,   36,  -26,  -39,   87,  -57,    0,   38,   21,    8,
        -33,  -46,  -17,  -45,  -30,   10,  -39,  -36,  -47,   22,  -26,
        -48,   22,   29,  -18,   33,    5,   23,   12,  -57,  -31,    5,
        -12,  -57,   42,  -17,  -15,  -41,   17,  -25,  -30,  -30,   23,
        -42,  -36,   36,   -1,  -57,   24,  -43,   -3,  -52,  -47,   17,
        -33,  -30,  -26,   -2,  -32,  -36,  -37,   -1,  -82,  -37,  -17,
         -2,   18,   -2,   -1,    0,  -42,  -39,  -71,  -15,  -34,   -5,
        -27,   36,  -59,  -52,  -52,  -53,   -6,  -74,    6,   36,  -26,
         -7,  -32,   12,  -20,    2,   -2,  -20,    3,   24,  -29,   46,
         20,   19,  -55,   16,    1,  -17,  -20,  -47,    0,   39,   26,
        -32,  -43,   21,   27,   63,   12,   65,  -29,   37,  -37,   66,
         12,   55,  -51,   45,   -5,   -4,  -33,   22,  -13,  -65,  -56,
        -54,   -3,   59,  -77,   -1,  -25,   13,    3,  -62,   28,    6,
        -21,  -17,  -39,   20,   14,   27,   91,    0,  -56,   17,   52,
         -2,   24,  -49,  -20,  -33,   17,   -6,  -65,    9,  -61,   17,
        -23,  -50,   54,   39,  -52,  -20,  -21,   28,   35,   20,   20,
         11,   39,   44,   16,   26,   36,  -66,  -20,    6,  -41,  -29,
        -16,   10,   28,   19,   51,   35,  -48,   19,    4,   25,   -4,
         18,   23,  -35,  -10,  -49,   37,  -39,   56,   -5,  -26,   36,
        -34,   43,   31,  -14,   34,  -20,  -39,   30,   -4,  -44,   -9,
         20,   44,   25,   20,   15,   -3,    5,   38,  -35,   24,    7,
        -14,  -28,  -38,  -28,   24,  -33,    3,   10,  -30,   24,   17,
        -47,  -24,  -37,   64,   28,  -36,   44,   43,  -22,  -27,  -42,
        -40,  -52,  -64,   16,  -29,   28,   31,   -1,  -83,  -27,  -59,
         28,  -51,    3,   22,   28,   31,   10,  -23,   -6,    8,  -67,
         17,  -80,   -1,  -46,   22,  -47,  -45,   15,   -9,  -48,  -48,
         -5,  -51,   11,  -45,   11,   14,   57,   40,  -51,   26,   -3,
         19,   12,    4,  -57,  -24,  -43,   11,   27,  -43,   31,  -35,
        -71,   10,  -60,    3,   19,  -42,  -10,  -14,   -1,  -35,  -61,
         15,   32,   20,    5,  -38,   40,  -26,  -35,  -33,  -39,   21,
         -1,  -41,  -45,   22,   18,  -32,   32,  -10,  -13,  -17,   -7,
        -25,   15,   10,   12,  -12,  -26,  -36,  -47,   53,    7,   16,
          0,  -10,   26,   31,  -18,   34,   50,  -20,  -30,  -39,  -58,
          9,  -14,    7,  -31,  -18,  -26,   -9,   -5,    1,   30,   33,
        -24,   -6,  -19,  -30,   26,  -28,   27,  -17,  -26,  -22,    1,
         35,   26,    2,  -54,   39,  -33,    3,   60,   57,  -18,   18,
        -10,   61,  -61,   43,  -34,   -9,  -57,   -1,  -28,    5,   -4,
         26,   -2,   -4,  -45,    8,   26,   -9,  -19,  -49,   20,  -19,
         16,  -14,    7,   37,  -66,  -30,   20,  -20,  -48,  -52,  -32,
         67,  -44,   14,   12,  -60,   28,  -38,  -25,   15,  -54,  -19,
         31,  -48,  -28,  -26,   27,   32,  -39,   36,  -39,  -52,  -33,
         28,    7,    2,  -44,  -20,  -19,  -50,  -32,   46,  -60,  -82,
          5,   27,    5,    9,    9,  -28,  -50,   20,  -52,  -28,  -61,
         -4,    2,   -9,    9,  -35,   41,   26,  -30,   55,   -9,    6,
         17,  -44,  -27,  -41,   50,  -43,  -21,  -12,  -17,    5,   -2,
        -26,  -14,   10,   -3,   31,   -6,   15,  -15,    6,   18,   30,
        -10,  -29,   10,  -40,   46,  -13,   45,   46,  -13,   36,    5,
         43,  -41,  -47,   23,   13,  -44,   -8,   30,   52,  -21,  -25,
        -33,   -6,  -24,    9,   10,   24,  -26,  -29,   62,  -24,   35,
        -16,   50,   31,  -55,   49,  -63,   15,  -12,  -49,   15,   -6,
         13,  -26,  -13,  -21,  -10,  -44,   45,  -21,    2,   -3,  -18,
         -7,  -15,  -30,   51,  -18,  -47,    2,  -14,   14,   23,    5,
        -40,  -15,  -16,  -10,   -5,  -17,  -10,  -12,   26,  -20,  -23,
        -21,  -17,   70,   70,   -6,  -15,   48,  -66,   64,  -26,   28,
          3,    0,   17,  -18,   41,  -13,  -10,  -16,   26,  -32,  -52,
        -56,   30,   11,  -11,  -29,  -15,  -42,   29,   48,   -4,  -21,
         18,  -72,   34,  -12,   -8,  -47,  -27,  -12,   25,   25,  -28,
         34,   23,    9,   21,    1,    4,  -52,   21,   28,  -19,    4,
         34,  -40,   -7,  -66,   22,   56,   10,    4,    0,   -2,   35,
        -14,   65,   25,  -15,    7,  -24,   -3,  -17,  -17,  -64,   19,
         32,  -14,   38,  -31,   12,   30,   37,  -24,    8,  -71,  -43,
         34,   33,    3,  -49,  -38,  -52,    0,   46,    6,   -5,  -32,
        -66,   24,  -25,  -64,  -68,  -23,   16,    1,   47,  -35,  -11,
         21,    5,   32,    5,  -25,   -5,    2,   -9,   -1,    6,    1,
        -35,   -9,   15,    7,   60,  -15,   20,   42,   -2,  -13,   -5,
          4,   -7,  -45,  -44,   20,   21,   11,  -17,  -11,  -56,  -51,
        -11,    6,  -23,    0,  -51,   -3,    4,   10,  -28,  -41,   15,
         35,  -57,   52,   43,  -35,   35,    4,  -52,  -28,  -22,  -38,
        -39,   11,   45,  -14,  -41,   71,  -21,   -5,    3,   18,  -36,
         40,  -24,  -27,   45,   61,  -10,  -13,   52,   33,   30,  -47,
        -90,   29,   -1,   -7,   30,   48,  -37,   20,  -41,   43,  -23,
        -42,   26,    7,    5,  -68,  -50,   48,  -46,  -23,    7,   26,
         48,   28,    0,   -8,   29,  -19,  -46,  -57,   -1,  -50,  -18,
        -11,  -31,   -3,   31,  -51,  -33,   -1,  -21,   24,   23,  -20,
        -35,  -30,   29,  -62,   19,  -20,   -6,   23,   33,   34,   13,
         -1,  -51,   -5,  -27,  -74,    0,  -19,  -46,    7,   -2,   26,
        -15,  -94,    4,   35,   23,   13,  -54,   34,  -21,   19,   49,
         42,   38,  -34,  -35,  -23,  -20,   11,  -50,  -26,  -40,   11,
          5,  -15,    9,   32,  -41,   11,   12,  -36,  -30,  -30,   33,
         18,  -34,   23,  -27,   20,  -60,   26,  -16,   44,    2,   45,
         38,   -2,  -23,    9,   -8,  -16,   30,   20,   -5,  -13,   -8,
        -21,   36,   -1,  -26,    7,   -1,  -63,  -43,  -41,   13,   79,
         26,   25,   40,  -37,  -12,   42,    3,  -42,   32,  -39,  -30,
        -23,   -8,   19,  -62,  -66,  -10,   67,    3,   -9,   25,  -10,
         50,    1,  -37,   37,  -23,  -78,  -22,   61,  -38,  -54,   27,
         28,   47,   21,    4,   20,  -23, -102,   18,   33,   46,   41,
        -21,   48,  -22,  -27,   22,   37,    9,  -36,  -22,  -51,   63,
        -20,    2,   15,   44,   12,   14,   18,   44,   -3,  -33,   -4,
         28,  -52,   12,  -21,  -12,  -37,  -27,  -56,   19,  -15,   35,
          8,  -56,  -80,   21,  -14,  -55,  -69,   18,  -25,   -2,   20,
         56,   55,   -3,  -78,  -32,  -30,  -75,  -57,  -38,   22,  -38,
          0,   51,   55,  -23,  -62,  -48,  -31,    2,   26,  -22,   38,
         48,   -1,   38,  -27,    5,  -42,   28,    5,  -32,  -26,   34,
        -18,   42,  -10,   14,   -7,   17,  -49,  -41,   38,  -16,   17,
         -4,   23,   24,    4,  -60,  -17,   17,    9,    9,   35,    3,
        -24,   -4,   -3,  -30,  -33,   28,  -42,  -24,  -82,  -55,    9,
        -29,  -62,  -23,   13,  -44,   14,  -23,   39,  -51,  -54,    0,
        -39,  -32,  -23,    0,   41,   -4,  -42,   -5,   -9,   32,  -63,
        -31,   -4,   -8,  -27,   31,   30,   36,  -13,   37,   41,  -35,
          4,    7,   41,  -17,  -16,  -11,   26,  -20,  -29,  -25,   28,
        -34,   41,   -7,   55,   56,   14,   50,  -16,   -1,  -42,    4,
        -24,  -42,   20,   13,    4,   40,  -41,  -13,  -31,  -16,  -80,
        -43,   28,   -9,  -69,   17,   66,  -73,  -15,  -36,   28,   15,
         -2,  -39,   82,   -3,   -1,  -15,    0,  -27,   11,  -34,    4,
         -2,  -38,   62,   -9,  -32,   -1,  -19,   21,  -38,   36,  -54,
        -19,   -5,   28,  -15,    5,    2,  -60,    1,  -25,   41,   34,
         38,  -24,  -36,   26,   44,    7,  -44,  -57,  -12,    8,   41,
        -29,  -13,   13,   58,    8,  -12,   52,  -31,  -30,  -61,    3,
         51,  -73,   51,  -11,  -34,  -73,   34,  -23,   15,  -47,   43,
        -27,   33,   35,   41,   42,  -64,   13,  -37,   11,  -54,   11,
        -38,   30,   -4,  -29,   -2,  -25,  -42,   18,  -13,   42,  -12,
         -8,   32,  -75,   52,   24,   26,  -20,  -38,  -30,   26,   13,
          2,   31,  -21,    7,   26,  -47,    4,  -11,    9,  -10,   11,
        -28,  -54,  -23,   -3,  -38,   45,   -4,  -18,   16,  -23,   -2,
         46,  -25,  -42,   41,  -35,   44,    2,  -11,  -35,    5,  -19,
        -70,  -19,  -44,  -26,  -21,  -32,   42,   30,   27,   -7,   43,
          7,  -25,  -49,   24,   23,   12,  -18,   54,   18,    2,  -50,
        -43,   -5,  -63,   -4,   25,  -49,    3,   28,  -60,  -58,   37,
        -74,   19,  -34,  -24,    6,    0,   -3,   12,   -2,   -8,   -2,
        -44,  -34,   27,   41,   32,   -5,   52,   -4,  -25,  -22,   -5,
          3,   34,   30,   51,  -11,  -35,    3,   52,  -20,  -41,   39,
         36,    2,   31,  -14,    5,  -29,  -15,   13,  -11,   13,  -19,
        -64,   57,   14,  -44,   37,  -14,   18,   10,  -12,    9,   32,
        -76,  -14,    5,   12,  -24,  -41,  -19,   36,   27,  -17,  -25,
        -21,  -14,  -57,   13,    4,  -37,  -34,   33,   48,  -44,   53,
         19,   43,   53,  -33,   22,   22,  -17,    5,  -33,  -41,   29,
        -14,   23,  -48,  -17,    0,  -24,  -25,  -34,  -46,   10,    7,
         -7,  -11,    9,   26,   28,   22,  -14,   25,  -22,   21,  -61,
        -48,  -21,   -4,  -18,   19,    6,   39,   -8,  -13,   21,    0,
         41,  -56,   -5,   30,   43,  -29,   53,   55,   47,   -3,   -8,
         37,   -7,   39,    6,   35,    3,    5,   73,   27,  -11,   -5,
         47,  -30,  -16,   48,   -2,   25,   16,  -11,  -10,   63,   21,
        -10,  -34,   13,    7,  -31,   27,  -36,    2,   -9,    4,  -21,
         14,  -33,   -1,   39,   12,  -30,   16,    9,   17,  -26,  -54,
         -7,  -12,  -28,  -22,   10,  -11,   15,    9,   19,   36,   22,
        -79,  -61,  -41,   55,   11,   51,   19,   -3,   -8,    6,   14,
         21,   -7,  -60,  -30,   23,  -56,   24,  -19,   44,   -1,  -13,
         -4,   52,    0,   -4,   12,   28,  -47,   13,   23,  -21,    6,
        -31,  -21,  -17,  -10,  -53,  -26,    9,  -52,    4,  -10,    1,
        -38,  -10,   55,   43,  -57,   -7,  -45,   -4,  -29,  -21,  -54,
         49,  -15,    5,  -27,  -13,  -89,  -14,   37,  -31,  -51,   28,
         14,  -25,   17,   -7,  -29,   32,   24,  -40,   17,  -21,   -4,
        -23,    2,   17,   19,   31,  -47,   35,  -21,   -1,   48,   37,
        -23,  -72,   32,   31,   54,   18,  -59,  -18,   45,  -17,   18,
         13,  -11,   -6,  -43,  -28,   -1,   14,    1,   -9,   15,  -31,
        -19,   49,   41,  -45,   10,   10,   24,  -28,  -48,  -37,  -13,
         62,    5,   48,  -19,    7,   24,   50,   19,  -32,    1,  -14,
         13,   46,   32,  -30,    3,  -18,  -27,    9,    0,  -22,  -23,
        -12,  -98,  -19,   -7,    0,   34,   51,   17,   63,   16,   -3,
        -52,  -37,  -74,   -3,  -12,   19,  -48,  -45,   20,   61,   10,
        -14,   16,   -1,   10,   30,   11,   10,    8,   -1,   38,   52,
         37,    9,   52,  -35,  -11,    8,  -26,  -41,   40,  -20,   17,
         -4,  -48,   28,  -20,  -54,  -81,   31,  -67,  -34,  -38,   32,
          8,   44,    1,   -9,    3,  -30,  -32,  -50,   33,   10,   28,
         53,  -13,   13,   -4,   56,  -31,   48,   20,  -37,  -34,   21,
         26,   11,   10,  -18,    8,   31,  -33,   78,   -1,   -7,    7,
        -36,   31,   12,  -19,   56,    8,   38,  -54,   23,  -25,  -51,
          8,   17,  -51,   26,   16,   62,   42,   15,  -91,   -9,    3,
         20,   28,   11,    1,  -38,   40,   47,   37,  -43,  -62,   35,
          9,  -17,  -42,  -44,  -21,  -30,   -4,  -27,  -18,  -11,  -56,
          7,   -3,  -36,  -15,  -12,    7,    1,   31,   35,   17,  -43,
         -1,   -3,  -54,   26,   29,   22,   31,   32,   31,   -2,   -3,
        -40,  -43,  -36,  -41,  -73,   19,   26,   12,   40,  -12,  -30,
          8,  -41,  -47,    7,  -52,   -2,   14,  -21,  -23,  -28,   52,
         51,  -62,  -36,   30,  -54,  -33,  -22,   36,  -37,   49,   27,
         35,   43,   71,   -3,   50,  -28,  -86,  -49,  -48,   51,   12,
         44,  -26,  -36,  -10,   10,   28,   30,  -21,   52,  -12,  -12,
         45,  -50,  -23,  -10,   14,   -1,   38,  -28,    4,  -46,  -30,
        -58,   -7,  -45,   -9,  -32,   33,  -21,  -23,  -40,  -86,  -65,
        -55,  -30,    1,  -19,  -47,  -21,  -34,   14,  -23,   28,   -7,
         15,  -29,   37,  -67,  -35,   11,   11,  -15,  -14,  -41,   17,
        -40,   15,    1,   26,   10,  -22,  -64,    8,  -13,  -30,   -5,
         20,  -38,   10,  -19,  -20,  -12,   -2,  -63,  -10,   13, -116,
        -16,  -24,    8,    6,   11,  -38,  -44,   -1,  -41,  -28,  -43,
        -71,  -31,   57,  -86,   -1,  -80,   12,  -12,    7,  -54,   -5,
         16,  -24,  -92,  -20,  -23,    9,   -2,  -53,    1,  -35,  -39,
        -26,   26,  -99,  -20,   20,  -66,   12,  -66,  -58,   -7,   -4,
          3,  -53,  -65,  -35,   -4,  -44,  -78,   33,  -57,  -46,   18,
         29,   31,   32,   32,   20,  -26,   10,  -25,  -35,  -40,  -31,
         17,   -6,  -36,    8,  -44,  -43,    7,   31,  -55,  -22,  -51,
        -30,   50,   -7,  -57]]; fc_w0 = np.asarray(fc_w0);

  fc_w1 = \
     [[ 22,  11,  47,  54,   9, -45,  43, -50, -27,  16,  -6,  -3, -45,
        37, -69,  -2, -16,   5,  15,   4,  14, -13,  -9,  -4,  13,  28,
       -52, -10,  20,   2, -68, -32, -23, -39,   6,  10, -27, -21,  18,
       -42, -53, -39, -15, -48,   0,  14,  13,  35,  -6,  15,  65,  38,
        19, -44,  29,  27, -15,  44,  -2, -11,  65,   9, -21,  28,  28,
       -22, -16,  25, -44,   8, -47, -38,   2,  27,  58,  63,  48,  -4,
        45, -39,  22,  36, -53,  37,  49,  -7,   6,  35, -42, -42,  37,
        54,   5, -19,  68,  -1,  41, -13,  43, -59,  -6, -48, -47,  20,
        32,  52,  26,  33,   4,  17, -29,  -1,  41, -16, -11,  23,  32,
        34,  12,  36, -55,  35,  51, -46, -22, -26, -10,  22, -68, -57,
        18, -39, -16, -23,   5, -60, -28, -36, -48, -66, -56, -51, -34,
       -67,  47,   4, -38,  -6, -10, -67, -62, -20, -37, -54, -43,  35,
        16, -39,  -9,  43,   3, -40,   5,  30,   6,  -5, -18,   5, -14,
        19, -47, -25,  15,   9,  56,  27,  -3, -27,   8,  24, -14, -34,
       -53, -38,  -2,  53,  16, -31,  39, -32, -46, -38, -52, -14, -11,
        10, -17,  25, -22, -43,  -5, -42,  30,  32, -36,  -9,  30,  19,
        24,  12, -11, -30,  50,   0,  17,  39,  -1, -51,  13,  52,  38,
        16, -28, -31,  46, -36, -40,   6,  37, -37,  56,  14,  49,  49,
        14, -26,  39, -36, -14,  63,  60, -56, -38,  60,  75,   2,  18,
        56, -38, -43, -22,  61, -39,  -1,  40,  21,  15,  19,  37, -20,
       -22, -15,  -9,   8, -53,  35, -48,  76,  29, -10, -14,  30,  -3,
       -15,  -7,  18, -32,  37,  10,  49,  -9,  45,   4,  33,  -8, -23,
        20,  10, -50,  22,  -3,  18,  61,  -7,   4, -40,  -3, -21,  -3,
        51,  17,   3,  -4,  -1,  27,  29, -56, -29,  45,   9, -26,   1,
        64, -21,  22, -11,  11, -57, -29,  30,   4,  67,   3,  17,  13,
        61,  20, -27,  11,  78, -34,  32, -33, -38,   7, -14, -34,  20,
        31, -43,  10,  48, -13, -52, -43,  10, -15,  22, -20,   4, -27,
       -45,  -7,  44, -12, -10, -32,  -4,  42,  15, -19,  25,   4,  39,
         3,  -8, -54,  35, -28, -21, -68, -25, -64, -23,  39,  19,   3,
        45, -27,  -6,  21,  11,  29,  -3,  19, -15,  15, -18, -12,  18,
       -35, -35, -40,  -4, -49,  34,   3, -82,  16,  67, -19,  24, -31,
        -1, -12, -24,   9,   5,  19, -18,  15,  82,  25, -61,  -7,  33,
         2, -19, -28,  15,  27, -36,  34,  -6, -39, -41, -45,   7, -47,
        29, -23, -21,  12,  -5, -24,  50,  48, -36, -31,  39,  18,   5,
       -17,  -6,  29, -23,  29, -57,  21,  42,  24,  36, -30, -61, -25,
       -58,  -5, -60,   7, -36,  21, -58, -39,  -7,  29,  32,  41,  11,
        -6,   4, -47, -35,  17,  11,   3,  28,   4,  36,  -2,  25,  25,
        -4, -19,   5, -27, -47,  44,  24,  65,  37,  14, -36, -19, -46,
         3,  12, -42,  -3, -23,  36, -34,   9, -16,   1, -60, -41,  15,
        30,  -5, -17,   6, -21, -44, -20, -28,  -9, -29,  10,  20,  -2,
        22, -51,  -5,  19, -19,  19,   7,  21, -31, -40, -12,  21, -27,
        -6, -57, -30, -35, -52,   5,  -5, -18, -68,  51,  -5,   8, -21,
       -31,  35, -13,  17,  27,  18, -14, -59, -13,   4,  11, -33,  18,
        27,  46, -22, -40,   9,  14, -73, -25,  24,  26, -28,  19,  41,
        40, -56, -39, -48,  37, -70, -28,  41,  27, -13,  -9,   5,  -5,
       -35,  49,  33,  29, -31, -59,  56, -50, -21,   5,  46,  28,  -3,
        29,  22,  43,  18,  33,  20, -46,  -4, -10,  43, -49, -32, -15,
        24,  26, -15, -70, -12,  33,   2,  18, -58, -15, -14,  -2,  -2,
       -61,   6,  -7, -22, -13, -44, -10, -32,  52,  40,  27,  62, -59,
       -53, -34,  53, -57,  32,  22, -55, -69,  -8,  36,  22,  21, -18,
        25, -13,  33, -31,  14,  26, -36, -51,  30,  22,  23, -16,  19,
       -67, -10, -20, -28,  -2,  -9, -29, -37, -50,  -1,  22,  14, -18,
         6, -16, -25,  28, -48,   4,  -5,  55, -63,   0,  27, -13,  -1,
       -43, -20,  26, -35, -35, -65,  11,  22, -23,  65,   4, -41,  24,
        21, -43,   0, -49, -52,  10, -48, -55, -26,  -3,  40,   4,  13,
       -13,  19, -37,  45, -11, -33,   1, -30, -25,  10,  13, -12, -33,
        10, -17,   4,   7,  33,  -3,  22, -21, -46, -20,  29,  34,  10,
       -37, -16,  35,  35,  16,  28,   7,  43,  -6, -50, -42,  46, -41,
         1,  -6,   8, -81,  32,  41, -16,  55, -45, -34, -47,  13,   4,
        44, -36,  35,  39,   0, -39, -22,  35, -20,  25, -41,  10, -48,
        21,  27, -36,  70,  65,   1, -13, -33,  30, -20,  51,  39,  16,
       -40, -57,  33, -11,  20, -42, -10, -49, -54,   6,  59,  -3, -45,
        19,  25,  -7,  45,   8, -64,   5,  25,  20,  -4,  21,   3, -53,
        27,  38, -38,   6, -40, -40, -43,  65,  10, -21, -14,  -6,  41,
        -1,   8,  -8, -37,  10,  59,  24, -41,   0, -22,  39,   3,  -1,
        -9,  10, -49,  12, -19, -55,  17,  40, -73,   5,  48,  -1, -47,
        34, -36,  24,   1, -18,  61, -33, -54, -43, -47,  34,  61, -26,
       -17,  70,  -7,  51,  48,  27,   8,  20,  33,  31, -21, -29,   6,
         2,  -8, -28, -39,  11,  -9,  12, -40, -32,  -5, -12,  14, -38,
       -19, -64,  -6, -26, -26,   2,  34, -28, -90,   5, -59, -66,  23,
        -8,   5, -29,  37,  14,  -7, -28, -15, -82, -19,   2, -29,  -7,
        11,  12,   8,   8, -55, -31, -39,  35, -34,  -5, -40, -25, -40,
        -5, -27,  54,  -8,  -3, -60,  68,  44,  49, -10,  -1,  40,  49,
        -2,  32,   6,  59, -21, -17, -21,  48,  -3,   0,  23, -49,  23,
       -63, -44, -58,  14,  43, -22, -35,  32,  18, -32,  -9,   5,  -2,
         6,  -3,  26,  13,  17,  -8,  19,  16,   8,  14, -25,  -6,  22,
       -10,   3, -17, -19, -41, -18, -30,  39,  34,  17,   6,  65, -40,
       -61,  42, -13, -43,  21,  -4,  50, -44, -69,   7,  35,  16,   5,
        -3, -25,  18, -16,  36,  23,  37,   4, -45, -62, -14,  -6,  -1,
        58,  39,  27,   9,  16,  10, -31,   8, -38,  10, -31, -49,  33,
        22, -82,  29,  13,  19,  -8, -28, -23,  39, -69, -36, -27,  20,
        12, -18, -19,  26,  42, -39, -47, -12, -20,  46,  -2, -47, -62,
        -1, -10,   6,   7, -16, -65, -21, -33, -54, -72, -15, -46, -16,
       -36,   1, -43,  14, -28,   3,  12,  65,   9, -13, -18, -35,  60,
        62,  67,  50,  35,  65,  15,  14, -51,  13,  36,  61, -11,  60,
       -19, -26,   3,  80,  -2,  -5, -17,  17,  -2,  67, -24,  57,  -8,
       -21,  28, -42,  11, -55, -48, -63, -35,  23,   5,  -4,  35,  42,
       -50, -19,  22, -31,  -9,   7, -55,  57, -26,  14, -24,  -9,  59,
       -26, -45,  -6,  37,  20, -27,  47, -50,   4, -14,  18,  48, -40,
       -23, -46, -14,  17, -10,  88, -55,  14, -14,  33,  46,  43,  14,
        27, -19,  18,   0,  17,  43,  52, -42,  18,  34, -25,  19,  11,
       -12,   4, -59,  46, -10,  29,  16, -41,  61, -41,  -8, -50,  57,
        30, -67,  28,  -7, -43, -12, -60,  19, -26,   8,  27,  -5, -17,
       -55, -17, -60,  40,  19,   5, -10, -25, -34, -16,  -9, -44,  22,
       -19, -58,  62,  48,  38, -54,   2,  21,  42,  25, -15,  -6, -21,
        43,  53,   5,  -2, -29,  37,  26, -24,   0,  -8,  11, -40,  22,
       -24, -32,  25,  38, -35, -21,  12,  19,  18,  25,   9, -15,  18,
        -1, -39, -37,  40, -56, -49,  21, -56, -60,  38,   9, -27, -21,
         1, -28,  -2, -45, -61, -17,  28, -16,  30,  42,  39, -40,   1,
        40,  19,  26, -38,   2,  24, -26, -29,  61,  11, -54,  20, -23,
       -26, -18, -23,   2, -16, -48,  24,  16, -33,  37,  58,  -3,  29,
       -35,  -2, -58,  19,  -3,  61, -15,   8,  14,  34,  46,  33, -29,
       -69,  46,   5, -11,   1,  -1, -28, -50, -38, -27,  33, -29, -38,
        52,  25, -69,  48,  35, -58, -43,  32,  22, -18,  -1,  21,  -8,
       -56,  10,  -6, -46, -79, -22,  39, -19,  -7,   0,  39, -50,   8,
        33,  -3,  31, -47,  56, -49, -45, -17,  42, -27,  26, -17, -25,
       -60, -12, -46, -31,  35,  42, -25,  36,  34, -18,  38,  34, -25,
        22,  16,  18,  -2,  34,  25,   7,  16,   7,  -8,  17,  -4,   7,
       -24,   7, -63, -30,  23, -37,  13,  46, -15, -59,   1,  33,  43,
       -36, -22,   0,   5, -20,   7,  27,  39, -10,  18,  -7,  -3, -16,
        -6,  -4,  23,   6,   3, -32, -42,  13,  32,  28,  41, -43,  44,
       -23,  15,  55, -17,  44,   4,  20,  -1,  -3,  44, -35, -11, -38,
        16,  13,  51,  14, -54,  -6,  53,  46,  49,  -4,  21, -17, -36,
        15,  58,  -4,  15, -51,  61, -35,  17,  28,   3,  -3, -24, -13,
       -44,  35,  43, -18,  -3,   1, -13,  11, -42, -28,  20, -17,   0,
         1,   0, -43, -17,   3,   1, -18, -26, -57,  -6,  14, -13,  -3,
       -42,  33, -31,  -9, -51, -21, -27,  -6, -37, -13, -45, -29,  33,
        57,   3, -58, -40, -25, -37,  17, -42,  50, -30, -21, -25,  59,
        17, -17, -12,  12,  65,  12, -10,   4,  23,   3, -20,  18,  23,
       -37,  17,  20,  -2,   3,  15, -30, -32,   1, -14, -21, -35, -38,
        34,  -5,  26,  10,  -3,   5, -37, -45, -56,  -9, -23, -22,   0,
         8,   1,   0,   4, -41,  12,   4,  31, -36,  12, -45, -35,  -9,
        53,  12,  44, -53,  69,   1, -34,  34, -22, -38,  56,   2,  23,
        29, -14, -26,   9, -11,  45,   3,  67, -20,   7, -22,  42,  26,
         6, -22, -44,  39, -31, -45,   1,  24,  27,  -4,  52,  54,  11,
         5, -22,  -2,  22, -43,  40, -29, -15, -13,   0,  -1,  40,  24,
        -8, -53,  32,  10, -22,   7, -14,  41, -16, -91, -15,  11,  -8,
       -32,  -5,  13,  15,  40,  29,  24,  36,  16,  -3,  38, -34, -17,
       -28,   5,  62,  24, -21,  75,   5, -68, -27, -25, -27,  20,  45,
       -12, -32, -10,  -6, -18,  48,  43, -26,  37,  18, -30, -17,  16,
         3,  55,   2, -10,   3,   0, -19,   2, -20, -12,  13,  27, -18,
       -33,  29,  23,  -4,  25,  55, -37,  51,  37,  44,  -8,   1,  68,
       -35, -37,   7,   7,  14, -23, -52, -41,   4, -45, -45, -26, -35,
        53,  26,  48,   7, -51,  -5,   1,  48,   9,  39,  15,  72, -28,
        29, -25,  44,  16,  22,  14, -20,   2,   7,  23,  29,  11,  29,
        59,  40,  -3, -35,  40, -12, -52,  26, -14,   1,   3, -24,  68,
       -13, -45, -46, -37,  56, -23, -32,  -1, -10, -31,   8,  17,  20,
       -16, -11,  -4, -22,   0,   9, -33,   9,  -7,  17,  52,  44,  22,
        18,   4,  16, -21,   9, -15, -29,  13,  26,  -1,  48,  22, -11,
         2, -15, -16,  48,  -1,  -5, -20,  -8,  35,  60, -39,  -6,  18,
        39,  64,  26, -18,   6, -32,  50, -28,  14,  64,  -6,  23,   5,
        56, -18,  18, -17,   0,   2,  41, -44,  41,  48,  37,  60,  50,
         3,  53,  15,  22, -27, -20,   6, -66, -52,  24,  -8, -31,  21,
       -33,  38,  49,  34, -14, -25, -12, -38,  34,   8,  42,  12, -36,
        37,  34,  30,  44, -39, -67,  50,  30,  15, -38,  25,   3,   0,
       -14, -51,  16,  15, -28,  -6,  27, -24, -19,   3, -24, -52, -47,
        47,  17, -13,  28, -21, -19,  34,  12,  -7, -45,  36, -16, -40,
       -26,  48, -27, -70, -35,  45,  28, -16,  56, -11,   9,  37,  43,
         4, -34, -33, -12, -41,  12,  -1,  60,  16, -23, -19,  20,  -2,
        40,  27,   0, -42,   6, -16, -19,  24,  31,  66,  33,  20,  -2,
       -39,   0, -30,  59, -29,  35,  60,   1,  43,  -4, -20,   1, -20,
        10, -31, -26,  -3,  54, -44,  38,  76,  21,   6, -40, -62,  18,
       -23,  27,  33,  47,  32,  20, -27,  29, -51,   7, -38,   0,  45,
        58, -31,   8, -38,  33, -28, -23, -58, -66,  20,  53, -36,  18,
        20,  15, -84, -53,  -3, -14, -81, -34,  52, -35, -68,  52,   9,
       -91,  15,  69,  53,  70,  30, -73,  52, -39, -26,  27,  71,  13]]; fc_w1 = np.asarray(fc_w1);

  fc_w2 = \
     [[  -6,   35,  -15,    1,  -40,  -51,  -57,  -62,  -60,   37,   49,
        -46,  -16,   35,   -5,  -14,  -16,  -18,   40,  -26,  -49,    4,
        -36,   45,    5,   47,  -43,  -34,   -2,  -46,    6,  -55,  -42,
         18,   -2,   39,  -15,   13,    7,    8,  -33,  -34,   53,   16,
         28,   -8,   35,   40,  -82, -123,  -24,  -47,   37,    0,   12,
        -32,   -7,    1,  -19,   11,  -23,    9,   31,   32,   12,   10,
         52,   34,   21,  -41,   19,   29,   57,  -15,  -18,    8,   -4,
          8,   13,  -29,   30,  -40,   12,  -19,  -67,   43,   39,  -52,
         -1,   -7,  -12,   39,  -24,  -24,   -5,  -12,    5,  -44,  -52,
        -11,    4,   30,  -26,  -51,   34,   56,   48,   27,  -50,  -16,
        -43,   -3,    3,   36,   14,    6,  -33,  -48,   23,  -34,  -22,
          0,   53,  -33,   48,   16,   32,  -20,  -36,  -31,    3,  -22,
         -2,    0,    0,  -21,  -20,   10,  -34,   37,  -17,  -15,   42,
        -55,  -64,  -70,  -33,  -28,  -24,  -37,   17,  -33,  -52,  -13,
        -54,   18,  -21,  -54,   20,  -49,    2,   45,  -14,  -21,  -37,
        -40,  -37,   23,   -3,   19,    7,   24, -108,  -36,   26,   16,
        -26,  -38,  -73,   57,   18,  -40,  -18,  -15,   27,  -45,   -3,
        -33,  -34,  -20,  -29,    1,   22,    4,  -30,   39,  -27,   19,
         26,   36,   40,   48,   44,   13,   39,   25,   46,  -16,  -49,
        -15,   59,   19,   41,  -18,   32,  -11,    9,   51,  -33,  -35,
         -1,   22,  -26,  -20,  -37,   53,    4,   20,  -39,   52,   17,
         11,   43,    2,   26,   20,   39,  -20,   50,   20,   46,   10,
        -12,   -2,   -4,  -12,  -16,   24,  -36,   30,  -43,   15,  -26,
          5,   29,  -32,   40,  -12,  -36,   35,    3,  -49,  -21,   30,
         27,   20,   -4,   11,   -4,    4,    6,  -13,  -16,  -10,  -24,
         -8,   -7,   42,  -69,   46,  -21,   16,   24,  -44,  -17,  -20,
        -54,   14,  -49,   19,    8,  -37,  -25,   26,  -43,  -29,  -47,
         -1,   48,    2,   16,  -48,  -66,   33,  -26,    2,  -10,  -58,
        -54,   19,    9,   16,   18,  -46,    1,  -14,   18,   11,   30,
         59,   45,  -26,  -13,  -28,  -48,  -34,  -11,   24,   16,    9,
         57,  -11,   50,    3,   11,   27,  -19,   12,   -3,   38,   57,
        -41,  -41,   39,   20,   -9,  -32,   17,   43,   20,   43,   30,
        -32,   15,    3,  -31,  -18,   24,   -1,   43,   50,   50,   50,
        -23,   15,  -56,   44,  -19,    1,  -13,  -10,  -37,  -10,    9,
         39,    7,   16,  -18,   37,   -2,  -18,   25,  -40,  -14,  -13,
         58,  -49,  -22,   35,  -25,   34,  -24,   -8,   45,   29,  -20,
        -24,   24,  -33,  -13,  -25,   22,  -15,    1,   33,   30,   37,
         20,   19,   55,    5,  -72,    2,   19,  -41,   23,   26,  -54,
        -46,   -7,    6,  -38,  -18,  -63,    5,  -24,   33,  -45,   24,
        -41,   -9,  -19,  -26,  -46,   26,  -27,    2,  -49,  -38,   45,
        -11,   20,  -33,  -43,   23,   17,  -15,  -80,   19,  -48,   -8,
         -6,    8,  -35,  -43,  -55,  -68,   13,  -28,   33,   16,  -44,
          2,  -61,   26,   -7,  -60,   39,   17,    3,  -23,   15,  -42,
        -29,  -17,   12,   43,    9,  -17,   -2,   -7,   10,    5,  -45,
        -32,  -37,  -27,    2,  -37,    3,    4,  -39,   45,   26,  -11,
          8,   37,  -61,  -11,    4,  -17,    9,   77,   20,   62,   -4,
        -50,   34,  -24,  -58,   25,   49,   10,  -16,    4,    0,   26,
         32,    2,   14,   16,    9,   27,   43,   -6,   -3,   62,   13,
         48,   -7,    6,  -18,    9,   24,  -47,   29,  -49,  -37,   39,
        -40,  -13,   58,   23,    2,  -16,   43,   13,  -11,   42,    5,
         10,   16,    7,   24,   -7,   -5,   12,   11,    4,  -39,   22,
         37,  -43,  -23,   25,   37,  -32,   -2,   -9,   18,   -6,   15,
         35,   -5,    3,  -23,  -10,  -14,  -20,    3,   14,    8,    7,
        -28,  -27,  -32,   11,   34,  -46,   -2,  -31,   -9,  -37,  -54,
         25,    8,   24,   10,  -39,  -15,  -32,  -65,  -13,  -70,   43,
        -14,   13,   -8,  -48,  -11,   39,  -25,  -38,  -37,   29,  -49,
        -71,  -39,  -16,  -56,   17,   14,    2,   19,   20,   -5,   -1,
        -19,  -40,  -32,   33,   23,   39,  -45,    7,    4,  -16,   45,
        -13,  -38,  -15,  -29,   38,  -19,   65,  -12,   61,   16,   -9,
         50,  -54,  -40,    9,   21,   54,   -4,  -10,   21,   69,   -9,
         15,   27,   -8,   15,  -20,   -4,  -50,   50,  -31,  -24,   11,
         -2,  -26,   72,  -46,   21,  -13,  -25,   32,  -37,   -1,    1,
         31,  -37,  -20,   -9,  -37,  -46,  -28,  -12,  -35,   24,  -36,
        -21,   24,  -32,   52,   33,   16,   -1,   16,   28,    7,  -20,
        -56,  -24,    9,    0,    6,   10,   56,   -6,   14,   55,  -33,
         15,  -56,  -35,  -13,  -27,    4,    3,   33,   16,  -14,   -7,
        -12,   12,   31,  -17,  -37,   -6,   35,  -10,  -19,   15,  -37,
        -39,    0,  -37,   13,   20,  -30,   23,  -25,  -33,   13,  -72,
        -34,   -6,  -30,   19,    9,  -48,   23,  -12,   18,  -49,  -40,
        -60,   17,  -51,    8,   -2,   10,   35,  -43,  -23,  -40,   17,
         37,   36,  -55,   46,    9,  -48,   -5,    5,   29,  -24,  -20,
        -14,   -6,   38,  -11,  -52,   18,  -25,   36,   66,    0,  -67,
         38,  -17,  -22,   26,   33,    7,   33,   31,  -44,   19,   -4,
          8,  -14,   58,  -31,  -30,   46,   64,  -37,   -9,   31,   44,
        -19,   30,  -19,   22,  -27,  -34,   11,   56,   28,   16,  -56,
         56,   60,   23,  -38,   -9,  -54,  -66,  -16,   22,  -27,  -30,
        -42,   13,   67,   11,   17,   43,  -11,  -49,  -26,    4,   33,
          0,  -20,  -48,    6,   13,   40,  -22,   14,    0,  -43,   16,
         32,   17,  -25,   36,   11,   23,    2,  -36,  -38,   12,  -39,
         56,   21,  -14,  -43,  -38,    5,   48,  -16,   38,  -24,   53,
        -33,    9,  -41,   -1,  -16,  -43,   34,   33,   30,  -42,  -36,
         44,   -1,  -23,   -7,   18,   24,   31,  -14,  -38,  -24,  -32,
        -15,   40,  -55,  -12,  -26,   41,   -4,   -8,  -36,   -9,   47,
        -27,  -17,   57,   -5,  -30,    7,   16,  -35,  -20,   64,  -23,
        -11,   -6,   31,   58,   39,   11,  -23,   49,   -9,   15,  -17,
         37,    7,  -41,  -29,   11,  -13,  -77,  -41,   37,  -13,   -9,
        -44,   33,   27,   49,  -43,  -37,   51,   13,   13,   68,    0,
         24,   67,  -17,  -32,  -26,  -12,   17,  -51,    2,    2,   37,
         13,   51,  -32,    3,   49,   34,  -51,  -47,   -6,   39,   49,
        -38,  -48,   53,   30,   11,  -18,    2,   19,  -32,  -89,   14,
         47,   20,  -65,   53,  -35,   29,   24,  -71,  -13,  -31,   13,
         64,   71,  -46,  -42,   74,  -43,   37,  -40,  -51,  -27,  -39,
          1,   58,    5,   18,  -29,   -6,  -38,   43,    7,  -59,  -22,
         18,   -5,    2,   42,    6,   22,   16,   29,   23,  -23,  -16,
        -33,   74,  -21,  -64,   20,   16,    2,   12,  -12,   17,    7,
        -25,    9,   39,  -54,  -56,  -20,  -19,    8,   30,   12,  -14,
        -10,   20,  -52,   42,  -15,  -38,   16,    7,    4,  -35,   23,
        -19,   12,   60,   63,   34,   20,  -64,   -7,   27,   37,   52,
         34,   12,   15,    1,   65,   35,   -8,   20,   49,  -21,   14,
          1,  -25,   59,  -49,  -28,   -7,  -19,  -45,   -4,  -34,  -21,
          6,   22,  -16,  -29,   33,  -18,  -35,   50,  -24,  -40,   39,
         10,   -3,  -32,  -29,  -42,  -35,    4,   19,   36,   -5,  -53,
         69,   -8,   37,   53,  -27,   67,   57,  -48,  -31,   24,  -58,
         21,   19,  -41,  -10,   41,   -7,   -2,  -17,  -31,  -38,   63,
        -18,   34,   28,  -39,  -14,   10,   46,   37,   30,  -21,  -18,
         46,  -31,  -34,   55,   17,  -11,   15,   16,   60,  -33,   19,
        -11,   -1,  -21,   51,  -15,   30,    0,   34,    1,   60,   58,
        -52,   27,   -5,   22,   21,    1,  -14,  -34,   37,   40,  -12,
         47,  -44,  -29,  -20,  -49,  -31,   15,  -23,    9,   15,   55,
        -16,   28,  -32,   37,  -13,   14,  -44,   22,  -31,   18,   44,
         45,  -33,   20,   19,  -32,   46,  -29,   31,   55,   24,  -36,
         43,   -3,   14,   52,    7,   73,   39,   47,   12,  -22,  -29,
         32,   10,   32,   28,   45,   68,   58,   69,   20,   22,   46,
         57,  -45,   76,  -12,  -18,   20,    1,   47,   22,  -22,  -33,
         43,   23,   31,   23,   -5,   25,  -61,   12,  -26,   10,   28,
        -27,  -15,   64,  -33,   22,  -45,  -19,  -20,  -53,  -30,   47,
        -43,  -42,    2,   44,   36,  -24,   28,   48,   44,   -1,  -15,
         75,  -11,  -16,   15,  -23,  -17,   11,   34,   16,  -15,  -37,
        -18,   78,   -7,  -20,  -35,  -24,   18,  -24,    4,  -16,  -52,
         15,  -21,    8,   29,  -66,  -11,   -5,   13,   35,   58,   52,
         30,   15,  -25,  -16,  -18,   37,   16,   44,   46,   14,   14,
        -34,   39,  -29,  -10,   -3,  -33,    1,    4,   -5,   18,   17,
         63,   22,   -2,   -6,  -25,   26,    9,   56,  -19,    4,  -29,
         35,   15,  -15,   41,   28,   -3,  -20,   13,   15,   13,  -13,
         33,  -23,   -1,   41,   70,   46,  -36,  -72,   -1,   81,   10,
          8,  -37,   60,   33,  -13,    1,   62,   24,   35,  -21,    8,
        -12,   -8,   -5,   41,   60,   45,   62,   47,   46,   38,   28,
         19,   15,   20,  -16,   61,    3,  -29,  -47,   23,   45,   55,
        -12,  -31,   43,   17,  -48,  -36,   20,  -10,   48,   40,   -2,
         49,  -11,  -20,   -5,  -50,  -12,   50,   19,   17,  -13,  -18,
         -6,   17,   53,  -90,   10,   52,   49,   17,  -19,  -29,   34,
         23,   46,   44,   -4,  -39,  -19,  -38,   13,    5,   39,   50,
        -33,   11,   -3,   26,   20,  -30,   41,  -26,   58,   11,   -5,
         30,   41,  -18,  -37,   -3,   47,   -9,    7,   47,  -37,  -30,
          1,   -5,   34,   -4,   -3,  -10,   58,  -75,   23,   13,   14,
        -12,   58,    8,    0,  -16,  -12,  -34,    8,    2,    3,   33,
         15,   40,    8,   55,   29,   64,   35,  -93,  -13,   32,  -25,
        -33,   47,  -29,   41,  -10,   23,   17,    9,  -58,   27,   62,
         -9,   13,   22,   34,  -54,   32,   38,   74,  -27,  -59,   -9,
         34,   -6,  -39,   56,   49,   11,   19,    5,    0,   26,   34,
        -21,    0,   45,   16,   56,   53,   25,  -21,   20,   38,   18,
          1,  -17,  -14,   41,  -11,   50,   54,    0,   33,  -15,  -36,
         50,    3,   24,  -26,   -5,   30,   19,    6,  -17,  -20,   45,
        -12,   26,  -11,   -2,   41,  -24,  -16,   -5,   51,   53,   -3,
        -10,   12,   26,  -17,   26,  -62,   -4,   39,   24,  -32,   -2,
        -12,   45,   -3,  -26,   22,  -17,  -71,  -64,  -12,  -35,  -45,
        -16,   12,  -20,  -22,   23,   -1,    6,   -8,  -42,   -2,  -25,
        -25,   -6,  -40,   45,   56,  -29,  -15,    0,  -59,  -47,   20,
         20,   37,   -1,   17,  -24,  -33,   15,  -30,   32,  -25,  -21,
        -22,  -30,    8,  -25,  -24,  -23,   13,   -3,   33,   25,   18,
        -23,   34,  -38,   34,   16,  -46,  -44,   50,   24,   10,   52,
         53,   -4,  -50,   36,   13,  -18,   35,   31,   27,  -18,  -18,
        -25,  108,    2,  -44,    1,   56,  -17,   22,    6,   29,  -21,
         -6,  -16,   12,   80,  -33,   -1,   35,    0,   60,   -7,   54,
         -9,  -26,   58,   25,   48,   32,  -26,   51,   23,  -29,  -31,
         -7,   46,   31,  -22,   33,   65,   16,  -13,   10,  -43,    4,
          5,  -15,  -20,   26,   11,  -58,   19,  -48,    9,   29,    4,
          7,  -43,  -40,    3,   -7,   44,  -33,   -2,  -13,   18,   51,
         25,  -60,  -40,    3,  -22,  -21,  -36,  -36,   -5,   10,  -46,
         12,    4,   29,    2,   48,  -35,    5,   14,    4,  -16,   -5,
        -43,   18,   41,  -15,  -31,   35,  -39,   -5,   10,  -23,  -34,
         52,  -13,    7,  -40,   16,  -11,   14,  -43,  -39,    7,  -26,
        -10,  -42,  -31,   41,   15,  -15,   20,   35,  -34,   -4,  -13,
         33,  -54,  -57,  -15,   -3,   28,    1,  -59,  -21,  -31,  -25,
        -31,    8,    7,  -67,  -42,   -3,  -42,  -20,   24,  -10,    3,
         -9,   37,   37,    4,   23,  -19,  -33,   23,   24,   54,    9,
          5,   -5,   41,   30,    7,  -11,    8,   51,    9,  -31,  -32,
         -8,   36,   34,   41,   32,   -1,  -26,   -2,   -7,  -25,    2,
        -57,   20,  -34,   47,   31,    4,   10,  -41,   11,  -51,  -11,
         53,   20,   26,   18,   21,    4,    4,   70,   10,   45,   43,
         54,   42,   27,  -71,   25,    4,    1,  -34,   48,   26,    4,
         -2,   31,   28,   -9,   -9,    1,   15,  -59,  -51,  -92,  -26,
          8,  -27,   19,  -66,   38,   35,   17,   48,   -8,   34,  -22,
        -49,  -36,   27,  -48,    6,   35,  -62,  -62,  -42,  -30,    4,
        -20,  -59,  -24,  -48,   16,  -31,  -64,  -17,  -36,  -19,    3,
          5,   52,  -33,  -67,   12,  -38,  -50,   39,   41,  -44,  -54,
        -28,   37,   26,  -77,  -47,  -19,    7,   23,  -42,   -4,    5,
         -5,  -16,  -32,   44,  -93,  -25,  -45,  -56,  -54,  -18,   -6,
        -23,  -14,    9,    9,  -20,  -32,  -39,   -3,   15,   -9,  -40,
        -10,    5,  -77,    9,   38,  -64,   -5,   31,  -27,  -53,  -50,
         35,   34,   16,  -16,  -16,   16,  -23,  -21,   42,    5,  -15,
        -28,  -12,   -1,  -14,   22,  -14,   27,  -31,  -50,  -37,  -61,
        -26,  -51,   24,  -13,   33,   -6,  -51,  -40,  -13,  -10,  -25,
        -16,   38,  -37,   48,   60,  -29,   25,  -35,  -58,   31,  -26,
          4,   26,   33,   39]]; fc_w2 = np.asarray(fc_w2);

  fc_w3 = \
     [[ -45,   42,   20,    0,   43,  -52,    2,   14,   35,   21,   26,
        -11,    1,  -17,  -42,    6,   -4,  -58,   20,  -13,  -46,  -26,
        -36,  -47,  -49,   24,  -33,   25,   15,  -10,   -6,   21,   16,
        -52,   26,   18,  -26,   46,   41,   13,   75,   55,   61,    4,
        -48,   51,  -11,  -31,  -18,   35,  -28,   39,   -2,  -25,  -46,
        -12,   54,   20,  -26,   23,   -6,  -39,   13,    0,  -60,   32,
        -46,  -19,   18,  -58,   24,   -5,  -18,   30,    6,  -17,   33,
         -2,  -24,   13,  -16,   -9,   -4,   15,  -52,   31,   26,  -49,
         -8,   -3,  -37,  -35,   29,   36,    6,  -14,  -11,   16,   23,
         24,   -1,  -16,   50,  -37,  -21,  -17,   20,  -13,   20,  -14,
         29,   32,  -18,   47,  -39,  -43,   14,  -20,   44,   29,    9,
         53,    4,   57,  -14,  -40,   28,  -60,    5,    0,   10,  -21,
         30,   44,  -55,  -41,  -13,  -29,   14,    8,    8,   25,  -30,
        -10,   32,   21,   23,  -16,  -51,  -87,  -22,   14,  -91,  -12,
         -7,   47,    6,   34,   -3,    1,  -30,   38,   59,   75,   21,
         18,    4,   61,  -27,   14,  -13,   -3,   29,   83,   18,  -28,
         -3,   14,  -42,  -27,   -2,  -25,  -12,  -18,   10,  -32,   37,
         39,  -21,   11,  -27,   38,   32,   40,    5,  -27,   35,   27,
        -36,   10,   12,   38,   43,   51,   27,    6,   40,   -8,  -36,
        -35,   25,   42,   35,   15,   10,   -6,   34,   56,   46,    3,
        -15,   18,  -15,  -46,   51,    6,  -23,   52,    1,   53,   31,
         17,   21,   30,   30,    1,  -23,  -52,  -25,   33,  -15,    4,
         44,   11,  -33,  -14,  -12,    7,  -27,  -41,    4,  -51,  -16,
          9,   -3,    1,  -48,    5,  -21,   -4,  -12,   30,  -12,  -59,
         40,   14,   42,   31,  -15,   32,  -31,  -45,   29,    1,  -41,
        -62,  -41,   18,   55,   30,   43,   28,   50,  -47,   18,   -9,
        -34,  -58,  -29,  -36,  -22,  -49,  -36,    8,  -49,  -59,  -36,
          3,  -56,   12,  -50,  -40,   14,    7,   36,   33,   17,   31,
         -5,   20,  -42,  -74,  -55,  -10,  -11,  -18,    0,    8,   37,
         13,   43,   56,   41,  -44,   94,   39,   34,  -18,   62,  -27,
        -18,   -7,  -34,   45,    1,   29,   12,  -11,  -11,   -6,   37,
         33,   -9,   36,   25,   40,   62,   31,   30,   -5,  -14,  -29,
         55,  -27,   39,  -16,  -22,   51,   13,   53,  -23,   64,  -22,
         -9,  -38,   10,   50,   23,    8,   -8,   28,   39,   58,   52,
          7,  -17,   45,   35,    7,   38,  -22,  -32,   -7,  -22,   -2,
         39,    0,  -52,  -45,   29,    1,  -36,   17,   -2,  -39,  -21,
          4,    8,  -36,  -13,  -29,   41,  -42,   20,  -26,  -38,  -54,
        -25,  -47,   16,  -38,   -3,  -12,  -16,   25,   18,   22,  -19,
        -49,   30,  -18,   31,  -36,  -37,   23,  -46,   19,  -46,  -33,
        -29,  -19,  -29,  -38,  -13,    6,  -54,   33,  -27,  -40,  -13,
        -20,  -13,  -33,  -40,  -48,  -56,  -27,  -17,  -39,    9,  -31,
          1,  -51,  -23,  -50,  -87,  -20,  -30,    2,    7,  -29,   -8,
        -12,    8,   30,  -12,   11,  -68,   23,   31,   -7,    7,   25,
         -1,   11,  -40,   24,   73,   59,   14,   50,    9,   44,  -34,
         44,   47,   -7,   63,   15,   28,   65,   47,    5,    5,   28,
        -28,    7,  -40,   29,   34,   -9,  -32,   62,   -9,  -24,    4,
        -14,  -32,   37,   21,  -39,   -2,   -1,   -9,   -8,   44,   10,
         54,   26,  -51,  -15,  -62,   21,   11,  -44,   56,   24,  -19,
        -31,   37,  -31,  -30,   30,  -74,   -3,  -40,   28,   36,  -30,
          6,   14,   21,   44,  -39,    8,  -25,  -26,  -66,   27,   39,
        -83,   19,  -10,   -9,  -28,   11,    0,   20,  -28,  -26,  -23,
          6,  -47,  -55,   24,  -16,  -39,  -12,   29,  -27,  -34,   15,
         22,   56,    4,  -29,    2,    2,  -16,  -35,   34,    1,   35,
         -6,   24,  -22,  -33,   -8,   38,  -36,   41,  -37,   33,   13,
        -43,   11,  -23,  -30,   10,  -38,    2,   15,  -77,  -58,  -13,
         16,   -8,   11,   35,   -2,  -61,  -56,    4,   16,  -64,   32,
        -12,    0,  -71,    2,   17,   15,   23,  -65,  -24,  -41,   51,
         26,  -14,  -45,  -27,  -13,   43,  -44,  -26,   54,  -22,   63,
        -33,  -10,   13,   20,   16,    4,   30,   62,   31,   -3,   75,
          4,    2,   25,   32,   26,   -5,   45,  -33,   -8,   31,    7,
         15,   64,  -31,  -13,  -37,  -51,    8,   22,  -12,  -37,   -2,
        -21,   39,    7,  -20,   -5,   -7,  -79,   60,    5,  -46,   44,
         37,   46,   17,   52,  -55,   33,  -14,  -46,  -13,    4,  -56,
         26,  -13,   11,   50,  -15,   15,   37,  -19,  -56,   15,  -49,
        -13,   14,    9,   72,   23,  -34,  -26,   44,   42,   -5,  -13,
         50,  -22,   12,   33,   22,   -9,  -38,  -49,   41,  -11,    4,
          8,   48,   41,   22,  -25,   14,  -18,  -30,   36,   -4,   11,
         -4,   33,   52,  -27,  -22,   -9,  -24,  -26,  -61,  -55,    3,
        -29,  -72,  -26,    4,   60,  -48,   66,   52,   33,  -85,   -7,
         -3,  -43,  -33,  -24,   -8,   42,  -64,    7,  -56,  -63,   21,
         45,   -5,   -4,  -49,   53,  -66,  -74,  -43,  -45,  -12,   22,
        -52,    5,    2,    0,  -26,  -32,  -40,  -40,   40,    6,  -79,
         -6,   13,   20,    0,   -1,  -37,  -13,  -47,  -40,  -23,   48,
        -28,  -16,    0,  -41,   28,   -3,   60,    3,   -5,   -9,   43,
         25,   17,   17,   17,  -23,   11,    6,   -6,   49,   13,  -62,
         -2,   86,   32,    2,    9,  -23,   -1,  -41,  -47,   56,   -3,
         -8,  -26,   -4,   14,  -35,   44,    4,   36,   27,  -23,   23,
        -47,  -55,   34,   37,   69,   49,  -30,   -7,   -6,  -41,   17,
         73,   -7,    4,   25,   57,   -7,  -29,  -19,  -58,   14,   12,
          2,    5,   46,  -16,  -27,   37,  -43,  -14,   26,  -58,  -24,
         45,  -57,   23,   28,   47,   54,   59,   46,   54,  -52,  -14,
         22,  -16,   37,   30,  -10,   38,  -23,   51,  -15,   64,  -47,
        -63,   45,   35,  -15,   36,   47,    2,  -11,  -24,   -9,   50,
       -101,  -33,    7,  -59,   -9,   20,  -33,  -42,   -7,   11,  -11,
        -20,  -44,  -62,  -36,  -15,  -24,  -61,  -53,   25,  -27,   31,
         51,  -18,  -55,  -25,   11,  -16,   52,   71,   56,  -55,   34,
        -44,    0,  -31,   12,  -73,  -36,    2,   17,   -4,   20,  -13,
         21,  -13,   22,   32,   23,  -44,  -57,  -62,   29,   21,   30,
         18,  -20,   44,  -55,    8,  -35,   53,  -21,   34,  -22,   28,
         21,  -40,  -26,  -37,   21,    6,  -18,   35,   25,  -23,  -42,
        -11,  -10,  -16,    0,    5,   34,  -12,  -11,   25,   25,  -43,
        -11,  -12,  -12,   -8,  -13,   18,   31,   39,    6,  -49,   11,
         58,   -1,   43,  -30,   21,   44,   64,   42,   35,   62,   18,
       -104,  -13,  -10,   -2,   -8,   31,  -37,  -29,  -10,  -15,   43,
        -38,  -45,   15,   39,   18,   24,   27,   -5,  -34,   19,   14,
        -20,    9,  -62,   13,   -2,  -32,  -24,   34,  -14,   48,  -10,
        -10,   30,   25,   30,  -37,    2,   12,  -10,  -47,   66,   37,
         -8,  -60,    6,   19,  -17,   14,   27,  -14,  -77,  -31,   28,
         -6,   29,   29,  -16,  -45,  -52,   -7,  -40,  -17,  -40,   30,
         19,  -63,  -31,  -29,   15,  -32,   36,    7,  -40,   -3,   -6,
         13,   50,   53,    9,   36,  -41,   12,   -3,  -60,   24,    3,
          8,   14,    1,  -10,   29,  -31,   15,  -29,  -28,   -3,   52,
        -19,   24,  -22,  -57,  -21,  -29,  -52,   15,  -26,  -28,   14,
         44,   36,  -46,  -13,  -23,  -17,    5,  -55,   -9,   -5,   13,
         51,  101,   -7,  -40,  -41,   33,  -37,  -37,   47,   25,   42,
        -20,  -25,   63,   13,    4,  -40,  -58,  -15,   -7,  -10,   94,
         -6,  -68,    6,   54,   17,   13,   16,   11,  -12,   -7,   36,
          6,   -6,  -23,  -19,    3,  -46,   22,   30,    4,   16,  -20,
        -47,    4,   11,   26,  -26,   -2,   27,   17,   28,   25,    7,
         -5,   32,  -19,    3,   29,   48,   -8,  -58,   11,  -50,   15,
        -26,  -16,   43,  -58,  -29,  -18,    0,   35,   27,  -33,   10,
         -8,    9,   35,  -70,  -13,  -48,  -71,  -41,  -12,    0,   24,
          6,  -51,  -44,   20,  -49,  -34,   19,  -38,  -46,   -9,   10,
        -60,   28,  -57,   26,  -28,   35,  -29,   14,   -7,  -43,    1,
         60,  -40,   38,    7,  -33,   24,   -9,  -20,   39,    1,  -47,
          0,  -24,   13,   69,   50,  -21,   48,   15,   12,   24,  -65,
        -31,   69,  -20,   28,  -11,   47,  -15,  -28,  -59,  -13,  -54,
          7,   45,   65,  -22,   21,   -2,   -3,    9,   -1,  -30,   27,
         26,  -69,  -24,   69,   29,  -63,   -9,   53,  -22,   23,  -25,
         47,    1,  -47,  -42,   82,   19,   -5,  -35,  -32,  -43,   -5,
         -4,   52,   14,  -14,    8,   83,   -4,  -38,  -66,   11,    0,
         24,  -50,  -16,   -7,   19,   44,   72,  -10,  -16,    7,    2,
        -35,   25,   23,   12,   18,   21,   27,   39,   24,  -51,  -22,
         -9,  -32,   13,   25,  -55,  -11,   22,   43,    0,   17,   15,
        -27,  -39,   -4,   11,   32,  -41,  -17,   41,   12,   20,  -48,
        -20,   28,   12,  -16,   15,   38,   19,  -42,    4,   18,    5,
        -41,  -49,   17,  -46,  -42,   -7,   -3,  -10,  -42,   24,  -42,
        -29,    7,  -19,  -22,  -25,  -76,  -33,  -49,   34,   -2,   -4,
         42,   -1,   31,  -10,   19,   -7,  -14,  -14,  -22,   15,  -17,
         42,   19,   13,  -17,   52,   24,  -17,  -14,   58,  -40,   13,
         10,  -45,  -44,   65,   46,   -1,   27,  -23,   31,   27,   19,
         33,  -40,  -36,  -24,   25,   41,  -35,   10,  -27,  -22,   -7,
          6,   35,  -16,  -62,   31,   55,    2,  -35,  -32,   27,  -70,
         67,   44,  -13,  -18,  -22,  -38,   62,   37,   10,  -55,   57,
        -15,  -23,    7,   28,  -25,  -11,   28,   29,   38,    7,   26,
         35,  -65,   45,  -44,  -14,   28,  -17,   -5,    1,  -21,  -37,
        -46,   45,  -36,   20,  -28,   14,   28,   20,   36,  -48,   40,
         13,   34,   18,   22,   35,   15,  -62,    6,   35,  -15,    1,
        -19,  -19,  -10,  -13,   44,    8,  -47,   -1,   -8,   11,   42,
        -59,  -60,   49,  -29,  -22,  -29,    6,   38,  -17,  -11,   22,
        -24,  -42,  -55,   -3,  -33,  -51,   21,  -41,    7,  -53,   -7,
        -63,   25,   37,  -40,   32,    3,  -23,  -60,  -33,    7,  -26,
        -19,  -16,  -15,  -37,   60,   52,   48,  -30,   51,   20,   -8,
         10,   -7,  -47,   31,    3,  -36,   44,  -21,   34,   17,   -7,
        -18,   34,   12,   14,   -6,   75,   44,  -26,    2,   41,  -11,
         25,  -39,   28,  -18,  -25,   16,   72,   51,  -36,   40,  -29,
         30,   10,   -2,  -23,    0,  -19,  -22,  -13,   36,   33,  -12,
         13,    6,  -32,  -20,  -25,  -40,  -57,    1,   17,   48,   -7,
          9,    6,  -46,   21,  -37,   25,  -26,   28,  -31,   20,  -13,
        -13,   35,  -29,  -24,    3,   -3,  -29,   36,   71,  -43,  -17,
        -10,   -3,   12,  -20,   51,  -31,  -33,   36,   15,   23,   23,
          6,   37,   22,   -4,   30,    3,  -17,  -19,  -32,   46,   52,
        -21,   -2,  -15,   58,  -25,   -2,   42,  -14,   45,  -34,   31,
        -17,  -60,   -8,    2,  -16,   28,  -16,   45,  -40,  -24,   -2,
         -7,  -41,  -38,  -13,   14,   44,   18,  -43,  -12,   39,    1,
         15,    7,   15,  -30,   32,   24,   29,   -2,  -65,    9,  -38,
        -41,   -9,    5,   25,   24,  -14,   14,   35,    1,    8,   45,
        -30,   31,   22,  -18,    1,  -24,   19,   -7,   54,   -5,   45,
         60,  -10,   30,   20,  -32,   -8,  -25,   63,   38,   44,    8,
         63,    0,   49,  -24,  -29,  -12,   46,   16,   18,    1,   -3,
         41,   32,    5,    0,    0,   34,  -38,    0,   21,   85,   21,
         29,  -27,  -20,   53,  -26,  -24,   -3,   13,  -13,   48,   18,
         31,  -24,   -3,   33,   52,   55,  -39,  -15,   49,  -23,  -55,
        -58,  -11,   18,  -11,   19,   52,   16,   17,   26,   -3,  -16,
        -32,    5,   59,   17,  -18,   20,  -10,   21,   -4,   -6,  -49,
          2,   -5,  -78,  -43,   44,   -7,  -25,    3,  -28,  -25,   -3,
         28,   71,  -39,  -14,    5,  -10,   31,  -10,    3,   25,  -34,
        -23,  -47,   42,  -46,  -27,   12,  -45,   15,   34,   10,  -45,
        -29,    7,   -6,   11,  -11,   -7,  -28,   16,  -24,    9,   -7,
        -23,   31,    5,   -9,  -28,   -2,   25,   31,  -80,  -21,  -65,
         40,  -46,   26,   -3,   13,  -47,  -24,  -22,  -34,   12,  -31,
        -17,   48,   25,    3,    9,   34,   11,  -25,  -47,    1,  -10,
         -9,  -22,   30,   17,   21,   17,    4,   58,   52,  -44,   68,
        -19,   36,   -5,    4,    0,  -28,   32,   17,  -21,   32,   53,
         36,   17,   -8,   61,   49,   14,   -4,   18,   25,  -42,   33,
        -51,  -23,  -29,   22,   30,   61,   46,  -12,   -4,   63,   14,
          9,  -23,  -24,  -17,  -41,   40,  -27,    2,  -12,  -31,   31,
        -20,   33,  -14,   -8,   40,   -8,   34,   28,   45,   38,   19,
         31,    1,  -34,  -15,   16,   -4,   -3,   82,   -5,   -3,  -14,
         34,   45,   23,   17,   19,   51,  -15,    7,   82,   35,  -32,
        -23,  -56,   14,  -23,    2,    1,   13,  -37,  -13,   26,  -43,
        -33,   21,  -46,   43,  -62,   -9,  -35,  -56,  -21,  -57,  -44,
          5,  -23,   -8,  -43,  -17,   61,  -69,  -33,  -27,  -32,   -5,
        -57,   22,  -42,    2,    5,  -24,  -11,  -16,  -19,  -32,   15,
         19,    2,  -45,  -67]]; fc_w3 = np.asarray(fc_w3);

  fc_w4 = \
     [[ -40,   15,  -65,   27,  -38,   40,   13,  -32,  -51,    2,   -7,
        -42,   41,  -27,  -59,   43,  -19,  -71,  -27,  -85,  -81,    4,
         62,  -16,  -25,  -81,   -2,  -39,  -88,  -32,   61,    7,   69,
        -56,    8,  -19,  -48,   11,  -60,   -1,   16,  -78,  -17,  -77,
        -15,   32,   55,    0,   10,  -13,  -20,  -50,    4,    2,  -82,
         20, -101,   10,  -33,  -74,   14,   31,  -32,   37,   30,   21,
         32,  -19,  -69,  -58,  -24,  -17,  -41,   -3,   -9,   28,    9,
        -16,  -24,   26,    2,  -59,  -41,  -29,  -24,   65,    4,  -16,
         -7,  -26,   31,  -31,   42,  -20,   31,   35,   -5,  -38,   10,
        -66,  -10,  -14,  -58,    8,  -18,   33,   37,   -2,  -64,   41,
         29,   -9,  -25,  -40,   35,  -16,   13,  -12,  -42,   16,   16,
        -47,  -36,  -10,   43,   34,  -42,   51,   41,   -2,   55,   42,
         41,  -25,  -51,  -42,  -40,   47,  -13,  -35,   24,  -23,   25,
        -30,  -53,    6,  -52,   -6,   23,  -38,    9,  -60,   14,   25,
          9,  -62,   -2,  -43,   23,  -44,  -29,   26,   23,   18,  -47,
         -6,    0,   32,  -30,  -38,  -54,   33,  -14,  -20,    7,   25,
        -51,   20,  -56,   23,   18,  -26,   -7,  -26,   27,  -32,   46,
         36,  -37,   48,    8,   58,   20,   11,  -32,   -9,    2,    4,
         13,  -30,  -30,   37,   50,    9,  -25,  -13,  -12,   24,   31,
          2,    9,   19,  -45,   18,    9,   29,    0,  -49,    3,   18,
         58,   19,   27,   -1,    5,   54,   31,   -6,   27,   11,   36,
        -39,   45,   -6,   -1,    0,  -54,   45,   20,   34,   -7,    2,
        -30,  -18,  -12,   28,   19,  -28,  -22,  -29,  -17,   43,    6,
         -8,  -10,   46,   19,  -27,  -24,  -11,  -17,  -31,   15,   46,
         53,  -13,    3,   72,  -41,   28,  -20,   43,  -59,   15,   35,
        -30,   -6,  -16,   53,   20,   -9,   33,  -15,   -5,   35,  -15,
         46,    7,  -36,    7,   24,   72,   48,   65,   -1,   20,   22,
        -12,   -2,   78,   13,   46,   32,    4,    2,  -14,  -18,   16,
         34,    3,   47,  -22,  -48,   -9,   50,   46,  -33,   37,  -11,
          8,   35,   13,   51,   48,   17,    5,   53,  -52,    9,   36,
         -7,  -28,   71,   -8,   50,   12,   48,    1,    2,    5,   21,
         35,  -11,   22,    8,  -13,   70,   23,   -8,  -10,   20,   48,
         -9,   20,    1,   51,  -26,  -26,   26,  -13,  -14,  -34,   31,
         -7,   22,   84,  -38,   38,   -7,   14,  -11,   33,   56,  -18,
        -19,   61,   -3,   24,  -24,  -17,    1,   -8,   -4,   10,    5,
        -39,  -21,   39,   53,   49,  -58,   20,  -47,  -17,  -13,   -2,
         52,  -79,    1,   47,  -23,   23,  -45,    3,   19,  -39,   25,
         31,   30,    7,   -2,   37,   21,  -27,   -2,   23,   23,    4,
        -14,   16,    8,    4,   21,    3,    9,  -19,  -27,   40,   25,
         -4,  -28,   13,   70,    3,   16,   45,  -49,   -1,    4,  -22,
         16,   50,   -4,   36,   14,  -28,   42,    6,  -34,   18,   46,
         23,    5,  -12,    0,   19,   29,  -43,   18,  -12,   48,   28,
          0,   27,    0,  -25,   30,    5,   48,   35,   31,   10,  -51,
        -55,  -28,    4,  -64,  -43,  -17,   15,  -15,  -10,   -7,   22,
        -19,   64,  -33,  -25,   34,  -30,  -13,  -28,    7,  -21,   40,
         12,   18,   40,  -20,  -20,   35,  -19,  -34,  -18,    6,  -56,
        -34,  -24,  -26,   70,    3,    0,   22,    0,  -45,    6,   -3,
        -23,   48,  -10,   32,   64,   27,   49,   47,  -28,  -14,   24,
         -9,  -50,  -24,    9,   -1,  -10,  -55,   53,    9,  -57,  -17,
        -34,   25,  -95,  -18,   92,   17,   -9,  -32,  -24,  -30,   34,
        -15,  -12,  -19, -121,   -4,  113,    3,   -3,  -55,   20,  -45,
        -70,   -1,   -9,   -3,  -59,   69,   36,    0,  -31,   -3,   -1,
          7,    7,   41,   59,  -33,  -87,   64,   85,   -8,  -32,    7,
        -21,  -15,   -4,   43,  -14,   50,   -7,   -2,   33,  -31,    8,
         30,   26,  -45,   20,  -31,   46,  -20,   -6,   -4,   46,  -42,
        -10,  -40,   41,   27,  -45,    0,   71,   44,  -24,   27,  -17,
        -24,  -38,   31,  -19,   41,   30,   -9,    2,  -50,   65,    3,
         47,   48,   40,  -44,   25,   21,   55,   44,   -3,  -19,  -11,
          3,   27,  -29,    7,  -48,  -17,   40,   42,   36,    5,  -41,
         34,  -13,   23,   -4,   47,  -35,  -12,  -45,  -17,   30,    8,
         13,  -73,   40,   57,  -28,   38,  -16,   19,  -44,   -4,   -2,
         -9,   -5,  -96,  -29,   32,  -27,   60,   -9,  -22,   34,   50,
         17,    5,    5,  -75,   19,   14,  -22,   48,    1,   49,  -37,
        -11,    5,  -10,   43,  -20,   31,   42,  -25,  -43,  -51,   16,
         37,   11,   24,  -26,   18,  -87,   52,   69,  -77,  -48,  -59,
         23,  -26,    0,  -40,   24,  -54,  -37,   44,   86,   40,   19,
         54,   -3,   56,   -8,  -46,  -18,   32,  -72,   32,   81,  -43,
        -12,  -14,   10,   -7,  -11,    6,  -43,  -29,  -15,  -12,    9,
        -29,  -46,   29,   50,    1,   41,   11,   -7,   -8,   35,  -26,
         43,   46,   13,  -15,   10,    3,  -34,   23,  -47,   38,    2,
         -6,   45,  -10,   15,  -16,   41,   22,  -67,  -44,   36,   -4,
        -33,   20,   44,   16,  -32,   -6,    6,   45,   -3,   33,  -36,
         14,   -5,   25,   31,   -2,  -35,  -48,  -26,    2,  -20,   -2,
        -10,  -11,   22,    5,  -25,   21,   42,   -7,   10,   12,   16,
        -59,   66,  -31,  -49,   31,   34,  -33,   48,   -3,   -3,   40,
        -18,  -26,   14,  -42,  -82,   -2,   61,    7,  -21,    5,    9,
         17,   44,  -57,   30,    1,  -27,  -40,  -17,  -32,   -2,   29,
         19,   35,  -48,    4,   31,  -22,  -33,  -11,   61,   18,   -9,
        -43,   -1,   29,  -15,   26,  -61,  -64,  -25,   13,   55,  -26,
        -26,  -21,    2,   20,    6,  -76,   32,  -45,  -71,  -19,    1,
         43,   -1,  -21,   65,  -22,   35,  -42,  -18,   39,  -18,  -10,
         -2,   19,  -22,   43,   43,   51,  -41,  -29,   17,    9,    7,
         14,   33,   38,    8,  -53,  -17,   20,   33,   32,  -42,   -7,
        -49,  -56,  -12,   -6,   -5,   31,   39,   -5,   44,    4,  -29,
          4,   18,  -34,   25,   -8,    3,    9,  -37,  -58,  -11,  -25,
        -55,  -12,   26,    1,   -1,  -38,    7,   38,   19,  -22,  -41,
          6,   65,    0,  -16,   18,   53,  -16,  -72,  -17,  -13,   45,
        -18,  -51,   30,  -29,   19,   38,   30,   -7,  -42,   27,   14,
         32,   12,    1,  -46,   25,  -10,   24,   33,   -8,  -58,   12,
         41,   43,  -21,   11,   41,    0,   24,   38,   33,   12,  -21,
         21,    9,   52,    8,    1,   13,  -39,   -5,    2,  -58,   22,
         13,  -13,   29,    3,  -15,  -29,   24,   52,  -55,  -21,  -40,
        -20,   45,   26,  -20,   24,    6,  -44,    0,   -9,  -47,   -5,
         10,   -6,   15,   -5,   20,   40,  -34,  -64,    1,    1,  -36,
         52,   34,   43,    0,   -6,  -17,   46,   -5,   26,   33,   -9,
         11,  -12,  -37,   -2,   -1,  -23,    1,   30,    0,  -23,  -39,
         39,   41,   39,  -17,   -2,  -50,  -29,   36,  -27,   33,   35,
          4,   43,   -9,  -22,    8,   39,  -12,  -36,   21,  -10,   -8,
         35,  -30,  -27,   68,  -39,   -8,    3,    2,   23,  -15,    7,
         29,    9,   68,    9,    1,   32,   38,  -22,  -50,  -35,    6,
        -23,  -23,   24,   38,   13,   32,   -4,  -52,  -12,  -32,   38,
        -54,   32,   11,   13,  -64,  -33,   68,  -37,    1,  -24,  -70,
        -30,  -38,  -45,    8,   36,  -32,    7,  -19,   -8,  -26,   53,
        -23,   19,    8,   51,   53,   23,   -8,   28,   34,    0,  -46,
        -35,  -42,  -31,   -4,   12,   11,   -7,  -58,    5,   27,   20,
        -50,    6,   54,  -22,   12,   41,   -4,   32,   26,   44,  -32,
         11,  -18,   24,   12,   67,  -56,   38,  -23,   24,   24,  -21,
        -51,   21,   46,   39,   -4,   -7,   14,   28,   -4,   -2,   -8,
         52,   33,  -13,  -68,   36,  -54,  -36,    7,   11,  -34,    6,
          6,   19,   26,  -50,   37,   62,   -5,    6,  -18,  -13,   41,
         -1,    0,   46,   29,   14,   67,   28,   18,  -10,   47,   38,
         -2,  -29,  -17,   10,    6,  -12,  -78,   17,   54,   31,   30,
         -4,   18,    5,   22,   20,  -41,   -2,   -9,    4,  -24,   17,
        -28,  -36,   50,  -13,   39,  -23,  -18,  -50,  -16,   48,  -20,
         20,   -1,  -13,   40,    2,   18,   26,  -34,  -10,   17,   -2,
        -33,   20,  -26,   37,   14,   18,  -50,   -6,   22,   24,  -28,
         32,  -28,   31,  -74,   28,  -25,   34,   -1,    2,    5,    7,
          4,   23,  -53,   -3,  -63,  -50,  -18,  -31,  -33,  -14,   13,
        -50,  -28,  -33,  -44,   19,  -16,    8,  -19,    6,   47,  -41,
         44,  -29,  -11,   46,  -23,   -2,   31,   14,  -19,  -42,    5,
          5,   57,   29,    6,   24,  -33,   26,    5,  -44,   -1,   42,
         16,   -7,   27,   33,   -4,    4,   -3,  -13,   -8,  -26,    4,
         31,    8,    2,   85,   29,  -61,  -20,  -61,  -12,  -21,   27,
        -33,    1,  -13,   -6,   15,  -38,  -22,    7,    8,  -30,  -29,
         15,  -62,   86,   -6,  -34,   29,  -38,   12,   34,  -39,    6,
        -31,  -18,   23,   52,  -12,  -31,   -9,  -19,   10,   -7,  -21,
         17,   43,  -25,   -5,  -41,  -19,   28,  -25,   35,   68,  -21,
        -16,    7,   44,  -39,  -53,    3,   55,  -23,  -15,   13,   27,
         10,  -57,   -7,  -89,   51,  -62,  -14,  -34,  -11,   20,   25,
          9,   18,   15,   28,  -47,  -43,    1,  -18,  -75,    0,  -10,
        -29,   38,   39,  -51,  -11,    2,   -6,   20,  -44,    5,   49,
        -40,    2,  -40,   30,  -20,   -8,  -15,   19,   30,  -34,   14,
          5,    2,  -52,   -3,  -15,  -13,  -41,  -33,    0,  -48,   42,
         24,  -27,    2,   13,  -39,   40,  -36,   -2,  -21,  -24,  -29,
        -38,  -15,   -1,   30,   -4,   -1,  -37,  -44,   18,  -20,  -45,
         22,   44,  -31,  -28,   15,   20,   24,  -30,  -35,   23,  -24,
         52,  -42,   14,   29,  -19,   29,   46,  -41,  -11,  -35,  -17,
        -39,  -36,  -26,   36,  -29,  -16,   12,  -35,  -63,  -12,  -29,
        -38,   13,    1,  -34,  -18,   10,   21,  -33,  -29,   -9,    8,
        -15,  -22,  -25,  -23,  -72,  -15,  -60,  -34,    9,  -33,   -4,
         14,  -38,   -4,   14,  -10,    6,    1,  -40,  -16,  -20,   23,
        -55,   12,  -28,  -56,  -52,  -17,   17,  -69,  -25,   63,  -32,
          0,   16,   27,    8,   20,   21,   -4,  -11,   18,  -53,  -29,
         -9,  -59,   12,    5,   40,  -34,  -38,  -11,    4,  -43,  -30,
          3,  -42,  -45,   -3,  -51,  -22,  -27,   -7,  -40,   53,   17,
        -35,   20,   13,    1,   14,  -31,  -63,   -5,   29,  -37,   35,
         13,    0,   29,  -59,   50,   62,  -19,   20,  -38,   41,  -41,
         19,   20,  -40,   33,   13,   -1,   23,   -4,  -30,    9,    2,
        -36,  -31,  -34,  -42,   35,  -60,   30,   13,    3,   21,  -42,
         36,   -9,  -13,   54,   -8,   -2,   19,  -28,   29,   16,   -8,
          5,  -35,   40,   19,  -28,  -10,  -30,   22,   11,   14,    3,
          1,  -16,  -35,  -45,   19,  -35,   35,  -59,    3,  -47,   12,
         13,  -27,   18,   30,   17,  -16,  -60,  -43,  -27,   47,    0,
        -13,  -15,  -42,   16,    1,   10,    1,    4,    2,  -24,  -16,
        -10,  -63,  -39,  -15,  -30,  -53,    4,  -10,   18,  -46,  -78,
         23,   47,    7,  -21,   28,   36,  -21,  -45,  -13,  -63,  -45,
         44,  -18,  -43,  -59,  -58,   24,  -40,   41,  -91,    4,  -58,
         32,   -7,  -34,  -22,   24,  -72,  -44,   30,   20,  -69,  -40,
          8,   22,  -44,  -49,  -30,  -30,   21,   26,   39,  -68,  -85,
         -4,    6,  -48,  -16,  -52,  -22,   42,    6,  -14,  -15,   54,
        -45,   44,  -37,  -62,   33,  -10,    3,    7,   41,    9,    2,
         58,  -29,    7,   54,  -54,  -44,  -38,   10,   33,   20,  -13,
        -14,   39,  -16,   14,  -44,  -64,  -32,  -14,   43,   60,  -55,
        -13,  -46,   36,  -16,  -69,   41,    0,  -16,   17,   39,   47,
         13,   -8,  -67,   24,   26,   19,  -33,   24,    1,   -1,   33,
         23,  -47,  -42,   -3,   38,   -4,   -6,  -58,  -21,  -52,   37,
        -33,  -45,    2,   43,   28,  -38,   -1,    0,  -14,  -43,    1,
         37,  -11,  -29,   -5,   54,    0,    3,    2,    2,  -29,  -35,
          5,   12,   -5,   48,   42,   -9,  -11,  -12,   17,    8,  -25,
         65,  -62,   17,   31,   28,  -42,  -15,   51,   -2,  -50,   25,
          1,   23,   25,   -6,   20,   31,   39,   32,    5,   13,   25,
         -1,   35,   48,  -85,   36,   15,   42,   32,  -46,  -50,  -10,
         -5,  -53,  -31,   31,   13,  -17,    2,  -51,  -25,    1,  -15,
        -26,   -8,  -13,  -58,   31,   42,  -17,   29,  -24,   36,  -48,
        -36,    1,  -24,  -47,    5,   54,   32,  -44,   13,  -28,  -32,
        -29,   26,   15,    0,  -14,   39,   -4,  -42,  -40,    8,   -3,
        -10,   21,  -81,   32,    1,  -35,   44,  -23,    9,    2,    3,
         -3,  -30,  -48,  -24,   26,   17,    1,   28,  -21,  -29,   13,
         43,   17,   35,   -6,    6,    6,  -28,   19,  -59,   30,   40,
        -32,  -17,   48,   34,  -51,  -21,  -26,  -24,   28,   -5,  -26,
         11,  -30,   11,   42,   51,   -7,  -40,  -10,  -43,    6,  -36,
         -6,   34,  -15,   46,   27,   15,  -13,    7,  -42,  -27,  -51,
         14,  -21,   54,   40,  -29,   31,  -48,   22,   32,   11,   31,
        -45,  -37,  -24,  -54,   32,  -39,  -45,  -47,  -56,   -8,  -39,
         -8,   44,  -57,   17]]; fc_w4 = np.asarray(fc_w4);

  fc_w5 = \
     [[  16,   27,   34,   20,    5,   20,   28,   13,   16,   -7,  -44,
        -20,   10,   18,  -32,    8,    9,   17,   15,  -57,   36,  -18,
         25,    0,  -52,  -44,  -83,  -65,  -38,  -19,  -30,  -12,  -38,
         18,   18,    1,  -35,   43,   67,   50,  -31,  -95,   32,   51,
         25,  -45,   44,   -1,   46,   21,    4,   33,   61,   -4,  -32,
         38,   20,    8,   47,  -24,  -25,   17,  -26,  -11,  -24,  -26,
        -37,  -12,   42,   -6,   13,  -15,  -44,   13,  -30,   14,  -57,
         11,  -17,   15,  -36,   11,   33,  -10,   43,  -29,   16,   42,
         10,   27,   17,    7,   24,   33,   34,   45,   -7,   53,   37,
          7,  -28,  -12,  -16,   18,  -28,   41,  -45,   27,   30,   -6,
          4,  -20,   -9,   73,  -25,  -13,  -24,  -25,   -8,  -21,  -29,
         53,  -22,   52,   47,   29,   27,  -27,  -15,   29,   -6,  -27,
         58,  -16,   37,   -3,   40,  -40,   46,   -9,  -15,  -15,   -1,
         38,  -36,   46,  -52,   23,   25,   16,  -17,   50,  -33,   -3,
         41,   38,   34,  -12,    0,   -6,  -15,   38,  -11,  -53,   17,
         -8,   40,  -38,  -11,  -42,   35,   28,   45,  -63,  -58,  -34,
        -30,   -1,  -25,  -55,  -73,   -5,   41,  -56,  -18,  -18,   24,
         31,  -65,   23,   17,  -36,   25,  -47,  -17,   16,   57,  -64,
        -32,  -40,   20,  -16,  -36,   37,   20,   -5,  -33,   33,   28,
          1,  -31,   12,   41,  -46,   55,  -17,  -23,  -18,   -3,  -10,
        -43,  -10,   -6,    1,   15,   11,   39,   16,  -54,   -9,  -55,
        -71,  -30,  -24,   -2,   16,  -28,  -34,  -13,   19,  -32,   21,
        -13,   16,  -76,    2,   -4,  -30,  -25,   27,    3,   28,  -29,
         24,   -8,   65,  -39,   -3,  -36,   20,   51,  -14,   -4,    8,
         39,   -2,   43,    8,  -25,   26,   -2,  -25,   -6,    7,   -3,
        -15,    0,    8,   -2,   -5,  -56,   -6,   14,  -29,   35,   11,
         12,  -39,   25,   43,   57,  -33,   25,   34,   -4,   49,  -40,
        -56,   -5,   48,   25,  -31,  -52,   27,  -16,  -28,   43,  -65,
        -25,   53,    6,   17,   -5,   18,   28,    4,  -47,   38,   16,
        -10,   13,   15,   47,   -2,  -63,  -29,   47,  -33,  -17,    8,
         30,  -11,    8,  -34,   26,  -16,  -26,  -31,   -1,  -19,   11,
        -24,  -43,   60,   -1,   40,   27,  -15,  -10,  -11,   34,    5,
        -34,    1,   19,  -36,  -49,   39,  -82,   -6,  -36,   -7,  -24,
        -43,  -20,    0,  -31,   27,    6,   31,    7,  -12,   38,   -9,
        -20,  -15,   40,  -26,    1,    3,  -33,  -16,   24,    7,  -15,
        -24,   38,  -41,  -49,   25,    3,   -9,   40,  -28,   19,    4,
          4,  -25,  -21,   15,   34,  -22,    6,  -27,  -25,  -46,    8,
        -10,   59,   17,  -22,   10,   13,   34,   41,    2,  -24,  -14,
          4,   -3,   59,  -20,  -13,  -20,    9,  -34,    0,   13,  -48,
         10,   85,   51,  -17,   29,  -22,   11,   11,   16,   -6,   39,
         23,   62,   57,  -38,   10,  -17,  -16,    0,  -22,   -3,  -31,
         43,   33,    8,   20,   57,   58,   45,   13,   56,   19,   19,
          1,   46,   55,   -9,   42,   -9,   51,  -59,  -19,   16,    1,
         -9,  -57,   40,   -9,   -2,   -7,  -38,    6,   11,   -8,  -24,
         22,  -13,  -29,  -21,  -69,  -62,  -60,  -16,  -57,  -28,   59,
         16,  -20,  -25,  -47,    6,  -45,   27,    5,   -5,  -41,  -40,
         15,    6,  -43,  -30,   34,  -29,   22,  -34,  -39,    9,  -23,
        -20,    5,   43,   -8,   -6,  -17,  -31,  -11,  -23,  -61,    0,
         29,    3,   17,  -18,   29,  -26,    9,   -4,   32,  -28,   -2,
         33,   26,   16,   36,  -19,  -49,  -19,   36,   -4,   38,  -16,
        -21,   -3,   -5,   53,   21,    0,   39,   -9,  -30,   17,   -2,
        -30,   25,  -58,   78,   20,  -14,  -33,  -45,   20,   35,  -23,
        -25,   42,   67,  -14,   66,   56,  -40,  -44,   32,  -16,   39,
        -18,   32,  -28,   60,   -1,    7,   59,    3,   36,  -51,   19,
         34,   -4,   22,  -19,    3,   35,    6,   70,  -13,   12,  -35,
          7,   -6,   33,   -6,   11,   -9,   13,   15,   73,    4,   72,
        -17,   78,   49,   58,   34,  -11,   50,    3,   31,   33,  -43,
        -62,   38,   32,  -10,   23,    2,  -11,    1,    8,  -64,    2,
         35,  -31,   19,  -40,   -4,    6,  -54,   25,  -38,  -43,  -61,
         -2,  -36,   39,  -32,  -11,  -71,   15,  -12,  -12,   20,  -26,
        -37,   16,    4,    4,  -16,   20,  -49,   53,  -22,   26,   -8,
        -30,  -43,  -49,   58,  -18,  -23,   57,  -49,   49,  -23,    0,
        -58,  -20,  -29,    8,  -21,  -46,   44,   19,   42,   30,  -12,
         28,  -47,   45,   -4,  -24,   23, -102,    6,   41,  -34,   -6,
        -14,  -55,   31,  -14,   46,   44,  -15,  -68,   -7,   67,   46,
        -75,   23,  -34,   18,  -29,  -10,   64,  -48,  -63,   -9,   34,
         24,  -93,  -13,   25,    5,  -11,   63,    9,  -36,  -64,   24,
         67,   43,  -50,  -33,  -12,    8,  -28,   18,   50,  -28,  -29,
         26,  -16,   -9,  -28,  -29,   42,   19,  -25,   58,   55,   94,
         20,   71,  -44,   42,  -30,  -34,  -11,   -7,  -22,   32,   44,
         67,   37,    4,   31,   80,   51,   51,   44,   47,   31,   -3,
         -9,  -10,    8,  -25,   40,   49,  -39,  -51,  -54,   26,   38,
         -8,  -15,   22,   31,   42,   22,   -7,  -38,  -33,    4,   12,
         -5,    5,  -30,    7,   32,    8,   -2,  -64,  -12,  -45,  -29,
        -38,   26,   15,  -21,   37,  -20,   33,   22,  -31,   49,  -38,
        -28,  -38,   27,   28,  -53,   -5,    5,   27,    0,  -14,  -17,
         13,    6,   24,  -30,  -37,   11,   -2,  -16,  -18,   47,   47,
         30,  -12,  -43,  -26,   20,   -1,   32,   -2,  -44,    4,   97,
          5,   -1,   23,   29,   43,    9,  -32,   29,  -59,  -64,   45,
         33,   18,    6,    4,  -30,   14,  -19,  -31,   51,   30,  -71,
        -13,   73,   64,  -45,  -15,  -29,    3,   -3,  -46,   34,  -11,
        -47,   23,   30,    9,  -39,  -72,  -18,  -15,    9,   -3,    2,
        -69, -112,   39,    2,   48, -100,  -29,   21,  -12,  -42,   10,
         56,  -36,  -54,   33,   18,   14,  -12,  -78,   -7,  -11,   24,
        -17,   12,   16,   70,   -5,  -21,   43,   12,   32,   48,  -23,
         59,   28,   23,  -30,   -1,  -43,   24,  -19,   -6,   -5,   39,
         31,   -5,    2,   46,  -47,  -48,  -36,   -6,  -36,   48,    9,
         22,    0,  -21,  -27,   37,  -44,   26,   61,   68,   -2,  -44,
        -39,   36,  -29,   -3,  -28,   16,   43,  -37,   -6,   29,   -9,
        -58,   -9,  -47,   20,  -28,  -42,   -6,   -7,   45,   15,   -9,
         15,  -25,  -49,   16,   35,   32,   12,   11,   14,   17,  -12,
         50,  -12,   26,   -4,   -2,   50,   51,    6,   64,   -1,  -33,
         32,    9,   31,  -25,    7,   27,   26,   13,   16,    4,   22,
        -17,   -7,   60,   -8,  -36,  -24,   18,  -24,   -9,  -47,   17,
        -40,  -69,   14,   77,    1,  -45,  -45,   -5,   26,  -38,   12,
         -1,  -17,  -57,  -31,   41,  -14,  -58,  -49,   32,  -37,   37,
        -46,   34,   14, -115,  -40,   11,  -22,  -60,  -17,  -38,  -59,
         -8,  -33,   60,   -2,  -69,   25,   29,   19,  -47,  -43,   41,
        -42,    0,   18,   75,   55,   49,   10,    2,  -37,  -45,   21,
         -6,  -42,   12,   25,  -36,  -48,    2,   51,  -36,  -11,  -27,
        -56,   -9,   -1,  -28,  -13,   54,  -29,   11,    1,   57,  -18,
        -15,   69,    4,   41,  -16,   55,   14,  -42,  -41,    2,   46,
         -4,   50,  -39,   41,   73,   19,   -6,   13,    5,  -34,   -4,
         58,  -28,   27,   22,   -7,   35,  -41,   28,   30,   -5,   30,
         59,   23,  -17,   17,   -5,   10,   30,  -34,   18,   47,   10,
        -59,  -30,   29,  -16,  -34,  -27,  -20,   64,   15,   23,   11,
        -61,    0,   22,   75,   35,   -3,    0,   21,   46,   28,   10,
        -15,   15,  -26,   13,   57,  -35,   17,  -62,   21,   31,    9,
        -65,   58,  -25,    5,   -6,   45,   19,  -14,   27,   -4,  -54,
        -35,  -49,   23,  -51,   -6,  -39,   -5,   29,  -10,  -33,   21,
        -61,  -25,   -1,  -41,   38,   -6,   47,  -15,   42,  -12,   -5,
         -4,  -71,   26,  -15,   34,  -67,  -20,  -39,   22,    4,  -43,
        -40,   29,  -54,  -25,  -43,  -52,  -48,  -57,   -9,  -75,    0,
        -12,    7,    1,  -55,  -11,   11,   40,  -48,    6,  -46,    6,
        -45,  -35,  -21,   45,    2,   11,  -39,   -1,   26,   15,   44,
         -7,   26,   22,   49,   13,   35,   23,  -22,  -10,   22,   22,
        -39,   17,   -1,   19,  -26,   11,  -25,   35,   -5,   85,    3,
        -20,   15,   85,   -6,  -30,  -31,  -23,   -8,   -3,   -3,   52,
        -21,   20,   12,   66,   32,  -13,    2,   -7,  -17,  -32,   47,
          6,  -12,   -8,   21,   79,   21,   16,  -21,   16,  -33,    1,
         32,   -5,  -26,   -1,   34,   10,  -16,   30,  -10,   13,   35,
          1,  -27,  -13,  -40,  -55,   33,   -2,   -9,   57,  -39,    8,
        -25,  -10,  -34,   25,   15,   -3,  -35,   -4,  -33,  -22,   21,
         18,    4,  -40,   11,   16,   39,    9,  -34,   31,   24,   15,
        -51,    6,  -66,   18,  -42,  -49,   15,    6,   39,   19,   36,
        -36,   10,  -59,   -6,   24,  -17,    8,    4,    6,  -24,  -19,
        -37,   42,   17,    7,    4,  -18,  -38,  -78,   25,  -30,   39,
        -14,   24,   20,   -7,    8,   24,  -15,    6,  -21,   16,   -3,
        -21,    5,   26,   -6,   10,  -14,   17,   36,    1,   18,   26,
         26,   35,  -47,  -52,   17,   28,  -50,   25,   53,   40,  -13,
          1,  -23,   53,   21,   66,   47,   20,   -4,   40,   23,  -16,
         17,  -44,  -16,    7,   95,   50,   19,  -13,   37,   38,  -29,
         15,   21,    1,   -3,   29,   61,   44,    9,   26,  -28,   -1,
         33,  -28,   11,  -47,  -26,  -50,   48,   24,  -53,  -44,  -29,
         19,   54,   16,  -20,   41,   35,   32,   26,  -27,   28,    7,
         50,  -43,   -4,   20,  -34,   27,   53,   40,   -7,    0,   -4,
         27,   24,   34,  -16,   40,   22,   -4,   37,  -35,   16,  -14,
        -36,  -22,  -29,  -32,   15,    4,   33,   13,   26,   -7,   27,
        -18,    6,   40,   12,   38,   20,  -12,   -1,  -13,   43,  -47,
         34,   46,  -23,   32,  -44,  -29,   -2,  -47,  -33,  -10,  -31,
         21,  -45,  -63,    4,   25,  -18,  -47,  -48,   50,   28,   20,
         45,   56,   27,  -11,    4,   50,   -6,   -7,   29,   29,  -52,
         10,   46,   23,   39,   42,   45,   65,   17,   -3,   12,   50,
         19,  -57,   45,   11,   52,   -3,   35,  -33,  -54,   26,   13,
         16,   16,    1,   22,  -24,   56,  -33,   21,   10,  -13,   -5,
        -17,   38,   21,   38,  -34,   15,   26,   14,  -24,   21,   18,
         10,    0,   44,  -17,   13,   17,  -33,  -21,    4,  -46,   31,
         33,   70,   21,   57,   -8,  -30,   10,  -22,   -7,   26,  -30,
         35,   26,  -35,   41,  -10,  -20,  -18,  -19,   33,   30,   18,
        -43,   35,   -8,  -28,   32,   41,   13,  -32,    2,   46,  -37,
         39,  -16,   -1,   -3,  -43,   16,  -28,  -45,   36,   -9,  -10,
         33,  -41,   44,    3,   17,   39,  -16,   -1,  -33,   -7,   21,
         -7,  -30,   -8,   37,   20,  -37,    7,   -5,   14,  -19,  -16,
         20,   -9,   -4,   48,   35,   43,   -7,   49,  -11,  -44,    5,
         -1,   47,   43,  -86,  -37,   24,   27,    2,   -1,   21,    9,
        -44,   23,   27,   -5,   14,    9,  -35,    3,    7,    6,  -25,
        -33,  -51,    7,   30,  -58,   13,   44,    6,  -39,   37,  -15,
         57,    2,   21,  -47,  -23,   -5,    3,  -13,   45,    5,   45,
         18,   -6,  -60,  -62,   19,  -39,   25,  -30,   60,    2,   25,
         41,   31,  -24,  -29,    3,   18,   29,  -28,   -3,   -8,  -19,
         38,  -15,  -11,    1,  -28,   20,   25,  -64,   27,   14,   53,
        -40,  -48,   -6,   39,   31,   33,   44,   27,  -18,  -43,   31,
         17,    5,   18,   15,  -17,    4,   32,  -41,   42,   22,   19,
         38,   37,   17,   -8,   15,  -35,   25,   21,   30,  -30,   -5,
        -16,   12,    8,   59,  -37,  -11,   -5,   48,  -25,  -39,  -19,
          0,  -37,   -1,   -5,   51,   48,   -3,   46,   18,   44,   -4,
         47,    2,  -50,   19,  -59,  -46,   35,   17,  -47,   32,  -53,
        -33,   12,   46,   -6,  -65,  -49,  -42,   10,  -11,   15,   28,
         12,  -21,   16,  -42,   34,   25,  -14,   34,   39,  -29,   -1,
         26,   44,   54,  -62,  -11,  -41,  -49,   -1,   29,   38,   61,
        -61,   23,   42,   17,    5,   52,  -12,   23,   -1,   17,   16,
         32,   19,  -23,   31,    1,   40,  -26,   14,  -11,   38,   34,
         75,   37,   60,   32,  -13,   -3,   28,  -40,   48,   65,   37,
        -46,   63,   23,   29,    5,    5,  -19,   54,   23,   18,  -11,
         50,  -14,  -18,    7,   57,   30,  -14,   17,  -47,    3,  -23,
          2,   53,  -34,  -15,   21,  -10,  -11,  -10,    2,   13,   25,
        -40,  -15,   49,    2,   43,   46,  -21,   25,    7,   18,   -3,
         19,  -11,  -37,   19,    1,  -21,   13,  -18,   -5,  -10,   57,
         47,  -10,  -32,   17,   47,   40,   -4,    2,   24,   24,  -26,
         50,   21,   -5,   25,  -36,   35,    6,  -17,    3,   -9,   55,
         41,  -18,   13,   -7,  -21,   11,  -43,    2,  -19,  -30,   22,
         54,  -33,  -20,  -22,  -15,    9,  -35,   21,   32,  -40,   31,
         18,   42,   56,   17,    3,   28,  -16,    5,  -25,   12,   41,
         -2,  -43,   14,   12,  -12,  -41,   63,   71,  -20,  -18,   47,
          5,   45,   63,   42]]; fc_w5 = np.asarray(fc_w5);

  fc_w6 = \
     [[  0, -40, -12,  18,  -7, -50, -24, -65, -38,  13,   2,  34,  46,
       -27,  -4,  60,  34,  -6, -10,  66,  84,  11,   9,   8,  13,  32,
        12,  31,  83,   8,  17, -33,  59,  40, -30, -16, -31,  69,  17,
        57,  32, -16,  21,  66,  31,  57,  -8,  -8, -26,  26,  52,   1,
        17,  83,  14,  15,  26, -16,  47,  -1,  12,  52,  48,  18,  72,
        26,  -1, -33,   4,   0,  41,  36,  25,  44,  20, -40,  42,  14,
        25,  57,   8,  43, -28,   5,  27,  75,  18,  17,  17, -50, -24,
        19,  29, -11, -46,  30,  43,  60,  15,  12,  -3,  45, -20,  29,
        37, -36, -35,  26, -12, -19, -27, -17, -22, -35,  19,  62,  65,
        14,   6, -26,  10,  13, -33,  -2,  41, -22,  59,  42, -18,  56,
        29,  80, -41,  53,   8,  66,  51,  32,  15, -20,  36,  57, -32,
       -13,  37,  78, -43,  60,  44,  77,  39,  31,  -2,  -6,  48,  56,
        17, -61,   6,  12, -52, -90,   5, -31, -14, -62,  -9,  50, -57,
       -38,  35,  -8, -23,  65, -11, -24,  27, -14,  15, -47, -13,  31,
        47,  56,  -5,  17, -30,  35,  44, -22,  -5,  -9, -16,   3,  40,
        59, -15,  -1,  35, -17,  -9,  -1, -37,  46,  -7, -27,  24,  60,
        66, -22, -38,  32, -16, -11, -25, -12,  55, -45, -46,   5, -13,
       -50, -14,  33, -29,  63,  78, -17,  19, -10,  35,  56,  -4, -57,
       -26, -24, -20,  29,   8,   4,   6, -40, -52, -30, -62, -19,  -7,
        45,  31,  46,  48,  35,  -5,  46, -22,   5,  13,   0,  -8,  43,
       -20, -36,  32, -43, -35, -42,  52,  70, -29,  23,  41,  -7,  48,
        24,  67,  -8, -25,  43, -30, -27, -24,  52,  27,  50,  42,   6,
        -7, -17, -13, -17,  24, -27,   1,  11,  62,  19,  42, -21,  55,
        -2,  11,  29,  38, -30,  50, -14,  17, -21,  -6,  -5, -18, -27,
       -34,  10, -15,  31,  45,  27,  62,  14,  -5, -37, -38, -11,  -8,
       -64,   8,  -8, -38, 100, -43,  -9,  20,  15, -57,  -3,  34, -37,
        13, -40,  16,   2,   9,  43, -36, -32, -29, -19,  36, -75,  13,
        42,  -4, -41, -50, -25, -13, -21,  40, -27, -38, -31,   7,  35,
        33, -16, -29, -23,  25, -14,  16, -44,  37, -19,  14,  31,  14,
        25, -16,  46,   2,  16,  24, -11,  17,  -1,  -2,  13, -14, -60,
         4, -15,  18,  24,  54, -47,  39,  12,  20,  49, -28, -79, -40,
        48,  15,  41,  14, -14,   6,  -4, -53,  33, -33, -22,  41,  23,
        15, -46, -12, -31,   3, -29,   9, -43,   7, -69,   7, -38,  14,
       -40,  28,  51,  52, -47, -29, -27,   7, -24,  26,  17, -33, -18,
       -14, -27,  22, -10, -14,  23, -28,  -6, -28,  56, -25, -25,  43,
        59,   3, -24,   2, -34,  27,  27, -15,  15,  61, -12,  53,  31,
        27, -45, -32,  29,  58, -51, -16,  35,   6,  33, -11,  27, -51,
       -74,  61,   8,  -9,  27, -19, -51,  37, -14,   7, -15,   1,   7,
        23,   0, -39, -23, -23,  29,  39, -33,  -9,  15, -33, -49, -42,
        15,  16, -58, -17,  53,  44,   7, -48, -18,  32, -29,  37,  -4,
       -16,  -3,   2, -43,  21, -36,  50, -49,   1, -10,  35,  50,  -5,
       -81, -51,  12, -31,   4,  11, -44, -18, -11, -35,  38, -55, -81,
        22,  16,  -8,  47, -34, -27,   0,  10, -56,  35,  -1, -31,   4,
       -17, -29, -44,  12, -10,  55,   8, -62,  66, -51,  -9,  20,  52,
       -15,  39,  45,   1,  23,  82, -51, -19,   8, -65,   9,  -1, -60,
       -36, -36,  30,  24,  46,  26,  40,  34,  47, -47, -17, -54,  43,
        48, -25,  23,  57,  29,  27,  -7,  10, -13, -13,  -9,  -8,  28,
        19,  57, -23,   4,   5, -12, -49, -63,  20, -34, -61,  52, -21,
       -54,   4,   5, -39,  56, -57, -40, -32,  -2,  30,  12, -64, -15,
       -62,  48,  -3,  15,  24, -57, -13,  39, -10,  15,  19, -25, -12,
        54,  45,   2, -71, -10,  37, -38,   1, -25, -52, -48,  28,  34,
       -13,  15,   9,  32,  10,  11,  18, -19,   8,  -8, -65,  35,  33,
       -41,  -9,  15,  18,   4, -20, -19,  26,  56, -45, -21,  23, -37,
       -73, -35,  29, -33,  -9,  49,  21,  16, -30,  -2,  29,  -5,   1,
       -15,   5,  30,  41,  63,  36, -28,  -3, -36, -49,  18,  31, -16,
        35, -28,  -6,  43, -31,  -7,  27, -63,  45, -48,  30,  15,  10,
       -18,  17,  31, -10,  -5,  96, -26, -37, -24,  52,  50, -27,  35,
       -21,   6,   6, -34,  24, -13, -54, -19,   8, -19, -25,  28, -13,
        17,  16, -33,  62,  19,   2, -14,  47,  51, -15, -15,  49,   2,
         9,  45, -36,  -2,  20, -32, -50, -53, -44,  20,  42, -42, -65,
       -32,  11,  -1, -46, -36, -35, -20,  37,   7,  -8,  50, -55,  43,
        14,   2,  32,  -6,   1, -63, -17, -25, -43, -16, -30,  20,  12,
       -33, -14, -35,  58,  -5, -36,  -8,  30, -37,  -9,  24, -41,  -3,
        -2, -17, -20,  36, -36,  50, -53,  49, -27, -24, -71, -63,  10,
       -39,  13, -40,  22, -14,  -5, -51, -34,   6, -31, -30,  65, -34,
       -71,  44,   5, -15,   8,  23, -37, -30, -61, -38,  54, -54, -65,
        43,  46, -29,  36, -39,   7,  16,  22,  -2, -30, -21,  57,  66,
        48, -30,  45, -48,  21, -18,  -3, -36,  13, -24,  11,  57,  12,
       -50,  -4,  24,  26, -26,  15, -35, -41,  -4,  17, -22, -45, -14,
        -3, -44, -10,  23,  -7, -37,  -2,  54,  22,  57,  28,  -7,  73,
        24,  13, -39, -40,  16, -98,  45,  47,  43,  10,  17,   1,  21,
       -21, -10, -52,  -8,   7,  42,  22,   7,  28,  40, -29, -14, -29,
       -60, -55,  -8, -26,  23, -33,  43, -69, -23, -13,  18, -23,  39,
       -33,  -9,  40, -21,   8,  -8,  12, -55,  20,  21, -16,   0,  -8,
        37,  66, -59, -34,   5, -16, -19, -41, -27, -10,  35,  -9,  36,
         1, -22, -53, -32,   4,  10,  41,  11,  58, -15, -75,  46,  -1,
       -32, -22, -33, -30,  50,  -8,  23,   6,  -1, -36, -43,  -6, -15,
       -61, -30,  30,  -1, -45, -52, -10,  23,  19,  -1, -12, -36,  -8,
        36, -21, -35,  14, -37,  25, -31,  20,  10, -22,  22,  21,  36,
        40, -28,  52,  -3,  39, -47, -14,  -8, -22, -14,  60,  -6,  44,
        33, -21,  39,  10, -17,  15,  49, -31,   9,   0,  18,  -4,  33,
        47, -63, -24, -19,  13,  -2, -25,  24,   0, -34,  -1, -17, -12,
       -50,   4, -26,  31,  45, -46,  47,   8, -27,  -2,  58,  14,  14,
        -9,   6, -29,   9, -54,  -8,  -7, -23,  -9,  34, -19,  -4, -18,
        -4, -40,  -7,  -8,  18, -50,  27, -23,  22, -52, -58, -29,  26,
       -39,  46,  31,  37,  46, -60,  13, -68,   8,   7, -68, -62,  20,
        64,  25, -49, -55, -13,  46,  14, -31,  14,  55,  37, -20,  44,
        18, -51, -21, -32, -19, -37, -52,   6,   2, -12, -43,  39,  16,
       -20,  26,  16, -36, -10, -14, -39, -18,  22,   5,   7,  13,  41,
       -50,  21,  49,  62,  -6, -66, -13, -35,  12, -27,  36,  20, -38,
        19,  49,  34,  43,  38,  45,   2,   7, -29, -21, -33,  75,  12,
       -40, -16, -24, -17,  36,  31,  24, -15,  -3, -36,  40, -33, -23,
       -38,  51,  48,  -1, -33,  -6, -49,  14, -22,  31,  15, -54,   8,
       -22,  -8, -38,  39,   4, -31,  14, -18, -17,   6,  32, -15,  -9,
         1,  43,  29, -40, -21,  20,   2, -40,   2, -11,  55,  -3,  44,
        20, -49,  18, -57, -70,  36,  33, -50,  52,  30,   9,  35,   5,
       -11,   6,   9, -22, -45,  31, -16, -47, -12, -25, -12,  20,  32,
        -1,  -1,  43, -35, -55, -37,   2, -43,   3,  44, -31, -50, -37,
        60,  -2, -35, -58, -20,  31, -15,   5,   5, -65,   8, -14,  45,
       -14, -13,   4, -42,  17,   4, -47, -53, -37,  13,   3,  -2,  47,
        21, -28,   1,  -7,  54, -23, -44,  -6, -54, -48,  33,  11,  35,
       -66, -16,   4,  22, -11,  -2,  10,  38,  15, -24,  31,  52,  11,
        12,  27,  50,   6, -41, -59,  26, -45,  -4,  15,  47,  37,  25,
        46, -18, -23, -50, -51,  38, -12,  -2,  -7, -15,  33,  17, -10,
        20,  27,  32,  12,  40,  36,  -8,  35,  13, -11, -15, -41,  45,
       -22,  31,  14, -22,  27, -12,  32,  33,  -9, -11,  27,  51,  56,
        37,  45,   0, -21,   9,  -2,  30,  -6, -36, -11, -13,  31,  -1,
       -31,   8, -23,  26, -48,  -7, -13, -19, -18,  -3,  12,  27,   4,
        29, -68, -50, -34,  41, -21, -62,  19,  -5,  26,  34, -52,  27,
         5,  -5, -15,  22,  37,  25, -77, -44, -41, -68,  -6, -44,  39,
       -25,   1,  41,  23,   9, -16, -22, -40,  11,   9,  14,   0,  42,
        18,   1,  -3,  -4, -35,   7, -56,  26, -44,  22,  -3,  -2,  19,
        69, -21,  20, -10,  -7,  14, -71, -22,  41, -10,  36, -26,  -6,
        16,  42,  36,   7,  24, -20,   4,  24,  12,  15,   6,  14,  56,
        47, -17,  32, -19,  -1,  36,  30,   4,  28,   7,  22, -12, -24,
       -25,  31,  31, -48, -10, -23,  34, -20,  60,  10,  -4,   5,   8,
        47, -24,  11,  -2,  57, -36,  25,  15, -26,   5, -31, -16,  37,
         2, -10, -11,  53, -26, -37, -22, -11, -11,  36, -30,  33,  42,
        12,  -3, -23, -50, -50,  69,  -4,  17, -24,  12,  32,  17, -25,
       -37, -18,   0,  29,  -6,  24, -35,  17,  44, -20,  27,  24,  43,
       -58, -27, -25,  45,  -1,  -8,  40,  19, -72,   0,  14, -69, -53,
       -46,   2, -57,  29, -37,  31,  -1,   0, -36, -16,  27,  24, -47,
       -29, -35,  39, -60,   5,   0, -14, -55, -58, -32, -62,  23,  20,
        -9, -32, -39, -36, -42, -36,   4,  34, -38, -24,  14,   0,  27,
        -5, -12,  12,  -3,  33, -32, -15,  17,  61,   2, -41, -69,  66,
         8, -16,  -3,   6, -50,  35,  37, -25,  28,  44, -72,  16,   8,
       -20,  48,  21, -37, -24,  -8,   0, -14,  27, -25,  17,  25,  33,
       -13,   4,  39,  30,  13,  16,  37,  26,  16,  50, -37,  35, -45,
         6,  26,  15, -10, -33, -44, -41,  26,  25,  31,  18, -27, -31,
        26,   4,  -1,  49,   4,  33,   5,  19,   9, -36,  31, -11,  18,
        -8, -16, -29, -55, -66, -21, -15, -68, -59,   7, -44,  14,   6,
        17,  42, -27,  16, -28, -13, -69, -23, -38,  -5, -21,  34,  51,
        10,  16, -54, -19,  48, -33, -20, -52,   5, -16, -38, -29, -42,
       -54, -28, -29, -57, -22, -47, -51, -60, -43, -61, -13, -18, -23,
        37, -67, -40, -37, -15, -46,   1,  33,  20, -11,  24, -28,   0,
       -51, -35,  31,   8, -18, -40, -61, -19,  17, -47,  14, -33,  -4,
       -15,  33,  18,   2,  -4, -21,  -1,  32,  -6,  -2,   4,  -9,  14,
        21,  12, -58, -17,   5,   3, -44, -31, -20,   2, -75,  25,  29,
       -58,  10,  42, -13, -33,  46,  21,   2,  14,  -2,  10, -61,  13,
       -19, -53, -11,  34,  20,  44,  19, -56, -47, -47,   5, -44,  -4,
       -51, -38,  23, -30, -46, -17,  21, -29,  31, -19,  13, -16, -36,
       -13, -39,  22, -22, -41, -17,   8, -52, -60,  15,   0,  -5, -10,
         0, -19,  18, -63, -20,  11, -33, -66, -90,   1,   3,  28, -49,
       -37,  -3,  47,  67, -13,   8,  27,  19, -72, -23,  33, -14, -20,
        21,  37, -49,  16,  48,  13,  38, -13, -14, -53,  17,  36,  -4,
       -25,   6, -12, -35, -67,  41, -20, -49, -56,  14,  24,   8, -52,
         6, -57,  -3,   9,  24,  25,  14,   9,   6,  45,   7, -57, -87,
       -76, -76, -50, -47, -11,  -1, -33, -73,  17, -29, -20, -29, -51,
       -18, -62,  25, -50,   8, -64,  -2, -46, -86,  17,  24, -38,   5,
       -49, -55, -29,   1,  -5, -40,   3,   0, -32,  -3, -57,  15, -55,
        19, -83, -37,  34, -74, -25,  27, -36, -40, -66, -22,  22,  25,
       -17, -27, -48,  43, -44, -19,  -1,   2, -41,  17, -33, -31,  20,
        42, -39, -28,  -8,  55, -33, -87, -26, -48, -11, -54,  -7, -27,
       -50, -17,  46,  26, -29,  33,  29,  39, -64, -37, -51, -83, -47,
       -45, -19, -85,  -9,  -1, -35,  40, -12, -13, -53, -46, -13, -48,
       -19,  47,  20, -21, -26,  47,  -2,  11,  42, -34, -22,   9,  35]]; fc_w6 = np.asarray(fc_w6);

  fc_w7 = \
     [[ -33,  -13,  -46,   38,   43,   29,   29,  -27,  -42,   10,  -44,
          6,   48,   23,  -61,  -49,  -45,   16,    7,   16,  -27,  -27,
        -28,   -6,  -16,   29,   -1,    3,  -15,  -12,   41,  -41,  -33,
         19,  -42,   21,  -21,   47,   31,  -30,  -19,   -6,   28,  -37,
         16,  -61,  -37,  -63,  -28,    0,  -42,   10,   22,    6,   24,
        -62,   -4,   25,   16,    5,   15,  -44,   28,  -56,   19,  -66,
         20,  -19,  -43,    9,   46,   18,  -26,  -12,   12,   31,  -38,
         -9,    9,  -59,  -78,  -53,  -17,  -26,  -33,   30,  -38,    1,
          1,  -66,  -58,   37,   -9,  -37,  -41,   -5,   20,  -51,   18,
        -48,   41,   -6,  -52,    1,  -28,   12,   27,  -37,  -31,  -31,
        -19,  -59,   33,  -54,  -78,  -60,  -57,  -30,    6,  -21,   27,
         -1,  -25,  -37,  -31,   12,   -8,   18,   36,   -6,   31,  -19,
        -19,  -21,  -19,  -17,  -31,   14,  -50,  -50,   36,   38,   29,
        -32,  -45,  -28,   13,  -45,   46,   -4,  -49,   -9,    5,   -7,
         19,  -38,   34,   -5,   -2,  -25,  -12,   -1,  -83,  -42,  -46,
        -27,  -24,    3,  -43,  -27,   29,   34,    3,  -68,  -17,    8,
         52,  -57,    2,  -50,   -3,   -6,  -22,  -62,  -30,   23,  -60,
         19,   43,  -46,    6,   49,  -51,   -3,   22,  -60,   -7,    6,
          9,   -7,   -9,   -8,   38,   10,  -47,   13,  -32,   -4,   15,
          0,  -16,   18,    7,   24,  -59,    5,  -28,   -1,   20,   42,
        -56,  -63,  -42,   13,   21,  -24,   -9,    7,    2,   -7,   -6,
        -42,   30,  -30,    8,   19,   16,  -42,    8,  -45,  -45,  -48,
         -2,   -2,  -24,   43,    5,  -54,   20,  -55,  -15,   -5,  -50,
         78,  -43,  -72,  -38,    9,  -63,  -69,  -25,  -50,   13,   -7,
        -52,  -47,   32,   15,  -26,   -1,  -20,  -61,   -2,    9,  -62,
        -18,  -13,  -56,  -39,  -48,  -65,  -81,  -68,  -42,  -40,  -42,
         31,  -12,  -28,  -71,  -54,  -28,  -51,    1,  -60,   40,  -69,
        -65,   13,   14,    8,   -9,  -12,  -37,    3,   31,   46,   22,
         41,  -26,  -30,   -9,  -39,  -33,   39,   42,   25,   -9,  -18,
        -15,   17,  -60,   49,   46,   53,  -18,  -14,  -45,    4,   36,
         18,  -17,   -7,    0,   33,  -53,   -6,   57,   45,  -34,   50,
         69,    0,  -30,  -30,    8,   29,   36,  -16,   -5,   55,    3,
         30,   18,  -10,    7,   15,   25,   34,   14,    7,   60,   43,
         17,   12,   25,  -18,    5,    3,    0,  -39,   50,  -61,   61,
        -29,   11,    5,   61,   15,   34,   27,   12,   13,  -29,  -13,
         19,   37,  -43,  -49,   34,   26,  -27,  -10,  -25,   29,   25,
        -17,   46,  -35,  -47,    5,   44,  -16,  -24,  -19,  -39,    5,
        -31,   21,   27,   23,   32,    0,   38,   -8,  -35,    3,  -35,
        -15,   -7,    7,  -15,  -52,  -41,  -41,  -19,  -36,   -3,   16,
        -31,  -45,  -45,   22,    8,   21,  -35,   10,   24,  -57,   18,
        -29,   40,  -19,  -42,  -54,   18,  -22,   33,   12,   23,    9,
         35,   18,   40,   -5,   58,    8,   -4,  -12,  -45,   48,   13,
         -3,  -27,  -51,  -30,   30,  -46,   40,   19,   -8,    9,    4,
         21,  -12,   65,   -8,    2,  -21,  -22,  -52,  -10,  -13,   54,
          1,   91,   41,   41,   41,   58,   30,   11,    8,   -9,    6,
          2,   60,   73,   19,   12,    6,    1,   30,   26,   -5,   48,
         -7,  -34,  -26,   88,   41,   45,    9,  -40,   37,   29,  -51,
         27,  -14,  -24,   40,   24,   -8,   51,  -15,   34,  -49,   -8,
         -6,   26,   12,  -56,   13,   42,   -3,   -2,  -11,    0,   52,
         29,  -23,   15,   46,   -9,   -9,   22,   14,   23,    5,  -44,
         22,   30,  -35,  -18,   45,   -7,  -26,   10,   12,   37,    4,
         25,  -31,  -37,   -6,    2,    5,  -57,   12,   39,   20,   -9,
         -9,  -12,  -27,  -14,   11,  -26,   25,   21,   19,   55,  -37,
         -4,    2,   -9,   33,   -3,   31,    7,  -48,  -19,   -4,   16,
         33,  -38,   42,   34,   31,   33,  -41,  -48,   24,  -69,   -2,
        -19,   20,   11,  -23,   -7,  -42,  -47,  -55,   15,   11,  -31,
        -44,  -40,  -57,  -34,  -54,    3,  -40,   -7,   61,   -3,  -30,
          9,    4,  -23,   14,   76,   95,  -28,   26,   20,   28,    6,
         22,   14,   25,   81,  -14,  -44,   59,   21,  -23,   30,   -2,
         52,   47,  -19,   26,  103,  -12,   -8,   15,  -20,    3,   34,
         33,   15,   33,  -62,   24,   -1,    6,   18,   31,    8,  -47,
        -32,    9,    3,  -29,  -40,   52,   -5,   20,  -45,   26,   14,
        -14,  -39,   18,   57,  -20,  -45,    4,    5,   24,  -46,  -39,
         12,  -10,    2,    8,    0,   -8,   -7,   25,   13,   44,    7,
         -4,  -60,   -9,    0,   -2,  -12,   48,   21,  -14,    3,   19,
         -2,  -20,   15,    8,   22,   53,   -7,   43,  -42,   29,   21,
         54,   -8,   19,  -23,  -23,   -6,   47,  -49,  -32,  -38,   -6,
        -42,   28,  -15,    5,    3,    1,  -27,   48,  -31,    1,   -1,
        -39,  -20,  -28,   21,   32,   15,   -1,  -14,  -37,   12,  -40,
        -28,   11,   -9,   18,   12,  -39,   -7,   35,   -4,    5,   -4,
        -53,   39,  -19,   -7,  -24,   28,  -53,   -5,   15,  -36,   27,
         80,   22,   82,   -7,  -41,    8,   49,   40,   34,   62,   59,
        -31,   29,   43,  -29,  -15,   -6,   -5,   39,    1,   48,  -52,
         45,   15,   53,  -57,   26,   -6,   73,   26,  -21,   13,  -51,
         22,   -9,  -52,   -2,  -12,    2,   12,   -1,   15,   -2,    7,
        -19,   48,  -51,   11,    5,  -28,  -44,  -10,   36,  -41,  -21,
         30,  -50,   63,  -28,   25,   -5,  -25,  -59,    9,  -47,  -40,
        -13,   20,  -42,   48,  -12,  -21,    1,  -10,   70,  -34,  -53,
        -42,  -40,  -37,  -86,   47,  -44,   20,   33,   14,   47,   44,
        -12,    0,    7,   20,  -44,  -18,    7,   24,  -29,  -16,   37,
        -33,  -21,   -1,   33,   53,  -17,   -9,  -16,   -7,   31,   10,
        -13,   -9,  -35,    5,   35,   17,  -51,   -8,   22,   25,    2,
         30,  -33,  -17,   36,  -29,  -30,   54,   -7,   -5,   25,    3,
        -30,  -28,  -51,  -50,    7,    6,   34,   13,  -73,   56,  -22,
        -37,  -68,   38,   23,    2,   19,  -50,  -30,  -10,  -31,    1,
         32,   18,    7,  -27,   46,  -13,   -6,   29,   21,   19,  -28,
         30,   58,   47,   34,  -28,   29,   60,  -58,    8,  -39,   35,
         14,   -8,   -9,    6,  -36,  -42,  -16,  -17,  -20,   38,  -12,
         39,   41,   72,  -19,  -15,   32,   16,  -37,   10,   -4,  -17,
        -43,   43,  -56,   72,  -30,   69,  -30,   -9,   40,   17,   -3,
          4,   36,  -28,    5,  -19,   42,   30,  -35,   -9,  -24,  -27,
        -24,   -1,   23,  -22,    0,   50,  -30,   31,  -15,   18,   23,
        -46,   -9,   28,  -29,  -57,  -61,   39,  -28,  -13,   16,   17,
         56,   -6,  -42,  -18,   35,   33,  -33,   29,  -30,   -6,   -1,
          5,   12,   37,  -27,  -19,  -17,   56,   25,  -33,   55,  -16,
         12,    5,   27,   54,   52,  -32,   40,   57,   27,   49,  -50,
        -41,  -46,   52,  -13,   21,   -5,   -2,   50,   -9,  -16,   14,
          8,  -20,    3,   43,   -7,   -5,   -9,   21,  -12,   23,   -9,
         26,  -16,  -60,   47,  -27,  -53,  -48,  -56,   -1,  -67,   29,
        -52,  -25,    9,   -8,   36,  -40,  -42,   48,   63,  -34,   -2,
          3,   63,   66,    8,   21,    1,    2,  -11,  -48,  -44,  -49,
         23,  -15,   -5,    6,  -41,  -25,   20,   -3,   35,   23,  -33,
         24,  -17,    3,   17,  -18,    6,   34,  -47,   10,   59,  -42,
         16,   45,   54,   -6,   25,   59,   -2,   63,  -15,   48,   45,
         22,   10,   28,  -14,  -49,   21,   61,   56,   37,  -67,  -39,
         80,  -84,  -51,   35,   16,  -48,    6,    1,   62,    6,  -83,
         14,   38,  -19,    1,   13,  -31,  -25,  -20,   -3,   31,  -15,
        -32,  -26,   70,  -33,  -12,   -8,   -2,  -26,   26,   45,   13,
         -3,   -5,  -27,   19,    1,  -24,  -34,   42,   -3,    2,   69,
         22,  -23,   32,  -42,   64,  -15,   15,  -28,   16,   -1,   41,
          9,  -44,   33,   36,   39,   16,   12,   57,  -43,    1,  -33,
         24,   35,   30,   34,  -46,  -45,  -35,   10,   24,    4,   25,
         33,   15,    9,   22,   19,  -42,   29,   10,   17,  -20,  -10,
        -72,    0,   49,    4,  -39,   33,  -35,  -17,  -16,  -43,    6,
         35,  -28,  -35,  -10,   54,   66,   11,   50,  -47,   49,   -1,
         35,  -40,   22,    5,    4,   21,  -40,    6,  -52,   18,    3,
        -55,  -37,  -21,   16,   24,   35,   47,  -15,    7,   35,   26,
         88,    8,  -44,    8,   -7,  -31,   15,   58,   -5,    0,  -47,
        -27,   24,    0,   27,   11,   30,  -49,   -5,   46,  -29,  -38,
        -44,   18,   55,  -28,  -64,  -46,   26,   28,   24,    6,   51,
         13,  -32,   42,   18,   27,  -45,   15,  -48,   -4,   21,  -20,
        -40,   30,    5,  -36,   46,   34,   -8,   16,  -10,  -44,    3,
        -23,  -25,   58,   40,   -3,   24,  -19,    0,   14,  -19,    7,
        -34,  -26,  -24,   50,  -11,   -3,  -15,   16,   34,  -39,  -33,
         33,    8,   15,   18,   13,   46,   20,    4,   -8,  -26,  -17,
          3,   42,   46,   14,   43,  -32,   55,   16,   37,  -70,   11,
         32,  -16,    0,  -56,  -22,   12,   28,   34,    3,    9,    5,
        -39,   13,  -33,   24,   24,  -27,   42,    5,  -15,   36,   20,
        -51,   63,  -23,  -42,  -30,   10,   56,   10,  -54,   -3,  -34,
         30,  -59,  -32,  -57,    0,   38,   15,   13,  -38,   -3,  -10,
        -31,  -20,  -18,   24,   25,   27,   13,   37,  -12,   28,   51,
         28,  -14,   37,  -22,  -52,  -17,   18,   24,  -38,    0,   44,
         51,  -52,  -13,  -37,   11,  -45,   32,  -16,  -19,  -28,   32,
         38,  -41,  -39,   -1,    0,  -45,  -52,   11,    9,    8,  -11,
         11,   -7,  -32,   -6,   -1,   60,   33,    4,   26,    8,   30,
        -26,   11,   34,    1,  -51,   16,  -11,   35,    2,  -19,   41,
        -29,  -62,   25,  -19,   14,    9,   20,  -22,   -9,  -67,    0,
         16,  -24,  -72,    1,   -6,  -30,  -12,  -12,   36,  -22,    4,
        -43,   -9,   -5,   -5,   24,   20,   40,  -26,  -56,  -32,  -32,
         -8,   18,  -50,  -53,  -20,   16,  -21,  -31,   32,   -9,   46,
        -64,  -73,  -42,   24,  -40,    4,  -25,  -22,  -34,   59,   33,
         42,  -17,  -13,  -49,  -69,    8,  -27,  -51,  -54,   64,  -22,
        -33, -110,  -72,   14,   -7,  -32,  -76,    4,   20,  -94,  -43,
         23,  -39,   26,   18,  -58,  -15,   20,  -22,    3,  -68,  -21,
         24,  -38,   23,   15,  -27,  -48,   12,  -52,    6,   33,   14,
         21,  -24,  -70,  -10,    5,  -13,  -66,   21,   18,  -31,  -30,
        -30,   -8,   14,  -24,   -8,   45,  -56,  -52,  -10,   15,   -8,
         39,   14,   -1,   25,  -86,   22,   30,  -52,  -33,  -44,  -49,
         25,    4,   10,   43,   43,  -34,   36,   -7,    9,   24,  -20,
        -26,   35,  -36,   38,  -13,  -30,    0,   38,   10,  -34,  -37,
        -65,   18,   19,  -14,    2,   13,   17,    1,   11,   47,  -22,
        -32,  -46,   13,   25,   -7,  -21,  -53,   24,  -59,  -49,   -9,
        -23,  -38,  -60,  -21,  -34,  -50,  -16,  -55,   18,  -48,  -45,
        -39,  -38,    2,  -16,   31,  -24,    2,  -12,  -20,  -70,  -30,
         54,   -4,   10,   24,   32,  -30,  -15,   49,  -21,  -50,  -54,
        -15,   46,  -26,  -20,  -26,  -40,   -6,  -12,   14,  -50,  -58,
        -21,  -39,  -63,  -20,   16,    9,  -20,   17,   -4,  -44,  -20,
         20,   27,  -59,  -42,   21,   -1,   -8,   -9,   16,    2,  -33,
        -43,   40,  -63,    9,   31,   23,  -77,  -63,   51,  -20,   37,
         38,    4,  -42,    6,  -72,   27,    7,  -30,  -28,   -5,   47,
        -51,  -28,    7,  -36,  -21,    0,  -15,   33,  -40,  -39,  -34,
          3,   52,   -8,   19,   29,   49,   -9,  -10,   -5,  -15,  -93,
         11,  -15,   -1,   -8,  -32,  -40,   18,    5,   19,   14,   41,
        -35,  -15,    0,   11,   13,   -7,  -12,  -21,  -32,  -13,   25,
        -27,  -30,  -28,  -29,  -15,  -28,  -10,    1,  -31,  -10,   -7,
         27,  -36,   25,  -55,   34,   -3,  -26,  -50,  -33,   29,  -16,
        -29,  -21,   14,    7,    6,  -11,    6,  -28,  -45,  -34,  -54,
        -18,  -27,  -46,   47,   82,  -28,  -25,  -19,   14,   27,  -21,
        -22,  -73,   -7,    3,   17,   16,   -4,  -45,   16,  -76,  -53,
        -19,   34,   16,   55,   11,   41,  -11,   -7,   39,   20,  -31,
        -12,   29,  -11,   54,   53,   42,   -3,   65,    5,   -3,   54,
         61,   -5,  -10,    0,  -17,   28,   58,   25,  -13,  -22,  -27,
         29,   41,   45,    3,   60,   12,  -22,   43,   55,  -21,  -11,
          4,  -37,   -8,   24,  -11,   61,  -12,    2,   93,   -5,  -41,
         74,   -5,   29,   48,   48,  -20,  -35,   36,   31,   -8,   21,
         -1,   54,   84,  -27,   53,  -18,   10,   -2,  -29,   50,   52,
        -28,  -50,  -33,   18,   30,   27,    0,    0,   12,    1,   -2,
         29,   23,   43,   16,    6,  -21,   31,  -13,    6,   42,   -1,
         39,   31,   43,  -23,   64,   63,   56,  -10,    5,   60,  -20,
        -12,   49,   13,  -19,  -30,  -13,    2,    8,  -41,   17,   43,
        -36,   27,    3,    0,  -32,   10,   21,  -15,   59,  -44,   23,
         35,   10,  -32,  -51,  -36,  -44,   36,    4,   -6,  -18,   -7,
        -25,   53,   -6,  -26,   29,    0,  -60,   25,  -43,  -18,   -1,
         35,  -23,   -3,   22,  -51,  -50,   -4,   49,    2,  -57,   -2,
        -25,   11,   16,  -44]]; fc_w7 = np.asarray(fc_w7);

  fc_w8 = \
     [[ -44,   37,   50,  -15,    4,   26,   40,   34,  -27,   22,   -1,
         27,   50,  -49,  -53,   14,   -8,   31,   29,    6,   36,    1,
         29,    4,  -43,  -11,  -25,  -30,   20,  -45,  -64,  -26,   -3,
        -49,   -9,  -17,  -12,   36,  -32,   33,  -45,  -10,   54,   29,
         48,  -62,  -54,   37,  -32,   40,  -47,   -4,   34,  -49,  -38,
          5,   36,  -21,  -52,  -17,  -14,   -5,  -64,   38,  -58,  -67,
        -33,  -67,   15,  -27,  -59,  -30,   27,  -49,   -4,  -53,  -48,
        -20,  -51,   16,  -23,   38,  -18,  -10,    6,    4,  -45,  -28,
         37,   -5,   24,    7,  -29,  -45,   19,   42,   11,  -33,   30,
         40,  -57,  -24,   15,   26,   22,  -62,  -11,   17,   12,  -21,
          8,  -15,   -5,  -36,  -31,   18,   -9,  -17,  -63,  -69,   23,
         -3,   -2,   -1,  -41,  -12,   -8,  -35,   23,    2,  -47,   10,
        -27,  -13,  -66,   27,  -79,  -14,   -8,   -5,    5,  -41,    3,
        -28,  -41,   15,   23,    4,  -52,  -67,    0,  -42,    7,  -72,
         10,  -12,   47,   10,  -45,  -34,   50,    5,   18,    5,   18,
         15,  -42,   15,    1,  -36,  -31,  -60,   23,   35,  -48,   -7,
        -37,   -6,   41,   32,  -69,  -83,    1,  -17,   -9,   -1,   -2,
         69,  -28,  -18,  -39,  -31,   36,    1,   24,   -8,   37,   26,
        -17,    4,   28,   20,   -9,   27,  -48,  -36,  -44,   21,  -61,
        -12,  -39,   11,  -16,  -34,    2,  -32,   -4,  -15,  -22,   18,
        -36,  -16,   -6,   28,  -18,    5,   32,   28,    0,  -38,    8,
         45,    8,   13,  -13,   20,   45,   36,   18,  -14,   32,  -50,
        -20,   43,   -5,   39,  -40,  -23,  -18,  -33,   38,   48,    5,
         35,    3,  -32,   -4,  -19,  -17,   33,   37,  -24,  -41,   19,
        -18,  -17,   11,  -30,  -26,   -5,   20,    2,   52,   -9,    9,
         29,   36,  -42,  -12,   32,  -28,  -15,  -14,    5,   49,  -34,
        -26,  -11,   21,   -1,   33,  -20,    3,  -31,   22,  -26,   23,
        -40,  -49,    1,   -8,  -47,  -34,   40,   38,   27,  -28,   11,
         34,    3,   39,   50,   13,   -5,   23,    3,  -49,  -51,    9,
        -51,  -36,  -19,  -34,   23,  -54,  -28,  -44,    6,   28,   -6,
        -43,  -28,  -66,   32,    8,  -28,   14,   12,  -36,   -5,  -27,
        -13,   -1,   32,   28,  -41,    6,   33,    9,    6,  -31,   17,
        -56,  -77,  -24,  -19,  -47,    5,   11,  -15,   51,   10,  -11,
         46,   19,   17,   34,  -34,  -43,   48,  -13,   29,   39,   31,
        -42,   14,   34,    9,   23,   39,  -42,  -33,   40,   41,  -13,
         18,   13,   21,   14,    5,   38,   -4,   22,   32,  -50,   39,
        -33,   22,  -20,    8,  -18,  -30,   21,  -35,  -25,   -7,   36,
         25,   23,   26,   13,  -26,    6,    8,  -19,   38,   16,    9,
        -19,   17,   26,    0,   -6,   28,    1,   -1,   39,   20,  -15,
         23,    2,   -8,   28,  -11,  -26,   31,   -1,   15,   10,   38,
         50,  -35,  -46,  -28,  -52,  -41,   39,   30,   23,   28,  -45,
          1,  -15,   44,   22,  -45,   -6,  -52,   -2,  -17,  -39,    6,
          9,  -42,  -26,   39,  -33,  -41,   36,  -30,   32,  -21,  -47,
        -32,   38,   -2,    0,    7,  -32,  -44,   -4,    5,   -3,   -4,
         20,  -56,    1,   18,   44,  -25,   -6,  -41,  -58,  -10,  -22,
        -12,    2,   29,   20,   22,   47,   43,  -49,  -23,   -1,  -35,
         30,   59,    1,  -21,  -39,    9,   46,  -12,    4,    5,   30,
        -13,   21,   -9,   14,   18,   -3,  -38,   39,  -16,   26,   42,
        -54,    9,  -30,  -23,  -26,   -3,  -10,   18,   36,   22,   13,
        -16,  -25,   47,   19,   -4,  -27,   -1,  -40,   -1,  -12,  -15,
         -1,   47,  -43,   54,   38,  -30,   11,   45,    6,  -18,   -2,
        -25,    6,   23,   -7,   11,   13,   -2,   36,  -17,  -29,  -11,
          0,   33,   10,  -17,  -31,    4,  -24,  -12,   -7,   30,    8,
        -45,   21,  -33,   28,   44,  -15,   45,   37,  -32,    1,   30,
         38,   11,    5,  -23,    8,  -17,   22,  -15,   42,  -29,  -10,
         24,  -40,  -38,   14,  -24,  -35,  -26,   47,    2,   47,   44,
          6,   39,   67,  -17,  -21,   37,   13,  -38,  -55,  -60,  -14,
        -38,   19,  -58,  -51,  -20,  -48,  -50,   23,    9,    9,  -16,
         19,   45,   27,   21,   27,  -28,   -7,  -31,  -51,  -57,   11,
         20,   54,   49,  -13,   -2,   24,    9,  -45,   -3,   15,  -37,
        -38,   13,   10,  -24,  -32,  -76,   35,   51,  -34,   16,  -28,
        -31,  -17,    5,   46,   35,   20,   20,  -21,   13,   37,   41,
        -16,    9,    7,  -14,   35,  -46,   34,   38,  -25,  -41,   16,
         33,  -31,   18,   25,  -22,   16,    7,   33,   37,  -18,    3,
         13,  -29,  -52,   45,   39,   20,  -35,    8,    5,   18,  -36,
         28,   22,  -15,  -55,  -43,  -15,    5,  -43,   55,  -34,  -19,
         21,  -18,   30,   21,  -43,   24,   39,   15,  -18,   58,   32,
          2,   14,   24,  -29,  -11,   27,  -32,  -13,  -19,   49,   -5,
         31,  -12,   36,   29,   21,   38,   33,    9,   50,   34,  -36,
        -15,    8,   15,  -40,    5,   54,   51,  -51,  -21,    8,    8,
          4,   48,   33,   21,   11,    4,    3,   21,   22,   53,  -67,
        -23,   -6,  -31,   36,  -10,    4,   16,  -68,   11,   41,  -32,
          8,  -11,   24,  -10,  -28,  -55,   -4,  -37,   17,    6,   33,
         11,   12,  -15,  -40,   61,  -23,   -8,  -22,   30,  -28,    8,
        -11,    1,   11,   36,  -11,  -24,   25,   23,   22,   47,  -45,
        -49,    2,   12,  -14,  -19,  -16,  -35,   -6,   11,  -52,  -15,
        -26,   27,  -14,  -14,    6,   21,   53,   21,  -13,   90,  -29,
         41,   -7,  -23,  -76,    3,    1,   -2,   23,  -49,  -18,   54,
          7,   18,  -14,  -11,  -70,  -35,  -50,    3,  -28,   -4,  -43,
        -34,  -28,   25,   14,   25,   -5,   24,  -28,   26,   11,    8,
         36,  -59,   -2,   44,   48,   13,   41,  -12,    5,   -4,  -19,
          9,  -24,  -38,   13,   13,   35,   64,  -12,  -17,  -19,  -35,
          3,   89,   12,   16,   23,   41,   34,   35,   45,  -14,    8,
        -42,  -39,   36,   50,   21,  -30,   50,  -35,    6,   24,  -24,
         32,   40,  -51,   57,   33,   -2,  -59,   18,  -43,  -13,   52,
         21,    0,   21,   -1,  -38,  -34,   76,   10,  -20,  -60,   27,
         35,   44,    2,  -18,  -16,   25,   21,  -50,  -35,  -53,   36,
          3,   17,    6,  -19,   44,   -4,  -31,   -4,  -44,   -1,  -12,
         31,  -17,   -4,   47,  -43,   22,  -40,  -57,   36,   41,   -5,
        -24,  -29,   47,  -24,  -28,  -11,   21,  -20,   13,  -19,   -7,
        -31,  -10,  -11,    9,  -72,  -21,  -45,  -26,    4,  -38,   17,
         60,   28,  -25,   45,    5, -105,    7,  -44,  -45,  -43,  -31,
         19,    3,  -58,  -10,  -23,   14,  -83,   37,  -16,   39,   -3,
        -36,   43,  -34,   31,   45,  -32,   -3,  -27,   28,    7,    2,
        -62,  -29,    7,  -23,   29,   15,    9,   36,   45,   -4,   40,
         48,  -35,   21,   -5,    8,  -26,   -2,  -30,   -8,   -8,    8,
         -7,   27,   21,  -31,  -36,   41,  -30,  -24,  -38,  -17,   16,
         31,   44,   39,   24,   15,  -33,  -17,  -25,    3,   12,   25,
        -31,   64,  -41,   20,  -79,   55,  -51,  -35,  -35,   50,   47,
         20,  -23,   42,  -23,  -31,   25,  -21,    0,   83,  -10,  -70,
        -54,   30,  -30,  -59,  -30,   18,   41,  -14,  -12,   -6,  -41,
         27,  -44,  -40,   34,   -6,  -13,   29,    2,  -46,  -39,  -26,
          8,   33,  -26,  -25,   28,    3,  -30,   13,   32,   25,  -26,
        -66,  -10,   22,  -40,    2,   -6,   19,  -27,   -6,   17,    7,
         -4,  -65,  -20,   42,   -1,   34,   27,    4,  -43,  -15,  -31,
         25,   22,  -73,  -37,    3,   42,  -13,  -35,   51,  -22,    5,
          0,  -37,   17,  -24,  -31,   18,   31,    6,   30,   29,   -1,
         -8,  -37,  -90,    9,   19,  -18,  -19,   31,   -2,   20,  -25,
         -3,    6,  -15,  -13,   23,   -6,   33,   31,    7,  -16,   32,
         -3,  -27,   31,  -52, -100,   28,  -13,   -5,   18,   -6,   -6,
         16,   48,  -57,   10,   -1,    5,   -2,   -1,   58,   35,   23,
        -31,  -51,    8,   54,   -7,   26,  -44,   -9,   53,   28,  -45,
          4,   16,  -15,  -15,  -35,  -67,   18,  -31,  -22,  -32,  -35,
        -40,   18,  -54,  -20,  -40,   26,   41,   15,    5,  -24,   12,
          2,  -50,    2,  -29,   -2,  -38,  -22,   30,    0,  -12,  -59,
        -38,   -6,  -16,  -69,   -4,   -4,  -60,   14,  -59,   47,    4,
         14,  -26,   47,  -18,   11,   28,   23,  -33,  -20,  -29,   -7,
         57,  -25, -113,   -2,   11,   43,  -34,   10,   48,    5,   -6,
        -13,   34,  -43, -107,  -28,   49,   53,   45,  -17,  -21,   11,
        -12,  -24,   22,   18, -105,  -28,   52,   -8,   28,   36,  -22,
         16,  -31,   31,  -68,   29,    1,  -58,   45,    2,   -6,   46,
          9,  -13,   36,  -39,   21,   -4,   11,   29,  -24,  -25,   24,
          6,   -3,    3,   37,  -14,  -31,   40,   69,   36,  -53,   -7,
        -38,  -54,  -24,  -54,    2,  -46,  -15,    3,  -14,  -12,  -27,
        -16,   45,    9,  -42,  -15,   21,  -49,  -53,  -15,   58,   43,
        -35,   27,  -38,  -92,    6,  -55,  -43,  -54,  -42,  -35,  -25,
        -17,  -24,  -28,   38,  -21,  -31,  -29,  -32,   30,  -58,  -54,
        -30,    7,    6,   22,  -44,   18,   29,   32,   46,  -12,  -51,
        -42,  -21,   13,   15,   -3,  -47,  -69,  -44,   42,  -11,   43,
        -25,   11,  -34,  -34,   12,   -5,  -22,    7,  -28,  -27,  -64,
         57,  -19,    6,  -32,   -9,   15,   41,   43,  -20,  -13,  -32,
        -46,   39,   44,    1,  -21,    6,   11,  -29,    7,  -39,   31,
        -24,   12,   26,   25,   -8,   -3,   24,   16,   11,  -34,   -3,
         14,   48,  -22,   -5,   71,  -19,  -26,  -44,   22,   22,   21,
        -35,   29,    7,  -10,   32,  -11,    9,   22,   -1,   46,  -14,
        -30,  -33,  -28,  -43,  -47,    9,   10,   15,   22,   16,  -15,
         39,  -38,  -69,   25,    7,  -25,  -28,   -7,   44,   11,   44,
          8,  -25,  -28,    4,  -18,  -62,   -2,   22,  -37,  -34,   -7,
         20,   41,   -2,  -38,  -11,  -18,  -39,  -41,  -39,  -57,   12,
        -27,   -9,  -35,   38,   -7,  -55,   34,  -16,  -31,    8,  -54,
        -20,   -6,    8,   31,  -26,  -62,  -43,  -11,    0,  -48,  -25,
        -39,  -21,    7,  -55,   42,   42,  -18,  -40,  -28,    5,   24,
         18,  -10,   -4,   52,  -39,  -63,  -39,  -27,  -42,  -20,   -7,
        -32,  -25,   41,   36,  -73,  -81,  -30,   19,   -3,  -12,  -68,
        -58,   -3,    0,  -28,    6,  -35,   -3,    3,   21,  -51,  -26,
          7,  -16,  -26,  -20,  -36,    9,  -40,  -48,   46,   -1,  -21,
        -31,   18,    5,    0,  -31,   -1,    9,  -41,  -61,   32,  -27,
        -60,  -71,  -20,  -57,   37,   21,  -10,  -10,  -25,   37,   43,
         44,    9,  -74,  -55,   12,  -15,  -19,  -29,  -36,  -19,   -1,
         37,   14,   45,  -62,   41,   24,   33,   -4,  -50,  -29,  -32,
        -15,   19,    7,   31,    6,   21,  -20,  -13,   25,  -46,   21,
        -20,   -2,  -15,  -15,   38,   34,  -27,  -23,  -43,  -29,  -38,
        -47,  -17,   41,   -7,  -33,  -35,   53,  -20,   16,   15,  -57,
          9,   18,    1,   18,   26,   35,   -3,  -59,  -38,  -26,  -25,
         36,  -18,  -58,   38,  -46,   10,   35,  -36,  -38,  -41,  -18,
        -60,  -33,  -27,  -36,  -16,   -3,  -13,  -19,   30,   25,   18,
        -33,  -70,   -7,   -7,   14,   43,  -18,   14,  -97,   34,  -43,
         34,  -55,    7,  -15,  -55,   -7,  -30,  -43,  -79,  -31,   -3,
        -53,  -22,  -14,    1,   24,  -21,  -19,    5,  -18,   -8,   35,
        -65,    7,  -61,  -29,    6,  -41,  -26,   22,  -38,  -27,   23,
        -29,  -42,  -33,  -16,    4,   34,   10,  -49,   29,   -9,  -47,
         24,  -16,  -10,   18,  -44,   -1,   16,  -27,  -45,   15,   34,
         21,  -40,   18,   43,  -54,    9,   54,   31,  -16,  -15,   31,
         18,  -13,    6,  -39,   26,  -55,  -13,   29,  -32,  -19,  -23,
          4,  -33,   44,  -32,    7,   19,   22,   15,   23,   25,   52,
         21,   31,  -29,  -14,   16,   45,    6,    4,  -35,   63,  -19,
        -21,   55,  -39,  -46,   28,  -16,  -16,   28,  -10,   -4,   -9,
          8,  -26,   11,  -26,  -31,  -42,  -14,   27,  -20,    2,   46,
         29,  -31,  -25,   77,  -11,   24,   12,  -16,  -27,  -45,   71,
        -29,   -8,  -45,   23,   10,   19,  -32,  -52,   13,  -62, -101,
         28,  -36,  -15,  -26,  -34,  -49,  -21,   34,  -41,  -28,   38,
         -1,  -45,  -25,    1,  -55,    9,  -26,   22,   25,   12,   30,
         22,  -54,   22,  -54,  -69,    9,  -28,    4,  -11,    7,  -32,
        -24,  -21,    3,    4,  -41,  -41,   12,  -62,   -5,   -2,  -16,
        -45,  -31,   21,  -23,   -2,  -25,  -40,   -8,  -52,  -16,  -22,
        -17,   27,  -22,    9,  -49,  -27,  -49,  -24,   10,   33,  -14,
          7,   -4,  -46,    7,   38,   -2,   52,  -48,    9,    4,  -24,
         27,  -43,  -54,   18,  -27,   13,   16,   10,   19,   36,   36,
         31,  -41,  -40,  -39,  -14,    6,  -47,  -33,   10,    6,  -43,
          0,  -62,   20,    0,  -58,  -16,   26,  -55,  -70,    9,   18,
         38,    6,   37,  -52,  -16,    8,  -40,   17,   11,    2,   26,
         50,   -5,  -23,  -44,   18,    6,  -43,   43,   34,  -13,   12,
        -36,   30,  -20,    1,  -45,   30,  -36,  -59,  -21,   26,  -10,
        -34,  -26,  -45,   15,  -10,    3,  -32,   22,   27,   27,   20,
        -42,   -5,  -60,   11]]; fc_w8 = np.asarray(fc_w8);

  fc_w9 = \
     [[  31,    4,  -37,   50,   32,  -53,  -61,   28,   20,   14,   13,
        -67,   44,   11,  -45,   -6,  -46,    3,    0,  -39,  -51,  -62,
         -4,  -20,   13,   21,  -35,  -36,   12,  -59,    4,  -49,   24,
        -52,   51,    0,    2,   42,  -15,   49,  -46,   30,  -42,  -27,
         25,   16,   56,  -48,  -43,   31,    0,   -3,  -65,   16,   -4,
        -82,  -17,  -15,  -22,  -18,    6,  -45,   35,  -49,  -47,  -42,
          6,  -25,   -7,  -70,   30,   14,    4,  -32,  -81,  -53,  -16,
         32,  -22,    4,  -56,   11,  -65,  -30,  -22,  -55,   18,   10,
        -72,  -31,   30,    2,   19,    0,    2,  -64,  -36,   -6,    8,
        -66,   -6,   31,   34,   11,  -74,  -27,   22,  -35,   45,   21,
          3,  -61,  -70,  -41,  -37,  -39,  -34,  -63,   22,  -34,   24,
         13,  -44,   21,  -43,   -3,   33,   31,  -68,  -69,  -33,   -7,
         -5,   27,   12,   15,  -44,    1,  -10,   -5,  -32,  -44,  -15,
        -46,  -48,   54,    6,   -3,   -8,  -23,   42,  -49,   22,  -13,
         48,  -15,    2,   13,   -2,   25,  -38,  -61,   -4,  -29,  -38,
        -38,   38,   13,  -30,  -12,  -32,   26,  -72,  -60,  -37,  -17,
        -46,  -30,   39,   -5,   36,   47,  -69,  -36,   26,  -29,  -65,
        -78,  -41,   13,  -10,  -69,   -7,    3,  -60,    4,  -62,   -8,
        -12,  -36,  -18,   20,  -12,  -30,  -60,  -46,   26,  -38,  -57,
        -37,   15,    0,   23,  -25,   13,   21,  -40,    3,  -51,  -27,
        -23,   12,    3,   21,   37,  -33,  -61,  -24,    4,  -22,  -39,
        -34,   30,  -42,  -30,  -25,  -56,  -16,  -55,  -27,  -56,  -59,
        -30,  -25,   -4,  -21,  -48,  -48,   13,  -55,  -35,  -61,  -60,
        -11,   34,  -11,    4,   -5,  -42,  -60,   26,   12,    0,    1,
         -1,  -89,    7,  -40,   21,   28,  -16,  -21,   33,  -43,   29,
          3,  -30,   41,  -45,  -62,  -31,   18,   -7,   -1,  -57,   -5,
         -3,  -54,  -70,   27,   19,  -15,  -44,  -67,   28,    2,    1,
        -25,  -46,   -7,    1,  -14,   24,   12,  -37,  -21,   -1,  -73,
          6,   29,   42,    1,   14,  -17,  -16,   -9,  -36,  -22,  -63,
        -63,  -31,  -19,  -18,  -14,  -52,   23,    3,  -41,    2,  -53,
        -77,  -19,  -28,  -41,   47,  -61,   18,    4,   -9,   18,  -22,
         -4,  -22,    8,  -33,   -6,   13,   -9,  -40,    1,  -22,  -36,
        -32,  -15,   10,   35,  -22,  -14,  -50,    9,  -26,  -58,  -21,
        -49,  -58,  -64,  -11,  -20,   14,  -16,  -36,   49,   16,    0,
        -37,  -33,   -2,  -10,  -11,   30,  -29,    7,  -38,  -13,   53,
         83,    4,  -17,   24,  -19,  -28,   60,   15,   50,   10,   -9,
        -62,    1,   -5,   -2,  -10,   51,   49,   32,   28,  -36,  -62,
         40,  -11,   45,  -41,   -6,   11,   42,   -9,   40,   -2,   15,
        -19,  -37,  -14,  -48,  -38,   -6,   41,   14,  -19,  -20,  -20,
        -29,   20,   17,  -28,   -3,  -20,  -32,  -20,   13,  -29,  -35,
         23,   35,    3,  -74,  -50,  -59,  -19,  -65,   40,   10,  -40,
        -39,  -22,   29,   10,   -7,  -47,  -19,    3,    0,  -58,    4,
         -6,  -51,  -76,  -65,  -55, -116,  -39,   26,  -29,   32,  -20,
         -7,  -31,   -2,  -21,  -64,    9,   -4,   14,  -38,    5,  -51,
         20,   -9,  -44,  -16,   -7,  -10,  -46,   -4,   -8,  -52,   27,
         38,  -26,  -17,   24,   15,  -55,   11,  -16,  -11,   13,  -22,
        -15,   11,  -63,  -98,   35,  -29,   11,   45,  -62,  -29,    9,
         11,  -47,   34,  -41,  -56,   32,    1,   -7,   54,   10,  -13,
         19,   68,  -57,   29,   53,  -66,   14,   29,   10,   25,  -17,
         31,   26,   17,   20,  -50,   41,   32,   14,    4,   46,   25,
         48,   14,   29,   -1,  -11,  -61,   10,   71,   60,   20,   34,
        -34,  -23,   45,    4,   29,   17,  -44,   -2,   29,   10,   29,
        -40,   -9,   -2,   10,    9,   17,    5,  -41,   18,   43,  -64,
         -2,   -2,   18,  -11,    7,   28,  -22,   -7,  -22,   14,   45,
         31,   13,   30,  -39,    8,   15,   24,  -48,  -12, -104,   -6,
        -62,   37,  -24,   35,   23,   -2,  -11,  -12,  -69,  -50,  -70,
         12,    3,  -22,   13,  -19,  -26,   13,  -75,   10,  -59,   25,
         -3,  -50,   38,   10,    7,    8,  -46,  -18,  -20,   13,   12,
         -1,   55,   11,  -53,   28,    1,   16,   -5,  -37,   44,   38,
         -3,   19,   47,  -28,  -86,    3,   42,    6,   28,  -13,   19,
          6,   -8,   29,   -7,  -25,  -68,   45,   40,  -34,   30,  -29,
         34,   16,  -33,   41,   46,  -10,  -21,  -11,  -33,  -20,   30,
         42,  -11,   -8,    8,  -39,   50,   16,   23,  -16,  -15,  -12,
         46,  -15,    7,   42,   51,   10,   34,   -9,   -1,  -34,  -10,
         18,   37,  -42,   15,   32,  -31,   -7,   12,   43,   64,  -35,
         33,  -36,    0,   28,   13,  -20,   18,   -4,  -70,   33,   50,
         19,  -41,   17,  -28,  -48,   45,  -36,    3,  -43,   10,   41,
         37,  -40,    2,   39,   -1,  -17,   47,    7,    9,  -53,   -4,
        -31,   11,  -45,    7,   22,  -10,  -64,  -33,  -25,  -62,   -7,
        -61,   -4,  -57,    7,  -26,    8,   32,  -41,  -18,    6,  -54,
          7,  -28,  -59,  -10,  -65,  -22,  -41,  -32,   -2,  -59,   55,
        -36,  -35,   14,  -40,   47,  -41,   36,   10,  -16,   -7,  -35,
        -48,    4,   -9,   19,  -54,   -2,   18,   54,   20,  -32,   11,
          2,  -16,   -3,  -36,  -18,   44,    5,   39,   43,   23,   -3,
         43,    6,    1,   12,    8,   62,  -10,  -60,  -48,   32,   42,
        -54,   27,   11,   33,  -31,   42,  -45,   10,   41,   31,  -15,
         46,  -12,   32,  -49,   30,    4,   -9,  -29,  -31,   -7,   46,
        -21,   35,   -8,    1,    0,  -24,   19,   39,   38,  -18,  -27,
         -7,   22,  -21,   -7,  -35,   17,  -44,  -14,   -6,  -17,  -19,
        -36,   17,   15,   -4,    6,  -54,   44,   13,   -9,  -19,  -25,
        -11,   43,  -29,  -19,   33,  -23,  -31,   -3,  -61,  -18,  -39,
        -42,   -3,   17,   41,   29,   28,  -11,   10,   14,   23,    5,
         40,  -34,   -4,   29,   -7,  -23,   19,  -67,  -13,   18,  -24,
         47,  -59,  -44,   21,   -4,  -41,   -3,   30,  -13,  -51,   -3,
        -43,  -10,  -33,  -96,   18,   41,  -25,  -11,   -6,  -42,  -31,
          9,  -12,   -5,  -16,  -17,  -61,  -70,   19,  -89,  -34,   30,
         18,  -57,  -62,   30,    9,   68,    6,  -18,  -56,    6,   57,
         34,  -38,  -25,   12,   25,   -1,   30,   27,  -12,  -50,   54,
        -36,  -46,  -44,   11,   14,    9,   -5,  -25,   16,   -1,  -20,
        -10,  -14,    4,  -34,  -21,   19,  -19,    8,  -20,    9,   -5,
        -65,   52,    5,   25,  -37,   22,  -11,   77,   36,  -22,  -40,
         -2,  -34,  -35,   21,   15,  -33,    2,   43,   50,   36,  -16,
        -18,    2,    9,  -46,  -10,   52,  -47,   23,   10,  -52,   23,
         -2,   35,    8,    7,   15,   49,  -24,   -7,  -10,   32,  -70,
         32,  -20,   -6,   -6,   27,    1,   -7,   25,    2,  -14,   22,
         21,  -13,   43,  -31,  -22,  -21,  -17,   27,  -60,    7,  -35,
        -26,  -59,  -24,   -9,    6,  -14,  -61,  -29,   47,  -71,   29,
        -21,   -3,   18,  -51,   -7,   -5,   14,  -32,   33,   -1,  -34,
         15,  -24,  -21,  -27,  -73,    8,  -39,   26,  -59,  -30,   30,
        -24,   -6,   15,  -63,  -10,  -29,    5,  -57,  -45,  -41,  -16,
        -26,   -1,   38,  -26,   40,   47,  -18,   18,   51,  -12,    1,
          9,   23,  -38,  -60,  -19,   -7,  -34,   21,  -30,   54,   12,
        -50,    8,  -38,  -13,  -56,  -49,   27,   11,   -5,   -9,   40,
         14,  -39,    4,   16,   -1,  -29,  -44,  -25,   54,   31, -100,
         33,   58,   -7,  -42,  -14,   19,  -55,  -18,   10,   36,   31,
        -17,   36,   46,    9,  -51,   -7,   -1,  -15,    1,  -32,   -2,
        -44,   36,  -24,   11,    4,   14,   33,   62,   38,   20,   38,
          4,  -16,   -5,   34,   -5,  -49,    3,   22,   18,    4,   44,
         34,  -29,  -54,  -27,  -24,  -69,   26,   -3,   -3,  -14,  -41,
         -6,   40,  -81,  -34,   18,   30,  -31,  -11,   17,    9,  -31,
         -1,  -25,  -29,  -19,   31,   42,  -72,  -55,  -81,   30,  -36,
         -7,  -31,  -34,   21,   20,  -53,   85,   50,   20,   18,  -15,
         19,  -62,   11,  -11,  -62,  -50,  -10,  -13,    5,  -95,  -52,
        -67,  -57,  -78,   12,  -33,   19,   36,  -45,  -28,   31,  -69,
        -42,  -62,   -9,  -13,  -46,  -78,  -51,  -12,   -3,  -24,  -19,
        -43,  -24,    7,   40,   -9,    1,  -77,  -21,   22,  -34,  -30,
         45,   -9,   18,  -24,   53,  -37,  -44,   48,   13,   56,   13,
        -59,   10,   43,   33,  -20,  -24,    4,   17,   31,   18,   60,
        -37, -111,   17,  -17,   30,   15,  -53,  -61,  -12,  -15,   45,
         29,  -20,  -37,   27,  -24,   -9,  -11,   28,   17,   33,  -24,
         -5,   32,   32,   28,  -12,   13,  -21,  -21,  -49,   -2,   -7,
          6,  -34,  -27,   51,    2,  -60,  -75,  -37,  -30,   31,   43,
        -34,   25,   -7,  -43,   17,   18,  -38,  -94,  -54,   -4,   21,
          6,   52,  -24,  -38,  -13,   13,  -36,    3,  -47,  -32,  -25,
         16,  -75,   -6,  -34,  -22,  -39,    8,  -15,   31,    5,  -17,
         20,    0,  -26,   23,   -9,  -46,  -32,  -41,   15,  -53,   -5,
         19,  -33,  -28,  -46,   27,    8,   -8,   21,  -54,  -24,  -46,
         58,   -8,  -49,   15,  -42,  -60,  -57,  -39,  -32,    4,  -29,
        -44,  -28,  -69,   42,  -84,  -12,    3,  -52,  -45,   16,    0,
         27,  -15,  -62,  -24,   13,  -24,  -25,   -6,   20,   33,   34,
         19,  -54,  -39,   61,  -56,   25,    9,  -28,   -5,  -19,  -13,
         62,  -10,   -2,  -15,   19,  -33,   30,  -33,    6,   -2,  -25,
        -12,   65,  -70,  -38,  -30,   57,  -26,  -62,   -6,   -7,   38,
          9,   16,   24,  -14,  -38,   14,   52,   52,   32,   11,   22,
        -45,    6,   -7,   -4,  -23,   31,  -55,  -14,   16,   41,   34,
         -1,   20,  -10,    3,  -28,   39,   60,   14,   -7,   24,  -24,
         33,  -50,   -6,   37,  -39,  -41,    9,   -7,   37,  -59,  -22,
         -5,  -44,  -20,  -17,  -54,  -38,   -4,   32,    0,   28,  -12,
         29,    3,   26,  -69,  -11,   -2,  -45,  -45,   14,   25,    7,
          2,   -5,   28,  -41,  -23,  -31,   22,  -11,    4,   -3,   45,
        -42,   40,   46,    2,  -36,   30,  -40,   27,  -45,   30,   18,
        -75,  -27,   15,   18,    2,    7,   56,  -10,    9,   25,  -23,
        -32,  -33,  -67,  -37,    2,    0,  -19,   15,   -8,   29,   20,
         10,  -12,   19,  -58,  -78,    5,    5,  -62,  -38,  -37,  -12,
        -36,   37,  -29,   28,   -8,  -37,  -38,   42,  -31,   37,   38,
         56,   24,   -7,  -41,   22,   29,  -19,    6,   32,   28,  -29,
        -35,  -49,  -55,  -24,   12,   30,    7,    7,   33,   20,    0,
         10,    5,   40,  -18,  -42,  -24,  -31,    1,   34,   38,    1,
         10,  -32,   22,  -30,   19,  -63,   32,   21,    1,   34,   -3,
         23,  -24,  -11,  -29,   -9,   -2,  -20,  -29,   16,   24,  -32,
        -21,  -29,   30,   27,  -44,   32,    5,  -56,  -18,   38,  -43,
         13,  -12,  -40,   -8,    3,  -22,  -41,   14,  -39,   20,  -33,
         31,   13,  -39,  -56,  -29,  -28,   31,   12,   10,   -2,  -40,
         26,   35,   27,   28,    8,   -9,  -12,    7,   -8,   43,   -5,
         25,  -76,   13,   36,  -39,  -28,   18,  -25,   52,    7,   44,
         93,  -46,   49,   41,    7,    4,   -7,   23,   -3,   13,  -36,
          2,   48,   18,  -45,  -73,   19,  -57,  -37,  -50,   49,   22,
         -3,  -15,   32,  -40,   -5,   26,  -36,    9,   15,  -15,  -36,
         26,   48,  -27,  -45,   22,  -12,  -34,  -15,   28,   36,  -18,
        -28,   -1,  -28,  -22,  -41,  -33,   25,   11,  -30,  -21,  -55,
        -44,    0,   47,    7,  -29,  -18,   -5,    3,  -56,  -37,  -40,
          5,   15,  -11,   10,   29,   26,   -8,   33,  -21,   -6,   -9,
        -20,  -11,   23,  -35,    6,    3,  -11,  -26,  -20,    6,  -29,
          0,   -7,  -29,   43,  -39,    8,   10,  -11,    2,   -3,   10,
          5,  -30,   30,  -13,  -31,  -23,  -48,  -25,  -45,  -17,   32,
         -4,   15,   -4,  -10,  -14,   -9,   42,  -20,  -16,  -27,  -61,
        -26,   32,   30,   26,   39,  -51,  -37,   -1,  -10,  -37,   30,
        -17,  -58,  -19,   52,   27,   -1,  -12,   49,    0,   33,    5,
        -15,   14,   -3,  -25,   -6,   23,   31,  -20,   15,   59,    9,
         -2,   44,  -14,  -19,  -23,  -24,   29,   55,   49,   -6,   42,
         22,    0,  -54,  -13,  -46,  -58,  -18,  -32,   19,    8,  -14,
        -22,   23,  -24,   44,   59,    0,   20,   35,  -36,   73,   55,
          3,   43,  -15,   12,   -6,  -35,   35,   -1,  -25,   51,  -53,
         50,   47,   66,   39,    4,   -5,   15,   25,    8,   28,   42,
        -30,   53,   45,    6,   25,   64,  -37,  -22,  -15,   33,  -28,
        -53,    7,  -15,   40,   22,  -16,   19,   41,  -25,   -8,   25,
        -34,   31,   27,  -18,   46,   36,   40,   35,   17,   29,  -25,
         56,   -6,   21,    2,    8,  -23,  -15,   12,  -28,   14,   -1,
         21,   28,   29,   36,   45,  -35,   -3,   31,  -39,   25,   37,
         47,  -10,   38,   40,   55,   48,  -36,  -32,   49,   25,   46,
          7,  -32,   44,  -48,   -7,   12,  -18,  -37,  -35,  -11,    1,
          4,   45,   49,  -35,  -41,   65,   33,   50,   67,    7,   -4,
         -2,   -1,    6,  -14,   12,  -40,   -3,    0,   47,   16,   71,
        -45,   57,  -35,  -12,  -14,   83,   43,   33,  -44,   -1,   47,
         52,   24,   82,   64]]; fc_w9 = np.asarray(fc_w9);

  fc_W = \
   [ fc_w0, fc_w1, fc_w2, fc_w3, fc_w4, 
     fc_w5, fc_w6, fc_w7, fc_w8, fc_w9 ];                  # tableau de poids

  fc_b = \
   [ -158,  1390,    84,  -331,   182,
      459,    26,   656, -1059,  -311];                    # tableau de bias

  scale = 0.04698627069592476;                             # quant_dense/BiasAdd
  M_fc  = 4.84112206322260665e-05 / scale;                 # (quant_dense/BiasAdd/ReadVariableOp)/(quant_dense/BiasAdd)--> (S1*S2)/S3 --> Sbias/SBiasAdd
  shift = c_int(); M0 = c_int();      
  monbib.QuantizeMultiplier( c_double(M_fc), byref(M0), byref(shift) );
  #print("M_fc= ", M_fc, "M0= ", M0.value, "shift= ", shift.value);
  offset_ent =  1;                                         # input_offset  =  -zero_point de l'entrée    quant_flatten/Reshape
  offset_sor = -1;                                         # output_offset =   zero_point de la sortie   quant_dense/BiasAdd
  offset_fil =  0;                                         # output_offset =   zero_point des paramètres quant_dense/BiasAdd
  full_vec =  full_np(flatten_aux, fc_W, fc_b, M0.value, shift.value, offset_ent, offset_sor, offset_fil, verbose=1);
  #print(full_vec);
  #sys.exit(0);                                            # Terminer l'execution

  print(" \n ");
  print("************************************** ");
  print(" De-quantization                       ");
  print("************************************** ");
  #full_vec = [-24,  -8, -12,  14, -16,  13,  -6,  -7, -10, -11]; #print(full_vec);
  #full_vec = np.asarray(full_vec);                        # Convertir données à tableau numpy
  scale = 0.04698627; zero_point = -1;                     # quant_dense/BiasAdd
  full_vec = np.asarray(full_vec);
  de_q = scale*( full_vec - zero_point );                  # r = S*(q-z)
  print(de_q);
  #sys.exit(0);                                            # Terminer l'execution

  print(" \n ");
  print("************************************** ");
  print(" Performance: Exactitude               ");
  print("************************************** ");
  predict = np.argmax(full_vec);
  return predict;


print(" \n ");
print("************************************** ");
print(" Evaluation du modèle                  ");
print("************************************** ");
 
# Load MNIST data set 
mnist = keras.datasets.mnist;
(train_images, train_labels), (test_images, test_labels) = mnist.load_data();
#test_images = test_images[0:1000];
#test_labels = test_labels[0:1000];
test_images = test_images[0:1000];
test_labels = test_labels[0:1000];
 
# Imprimer quelques images
fig = plt.figure(figsize=(3,3));
plt.imshow(test_images[0], cmap="gray", interpolation=None);
plt.title(test_labels[0]);
plt.tight_layout();
plt.show();
#print(img_test);
 
pre_vec = [];                                              # Vecteur des predictions
for idx, test_image in enumerate(test_images):
  test_image = np.float32(test_image); 
  pre_vec.append( eva_model(test_image, verbose=1) );
pre_vec     = np.asarray( pre_vec );     # print( pre_vec );
test_labels = np.asarray( test_labels ); # print( test_labels );

count = 0;
for x in range(0,len(test_labels)):
  if test_labels[x] == pre_vec[x]:
    count += 1;


accuracy = ( pre_vec == test_labels ).mean();
print("Predictions: ", pre_vec );
print("Test Labels: ", test_labels );
print("Exactitude:  ", accuracy);
print("Accuracy: ", count,"/1000");


print("                                      ");
print("**************************************");
print("*  ¡Merci d'utiliser ce logiciel!    *");
print("*             (8-)                   *");
print("**************************************");        
