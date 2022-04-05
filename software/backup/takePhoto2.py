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
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3';                  # TF debug messages
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed

import sys
import tensorflow as tf
from tensorflow import keras

from ctypes import *
from mes_fonctions import *


import cv2
import numpy as np
import math
from scipy import ndimage


def getBestShift(img):
    cy,cx = ndimage.measurements.center_of_mass(img)

    rows,cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx,shifty


def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted

gray = cv2.imread("numero3.jpg", 0)
# gray = cv2.imread(no, 0)
# rescale it
gray = cv2.resize(255-gray, (28, 28))
# better black and white version
(thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
while np.sum(gray[0]) == 0:
	gray = gray[1:]
while np.sum(gray[:,0]) == 0:
	gray = np.delete(gray,0,1)
while np.sum(gray[-1]) == 0:
	gray = gray[:-1]
while np.sum(gray[:,-1]) == 0:
	gray = np.delete(gray,-1,1)
rows,cols = gray.shape
if rows > cols:
	factor = 20.0/rows
	rows = 20
	cols = int(round(cols*factor))
	# first cols than rows
	gray = cv2.resize(gray, (cols,rows))
else:
	factor = 20.0/cols
	cols = 20
	rows = int(round(rows*factor))
	# first cols than rows
	gray = cv2.resize(gray, (cols, rows))

print(gray)
colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')

shiftx,shifty = getBestShift(gray)
shifted = shift(gray,shiftx,shifty)
gray = shifted
# save the processed images
print(gray)
cv2.imwrite("own3.png", gray)






print(gray.ndim)
img_test = gray







