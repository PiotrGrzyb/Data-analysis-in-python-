import pandas
import numpy
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization
from keras_visualizer import visualizer
import matplotlib.pyplot as plt


def main():
    dataSetInitial = pandas.read_csv('../magic04(gamma-1, hardon-0).data')
    dataSet = dataSetInitial.values
    inputData = dataSet[:, 0:10]
    outputData = dataSet[:, 10:11]
    min_max_scaler = preprocessing.MinMaxScaler()
    inputDataScaled = min_max_scaler.fit_transform(inputData)
    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(inputDataScaled, outputData, test_size=0.3)
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
    # print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)
    # print(X_train)
    model = Sequential([
        Dense(10, activation="tanh", input_dim=10),
        BatchNormalization(),
        Dense(32, activation="tanh"),
        BatchNormalization(),
        Dense(1, activation="sigmoid")
    ])

    model.compile(optimizer='sgd',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    hist = model.fit(X_train, Y_train,
                     epochs=10,
                     validation_data=(X_val, Y_val))
    model.evaluate(X_test, Y_test)
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
