import sys
import tensorflow as tf
from tensorflow import keras

from numba import jit, cuda
import numpy as np, numba as nb
# to measure exec time
from timeit import default_timer as timer
#import code

@nb.jit#(target ="cuda")
def conv_fp(entree, filtre, bias, verbose):

  #if (verbose == 1):                                       # Imprimer tout
    #np.set_printoptions(threshold=sys.maxsize); 

  rstl = 0
  rangs, colonnes = entree.shape;
  conv_tab = np.zeros( (rangs-2, colonnes-2) );            # Map des caractéristiques
  for i in range(0, rangs - 2):
    for j in range(0, colonnes - 2):

      ent = entree[0+i:3+i, 0+j:3+j];                      # Desplacer l'entrée
      #conv_tab[i][j] = np.tensordot(ent, filtre) + bias;   # W*x + bias
      #conv_tab[i][j] = np.vdot(ent, filtre) + bias;
      for k in range(0,3):
        for l in range(0,3):
          rstl = rstl + ent[k][l]*filtre[k][l]
      conv_tab[i][j] = rstl + bias; 
      #print(ent)
      #print(filtre)
      #print(conv_tab[i][j]);
      #print(rstl);
      #input() 
      rstl = 0;
      conv_tab[i][j] = max(conv_tab[i][j], 0);             # ReLU

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

@nb.jit#(target ="cuda")
def full_np(entree, poids, bias, verbose):
  full_vec = [];                                           # Vecteur de sortiee
  rstl = 0;
  for idx in range(0, len(poids)):

    # Full-connected
    #----------------------------------
    #Wx_b = np.tensordot( entree, poids[idx] ) + bias[idx];    # W*x + b
    #print(entree);
    #print(poids[idx]);
    #print(Wx_b);
    #print(len(poids[idx][0]));
    #print(len(entree[0]));
    #input()
    for i in range(0,len(entree[0])):
      rstl = rstl + entree[0][i]*poids[idx][0][i]   
    Wx_b = rstl + bias[idx]
    rstl = 0; 
    #print(Wx_b);
    #print(len(poids[idx][0]));
    #input()    
    full_vec.append(Wx_b);

  return full_vec;  



@nb.jit#(target ="cuda")
def maxpool_fp( entree, verbose):

  #if (verbose == 1):                                       # Imprimer tout
  #  np.set_printoptions(threshold=sys.maxsize); 

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


