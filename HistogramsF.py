import pandas
import plotly.express as px


def histograms(dataSet=None, choice=None):
    if int(choice) == 1:
        print("[1] fLenght")
        print("[2] fWidth")
        print("[3] fSize")
        print("[4] fConc")
        print("[5] fConc1")
        print("[6] fAsym")
        print("[7] fM3Long")
        print("[8] fM3Trans")
        print("[9] fAlpha")
        print("[10] fDist")
        print("[11] class")
        choice1 = input("Which attribute histogram to show ")
        if int(choice1) == 1:
            fLenghtHis = px.histogram(data_frame=dataSet, x='fLength')
            fLenghtHis.show()
        elif int(choice1) == 2:
            fWidthHis = px.histogram(data_frame=dataSet, x='fWidth')
            fWidthHis.show()
        elif int(choice1) == 3:
            fSizeHis = px.histogram(data_frame=dataSet, x='fSize')
            fSizeHis.show()
        elif int(choice1) == 4:
            fConcHis = px.histogram(data_frame=dataSet, x='fConc')
            fConcHis.show()
        elif int(choice1) == 5:
            fConc1His = px.histogram(data_frame=dataSet, x='fConc1')
            fConc1His.show()
        elif int(choice1) == 6:
            fAsymHis = px.histogram(data_frame=dataSet, x='fAsym')
            fAsymHis.show()
        elif int(choice1) == 7:
            fM3LongHis = px.histogram(data_frame=dataSet, x='fM3Long')
            fM3LongHis.show()
        elif int(choice1) == 8:
            fM3TransHis = px.histogram(data_frame=dataSet, x='fM3Trans')
            fM3TransHis.show()
        elif int(choice1) == 9:
            fAlphaHis = px.histogram(data_frame=dataSet, x='fAlpha')
            fAlphaHis.show()
        elif int(choice1) == 10:
            fDistHis = px.histogram(data_frame=dataSet, x='fDist')
            fDistHis.show()
        elif int(choice1) == 11:
            classHis = px.histogram(data_frame=dataSet, x='class')
            classHis.show()
    else:
        print("[1] Quality")
        print("[2] Pre-screeening")
        print("[3] Microaneurysms1")
        print("[4] Microaneurysms2")
        print("[5] Microaneurysms3")
        print("[6] Microaneurysms4")
        print("[7] Microaneurysms5")
        print("[8] Microaneurysms6")
        print("[9] Exudates1")
        print("[10] Exudates2")
        print("[11] Exudates3")
        print("[12] Exudates4")
        print("[13] Exudates5")
        print("[14] Exudates6")
        print("[15] Exudates7")
        print("[16] Exudates8")
        print("[17] Euclidean distance of the center of macula")
        print("[18] The diameter of the optic disc")
        print("[19] AM/FM-based classification")
        print("[20] class")
        choice1 = input("Which attribute histogram to show ")

        if int(choice1) == 1:
            Histogram = px.histogram(data_frame=dataSet, x='Quality')
            Histogram.show()
        elif int(choice1) == 2:
            Histogram = px.histogram(data_frame=dataSet, x='Pre-screeening')
            Histogram.show()
        elif int(choice1) == 3:
            Histogram = px.histogram(data_frame=dataSet, x='Microaneurysms1')
            Histogram.show()
        elif int(choice1) == 4:
            Histogram = px.histogram(data_frame=dataSet, x='Microaneurysms2')
            Histogram.show()
        elif int(choice1) == 5:
            Histogram = px.histogram(data_frame=dataSet, x='Microaneurysms3')
            Histogram.show()
        elif int(choice1) == 6:
            Histogram = px.histogram(data_frame=dataSet, x='Microaneurysms4')
            Histogram.show()
        elif int(choice1) == 7:
            Histogram = px.histogram(data_frame=dataSet, x='Microaneurysms5')
            Histogram.show()
        elif int(choice1) == 8:
            Histogram = px.histogram(data_frame=dataSet, x='Microaneurysms6')
            Histogram.show()
        elif int(choice1) == 9:
            Histogram = px.histogram(data_frame=dataSet, x='Exudates1')
            Histogram.show()
        elif int(choice1) == 10:
            Histogram = px.histogram(data_frame=dataSet, x='Exudates2')
            Histogram.show()
        elif int(choice1) == 11:
            Histogram = px.histogram(data_frame=dataSet, x='Exudates3')
            Histogram.show()
        elif int(choice1) == 12:
            Histogram = px.histogram(data_frame=dataSet, x='Exudates4')
            Histogram.show()
        elif int(choice1) == 13:
            Histogram = px.histogram(data_frame=dataSet, x='Exudates5')
            Histogram.show()
        elif int(choice1) == 14:
            Histogram = px.histogram(data_frame=dataSet, x='Exudates6')
            Histogram.show()
        elif int(choice1) == 15:
            Histogram = px.histogram(data_frame=dataSet, x='Exudates7')
            Histogram.show()
        elif int(choice1) == 16:
            Histogram = px.histogram(data_frame=dataSet, x='Exudates8')
            Histogram.show()
        elif int(choice1) == 17:
            Histogram = px.histogram(data_frame=dataSet, x='Euclidean distance of the center of macula')
            Histogram.show()
        elif int(choice1) == 18:
            Histogram = px.histogram(data_frame=dataSet, x='The diameter of the optic disc')
            Histogram.show()
        elif int(choice1) == 19:
            Histogram = px.histogram(data_frame=dataSet, x='AM/FM-based classification')
            Histogram.show()
        elif int(choice1) == 20:
            Histogram = px.histogram(data_frame=dataSet, x='class')
            Histogram.show()
