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

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'; # TF debug messages
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed

import sys
np.set_printoptions(threshold=sys.maxsize) # Printing all the weights
import tensorflow as tf
from tensorflow import keras


print(" \n ");
print("************************************** ");
print(" Evaluer la performance du modèle CNN  ");
print(" TensorFlowLite, i.e. Exactitude.      ");
print("************************************** ");

# See persistence of accuracy from TF to TFLite
def evaluate_model(interpreter, test_images, test_labels):
  input_index  = interpreter.get_input_details()[0]["index"];
  output_index = interpreter.get_output_details()[0]["index"];
 
  # Run predictions on every image in the "test" dataset
  prediction_digits = [];
  for i, test_image in enumerate(test_images):
    if ( (i % 1000) == 0):
      print("Evaluated on {n} results so far.".format( n=i ) );

    # Pre-processing: add batch dimension and convert to float32 to match
    # the model's input data format
    test_image = np.expand_dims( test_image, axis=0 ).astype( np.float32 );
    interpreter.set_tensor( input_index, test_image );
 
    # Run inference
    interpreter.invoke();
 
    # Post-processing: remove batch dimension and find the digit with high probability
    output = interpreter.tensor( output_index );
    digit = np.argmax( output()[0] );
    prediction_digits.append( digit );
 
  print(" ");
  # Compare prediction results with ground truth labels to calculate accuracy 
  prediction_digits = np.array( prediction_digits );
  accuracy = ( prediction_digits == test_labels ).mean();
  return accuracy
 
# Charger le base de données MNIST
mnist = keras.datasets.mnist;
(train_images, train_labels), (test_images, test_labels) = mnist.load_data();
test_images = test_images[0:100];
test_labels = test_labels[0:100];

# Charger le modèle tflite et allouer tensors.
#----------------------------------
# modèle du réseau CNN avec 1 filtre et Mnist
#inter = tf.lite.Interpreter( model_path="models/quantized_tflite_model_test.tflite" );
# modèle du réseau CNN avec 12 filtres et Mnist
inter = tf.lite.Interpreter( model_path="models/quantized_tflite_model_test_k3.tflite" );
 
#interpreter = tf.lite.Interpreter( model_content=quantized_tflite_model );
inter.allocate_tensors();
accuracy = evaluate_model( inter, test_images, test_labels );
print(" TFlite model test_accuracy: ", accuracy );


print(" \n ");
print("************************************** ");
print(" Image d'entrée                        ");
print("************************************** ");

# Definer l'image d'entrée (28,28,1)
img_test = \
[[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   3,  18,  18,  18, 126, 136, 175,  26, 166, 255, 247, 127,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,  30,  36,  94, 154, 170, 253, 253, 253, 253, 253, 225, 172, 253, 242, 195,  64,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,  49, 238, 253, 253, 253, 253, 253, 253, 253, 253, 251,  93,  82,  82,  56,  39,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,  18, 219, 253, 253, 253, 253, 253, 198, 182, 247, 241,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,  80, 156, 107, 253, 253, 205,  11,   0,  43, 154,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,  14,   1, 154, 253,  90,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 139, 253, 190,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  11, 190, 253,  70,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  35, 241, 225, 160, 108,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  81, 240, 253, 253, 119,  25,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  45, 186, 253, 253, 150,  27,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  16,  93, 252, 253, 187,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 249, 253, 249,  64,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  46, 130, 183, 253, 253, 207,   2,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  39, 148, 229, 253, 253, 253, 250, 182,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  24, 114, 221, 253, 253, 253, 253, 201,  78,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,  23,  66, 213, 253, 253, 253, 253, 198,  81,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,  18, 171, 219, 253, 253, 253, 253, 195,  80,   9,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,  55, 172, 226, 253, 253, 253, 253, 244, 133,  11,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0, 136, 253, 253, 253, 212, 135, 132,  16,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
 [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]];

img_test = np.asarray(img_test);                           # Convertir données à tableau numpy

# Imprimer quelques images
fig = plt.figure(figsize=(3,3)); 
plt.imshow(img_test, cmap="gray", interpolation=None);
plt.title(r"$~5~$");
plt.tight_layout();
plt.show();

# Pre-processer l'image d'entrée: ajouter dimension et convertir à virgule flottante
img_test = np.expand_dims( img_test, axis=0 ).astype( np.float32 );
print(img_test);

#sys.exit(0); # Terminer l'execution


print(" \n ");
print("************************************** ");
print(" Charger le modèle                     ");
print("************************************** ");

# Charger le modèle tflite et allouer tensors.
#----------------------------------
# modèle du réseau CNN avec 1 filtre et Mnist
#inter = tf.lite.Interpreter( model_path="models/quantized_tflite_model_test.tflite" );
# modèle du réseau CNN avec 12 filtres et Mnist
inter = tf.lite.Interpreter( model_path="models/quantized_tflite_model_test_k3.tflite" );
inter.allocate_tensors();
#print(inter);

# Imprimer les détails du modèle
input_details  = inter.get_input_details();  #print("input_details:  ", input_details);
output_details = inter.get_output_details(); #print("output_details: ", output_details);
tensor_details = inter.get_tensor_details(); #print("tensor_details: ", tensor_details);
output_index = inter.get_output_details()[0]["index"];     # Dernier index
  
# Imprimer poids per couche
#----------------------------------
'''
for i in range( 0, len(inter.get_tensor_details()) ):
  try: 
    print("prenom: ", inter.get_tensor_details()[i]["name"] );
    if ("sequential" in inter.get_tensor_details()[i]["name"] ):
      print("paramètres: ", inter.get_tensor(i) );
      print(" ");
  except:
      print("Le tensor ",i," est null.");
'''

# Créer dictionnaire avec l'information des couches.
#----------------------------------
dic_mod = {}; # Dictionnaire avec les nom du chaque couche
for idx in range( 0, len(inter.get_tensor_details()) ):
  try: 
    dic_mod[idx] = inter.get_tensor_details()[idx]["name"];
    #print("couche: ", inter.get_tensor_details()[idx]["name"] );
  except:
      print("Le position ",idx," est null.");
print("Dictionnaire des couches: \n", dic_mod);




print(" \n ");
print("************************************** ");
print(" Entrées et sorties des couches        ");
print("************************************** ");

# Mettre l'image du test en la couche d'entrée "input_1" avec idx = 0. (voir dic_mod)
inter.set_tensor( 0, img_test );                           # 0:"input_1"
inter.invoke();                                            # L'inference

for idx_ten in range( 0, output_index + 1 ):
  print("\n Couche: ", idx_ten);
  print("-------------------------------------- ");
  print("Paramèters: \n", inter.get_tensor_details()[idx_ten]);
  print("Tensor:     \n", inter.get_tensor(idx_ten));
  for ele_ten in range( 0, 20 ): 
    try: 
      output = inter.tensor(idx_ten); 
      print("Sortie du tensor ", ele_ten, ": \n", output()[ele_ten] ); 
      print("tf.print: ");  tf.print( output()[ele_ten] );  
    except:
      #print("Il n'y a pas résultat pour ce tensor. \n ");
      break;

#sys.exit(0); # Terminer l'execution


print("                                      ");
print("**************************************");
print("*  ¡Merci d'utiliser ce logiciel!    *");
print("*             (8-)                   *");
print("**************************************");
