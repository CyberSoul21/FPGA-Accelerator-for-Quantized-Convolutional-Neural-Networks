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


# Importer la bibliothèque C++
monbib = CDLL("mes_fon_CPP/monbib.so");                    # Bibliothèque CPP
#print(monbib);  monbib.print_cpp();                       # preuve la bibliothèque

def conv_np(entree, filtre, bias, output_multiplier, output_shift, offset_ent, offset_sor, verbose):
  ''' Cette fonction fait la convolution (i.e. matmul, bias,
      clamp, ReLU6, quantization) utilisée  pour tflite en 
      utilisant Numpy. 
      entree:            tableau Numpy de entrée (uint8).
      filtre:            filtre 3x3 (uint8).
      bias:              valeur bias  (int32).
      output_multiplier: facteur de échelle M0.
      output_shift:      facteur n < 0 de 2^(-n).
      offset_ent:        offset d'entrée.
      offset_sor:        offset de sortie.                
      conv_tab:          tableau avec la convolution.      '''

  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize); 

  # Initialisation
  #----------------------------------
  min_val = -128; max_val = 127;                           # min/max pour int8
  rangs, colonnes = entree.shape;
  conv_tab = np.zeros( (rangs-2, colonnes-2) );            # Map des caractéristiques
  for i in range(0, rangs - 2):
    for j in range(0, colonnes - 2):

      # Faire la convolution
      #----------------------------------
      ent = entree[0+i:3+i, 0+j:3+j];                      # Desplacer l'entrée
      ent = ent + offset_ent;   
      conv_tab[i][j] = np.tensordot(ent, filtre) + bias;   # W*x + bias
      #print(conv_tab[i][j]);
      #print("ent = ")
      #print(ent)
      #print("filtre = ")
      #print(filtre)
      #print("conv_tab[i][j] = ")
      #print(conv_tab[i][j])
      # À échelle réduite
      #----------------------------------
      nom_int = c_int( int(conv_tab[i][j]) );              # Ctype int32_t
      monbib.MultiplyByQuantizedMultiplier.restype = c_int;# Valeur à rendre
      conv_tab[i][j] = monbib.MultiplyByQuantizedMultiplier(nom_int, output_multiplier, output_shift);
      #print("Quantized_conv_tab[i][j] = ")
      #print(conv_tab[i][j])
      #input("Press Enter to continue...")
      # Cast à uint8 [0, 255]
      #----------------------------------
      conv_tab[i][j] = min( max(conv_tab[i][j], 0), 255 ); # Cast à uint8
      conv_tab[i][j] = conv_tab[i][j] +  offset_sor;       # de tflite: acc + output_offset

      # Faire le clamp entre [-128, 127]
      #----------------------------------
      conv_tab[i][j] = max( conv_tab[i][j], min_val );     # Clamp 
      conv_tab[i][j] = min( conv_tab[i][j], max_val );     # Clamp

  return conv_tab;


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


def full_np(entree, poids, bias, output_multiplier, output_shift, offset_ent, offset_sor, offset_fil, verbose):
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
  min_val = -128; max_val = 127;                           # Cast de int32 à int8  
  full_vec = [];                                           # Vecteur de sortiee

  for idx in range(0, len(poids)):

    # Full-connected
    #----------------------------------
    ent = entree + offset_ent;                             # de tflite: input_val + input_offset
    poids[idx] = poids[idx] + offset_fil;                  # de tflite: filtre + filtre_offset
    Wx_b = np.tensordot( ent, poids[idx] ) + bias[idx];    # W*x + b
    #print(Wx_b);
    #print(idx);
    #sys.exit(0);
    # À échelle réduite
    #----------------------------------    
    nom_int = c_int( int(Wx_b) );                          # Ctype int32_t       
    monbib.MultiplyByQuantizedMultiplier.restype = c_int;  # Valeur à rendre
    nom_int = monbib.MultiplyByQuantizedMultiplier(nom_int, output_multiplier, output_shift); 

    # Faire le clamp entre [-128, 127]
    #----------------------------------
    nom_int = nom_int + offset_sor;                        # de tflite: acc += output_offset
    nom_int = max( nom_int, min_val );                     # Clamp 
    nom_int = min( nom_int, max_val );                     # Clamp
    #print(nom_int);
    #sys.exit(0);
    full_vec.append(nom_int);

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
    print( "--> couche: ", layer ); 
    print( "--> configuration du couche: ", layer.get_config() ); 
    print( "--> paramètres du couche: ", layer.get_weights() );
    print(" ");


def lir_tflite_mod(fic_mod, verbose):
  ''' Cette fonction imprime les paramètres du modèle en 
      format tflite: poids et biais.
      fic_mod:   nombre et position du modèle tflite. 
      verbose:   imprimir les paramètres: 0 min, 1 tout.   '''

  if (verbose == 1):                                       # Imprimer tous les paramètres
    np.set_printoptions(threshold=sys.maxsize); 

  # Charger le modèle tflite en allouer tensors.
  #----------------------------------
  interpreters = tf.lite.Interpreter( model_path=fic_mod );
  interpreters.allocate_tensors();
  
  # Obtenir tensor de entrée et sortie.
  input_details  = interpreters.get_input_details();
  output_details = interpreters.get_output_details();
  tensor_details = interpreters.get_tensor_details();
  #print("tensor_details: ", tensor_details);
  
  # Imprimer poids per couche
  #----------------------------------
  print(" ");
  for i in range( 0, len(interpreters.get_tensor_details()) ):
    try: 
      print("prenom: ", interpreters.get_tensor_details()[i]["name"] );
      if ("sequential" in interpreters.get_tensor_details()[i]["name"] ):
        print("paramètres: ", interpreters.get_tensor(i) );
        print(" ");
    except:
      print("Le tensor ",i," est null.");


def maxpool_np( entree, verbose):
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


def quant_np( entree, scale, zero_point, verbose):
  ''' Cette fonction fait la quantization utilisée pour 
      tflite en utilisant Numpy. 
      entree:     tableau Numpy de entrée.
      scale:      scale des quantization.
      zero_point: position des zero.                      
      clampled:   tableau Numpy de sortie.                 '''

  if (verbose == 1):                                       # Imprimer tout
    np.set_printoptions(threshold=sys.maxsize); 

  # Initialisation
  #----------------------------------
  rangs, colonnes = entree.shape;
  print("nombre des rangs:    ", rangs); 
  print("nombre des colonnes: ", colonnes);
  clamped = np.zeros( (rangs, colonnes) );
  min_val = -128; max_val = 127;                           # min/max pour int8
  
  # Faire la quantization
  #----------------------------------
  unclamped = ( entree / scale ) + zero_point;             # q = r/s + z
  #print(unclamped);
 
  # On utilise clamped pour l'entrée
  for i  in range(0, rangs):                               # rangs
    for j  in range(0, colonnes):                          # colonnes
      clamped[i, j] = max( unclamped[i, j], min_val );     # clamp
      clamped[i, j] = min(   clamped[i, j], max_val );     # clamp
      clamped[i, j] = int( np.round(clamped[i, j]) );       

  return clamped;


#print("                                      ");
#print("**************************************");
#print("*  ¡Merci d'utiliser ce logiciel!    *");
#print("*             (8-)                   *");
#print("**************************************");
