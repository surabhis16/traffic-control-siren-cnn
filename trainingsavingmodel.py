#Audio Processing Libraries
import librosa
import librosa.display
from scipy import signal

#For Playing Audios
import IPython.display as ipd

#Array Processing
import numpy as np

#Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

#Display the confusion matrix
from sklearn.metrics import confusion_matrix

#Deal with .pkl files
import pickle

#Create a dataframe
import pandas as pd

#Transform and encode the categorical targets
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder

#Split dataset
from sklearn.model_selection import train_test_split

import os
def features_extractor(file_name):
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_best') 
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=80)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)

    return mfccs_scaled_features
audio_dataset_path = r'C:\\Users\\surabhi\\Downloads\\ML\\sounds'

extracted_features = []
for path in os.listdir(audio_dataset_path):
    for file in os.listdir(os.path.join(audio_dataset_path, path)):
        if file.lower().endswith(".wav"):
            file_name = os.path.join(audio_dataset_path, path, file)
            # Assuming features_extractor is a function defined elsewhere
            data = features_extractor(file_name)  
            extracted_features.append([data, path])
f = open(r'C:\\Users\\surabhi\\OneDrive\\Desktop\\Extracted_Features352.pkl', 'wb')
pickle.dump(extracted_features, f)
f.close()
f = open(r'C:\\Users\\surabhi\\OneDrive\\Desktop\\Extracted_Features352.pkl', 'rb')
Data = pickle.load(f)
f.close()
df = pd.DataFrame(Data,columns=['feature','class'])
print(df.head())
print(df['class'].value_counts())
X = np.array(df['feature'].tolist())
Y = np.array(df['class'].tolist())
labelencoder = LabelEncoder()
y = to_categorical(labelencoder.fit_transform(Y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y, shuffle=True)
print(y_test.shape)
from keras.layers import *
from keras.models import *
from keras.callbacks import *
from keras import backend as K
from sklearn import metrics
from keras.callbacks import ModelCheckpoint, EarlyStopping
from scikeras.wrappers import KerasClassifier, KerasRegressor
from sklearn.model_selection import GridSearchCV
from datetime import datetime
X_train_features  = X_train.reshape(len(X_train),-1,1)
X_test_features = X_test.reshape(len(X_test),-1,1)
print("Reshaped Array Size", X_train_features.shape)
def cnn(optimizer="adam", activation="relu", dropout_rate=0.5):
    K.clear_session()
    inputs = Input(shape=(X_train_features.shape[1], X_train_features.shape[2]))
    
    #First Conv1D layer
    conv = Conv1D(3, 13, padding='same', activation=activation)(inputs)
    if dropout_rate != 0:
        conv = Dropout(dropout_rate)(conv)
    conv = MaxPooling1D(2)(conv)

    #Second Conv1D layer
    conv = Conv1D(16, 11, padding='same', activation=activation)(conv)
    if dropout_rate != 0:
        conv = Dropout(dropout_rate)(conv)
    conv = MaxPooling1D(2)(conv)
    
    #MaxPooling 1D
    conv = GlobalMaxPool1D()(conv)
    
    #Dense Layer 
    conv = Dense(16, activation=activation)(conv)
    outputs = Dense(y_test.shape[1], activation='softmax')(conv)
    
    model = Model(inputs, outputs)
    model.compile(loss='binary_crossentropy',optimizer=optimizer,metrics=['acc'])
    return model
model_cnn = cnn(optimizer="adam", activation="relu", dropout_rate=0)
model_cnn.summary()
early_stop = EarlyStopping(monitor = 'val_accuracy', mode ='max',
                          patience = 10, restore_best_weights = True)

history = model_cnn.fit(X_train_features, y_train, epochs = 200, 
                       callbacks = [early_stop],
                       batch_size = 64, validation_data = (X_test_features, y_test))
model.save("C:\\Users\\surabhi\\OneDrive\\Desktop\\ML\\saved_model352.h5")
