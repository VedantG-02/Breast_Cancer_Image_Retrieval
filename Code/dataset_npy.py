import os
import cv2
import random
import numpy as np

X = []
y_subclass = []
y_mainclass = []

i = 1

path = os.path.join(os.getcwd(),'BreaKHis_v1','Dataset_400X')

for files in os.listdir(path):
    for img_fldr in os.listdir(os.path.join(path, files)):
        for imgs in os.listdir(os.path.join(path, files, img_fldr)):
            img = cv2.imread(os.path.join(path, files, img_fldr, imgs))
            img = cv2.resize(img, (256, 256))
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            img = img.astype(np.float64)
            X.append(img)
            y_subclass.append(int(i))
            if i<=4:
                y_mainclass.append(0)
            else:
                y_mainclass.append(1)           
        i += 1

data_X = np.array(X)
data_X /= 255
data_y_subclass = np.array(y_subclass)
data_y_subclass -= 1
data_y_mainclass = np.array(y_mainclass)


np.save('X_classification_400X.npy', data_X)
np.save('y_subclass_classification_400X.npy', data_y_subclass)
np.save('y_mainclass_classification_400X.npy', data_y_mainclass)
