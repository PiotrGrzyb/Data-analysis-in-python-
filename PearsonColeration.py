import pandas
from numpy import float64


def main():
    telescopeDataSet = pandas.read_csv('../Data-analysis-in-python-/magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']
    # print(telescopeDataSet.head())

    fLenghtCorrVal = telescopeDataSet['fLength'].corr(telescopeDataSet['class'], method="pearson")
    fWidthCorrVal = telescopeDataSet['fWidth'].corr(telescopeDataSet['class'], method="pearson")
    fSizeCorrVal = telescopeDataSet['fSize'].corr(telescopeDataSet['class'], method="pearson")
    fConcCorrVal = telescopeDataSet['fConc'].corr(telescopeDataSet['class'], method="pearson")
    fConc1CorrVal = telescopeDataSet['fConc1'].corr(telescopeDataSet['class'], method="pearson")
    fAsymCorrVal = telescopeDataSet['fAsym'].corr(telescopeDataSet['class'], method="pearson")
    fM3LongCorrVal = telescopeDataSet['fM3Long'].corr(telescopeDataSet['class'], method="pearson")
    fM3TransCorrVal = telescopeDataSet['fM3Trans'].corr(telescopeDataSet['class'], method="pearson")
    fAlphaCorrVal = telescopeDataSet['fAlpha'].corr(telescopeDataSet['class'], method="pearson")
    fDistCorrVal = telescopeDataSet['fDist'].corr(telescopeDataSet['class'], method="pearson")
    print(fLenghtCorrVal)

if __name__ == '__main__':
    main()
