from tensorflow.keras.layers import Input, Conv1D, LSTM, Dense
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.callbacks import ModelCheckpoint
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# Hyperparameters

sequence_length = 100
n_channels = 1
n_classes = 3
batch_size = 16
n_epochs = 20
n_lstm_units = 32

# A simple LSTM classifier

def build_model():
    inputs = Input((sequence_length, n_channels))

    layer_LSTM = LSTM(units = n_lstm_units, return_sequences = False)(inputs)

    layer_Dense = Dense(n_classes, activation = 'softmax')(layer_LSTM)

    model = Model(inputs, layer_Dense)

    model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy'])

    return model

def load_data(type = 'train'):
    avide = pickle.load(open('data/avide/' + type + '.pkl', 'rb')) #shape (batch, time, features)
    connecte = pickle.load(open('data/connecte/' + type + '.pkl', 'rb'))
    touche = pickle.load(open('data/touche/' + type + '.pkl', 'rb'))
    X = np.concatenate((avide, connecte, touche), axis = 0)

    Y = np.zeros((len(avide) + len(connecte) + len(touche), n_classes))
    Y[:len(avide)] = np.array([1,0,0])
    Y[len(avide):len(avide) + len(connecte)] = np.array([0,1,0])
    Y[len(avide) + len(touche):len(avide) + len(connecte) + len(touche)] = np.array([0,0,1])

    return X, Y

# Training

X_train, Y_train =  load_data(type = 'train')
model = build_model()
model.summary()

checkpoint = ModelCheckpoint('best_model.h5', monitor='val_acc', verbose=0, save_best_only=True, mode='max')
model.fit(X_train, Y_train, batch_size= batch_size, epochs=n_epochs, verbose=1, callbacks=[checkpoint], validation_split=0.05)
model = load_model('best_model.h5')

# Test and confusion matrix

X_test, Y_test = load_data(type = 'test')
Y_pred = model.predict(X_test)

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


plot_confusion_matrix(Y_test.argmax(axis=1), Y_pred.argmax(axis=1), ['avide', 'connecte', 'touche'],normalize=True, title=None,cmap=plt.cm.Blues)
plt.savefig('confusion_matrix.png', bbox_inches='tight')
plt.show()