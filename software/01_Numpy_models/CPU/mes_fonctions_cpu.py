# -*- coding: utf-8 -*-
## 
# @file    mes_fonctions.py 
# @brief   Module des fonctions nécessaires  
# @details Module qui contient les fonctions pour lire les modèles crée
#          avec TensorFlow en format hdf5 et h5.
# @author  Dorfell Parra - dlparrap@unal.edu.co
# @date    2020/10/12
# @version 0.1
"""@package docstring
"""

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


def conv_fp(entree, filtre, bias, verbose):
  ''' Cette fonction fait la convolution (i.e. matmul, bias,
      ReLU6) utilisée en point flotant en  utilisant Numpy. 
      entree:            tableau Numpy de entrée.
      filtre:            filtre 3x3.
      bias:              valeur bias.
      conv_tab:          tableau avec la convolution.      '''

  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize); 

  # Initialisation
  #----------------------------------
  rangs, colonnes = entree.shape;
  conv_tab = np.zeros( (rangs-2, colonnes-2) );            # Map des caractéristiques
  for i in range(0, rangs - 2):
    for j in range(0, colonnes - 2):

      # Faire la convolution
      #----------------------------------
      ent = entree[0+i:3+i, 0+j:3+j];                      # Desplacer l'entrée
      conv_tab[i][j] = np.tensordot(ent, filtre) + bias;   # W*x + bias
      #print(conv_tab[i][j]);
      conv_tab[i][j] = max(conv_tab[i][j], 0);             # ReLU

  return conv_tab;


def dict_par_conv(parametres, verbose):
  ''' Cette fonction sert à créer un dictionnaire avec 
      les paramètres d'une couche de convolution en 
      format du dictionnaire des listes. La fonction 
      termine avec l'impression des paramètres.
      parametres:   nombre et position du modèle hdf5.              
      verbose:   imprimir les paramètres: 0 min, 1 tout.   '''

  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize); 

  # Initialisation
  #----------------------------------
  par = np.squeeze( parametres );
  rang, col, fil = par.shape;                              # rangs, colonnes et filtres
  filtres = {};                                            # dictionnaires des filtres
  for k in range(0, fil):                                  # initialiser dictionnaire
    filtres[ "fil"+str(k) ] = [];

  # Remplir le dictionnaire
  #----------------------------------
  for i in range(0, rang): 
    for j in range(0, col): 
      #print( " vecteur: \n ", par[i][j] );
      for k in range(0, fil):
        filtres["fil"+str(k)].append( par[i][j][k] );
  print( filtres );
  print(" ");


def dict_par_dense(parametres, verbose):
  ''' Cette fonction sert à créer un dictionnaire avec 
      les paramètres d'une couche full connected en 
      format du dictionnaire des listes. La fonction 
      termine avec l'impression des paramètres.
      parametres:   nombre et position du modèle hdf5.              
      verbose:   imprimir les paramètres: 0 min, 1 tout.   '''

  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize); 

  # Initialisation
  #----------------------------------
  par = np.squeeze( parametres );
  rangxcol, neu = par.shape;                               # rangs x colonnes et neurones
  neurones = {};                                           # dictionnaires des neurones
  for k in range(0, neu):                                  # initialiser dictionnaire
    neurones[ "neu"+str(k) ] = [];

  # Remplir le dictionnaire
  #----------------------------------
  for ij in range(0, rangxcol): 
    #print( " vecteur: \n ", par[ij] );
    for k in range(0, neu):
      neurones["neu"+str(k)].append( par[ij][k] );
  #print( neurones );

  # Imprimer les neurones de la couche
  #----------------------------------
  for k in range(0, neu):
    print("neu"+str(k)+":");
    print( neurones["neu"+str(k)] );
  print(" ");


def flatten_np(entree, verbose):
  ''' Cette fonction fait l'operation  flatten pour convertir
      un tableau à un vecteur en utilisant Numpy.E.g.: un 
      tableau (13, 13) à un vecteur (1, 169).
      entree:   tableau Numpy de entrée (int8).                
      flat_vec: vecteur Numpy de sortie.                   '''

  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize); 

  # Initialisation
  #----------------------------------
  rangs, colonnes = entree.shape;
  flat_vec = [];                                           # Vecteur de sortie
  for i in range(0, rangs):
    for j in range(0, colonnes):

      # Flatten (1, rangs*colonnes)
      #----------------------------------
      flat_vec.append(entree[i, j]);                       # Ajouter éléments au vec.
  flat_vec = np.asarray(flat_vec);
  return flat_vec;      


def full_np(entree, poids, bias, verbose):
  ''' Cette fonction calcule la couche full-connected 
      utilisée par Tensorflowlite en 
      utilisant Numpy.
      entree:            tableau Numpy de entrée (int8).                
      poids:             tableau de poids (int8).                
      bias:              tableau de bias  (int32).                
      output_multiplier: facteur de échelle M0.
      output_shift:      facteur n < 0 de 2^(-n).
      offset_ent:        offset d'entrée.
      offset_sor:        offset de sortie.                
      offset_fil:        offset de filtre.
      full_vec:          vecteur Numpy de sortie.          '''

  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize); 

  # Initialisation
  #----------------------------------
  full_vec = [];                                           # Vecteur de sortiee

  for idx in range(0, len(poids)):

    # Full-connected
    #----------------------------------
    Wx_b = np.tensordot( entree, poids[idx] ) + bias[idx];    # W*x + b
    #print(Wx_b);
    full_vec.append(Wx_b);

  return full_vec;  


def lir_h5_mod(fic_mod, verbose):
  ''' Cette fonction imprime les paramètres du modèle en 
      format hdf5: poids et biais.
      fic_mod:   nombre et position du modèle hdf5.              
      verbose:   imprimir les paramètres: 0 min, 1 tout.   '''

  if (verbose == 1):                                       # Imprimer tous les paramètres
    np.set_printoptions(threshold=sys.maxsize); 

  # Charger le modèle
  #----------------------------------
  model = tf.keras.models.load_model(fic_mod);
  model.summary();

  # Imprimer poids per couche
  #----------------------------------
  print(" ");
  for layer in model.layers:
    print("\n --> couche:                  \n \r", layer ); 
    print("\n --> configuration du couche: \n \r", layer.get_config() ); 
    #print("\n --> paramètres du couche:    \n \r", layer.get_weights() );
    if( layer.get_config()["name"] == "conv2d" ): 
      print("\n --> paramètres du couche:    \n \r");
      dict_par_conv(layer.get_weights()[0], 0);            # Imprimer poids
      print("biais: \n", layer.get_weights()[1]);          # Imprimer biais
    if( layer.get_config()["name"] == "dense" ): 
      print("\n --> paramètres du couche:    \n \r");
      dict_par_dense(layer.get_weights()[0], 0);           # Imprimer poids
      print("biais: \n", layer.get_weights()[1]);          # Imprimer biais
    print(" ");


def maxpool_fp( entree, verbose):
  ''' Cette fonction fait l'operation  MaxPool avec un 
      fenêtre de (2,2) utilisée  pour tflite en 
      utilisant Numpy. 
      entree:  tableau Numpy de entrée (int8).                
      max_tab: tableau Numpy de sortie.                    '''

  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize); 

  # Initialisation
  #----------------------------------
  rangs, colonnes = entree.shape;
  rangs = int(rangs/2); colonnes = int(colonnes/2);        # Dimensions de sortie
  max_tab = np.zeros( (rangs, colonnes) );                 # Map des caractéristiques
  for i in range(0, rangs):
    for j in range(0, colonnes):

      # MaxPooling (2, 2)
      #----------------------------------
      max_tab[i,j] = np.max(entree[2*i:2*i+2, 2*j:2*j+2]); # Max du fenêtre (2, 2)

  return max_tab;      


#print("                                      ");
#print("**************************************");
#print("*  ¡Merci d'utiliser ce logiciel!    *");
#print("*             (8-)                   *");
#print("**************************************");
