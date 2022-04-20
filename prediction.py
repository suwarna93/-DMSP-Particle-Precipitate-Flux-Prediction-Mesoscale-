import numpy as np
import tensorflow as tf 
from tensorflow import keras

from keras.models import load_model



NN_model = load_model('NN_model/keras_NN_model.h5')



def get_prediction(data,NN_model):
    """
    Predict the class of a given data point.
    """
    return NN_model.predict(data)