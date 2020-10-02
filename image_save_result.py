import os 
import cv2
import numpy

path = "D:/Adiss/Adiss_RC_TI/A2B/"


folder = os.listdir(path)
#batch  = len(folder)
name="tsi"
print(name)
def batch_generator():
    images = []
    for i in range(len(folder)):
        im = cv2.imread(path + folder[i])
        #im = im[:,:256,:]
        im = cv2.flip(im, 1) 
        cv2.imwrite(path + folder[i], im)
    return images
batch_generator()