import pandas
from numpy import float64


def pearson(dataSet=None, choice=None):
    if int(choice) == 1:
        fLenghtCorrVal = dataSet['fLength'].corr(dataSet['class'], method="pearson")
        fWidthCorrVal = dataSet['fWidth'].corr(dataSet['class'], method="pearson")
        fSizeCorrVal = dataSet['fSize'].corr(dataSet['class'], method="pearson")
        fConcCorrVal = dataSet['fConc'].corr(dataSet['class'], method="pearson")
        fConc1CorrVal = dataSet['fConc1'].corr(dataSet['class'], method="pearson")
        fAsymCorrVal = dataSet['fAsym'].corr(dataSet['class'], method="pearson")
        fM3LongCorrVal = dataSet['fM3Long'].corr(dataSet['class'], method="pearson")
        fM3TransCorrVal = dataSet['fM3Trans'].corr(dataSet['class'], method="pearson")
        fAlphaCorrVal = dataSet['fAlpha'].corr(dataSet['class'], method="pearson")
        fDistCorrVal = dataSet['fDist'].corr(dataSet['class'], method="pearson")
        print("Corelation between attributes and class")
        print("fLenght:", fLenghtCorrVal)
        print("fWidth:", fWidthCorrVal)
        print("fSize:", fSizeCorrVal)
        print("fConc:", fConcCorrVal)
        print("fConc1:", fConc1CorrVal)
        print("fAsym:", fAsymCorrVal)
        print("fM3Long:", fM3LongCorrVal)
        print("fM3Trans:", fM3TransCorrVal)
        print("fAlpha:", fAlphaCorrVal)
        print("fDist:", fDistCorrVal)
        return 0
    
    else:
        QualityCorrVal = dataSet['Quality'].corr(dataSet['class'], method="pearson")
        PrescreeeningCorrVal = dataSet['Pre-screeening'].corr(dataSet['class'], method="pearson")
        Microaneurysms1CorrVal = dataSet['Microaneurysms1'].corr(dataSet['class'], method="pearson")
        Microaneurysms2CorrVal = dataSet['Microaneurysms2'].corr(dataSet['class'], method="pearson")
        Microaneurysms3CorrVal = dataSet['Microaneurysms3'].corr(dataSet['class'], method="pearson")
        Microaneurysms4CorrVal = dataSet['Microaneurysms4'].corr(dataSet['class'], method="pearson")
        Microaneurysms5CorrVal = dataSet['Microaneurysms5'].corr(dataSet['class'], method="pearson")
        Exudates1CorrVal = dataSet['Exudates1'].corr(dataSet['class'], method="pearson")
        Exudates2CorrVal = dataSet['Exudates2'].corr(dataSet['class'], method="pearson")
        Exudates3CorrVal = dataSet['Exudates3'].corr(dataSet['class'], method="pearson")
        Exudates4CorrVal = dataSet['Exudates4'].corr(dataSet['class'], method="pearson")
        Exudates5CorrVal = dataSet['Exudates5'].corr(dataSet['class'], method="pearson")
        Exudates6CorrVal = dataSet['Exudates6'].corr(dataSet['class'], method="pearson")
        Exudates7CorrVal = dataSet['Exudates7'].corr(dataSet['class'], method="pearson")
        Exudates8CorrVal = dataSet['Exudates8'].corr(dataSet['class'], method="pearson")
        EuclideanCorrVal = dataSet['Euclidean distance of the center of macula'].corr(dataSet['class'], method="pearson")
        DiaCorrVal = dataSet['The diameter of the optic disc'].corr(dataSet['class'], method="pearson")
        AMFMCorrVal = dataSet['AM/FM-based classification'].corr(dataSet['class'], method="pearson")

        print("Corelation between attributes and class")
        print("Quality:", QualityCorrVal)
        print("Pre-screeening:", PrescreeeningCorrVal)
        print("Microaneurysms1:", Microaneurysms1CorrVal)
        print("Microaneurysms2:", Microaneurysms2CorrVal)
        print("Microaneurysms3:", Microaneurysms3CorrVal)
        print("Microaneurysms4:", Microaneurysms4CorrVal)
        print("Microaneurysms5:", Microaneurysms5CorrVal)
        print("Exudates1:", Exudates1CorrVal)
        print("Exudates2:", Exudates2CorrVal)
        print("Exudates3:", Exudates3CorrVal)
        print("Exudates4:", Exudates4CorrVal)
        print("Exudates5:", Exudates5CorrVal)
        print("Exudates6:", Exudates6CorrVal)
        print("Exudates7:", Exudates7CorrVal)
        print("Exudates8:", Exudates8CorrVal)
        print("Euclidean distance of the center of macula:", EuclideanCorrVal)
        print("The diameter of the optic disc:", DiaCorrVal)
        print("AM/FM-based classification:", AMFMCorrVal)
        return 0



