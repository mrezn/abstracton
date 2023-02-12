from tensorflow import keras
import seaborn as sns

from numpy.random import seed
from tensorflow.random import set_seed
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from keras.datasets import mnist
from keras.utils import np_utils
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import os
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.io import imread
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
import pickle
from data_pre import datagenerator
from find_next import findesec


def ANN_chart(y_train,Xp_chart,Xt_chart,y_test):
    y_train_ANN = np_utils.to_categorical(y_train)
    y_test_ANN = np_utils.to_categorical(y_test)
    set_seed(mode_num*28)
    inputs = keras.Input(shape=Xp_chart.shape[1])
    hidden_layer = keras.layers.Dense(128, activation="relu")(inputs)
    output_layer = keras.layers.Dense(10, activation="softmax")(hidden_layer)
    model = keras.Model(inputs=inputs, outputs=output_layer)
    print(model.summary())
    model.compile(optimizer='adam', loss=keras.losses.CategoricalCrossentropy())
    history = model.fit(Xp_chart, y_train_ANN, epochs=500)
    sns.lineplot(x=history.epoch, y=history.history['loss'])
    model.save('model_Ann_4*28_6000_chart')
    y_pred = model.predict(Xt_chart)
    cc=0
    for  i in range(len(y_pred)):
        if np.argmax(y_pred[i]) == np.argmax(y_test_ANN[i]):
            cc += 1
    ACC=((cc/len(y_pred))*100)
    print(ACC)
    re_list=np.zeros([len(y_pred),6])
    for i in range(len(y_pred)):
        list_acc=findesec.finde_second(y_pred[i])
        for j in range(4):
            re_list[i][j]=list_acc[j] 
        re_list[i][4]=ACC            
        re_list[i][5]=np.argmax(y_test_ANN[i])
    return re_list


def ANN_len(y_train,Xp_len,y_test,Xt_len):
    y_train_ANN = np_utils.to_categorical(y_train)
    y_test_ANN = np_utils.to_categorical(y_test)
    set_seed(mode_num*28)
    inputs = keras.Input(shape=Xp_len.shape[1])
    hidden_layer = keras.layers.Dense(128, activation="relu")(inputs)
    output_layer = keras.layers.Dense(10, activation="softmax")(hidden_layer)
    model = keras.Model(inputs=inputs, outputs=output_layer)
    print(model.summary())
    model.compile(optimizer='adam', loss=keras.losses.CategoricalCrossentropy())
    history = model.fit(Xp_len, y_train_ANN, epochs=500)
    sns.lineplot(x=history.epoch, y=history.history['loss'])
    model.save('model_Ann_4*28_6000_len')
    y_pred = model.predict(Xt_len)
    cc=0
    for  i in range(len(y_pred)):
        if np.argmax(y_pred[i]) == np.argmax(y_test_ANN[i]):
            cc+=1
    ACC=((cc/len(y_pred))*100)
    print(ACC)
    re_list=np.zeros([len(y_pred),6])
    for i in range(len(y_pred)):
        list_acc=findesec.finde_second(y_pred[i])
        for j in range(4):
            re_list[i][j]=list_acc[j] 
        re_list[i][4]=ACC            
        re_list[i][5]=np.argmax(y_test_ANN[i])
    return re_list