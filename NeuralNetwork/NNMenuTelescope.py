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
    batch = input("Podaj rozmiar serii/batch size dla sieci: ")

    dataSetInitial1 = pandas.read_csv('../magic04(gamma-1, hardon-0).data')
    dataSetInitial = dataSetInitial1.sample(frac=1)
    dataSet = dataSetInitial.values
    inputData = dataSet[:, 0:10]
    outputData = dataSet[:, 10]
    min_max_scaler = preprocessing.MinMaxScaler()
    inputDataScaled = min_max_scaler.fit_transform(inputData)
    # print(inputDataScaled)
    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(inputDataScaled, outputData, test_size=0.3)
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)

    model = Sequential()
    model.add(Dense(10, activation="relu", input_dim=10, kernel_regularizer="l2"))
    model.add(BatchNormalization())
    for i in layers:
        model.add(Dense(int(neurons), activation="relu", kernel_regularizer="l2"))
        model.add(BatchNormalization())
    model.add(Dense(1, activation="sigmoid"))

    optimizer = tf.keras.optimizers.SGD(learning_rate=float(learn))

    model.compile(optimizer=optimizer,
                  loss='binary_crossentropy',
                  metrics=['accuracy', 'mse', 'mae', 'crossentropy', 'poisson'])

    hist = model.fit(X_train, Y_train,
                     epochs=int(epochs),
                     validation_data=(X_val, Y_val),
                     batch_size=int(batch))

    model.evaluate(X_test, Y_test)
    print(model.optimizer.get_config())

    plt.subplot(3, 2, 1)
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='upper right')

    plt.subplot(3, 2, 2)
    plt.plot(hist.history['accuracy'])
    plt.plot(hist.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='lower right')

    plt.subplot(3, 2, 3)
    plt.plot(hist.history['mse'])
    plt.plot(hist.history['val_mse'])
    plt.title('Mean squared error')
    plt.ylabel('MSE')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='lower right')

    plt.subplot(3, 2, 4)
    plt.plot(hist.history['mae'])
    plt.plot(hist.history['val_mae'])
    plt.title('Mean absolute error')
    plt.ylabel('MAE')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='lower right')

    plt.subplot(3, 2, 5)
    plt.plot(hist.history['poisson'])
    plt.plot(hist.history['val_poisson'])
    plt.title('Poisson')
    plt.ylabel('Poisson')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='lower right')

    plt.subplot(3, 2, 6)
    plt.plot(hist.history['crossentropy'])
    plt.plot(hist.history['val_crossentropy'])
    plt.title('Crossentropy')
    plt.ylabel('Crossentropy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='lower right')

    plt.show()


if __name__ == '__main__':
    main()
