import cv2
from tensorflow.keras.models import Sequential, load_model
import tensorflow as tf
import numpy as np # linear algebra
import pandas as pd
import os
from datetime import datetime
import random


def create_testing_data(path, input_shape):
    '''This function will get and format both the testing data from the dataset and my own pictures.
    It works in almost the exact same way as training_data except it returns image names to evaluate predictions'''
    testing_data = []
    names = []
    for img in os.listdir(path):
       
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        
        imgs = [img_array]
        final_imgs = []
        for image in imgs:
            final_img = cv2.resize(image, (64, 64))
            final_imgs.append(final_img)
        # print(len(final_imgs))
        for final_img in final_imgs:
            testing_data.append(final_img) 
            names.append(img)
   
    new_testing_data = np.array(testing_data).flatten().reshape(-1 , input_shape)
    new_testing_data = new_testing_data.astype('float32')/255.0
    return (testing_data, new_testing_data, names)


def prediction_generator(testing_data, input_shape, model):
    '''This function generates predictions for both sets of testing data'''
    predictions=[]
    for img in testing_data:
        img = img.reshape(1,  input_shape)
        pred = model.predict_classes(img)
        predictions.append(pred[0])
    predictions = np.array(predictions)
    return predictions



def verf():
    model = load_model('weights2.best.h5')
    testing_data, new_testing_data, names = create_testing_data("verifier", 4096)

    predictions = prediction_generator(new_testing_data, 4096, model)

    CATEGORIES = ['A', 'B' , 'C' , 'D' , 'del', 'E' , 'F' , 'G' , 'H', 'I', 'J', 'K', 'L' ,'M' , 'N', 'nothing', 'O', 'P' , 'Q' , 'R' , 'S' , 'space' , 'T' ,'U' , 'V', 'W', 'X' , 'Y' , 'Z']
    answers = []
    for i in predictions:
        print(CATEGORIES[i])


def predict():
    model = load_model('weights2.best.h5')
    testing_data, new_testing_data, names = create_testing_data("verifier", 4096)

    predictions = prediction_generator(new_testing_data, 4096, model)

    CATEGORIES = ['A', 'B', 'C', 'D', 'del', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'nothing', 'O', 'P', 'Q',
                  'R', 'S', 'space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    return CATEGORIES[predictions[0]]


if __name__ == "__main__":
    verf()
