import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas
from sklearn.linear_model import LinearRegression


def main():
    telescopeDataSet = pandas.read_csv('../Data-analysis-in-python-/magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']

    X = telescopeDataSet.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = telescopeDataSet.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y)  # perform linear regression
    Y_pred = linear_regressor.predict(X)  # make predictions
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()

if __name__ == '__main__':
    main()
