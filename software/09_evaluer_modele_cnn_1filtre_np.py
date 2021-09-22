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
  #sys.exit(0);   


  print(" \n ");
  print("************************************** ");
  print(" Convolution                           ");
  print("************************************** ");
  entree = img_test;
  '''entree = \
  [[ -6, -6, -6],
   [ -6, -6, -6],
   [ -6, -6, 55]]; entree = np.asarray(entree);'''

  filtre = \
  [[-127,  -7, -64],
   [ -82,  34, -60],
   [ -43,  64,  48]]; filtre = np.asarray(filtre);
  bias = -998;

  # Répresenter M comme 2^(-n)* M0
  scale = 0.04698891192674637;                               # quant_conv2d/Relu
  M = 0.0001722 / scale;                                     # (quant_conv2d/BiasAdd/ReadVariableOp)/(quant_conv2d/BiasAdd)--> S1*S2/ S3 --> Sbias/SBiasAdd
  shift = c_int();                                           # int8_t 
  M0    = c_int();                                           # int32_t 
  monbib.QuantizeMultiplier( c_double(M), byref(M0), byref(shift) );
  print("--- M  = 2^(-n)*M0 ---");
  print("M= ", M, "M0= ", M0.value, "shift= ", shift.value);
  offset_ent =  6;                                           # input_offset  =  -zero_point de l'entrée  quant_reshape/Reshape
  offset_sor = -1;                                           # output_offset =   zero_point de la sortie quant_conv2d/Relu

  # convolution
  conv_test = conv_np(entree, filtre, bias, M0.value, shift.value, offset_ent, offset_sor, verbose=1);
  print(conv_test);
  #sys.exit(0);                                              # Terminer l'execution

  print(" \n ");
  print("************************************** ");
  print(" MaxPooling (2,2)                      ");
  print("************************************** ");
  maxpool_test = maxpool_np(conv_test, verbose=1);
  print(maxpool_test);
  #sys.exit(0);                                              # Terminer l'execution

  print(" \n ");
  print("************************************** ");
  print(" Flatten                               ");
  print("************************************** ");
  flatten_test = flatten_np(maxpool_test, verbose=1);
  print(flatten_test);
  #sys.exit(0);                                              # Terminer l'execution

  print(" \n ");
  print("************************************** ");
  print(" Full connected                        ");
  print("************************************** ");
  '''entree = \
  [[ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 33, 40, 29, 29, 29, 29,
      6, -1, -1, -1, 19, 50, 29, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  6, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
      9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1,  0, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 50, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     50, 50, 16, -1, -1, -1, -1, -1, -1, -1, -1, 50, 50, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     37, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1]]; entree = np.asarray(entree);
  ''' 

  entree = flatten_test; entree = np.asarray([entree]);

  fc_w0 = \
  [[ -56,  19, -45, -37,  18, -14,  37,  -31,  43,  -40,  -4,  60,   54,  59,
     -42, -45,   0,  -4,  24,  26,  54,   -2,   8,   -9,   6,  22,  -94,  32,
     -15,  23, -66,  32,  14,  39,  -7,   -2,  30,  -95, -65,  30,  -12, -39,
      12, -17,  -2,  29,   6,  17,  -5,   -7,  37,  -78,  37,  18,   18,   9,
      49,   3, -83, -60,  52, -18,  41,   23, -22,  -62,  39,  71,  -26, -49,
     -67,-122, -51, -11,  -4, -23,  71,  -76, -94,   46,  73,   3,  -10, -67,
    -125, -34,  69,   1,  55, -43, -41,  -49,  38,   10, -10,  16,  -85,  -3,
       4,  63,   4,   6,   6,-117, -71,    6,  -8,   17, -59,  12,   58,  44,
      58,  77, -35, -13, -65, -13,  15,   28,  13,   24, -19,  52,   36,  -3,
      65,  71,  53,  81,  59,  39,  52,   14, -37,  -11,   3,  96,   51,  10,
      18,  71,  40, -71, -83,  18, -17,   -6,   4,  -28, -31,  36,   10, -53,
      64,  42,  78, -24, -25, -92, -62, -110,  45, -125,  22, -55,   22,  18,
      20]]; fc_w0 = np.asarray(fc_w0);

  fc_w1 = \
  [[ -64, -61, -95, -45,  18,  34,  29,  7,   17, -81, -20,  34,  -1,  39,
     -75,   4,  31, -42,  63,  59,  56, -11,  59,   8,  31,  38,   3, -22,
     -48, -28,-109, -10,  45,   3,   2,  13,  17,  42,  -1,  23,  61, -90,
     -14, -15,   3,  22,  10, -43,  40, -10, -87, -17,   4, -65, -63, -92,
      54, -24,  89, -13, -56, -14, -74, -67, -28, -69,  62, -57, -59,-107,
      15,  29, -67, -84, -33,  14,  28, -20,  56,  18, -62,-119,   2,  38,
      -3, -18,   0, -49, -14, -68,   0,  49, -79, -26,  10,  24,   8,  22,
     -68, -50,  -1,  35, -75,  54,  62, -57, -83, -72,  47,   9,  65, -88,
      23,  38,  26,  15,  62, -88, -67,  77,  -3,   1,  40, -13, -64, -17,
      23, -49,  17,  73, -97,  39,  46,  37, -15, -46,   0,  -5,  37, -48,
      45,  31,  29, -42,  -2, -49,  38,  44,  40,  51,  21,  72, -15,  21,
      47, 108,  46, -91, -34,   4,   6, -72,  72, -77, -92,  -1,  37, -53,
      31]]; fc_w1 = np.asarray(fc_w1);

  fc_w2 = \
  [[  22, -24,  56,  -7, -17,  53,  21,  12,  31,  21,  -6, -65,  -5, -53,
      67, -38,  23,   7,  35,  29,  47, -24,  23, -36, -59,   5, -12, -11,
      31, -14, -41, -18,  16,   0,  -4, -11, -42, -70,  -5, -53,  18,  16,
     -61,  60,  -8,  -8, -29,  -5, -15,  -1,  17,  45,  52,  -1,  -7,  15,
     -80, -21, -38,  14,  29,   0, -54,   3,  65, -90,  19,  -4, -30,  -6,
      13, -13,  -4, -19,  -9,  20,  18,  31,  71,  27,  59,  47,  -4,  15,
      39, -45,  52, -14,   8, 114,  94, -14,  19,  56,  10,  80, -12,  36,
     -10,  19,   0,  45,  -4,  81,  74,  32, -11,  25,  19,   3,  40,  20,
      21,  14,  69,  98,  31, -50,  26,  86,  41,  52, -28,  -4,   3, -14,
      57, 100, 117,  57,  33,  39, -47,  44, -41, -26, -12, -36,  41,  62,
      99,  23,  42, -89,   7, -17, -12,  13,  -3,  25, -57, -40,  72, -13,
     -23,  36,  75, -16, -49,  25,  61,-109,  52, -64,  39, -55,   2, -74,
    -13]]; fc_w2 = np.asarray(fc_w2);

  fc_w3 = \
  [[   8, -51, -45,  -7, -51,  72, -14,  14,  19,  -7,  18,  38,  -2,  -7,  40, -11,  53,  22,
      -1,  35,   7, -15, -15, -26,  28, -43,  95,  40,   5, -10, -16,  23,  24, -40,  17, -47,
     -12, -68,  24, -56,  47,  20, -16, -13,  27,  28, -14, -68,  43, -77,  19,  38,  70,  -1,
     -62,  40,  32,  48,  29,  20,  57, -34, -42, -28, -53,  40,  31,  18, -41,  -4,  24,   5,
      -6, -47, -13, -62, -33, -98,  62,  36,  21,  -9, -13,  15, -38, -51,  25,  33,  12,  -8,
      17,  27,  98,  -7, -26,  49, -61, -37, -75,  14, -68, -41, -28,  34,  81,  56,  27,  45,
       0,  18,  27,   9,  -6,  24, -11,  14,   6,  17,  52,  51,  74,  36,  48,  17,  15, -30,
     -18, -75,  33, -15,  73,  12,  79,  33,  28,  42,  12,  62, -41,  60, -90, -95,  -8,  26,
       8,  54,  66,  34,  30,  48,  36,  19,  44,  12,   8, -31,  33, -53, -86,  25,  13,  34,
     -45,  34,  51,  40, -29,  40,  73]]; fc_w3 = np.asarray(fc_w3);

  fc_w4 = \
  [[  32, -84,  58, -93, -32, -74, -56,  24, -16,  56, -35, -51,   9, -60,
     -15,  27,  20, -20,   8,  19,  23,  11,   4,  43,  27,  68,   1,  21,
       9,  32, -15,  12, -58,  31,  33,  35, -28,  35,  40,  37,  12,  -7,
     -47,  41,  49, -13, -45,  56,  53,  42, -25, -91, -76,  14,  18,  30,
      -5,  39, -22,  49,  65,  60, -13,  26, -71, -45,   7,  48,  66,  -3,
     -26,  29,  13,  13, -37,  91, -47,  57,  31,  42, -11,   5,  -2, -22,
      26,  -2,  16,  67,  53,  65, -20, -36,  -1,  -4, -23, -17,  23,   0,
      -4, -45, -18, -44,  63, -44,  28, -27, -18, -89, -42, -19, -17,  30,
     -19, -10, -10, -25, -53,  47, -22,  26, -75,  34, -15, -23, -98,   5,
       5,  49, -76,   8, -95,   3,  31,   1, -14,  25, -50,  37, -32,  38,
      16,  28,  94, -60, -30, -25, -27, -14,  12, -64,  50,  36, -60,  40,
     -11, -25,  28,  35,-115, -78, -28, -94, -12,  -5,  59, -22, -14,  27,
      26]]; fc_w4 = np.asarray(fc_w4);

  fc_w5 = \
  [[ -82, -26,  13, -54, -33,   8,  31, -42,  36,  51, -39,  -2, -37, -85,
     -23,  -4, -11,  32, -23,  41,  12,   6,  27,   6,  76,  47,-116,   7,
     -23,  -3, -42,  10,  19, -17,  47,  10,  37,   8,  78, -58, -45, -23,
     -11,  -7,  29,  -2, -20,  -9,  57,  57,  82,  67, -74, -16,  18,  -3,
      10,  35,   7,  31,   5,   9,  34,  28,  50,  10, -44,   0, -29, -48,
     -29,  17,  -1, -21,  -9, -59,  15,  65, -61,   6, -11, -23, -64,  -6,
     -74,  -6,  -6,   8,  14,  16, -30,  21,   1,  51, -35, -19, -77,   4,
     -47,   4, -58, -19,  -2,  53, -86,  62,  -6,  78, -31,  52,   7,  29,
     -28,  23, -66,  42,  56,   1,  -5,  62,  34,  72,  -1,  56,  39,  28,
     -22,  -9,  64,  14, -13, -11,  43,  61,  19,  44,  -1,  81,  94,  37,
      57, -19, -75, -10,  10, -26,  31,  35,  58,  45,  19,   3, -25,  75,
     -10, -56, -28,  71, -55, -59, -23,  92,  40,  16,  12,  29,   8, -72,
     -62]]; fc_w5 = np.asarray(fc_w5);

  fc_w6 = \
  [[ -41,  10,  87,  -2,   7,  36,  30,  59,  36, 100,  29,  76, -35,  28,
      47, -57, -17,   9,  22,  26,  37,   4,  14,  38, -14,  -4,-106, -13,
      24, -23, -76, -22,  33,   5, -33,  23, -42,  -1,  10, -17, -17,   9,
     -68,  38,  -1,  38, -17,  32, -60,  71, -50,  38,  46, -58,  51,  -8,
      -5,  -4,  -3,  59,  80,  28,  53, -20,  -4,   4, -66,  23,  28, -66,
       3,   3,  19,  55,  -4,  35,  -3,  -8,  -7, -52,   1,  -3,  18, -68,
      10,  47,  21,  63,  12,  78,  25,-107, -46, -50,  -6,  26, -32, -24,
      28,  31,   0, -11,  21,  28, -21,-110, -50, -59, -30, -22,   7,  32,
      71,  29,  13,  -6, -76,  32,-109, -83,  32,  12, -27, -18,  17,   1,
      50,  91,  -1, 101, -35,  14, -35, -71, -32, -77, -29,  11, -57, -41,
      48,  15,  22, -88,  52,   2, -17, -89, -72,-112,-103, -89,  19, -38,
      51, -37,  -1, -78,  40,  74,  15, -27, -98,-104,-102,  71,  82, -89,
      57]]; fc_w6 = np.asarray(fc_w6);

  fc_w7 = \
  [[ -74,  12,  36, -74, -95, -96, -23,  28, -30, -61,  30, -71,  87,  -1,
      13, -18,  11, -15, -28, -21,  21, -70, -60,   0,  36, -71,  19,  24,
      46,   8,   1,  48, -10,  17,  34,  -5, -59,  -8, -46,  73,   8, -31,
      14,  14,  75,  70, -25,  37,  62,  38, -81, -65,  67,  36,   1,  -9,
      -5,  -6,  52,  52,  49,  20,  15, -17,-112,  76,  37,  37, -13, -62,
     -23, -48,   5,  -2,  -6,  31,  -2, -83,  37,  11, -10,  -7, -22, -16,
       3, -21,  16,  37,  48,  31,  19,  23, -85,   9, -45,  43,  -6,  37,
     -17, -26,  10,   4, -63,  71, -47, -12,-127,  51, -33,  28,  27,   8,
      21,  -2, -12, -82, -97, -45, -19,  23, -41,  60, -24,  52, -93,  12,
    -101,  59, -53, -51, -79,  48,  64,  39,  38,  22, -64,  59, -88,  25,
     -10,  41, -17, -20,  -7,  69,  -3,  16,  22, -21,  13, -29, -88,  50,
     -16,  35,  77,  42, -50, -40, 101,  45, 110, -13,  56,  41,  52,  94,
      57]]; fc_w7 = np.asarray(fc_w7);

  fc_w8 = \
  [[  45,-102, -15,   1, -41,  -4,  -5,   3,   4,  41, -18,  15, -22,  39,
      36,  -6,  -1,  13,  34,  43,  37,  -7,  26,   4,  38, -52, -27, -44,
     -12,  40, -49,  11,  53,  -6,  28,  25,  -9,  26,   7,  32,  27, -15,
     -32,  51,  -4,  36,  12, -30,  58,  67,   0,  22, -38, -13,  19,   2,
       0,  26,  -4,  45,  77,  19,  55,  -1, -11, -70,  49, -51,   5, -51,
     -28,  -7,  30,  17,  -3,  60,  19, -61,  12,-111, -39, -15, -22,   3,
     -65, -23,  60, -61, -14,  37, -21, -95,  31, -15,  18,  57, -40, -33,
     -40, -39, -41, -16, -81, -16,  30, -56, -21,  37,  11,  11, -30, -36,
     -24,  13,-101,   3,  50,  18,  38, -19,  24,  -2,  27,  -2,   6, -11,
      23,  10,   1, -36,  42, -92,  18,   4,   2,   7,  18,  47,  27,  32,
      44,  35, -55,  66,   1,  -8, -83,   5,  17, -13,  29,  -5, -68,  39,
     -90, -45,  42,  43,-104,  -9,  -3, -46,  56, -95,  62,  30, -10, -80,
     -21]]; fc_w8 = np.asarray(fc_w8);

  fc_w9 = \
  [[ -93, -12, -26, -72, -47,-101,  17, -97,  -7,  21, -15, -92,  39, -27,
     -30, -18, -11, -19,  13,  23,   4, -33, -20, -98,  44,  -1, -53, -16,
       7,   9,  -6,  19,  51, -11,  33, -23, -61, -47, -74, -39,  33, -44,
     -18,  32,  72,  33,   9,  -1,  43, -14, -47, -33, -36,  11,  29,   7,
      -7,  51,   7,  35,  83,  33, -15,   5, -66,  39,  54,  14,  24, -41,
       5,  15,  -3,  52, -32,  28,   2, -81, -84,  51, -18,  -7, -27,   3,
       8, -13,  -8,  -5,  19, -11,  63, -36, -24, -55, -63,  36,  12,   4,
       5, -55, -26, -27,-101,  30, -20,  19, -47, -30,  -6,   0,  18,   3,
      43, -63, -80, -65, -19,  -4, -21,  29, -14,  -3,   3,  19, -66,  27,
      43,  35,  44,   6, -69,  36,   7,  30,  42,  16, -76,  46, -52,  43,
      46, -55,  83,  73, -33,  84, -17, -17,  -9,  -7,  -9,  -8, -15,  17,
      16,  90,  90,  15,  13,  35,  13,  37,  62, -21, 109,  69, -50,  98,
     -65]]; fc_w9 = np.asarray(fc_w9);

  fc_W = \
  [ fc_w0, fc_w1, fc_w2, fc_w3, fc_w4, 
    fc_w5, fc_w6, fc_w7, fc_w8, fc_w9 ];                     # tableau de poids

  fc_b = \
  [ -722, 4360, -1375, -2569, 1550, 
     324,  654,  -367,  -529, -527 ];                        # tableau de bias

  # Répresenter M comme 2^(-n)* M0
  scale = 0.04699312895536423;                               # quant_dense/BiasAdd
  M = (8.9531451521907e-5) / scale;                          # (quant_dense/BiasAdd/ReadVariableOp)/(quant_dense/BiasAdd)--> S1*S2/ S3 --> Sbias/Sbiasadd
  shift = c_int();                                           # int8_t 
  M0    = c_int();                                           # int32_t 
  monbib.QuantizeMultiplier( c_double(M), byref(M0), byref(shift) );
  print("--- M  = 2^(-n)*M0 ---");
  print("M= ", M, "M0= ", M0.value, "shift= ", shift.value);
  offset_ent =  1;                                           # input_offset  =  -zero_point de l'entrée  quant_flatten/Reshape
  offset_sor = -1;                                           # output_offset =   zero_point de la sortie quant_dense/BiasAdd
  offset_fil =  0;                                           # output_offset =   zero_point des paramètres quant_dense/BiasAdd

  # full connectted 
  full_vec =  full_np(entree, fc_W, fc_b, M0.value, shift.value, offset_ent, offset_sor, offset_fil, verbose=1);
  print(full_vec);
  #sys.exit(0);                                              # Terminer l'execution

  print(" \n ");
  print("************************************** ");
  print(" De-quantization                       ");
  print("************************************** ");
  scale = 0.04699313; zero_point = -1;                       # quantization
  full_vec = np.asarray(full_vec);
  de_q = scale*( full_vec - zero_point );                    # r = S*(q-z)
  print(de_q);
  #sys.exit(0);                                              # Terminer l'execution


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
test_images = test_images[0:100];
test_labels = test_labels[0:100];
 
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
print("Accuracy: ", count,"/100");


print("                                      ");
print("**************************************");
print("*  ¡Merci d'utiliser ce logiciel!    *");
print("*             (8-)                   *");
print("**************************************");      