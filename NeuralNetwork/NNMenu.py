import pandas
import numpy
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout, Activation
import matplotlib.pyplot as plt
from keras import backend as K
import keras
import tensorflow as tf

def main():
    epochs = input("Podaj liczbe epok:")
    layers = input("Podaj liczbe warstw sieci:")
    neurons = input("Podaj liczbe neuronow w warstwach:")
    learn = input("Podaj współczynnik uczenia:")

    dataSetInitial1 = pandas.read_csv('../messidor_features.data')
    dataSetInitial = dataSetInitial1.sample(frac=1)
    dataSet = dataSetInitial.values
    inputData = dataSet[:, 0:19]
    outputData = dataSet[:, 19]
    min_max_scaler = preprocessing.MinMaxScaler()
    inputDataScaled = min_max_scaler.fit_transform(inputData)
    # print(inputDataScaled)
    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(inputDataScaled, outputData, test_size=0.3)
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)

    model = Sequential()
    model.add(Dense(19, activation="relu", input_dim=19))
    i = 0
    while i < int(layers):
        model.add(Dense(int(neurons)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.1))
        i = i + 1
        print(neurons)

    Dense(1, activation="sigmoid")

    optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
    model.compile(optimizer=optimizer,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    hist = model.fit(X_train, Y_train,
                     epochs=int(epochs),
                     validation_data=(X_val, Y_val))

    model.evaluate(X_test, Y_test)
    print(model.optimizer.get_config())

    """
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='upper right')
    plt.show()
    """
    plt.plot(hist.history['accuracy'])
    plt.plot(hist.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='lower right')
    plt.show()


if __name__ == '__main__':
    main()
