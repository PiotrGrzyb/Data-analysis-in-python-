import pandas
import numpy
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout
import matplotlib.pyplot as plt
from keras import backend as K
import keras

def main():
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
    print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)
    print(X_train)
    model = Sequential([
        Dense(32, activation="relu", input_dim=19),
        BatchNormalization(),
        Dense(32, activation="relu"),
        BatchNormalization(),
        Dense(32, activation="relu"),
        BatchNormalization(),
        Dense(1, activation="sigmoid")
    ])

    model.compile(optimizer='sgd',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    #K.set_value(model.optimizer.learning_rate, 0.01)

    hist = model.fit(X_train, Y_train,
                     epochs=500,
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
