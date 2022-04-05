import matplotlib.pyplot as plt
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'; # TF debug messages

import random
import sys
import tempfile
import tensorflow as tf
from tensorflow  import keras

import tensorflow_model_optimization as tfmot

from mes_fonctions import *
 

# Load MNIST data set 
mnist = keras.datasets.mnist;
(train_images, train_labels), (test_images, test_labels) = mnist.load_data();

# Imprimer quelques images
fig = plt.figure(figsize=(3,3)); 
for i in range(4):
  plt.subplot(2,2,i+1);
  num = random.randint(0, len(train_images));
  plt.imshow(train_images[num], cmap="gray", interpolation=None);
  plt.title(train_labels[num]);
plt.tight_layout();
#plt.show();

#print("**************************************************");
#print( train_images[0] );
#print( type(train_images[0]) );
#print("**************************************************");

# Normalize the input image so that each pixel value is between 0 to 1
#train_images = train_images / 255.0;
#test_images  = test_images  / 255.0;




print(" \n ");
print("************************************** ");
print(" Model                                 ");
print("************************************** ");

# Define the model architecture
model = keras.Sequential( [
  keras.layers.InputLayer( input_shape=(28, 28) ),
  keras.layers.Reshape( target_shape=(28, 28, 1) ),
  keras.layers.Conv2D( filters=3, kernel_size=(3, 3), activation="relu" ),
  #keras.layers.Conv2D( filters=1, kernel_size=(3, 3), activation="relu" ),
  keras.layers.MaxPooling2D( pool_size=(2, 2) ),
  keras.layers.Flatten( ),
  keras.layers.Dense( 10 )   ] );

# Train the digit classification model
model.compile( optimizer="adam", 
               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
               metrics=["accuracy"] ) ;
model.summary();

model.fit( train_images, train_labels, epochs = 1, validation_split = 0.1 );

# En sauvegardant le modèle en hdf5 
#------------------------------
#model.save("models/model_test.h5");
#model.save_weights("models/model_weights_test.h5");

model.save("models/model_test_12filter.h5");


print(" \n ");
print("************************************** ");
print(" Quantization aware model              ");
print("************************************** ");
           
# Quantize model
quantize_model = tfmot.quantization.keras.quantize_model;

# q_aware stands for quantization aware
q_aware_model = quantize_model(model);

# "quantize_model" requieres a recompile
q_aware_model.compile(optimizer="adam",
                      loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=["accuracy"] );                       
q_aware_model.summary();

# Train and evaluate the model against baseline
train_images_subset = train_images[0:1000];    # out of 6000
train_labels_subset = train_labels[0:1000];    # out of 6000

q_aware_model.fit( train_images_subset, train_labels_subset, batch_size=500, epochs=1, validation_split=0.1 );
 
_, baseline_model_accuracy =         model.evaluate( test_images, test_labels, verbose=0 );
_, q_aware_model_accuracy  = q_aware_model.evaluate( test_images, test_labels, verbose=0 );

print("Baseline test accuracy: ", baseline_model_accuracy);
print("q aware  test accuracy: ", q_aware_model_accuracy);

# En sauvegardant le modèle en hdf5 
#------------------------------
#q_aware_model.save("models/q_aware_model_test.h5");
#q_aware_model.save_weights("models/q_aware_model_weights_test.h5");

q_aware_model.save("models/q_aware_model_test_12filter.h5");



print(" \n ");
print("************************************** ");
print(" Quantized quantization aware model    ");
print("************************************** ");

# Create quantized model for TFLite backend
converter = tf.lite.TFLiteConverter.from_keras_model(q_aware_model);
converter.optimizations = [ tf.lite.Optimize.DEFAULT ];
quantized_tflite_model = converter.convert();

# See persistence of accuracy from TF to TFLite
def evaluate_model(interpreter, test_images):
  input_index  = interpreter.get_input_details()[0]["index"];
  #print("get_input_details: ", interpreter.get_input_details());
  #print("input_index: ", input_index);
  output_index = interpreter.get_output_details()[0]["index"];
  #print("get_output_details: ", interpreter.get_output_details());
  #print("output_index: ", output_index);
 
  # Run predictions on every image in the "test" dataset
  prediction_digits = [];
  for i, test_image in enumerate( test_images):
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
    #print("output()[0]:", output()[0]);
    digit = np.argmax( output()[0] );
    prediction_digits.append( digit );


  print(" ");
  # Compare prediction results with ground truth labels to calculate accuracy 
  prediction_digits = np.array( prediction_digits );
  accuracy = ( prediction_digits == test_labels ).mean();
  return accuracy


interpreter = tf.lite.Interpreter( model_content=quantized_tflite_model );
#print("interpreter: ", interpreter);
#sys.exit(0); # Terminer l'execution
interpreter.allocate_tensors();
quantized_q_aware_accuracy = evaluate_model( interpreter, test_images );


# En sauvegardant le modèle tflite 
#with tf.io.gfile.GFile('models/quantized_tflite_model_test.tflite', 'wb') as f:
#  f.write(quantized_tflite_model);

# En sauvegardant le modèle tflite 
with tf.io.gfile.GFile('models/quantized_tflite_model_test_12filter.tflite', 'wb') as f:
  f.write(quantized_tflite_model);


print("***            Accuracies          ***");
print("--------------------------------------");
print("TF float (default): ", baseline_model_accuracy);
print("TF q_aware:         ", q_aware_model_accuracy);
print("Quantized q_aware (TFlite):  ", quantized_q_aware_accuracy );


print("                                      ");
print("**************************************");
print("*  ¡Merci d'utiliser ce logiciel!    *");
print("*             (8-)                   *");
print("**************************************");
