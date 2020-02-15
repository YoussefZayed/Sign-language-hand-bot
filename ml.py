import numpy as np # linear algebra
import pandas as pd
import os

import random

#deep learning imports
import keras
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.utils import to_categorical
from keras.callbacks import TensorBoard
from keras.models import load_model
from keras.optimizers import Adam
from keras import regularizers
from keras.losses import categorical_crossentropy
from keras import backend as K
from keras.utils.vis_utils import plot_model

#data visualization and plotting imports
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import cv2
import matplotlib.pyplot as plt
import seaborn as sn
import time



DATADIR = "asl-alphabet/bsl_alphabet_train" #training data directory
CATEGORIES = ['A', 'B' , 'C' , 'D' , 'del', 'E' , 'F' , 'G' , 'H', 'I', 'J', 'K', 'L' ,'M' , 'N', 'nothing', 'O', 'P' , 'Q' , 'R' , 'S' , 'space' , 'T' ,'U' , 'V', 'W', 'X' , 'Y' , 'Z']
test_dir = "asl-alphabet/bsl_alphabet_test"
def create_training_data(modeltype):
    '''This function is run for each model in order to get the training data from the filepath 
    and convert it into array format'''
    training_data = []

    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) #path to alphabets
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (64, 64))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
    return training_data
def make_data(modeltype, training_data):
    '''This formats the training data into the proper format and passes it through an generator 
    so that it can be augmented(shifted left/right, rotated, etc) and fed into the model '''
    X=[]
    y=[]
    for features,label in training_data:
        X.append(features)
        y.append(label)
    
    X = np.array(X).flatten().reshape(-1, 4096)
    X = X.astype('float32')/255.0
    y = keras.utils.to_categorical(y)
    y = np.array(y)
    return (X, y)
    
def build_model(modeltype):
    '''Builds the model based on the specified modeltype(either convolutional or fully_connected)'''
    model = Sequential()
   
    model.add(Dense(4096, activation = 'relu'))
    model.add(Dense(4096, activation = 'relu'))
    model.add(Dense(2000, activation = 'relu'))
    model.add(Dense(29, activation = 'softmax'))

    model.compile(optimizer = Adam(lr=0.0005), loss = 'categorical_crossentropy', metrics = ["accuracy"]) #learning rate reduced to help problems with overfitting
    return model
def fit_fully_connected_model(X, y, model):
    '''fits the fully connected model'''
    
    filepath = "weights2.best.h5"
    
    # saving model weights with lowest validation loss to reduce overfitting
    checkpoint = keras.callbacks.ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
    #tensorboard
    
    model.fit(X, y, epochs = 1, validation_split = 0.2, callbacks = [checkpoint])




def rotate_image(img):
    '''This function will be applied to the given test data and my own test data
    to see how rotating the data effects prediction accuracy.
    It rotates it in a way such that no part of the image is lost'''
    (h, w) = img.shape[:2]
    
    # calculate the center of the image
    center = (w / 2, h / 2)

    angle90 = 90
    angle180 = 180
    angle270 = 270

    scale = 1.0

    # Perform the counter clockwise rotation holding at the center
    # 90 degrees
    M = cv2.getRotationMatrix2D(center, angle90, scale)
    rotated90 = cv2.warpAffine(img, M, (h, w))

    # 180 degrees
    M = cv2.getRotationMatrix2D(center, angle180, scale)
    rotated180 = cv2.warpAffine(img, M, (w, h))

    # 270 degrees
    M = cv2.getRotationMatrix2D(center, angle270, scale)
    rotated270 = cv2.warpAffine(img, M, (h, w))
    
    return (rotated90, rotated180, rotated270)



def create_testing_data(path, input_shape, modeltype):
    '''This function will get and format both the testing data from the dataset and my own pictures.
    It works in almost the exact same way as training_data except it returns image names to evaluate predictions'''
    testing_data = []
    names = []
    for img in os.listdir(path):
       
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        
        rotated_90, rotated_180, rotated_270 = rotate_image(img_array) #in order to test predictions for rotated data
        imgs = [img_array, rotated_90, rotated_180, rotated_270]
        final_imgs = []
        for image in imgs:
            final_img = cv2.resize(image, (64, 64))
            final_imgs.append(final_img)
        # print(len(final_imgs))
        for final_img in final_imgs:
            testing_data.append(final_img) 
            names.append(img)
   
    new_testing_data = np.array(testing_data).flatten().reshape((-1,) + input_shape)
    new_testing_data = new_testing_data.astype('float32')/255.0
    return (testing_data, new_testing_data, names)


def calculate_loss(names,predictions):
    y_true = K.variable(np.array([CATEGORIES.index(name[0].upper()) for name in names]))
    y_pred = K.variable(np.array(predictions))
    print(y_true)
    print(y_pred)
    error = K.eval(categorical_crossentropy(y_true, y_pred))
    print(error)


modeltype = "fully_connected"
input_shape = 4096,

#getting training data
training_data = create_training_data(modeltype)
random.shuffle(training_data)

#building the model
model = load_model("weights2.best.h5")

#formatting data
X, y = make_data(modeltype, training_data)

#fitting model
fit_fully_connected_model(X, y, model)
