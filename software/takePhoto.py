import matplotlib as mpl
from PIL import Image, ImageFilter

import matplotlib.pyplot as plt
import numpy as np
#np.set_printoptions(threshold=sys.maxsize) # Printing all the weights

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3';                  # TF debug messages
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed


from ctypes import *
from mes_fonctions import *

'''
im = Image.open('./numero3_6.jpg').convert('L')
width = float(im.size[0])
height = float(im.size[1])
newImage = Image.new('L', (28, 28), (255))  # creates white canvas of 28x28 pixels

if width > height:  # check which dimension is bigger
	# Width is bigger. Width becomes 20 pixels.
    nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
	if (nheight == 0):  # rare case but minimum is 1 pixel
		nheight = 1
        # resize and sharpen
        img = im.resize((20, nheight), Image.ANTIALIAS) #.filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
        newImage.paste(img, (4, wtop))  # paste resized image on white canvas
    else:
    	# Height is bigger. Heigth becomes 20 pixels.
    	nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
        if (nwidth == 0):  # rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
    	img = im.resize((nwidth, 20), Image.ANTIALIAS) #.filter(ImageFilter.SHARPEN)
    	wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
    	newImage.paste(img, (wleft, 4))  # paste resized image on white canvas

    # newImage.save("sample.png

tv = list(newImage.getdata())  # get pixel values 
lst=[]
for k in tv:
lst.append(int(255-k))
tv=lst	
print(tv)
'''

#lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 23, 32, 34, 35, 35, 35, 35, 34, 35, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 148, 150, 134, 137, 136, 136, 136, 135, 136, 58, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 135, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 135, 39, 4, 5, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 138, 27, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 128, 71, 35, 36, 35, 34, 35, 17, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 14, 112, 136, 135, 136, 136, 136, 134, 86, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 80, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 3, 3, 1, 2, 144, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 142, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 3, 4, 0, 15, 178, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 190, 124, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 25, 75, 72, 73, 73, 92, 164, 180, 119, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 11, 98, 109, 109, 109, 113, 72, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 113, 114, 117, 114, 119, 132, 140, 141, 141, 118, 108, 114, 114, 114, 114, 114, 112, 111, 109, 101, 0, 0, 0, 0, 0, 0, 0, 0, 116, 117, 115, 129, 158, 150, 141, 134, 148, 173, 132, 109, 114, 113, 114, 114, 113, 111, 111, 107, 0, 0, 0, 0, 0, 0, 0, 0, 119, 118, 117, 122, 120, 112, 111, 113, 99, 148, 176, 103, 113, 113, 113, 113, 112, 112, 112, 111, 0, 0, 0, 0, 0, 0, 0, 0, 121, 120, 119, 118, 117, 114, 110, 106, 110, 174, 137, 105, 111, 112, 113, 114, 113, 113, 114, 115, 0, 0, 0, 0, 0, 0, 0, 0, 122, 120, 120, 120, 117, 128, 140, 149, 193, 160, 101, 111, 111, 112, 113, 115, 116, 116, 118, 121, 0, 0, 0, 0, 0, 0, 0, 0, 123, 121, 121, 120, 115, 150, 174, 153, 139, 157, 145, 106, 113, 114, 116, 118, 119, 121, 124, 128, 0, 0, 0, 0, 0, 0, 0, 0, 124, 123, 123, 121, 119, 114, 108, 107, 107, 107, 172, 127, 111, 117, 119, 121, 123, 125, 128, 134, 0, 0, 0, 0, 0, 0, 0, 0, 125, 124, 124, 123, 120, 120, 118, 113, 106, 119, 178, 123, 115, 119, 121, 124, 127, 129, 132, 138, 0, 0, 0, 0, 0, 0, 0, 0, 127, 125, 125, 124, 123, 117, 120, 139, 159, 181, 144, 113, 120, 120, 123, 127, 130, 132, 135, 141, 0, 0, 0, 0, 0, 0, 0, 0, 127, 126, 126, 125, 123, 158, 190, 191, 167, 131, 114, 121, 122, 124, 127, 129, 132, 135, 138, 142, 0, 0, 0, 0, 0, 0, 0, 0, 129, 127, 126, 126, 124, 136, 137, 119, 114, 119, 123, 123, 124, 126, 128, 131, 135, 137, 139, 144, 0, 0, 0, 0, 0, 0, 0, 0, 130, 128, 127, 127, 126, 121, 121, 124, 125, 125, 124, 125, 126, 128, 131, 133, 136, 139, 141, 145, 0, 0, 0, 0, 0, 0, 0, 0, 130, 129, 128, 128, 127, 127, 127, 126, 126, 126, 126, 126, 127, 129, 131, 134, 136, 138, 140, 142, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 19, 18, 17, 17, 15, 15, 15, 15, 14, 14, 14, 14, 13, 14, 14, 14, 14, 15, 0, 0, 0, 0, 0, 0, 0, 0, 20, 19, 18, 17, 16, 16, 12, 7, 5, 5, 5, 6, 12, 12, 12, 12, 13, 13, 14, 15, 0, 0, 0, 0, 0, 0, 0, 0, 20, 19, 18, 17, 16, 13, 24, 43, 51, 52, 49, 38, 7, 9, 12, 12, 13, 14, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 20, 19, 17, 17, 13, 24, 70, 59, 46, 37, 39, 84, 79, 13, 11, 13, 13, 13, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 20, 18, 17, 16, 14, 14, 10, 3, 3, 4, 5, 0, 100, 68, 0, 13, 12, 13, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 20, 18, 17, 16, 13, 12, 11, 13, 12, 11, 5, 6, 105, 48, 2, 12, 12, 13, 14, 15, 0, 0, 0, 0, 0, 0, 0, 0, 19, 18, 17, 15, 13, 12, 10, 3, 0, 2, 20, 93, 78, 1, 10, 10, 12, 12, 14, 15, 0, 0, 0, 0, 0, 0, 0, 0, 20, 18, 16, 15, 13, 12, 8, 70, 98, 92, 136, 97, 0, 8, 8, 10, 12, 12, 14, 15, 0, 0, 0, 0, 0, 0, 0, 0, 19, 18, 16, 14, 13, 11, 8, 35, 50, 34, 23, 71, 76, 3, 9, 11, 12, 13, 14, 15, 0, 0, 0, 0, 0, 0, 0, 0, 18, 17, 16, 14, 13, 11, 10, 3, 0, 3, 5, 0, 90, 39, 2, 12, 12, 13, 15, 16, 0, 0, 0, 0, 0, 0, 0, 0, 18, 17, 16, 14, 12, 11, 9, 11, 9, 5, 2, 0, 110, 44, 2, 12, 12, 13, 15, 16, 0, 0, 0, 0, 0, 0, 0, 0, 18, 17, 16, 14, 12, 11, 8, 3, 13, 26, 37, 94, 81, 1, 11, 11, 12, 13, 15, 17, 0, 0, 0, 0, 0, 0, 0, 0, 18, 18, 16, 14, 14, 6, 44, 99, 122, 115, 102, 58, 6, 10, 11, 11, 12, 14, 16, 18, 0, 0, 0, 0, 0, 0, 0, 0, 18, 18, 16, 14, 13, 10, 19, 44, 33, 14, 3, 1, 10, 11, 12, 12, 14, 15, 17, 18, 0, 0, 0, 0, 0, 0, 0, 0, 19, 18, 17, 15, 14, 13, 9, 4, 5, 9, 11, 12, 11, 11, 12, 13, 14, 16, 17, 19, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 17, 16, 14, 13, 12, 13, 12, 11, 11, 11, 11, 12, 13, 14, 15, 17, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 19, 18, 18, 16, 15, 14, 13, 13, 12, 12, 12, 12, 12, 12, 14, 16, 17, 18, 19, 21, 0, 0, 0, 0, 0, 0, 0, 0, 17, 16, 15, 14, 13, 12, 12, 12, 11, 11, 10, 10, 10, 11, 11, 11, 12, 13, 15, 17, 0, 0, 0, 0, 0, 0, 0, 0, 26, 25, 24, 24, 22, 21, 19, 18, 17, 17, 18, 20, 22, 23, 26, 31, 33, 33, 33, 32, 0, 0, 0, 0, 0, 0, 0, 0, 103, 103, 102, 102, 101, 101, 99, 98, 97, 97, 99, 100, 101, 103, 105, 108, 110, 109, 112, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 14, 13, 12, 11, 11, 11, 11, 11, 10, 9, 8, 10, 9, 9, 9, 10, 10, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 13, 13, 11, 11, 11, 10, 2, 0, 0, 0, 1, 3, 0, 6, 8, 7, 8, 9, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 11, 10, 10, 8, 45, 75, 86, 103, 116, 124, 83, 7, 6, 8, 8, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 11, 10, 8, 8, 108, 140, 99, 91, 83, 84, 141, 87, 0, 8, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 10, 9, 8, 5, 8, 7, 0, 0, 0, 0, 37, 145, 35, 0, 8, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 10, 9, 8, 6, 3, 3, 3, 3, 2, 0, 55, 139, 23, 1, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 10, 9, 7, 5, 4, 0, 8, 12, 18, 70, 144, 53, 0, 5, 5, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 10, 8, 7, 4, 9, 112, 148, 148, 156, 175, 66, 0, 5, 3, 5, 6, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 12, 11, 10, 8, 6, 6, 2, 69, 109, 91, 88, 110, 136, 30, 1, 5, 5, 6, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 12, 11, 9, 7, 6, 5, 5, 0, 0, 0, 0, 0, 88, 115, 0, 5, 5, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 12, 11, 9, 8, 6, 5, 1, 2, 4, 4, 0, 0, 87, 128, 2, 4, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 12, 10, 9, 7, 7, 4, 15, 17, 6, 11, 36, 107, 153, 33, 1, 6, 6, 7, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0, 12, 11, 9, 8, 8, 0, 79, 158, 143, 142, 139, 99, 22, 0, 5, 4, 5, 7, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 12, 11, 10, 8, 7, 5, 10, 51, 69, 44, 12, 0, 0, 6, 4, 6, 7, 9, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 12, 11, 10, 8, 7, 6, 3, 0, 0, 0, 2, 7, 5, 5, 6, 7, 8, 9, 10, 12, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 10, 9, 8, 7, 6, 7, 7, 6, 6, 5, 5, 5, 6, 7, 9, 10, 11, 13, 0, 0, 0, 0, 0, 0, 0, 0, 14, 13, 11, 10, 10, 8, 7, 7, 6, 6, 6, 7, 7, 7, 8, 9, 11, 12, 13, 14, 0, 0, 0, 0, 0, 0, 0, 0, 10, 9, 8, 6, 6, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 6, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 27, 29, 28, 27, 25, 24, 22, 20, 19, 20, 21, 22, 24, 27, 32, 35, 35, 34, 33, 32, 0, 0, 0, 0, 0, 0, 0, 0, 77, 79, 83, 87, 88, 90, 91, 90, 91, 91, 93, 93, 92, 92, 93, 93, 96, 97, 98, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lst = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 5, 5, 6, 2, 1, 1, 3, 6, 5, 5, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 5, 6, 0, 19, 26, 21, 13, 2, 4, 5, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 6, 0, 43, 62, 20, 22, 31, 36, 10, 4, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 6, 1, 29, 57, 0, 1, 2, 0, 14, 35, 3, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 6, 57, 4, 4, 6, 6, 7, 0, 29, 11, 4, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 6, 31, 5, 5, 5, 6, 4, 4, 35, 6, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 6, 3, 33, 7, 5, 6, 2, 2, 35, 20, 2, 6, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 6, 1, 27, 21, 0, 4, 16, 36, 20, 1, 6, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 5, 5, 35, 20, 29, 29, 10, 3, 6, 5, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 5, 5, 39, 59, 26, 4, 2, 1, 2, 5, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 4, 36, 13, 4, 26, 35, 34, 28, 17, 3, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 6, 1, 28, 20, 0, 6, 1, 3, 9, 17, 31, 32, 4, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 4, 10, 32, 2, 6, 5, 6, 5, 4, 2, 0, 27, 23, 1, 6, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 6, 1, 22, 19, 2, 6, 5, 5, 5, 6, 6, 2, 10, 28, 1, 6, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 6, 1, 23, 21, 0, 2, 2, 2, 2, 1, 3, 10, 33, 17, 3, 6, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 4, 8, 37, 26, 19, 17, 17, 18, 23, 29, 30, 14, 3, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 4, 6, 20, 24, 25, 25, 23, 18, 10, 2, 3, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 5, 2, 1, 1, 1, 1, 2, 4, 6, 5, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]

lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 83, 255, 197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 241, 255, 197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 125, 47, 47, 47, 47, 47, 47, 47, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 114, 60, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 125, 24, 0, 0, 0, 0, 0, 0, 63, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 177, 154, 154, 154, 154, 154, 154, 154, 192, 222, 154, 154, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 235, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 245, 255, 255, 255, 255, 255, 175, 128, 128, 128, 128, 128, 128, 128, 156, 255, 239, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 236, 255, 255, 255, 172, 141, 53, 0, 0, 0, 0, 0, 0, 0, 32, 161, 255, 236, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 143, 154, 154, 154, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 127, 255, 243, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 74, 115, 255, 255, 249, 181, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 124, 255, 255, 255, 247, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 47, 47, 13, 0, 29, 47, 47, 47, 47, 125, 255, 255, 244, 208, 182, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 227, 255, 255, 94, 33, 172, 255, 255, 255, 255, 255, 244, 222, 172, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 217, 235, 235, 235, 249, 255, 242, 235, 235, 235, 235, 235, 158, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 185, 255, 96, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 26, 26, 45, 255, 159, 26, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 180, 255, 185, 179, 179, 210, 255, 121, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 181, 181, 128, 11, 0, 0, 53, 202, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 198, 180, 32, 0, 0, 0, 0, 0, 45, 210, 185, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 255, 149, 0, 0, 0, 0, 0, 0, 0, 191, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 191, 0, 0, 0, 0, 0, 0, 0, 15, 198, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 191, 0, 0, 0, 0, 0, 0, 0, 149, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 191, 0, 0, 0, 0, 0, 0, 0, 149, 255, 138, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 91, 191, 0, 0, 0, 0, 0, 0, 74, 223, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 76, 229, 229, 229, 229, 229, 229, 240, 255, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 96, 229, 229, 229, 229, 172, 0, 149, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 149, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 149, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 223, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 106, 255, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 159, 255, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 223, 198, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 149, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 149, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 149, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 83, 255, 197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 241, 255, 197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 125, 47, 47, 47, 47, 47, 47, 47, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 114, 60, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 125, 24, 0, 0, 0, 0, 0, 0, 63, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 177, 154, 154, 154, 154, 154, 154, 154, 192, 222, 154, 154, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 235, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 245, 255, 255, 255, 255, 255, 175, 128, 128, 128, 128, 128, 128, 128, 156, 255, 239, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 236, 255, 255, 255, 172, 141, 53, 0, 0, 0, 0, 0, 0, 0, 32, 161, 255, 236, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 143, 154, 154, 154, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 127, 255, 243, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 74, 115, 255, 255, 249, 181, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 124, 255, 255, 255, 247, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 47, 47, 13, 0, 29, 47, 47, 47, 47, 125, 255, 255, 244, 208, 182, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 227, 255, 255, 94, 33, 172, 255, 255, 255, 255, 255, 244, 222, 172, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 217, 235, 235, 235, 249, 255, 242, 235, 235, 235, 235, 235, 158, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 185, 255, 96, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

row = []
colum = []
count = 0
for x in lst:
	if x != 0:
		x = x + 20	
	row.append(x)
	if count == 28 - 1:
		colum.append(row)
		row = []
		count = 0
	else:
		count = count + 1    

print(colum)	


img_test = np.asarray(colum);

# Imprimer quelques images
fig = plt.figure(figsize=(3,3)); 
plt.imshow(img_test, cmap="gray", interpolation=None);
plt.title(r"$~5~$");
plt.tight_layout();
plt.show();
print(img_test);


'''
print(" \n ");
print("************************************** ");
print(" Quantization de l'image               ");
print("************************************** ");
scale = 0.04896376;  zero_point = -6;
img_test = quant_np(img_test, scale, zero_point, verbose=1);
print(img_test);
#sys.exit(0); 
'''