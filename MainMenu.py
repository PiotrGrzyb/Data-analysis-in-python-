import pandas
from pandas import Series, DataFrame
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader

from AnalysisF import analysis
from PearsonColerationF import pearson
from ScatterWithRegressionF import scatterRegression
from ValuePlotF import valueplot
from BoxPlotF import box
from HistogramsF import histograms
from ScatterF import scatter


def main():
    run = True
    while run:
        print("\n")
        print("[1] Telescope data set")
        print("[2] Sonar data set")
        choice = input("Choose data set to load:")
        dataSet = None
        if int(choice) == 1:
            dataSet = pandas.read_csv('../Data-analysis-in-python-/magic04(gamma-1, hardon-0).data')
            dataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                               'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']
        else:
            dataSet = pandas.read_csv('../Data-analysis-in-python-/messidor_features.data')
            dataSet.columns = ['Quality', 'Pre-screeening', 'Microaneurysms1', 'Microaneurysms2', 'Microaneurysms3',
                               'Microaneurysms4', 'Microaneurysms5', 'Microaneurysms6', 'Exudates1', 'Exudates2',
                               'Exudates3', 'Exudates4', 'Exudates5', 'Exudates6', 'Exudates7',
                               'Exudates8', 'Euclidean distance of the center of macula',
                               'The diameter of the optic disc',
                               'AM/FM-based classification', 'class']

        print("[1] Analysis")
        print("[2] Pearson Coleration")
        print("[3] Scatter plot")
        print("[4] Scatter plot with regression")
        print("[5] Value plot")
        print("[6] Box plot")
        print("[7] Histograms")
        print("[8] Quit")
        choice2 = input("What you want to view?:")

        if int(choice2) == 1:
            if int(analysis(dataSet)) == 0:
                continue
            else:
                pass
        elif int(choice2) == 2:
            pearson(dataSet, choice)

        elif int(choice2) == 3:
            scatter(dataSet, choice)

        elif int(choice2) == 4:
            scatterRegression(dataSet, choice)

        elif int(choice2) == 5:
            valueplot(dataSet, choice)

        elif int(choice2) == 6:
            box(dataSet, choice)

        elif int(choice2) == 7:
            histograms(dataSet, choice)

        elif int(choice2) == 8:
            run = False


if __name__ == '__main__':
    main()
