from tensorflow.keras.layers import Input, Conv1D, LSTM, Dense
from tensorflow.keras.models import Model, ModelCheckpoint
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix

# Hyperparameters

sequence_length = 100
n_channels = 1
n_classes = 3
batch_size = 16
n_epochs = 20
n_lstm_units = 32

# A simple LSTM classifier

def build_model():
    inputs = Input(sequence_length, n_channels)

    layer_LSTM = LSTM(units = n_lstm_units, return_sequences = True)(inputs)

    layer_Dense = Dense(n_classes, activation = 'softmax')(layer_LSTM)

    model = Model(inputs, layer_Dense)

    model.compile(loss = 'binary_crossentropy', optimizer = 'adam')

    return model

# Architecture base de données :
# data/classe_1/
# data/classe_2/
# ...
# Dans chaque dossier classe, des séquences de signaux types
# Périodiques, même longueur

def load_data(type = 'train'):
    with open('data/classe_1/' + type + '.pkl', 'rb') as f1:
        classe_1 = pickle.load(f1) #shape (batch, time, features)
    with open('data/classe_2/' + type + '.pkl', 'rb') as f2:
        classe_2 = pickle.load(f2)
    with open('data/classe_3/' + type + '.pkl', 'rb') as f3:
        classe_3 = pickle.load(f3)
    X = np.concatenate((classe_1, classe_2, classe_3), axis = 0)

    Y = np.zeros((len(classe_1) + len(classe_2) + len(classe_3), n_classes))
    Y[:len(classe_1)] = np.array([1,0,0])
    Y[len(classe_1):len(classe_1) + len(classe_2)] = np.array([0,1,0])
    Y[len(classe_1) + len(classe_2):len(classe_1) + len(classe_2) + len(classe_3)] = np.array([0,0,1])

    return X, Y

# Training

X_train, Y_train =  load_data(type = 'train')
model = build_model()

checkpoint = ModelCheckpoint('model_best.h5', monitor='val_acc', verbose=0, save_best_only=True, mode='max')
model.fit(X_train, Y_train, batch_size= batch_size, epochs=n_epochs, verbose=1, callbacks=[checkpoint], validation_split=0.05)
model.save('model.h5')

# Test and confusion matrix

X_test, Y_test = load_data(type = 'test')
model.evaluate(X_test, Y_test)
Y_pred = model.predict(X_test)

confusion_matrix(Y_test, Y_pred)