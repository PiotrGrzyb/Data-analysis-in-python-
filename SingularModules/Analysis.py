import pandas


def main():
    telescopeDataSet = pandas.read_csv('../magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                            'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']
    #print(telescopeDataSet.head())
    #print(telescopeDataSet.min('fLength'));
    minValue = telescopeDataSet.min()
    # print(minValue)

    maxValue = telescopeDataSet.max()
    # print(maxValue)

    averageValue = telescopeDataSet.mean()
    #print(averageValue)

    standardDeviation = telescopeDataSet.std()
    #print(standardDeviation)

    medianValue = telescopeDataSet.median()
    #print(medianValue)

    q1 = telescopeDataSet.quantile(0.25)
    q3 = telescopeDataSet.quantile(0.75)

    iqrValue = q3 - q1
    #print(iqrValue)

    q01 = telescopeDataSet.quantile(0.1)
    q09 = telescopeDataSet.quantile(0.9)
    # print(q01)
    print(q09)

if __name__ == '__main__':
    main()
