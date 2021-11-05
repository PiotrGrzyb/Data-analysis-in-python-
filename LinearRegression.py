import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas
from sklearn.linear_model import LinearRegression


def main():
    telescopeDataSet = pandas.read_csv('../Data-analysis-in-python-/magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']

    X = telescopeDataSet.iloc[:, 0].values.reshape(-1, 1)
    Y = telescopeDataSet.iloc[:, 1].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()

if __name__ == '__main__':
    main()
