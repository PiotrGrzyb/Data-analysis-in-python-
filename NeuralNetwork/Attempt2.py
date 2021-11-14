import pandas
import numpy
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


def main():
    dataSetInitial = pandas.read_csv('../magic04(gamma-1, hardon-0).data')
    dataSet = dataSetInitial.values
    inputData = dataSet[:, 0:10].astype(float)
    outputData = dataSet[:, 10:11]


    min_max_scaler = preprocessing.MinMaxScaler()
    inputDataScaled = min_max_scaler.fit_transform(inputData)

    X_train, X_test, Y_train, Y_test = train_test_split(inputDataScaled, outputData, test_size=0.1)
    print(X_train.shape)
    print(Y_train.shape)
    print(X_test.shape)


    model = Sequential([
        Dense(19, activation="relu", input_dim=10),
        Dense(32, activation="relu"),
        Dense(1, activation="sigmoid")
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    hist = model.fit(X_train, Y_train,
                     epochs=200,
                     batch_size=64)
    model.evaluate(X_test, Y_test)


if __name__ == '__main__':
    main()
