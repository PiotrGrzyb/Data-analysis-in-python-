import pandas
import plotly.express as px


def valueplot(dataSet=None, choice=None):
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
        choice1 = input("Which attribute value plot to show ")
        if int(choice1) == 1:
            fLenghtLine = px.line(data_frame=dataSet, y='fLength')
            fLenghtLine.show()
        elif int(choice1) == 2:
            fWidthLine = px.line(data_frame=dataSet, y='fWidth')
            fWidthLine.show()
        elif int(choice1) == 3:
            fSizeLine = px.line(data_frame=dataSet, y='fSize')
            fSizeLine.show()
        elif int(choice1) == 4:
            fConcLine = px.line(data_frame=dataSet, y='fConc')
            fConcLine.show()
        elif int(choice1) == 5:
            fConc1Line = px.line(data_frame=dataSet, y='fConc1')
            fConc1Line.show()
        elif int(choice1) == 6:
            fAsymLine = px.line(data_frame=dataSet, y='fAsym')
            fAsymLine.show()
        elif int(choice1) == 7:
            fM3LongLine = px.line(data_frame=dataSet, y='fM3Long')
            fM3LongLine.show()
        elif int(choice1) == 8:
            fM3TransLine = px.line(data_frame=dataSet, y='fM3Trans')
            fM3TransLine.show()
        elif int(choice1) == 9:
            fAlphaLine = px.line(data_frame=dataSet, y='fAlpha')
            fAlphaLine.show()
        elif int(choice1) == 10:
            fDistLine = px.line(data_frame=dataSet, y='fDist')
            fDistLine.show()
        elif int(choice1) == 11:
            classLine = px.line(data_frame=dataSet, y='class')
            classLine.show()
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
        choice1 = input("Which attribute value plot to show ")

        if int(choice1) == 1:
            ValuePlot = px.line(data_frame=dataSet, y='Quality')
            ValuePlot.show()
        elif int(choice1) == 2:
            ValuePlot = px.line(data_frame=dataSet, y='Pre-screeening')
            ValuePlot.show()
        elif int(choice1) == 3:
            ValuePlot = px.line(data_frame=dataSet, y='Microaneurysms1')
            ValuePlot.show()
        elif int(choice1) == 4:
            ValuePlot = px.line(data_frame=dataSet, y='Microaneurysms2')
            ValuePlot.show()
        elif int(choice1) == 5:
            ValuePlot = px.line(data_frame=dataSet, y='Microaneurysms3')
            ValuePlot.show()
        elif int(choice1) == 6:
            ValuePlot = px.line(data_frame=dataSet, y='Microaneurysms4')
            ValuePlot.show()
        elif int(choice1) == 7:
            ValuePlot = px.line(data_frame=dataSet, y='Microaneurysms5')
            ValuePlot.show()
        elif int(choice1) == 8:
            ValuePlot = px.line(data_frame=dataSet, y='Microaneurysms6')
            ValuePlot.show()
        elif int(choice1) == 9:
            ValuePlot = px.line(data_frame=dataSet, y='Exudates1')
            ValuePlot.show()
        elif int(choice1) == 10:
            ValuePlot = px.line(data_frame=dataSet, y='Exudates2')
            ValuePlot.show()
        elif int(choice1) == 11:
            ValuePlot = px.line(data_frame=dataSet, y='Exudates3')
            ValuePlot.show()
        elif int(choice1) == 12:
            ValuePlot = px.line(data_frame=dataSet, y='Exudates4')
            ValuePlot.show()
        elif int(choice1) == 13:
            ValuePlot = px.line(data_frame=dataSet, y='Exudates5')
            ValuePlot.show()
        elif int(choice1) == 14:
            ValuePlot = px.line(data_frame=dataSet, y='Exudates6')
            ValuePlot.show()
        elif int(choice1) == 15:
            ValuePlot = px.line(data_frame=dataSet, y='Exudates7')
            ValuePlot.show()
        elif int(choice1) == 16:
            ValuePlot = px.line(data_frame=dataSet, y='Exudates8')
            ValuePlot.show()
        elif int(choice1) == 17:
            ValuePlot = px.line(data_frame=dataSet, y='Euclidean distance of the center of macula')
            ValuePlot.show()
        elif int(choice1) == 18:
            ValuePlot = px.line(data_frame=dataSet, y='The diameter of the optic disc')
            ValuePlot.show()
        elif int(choice1) == 19:
            ValuePlot = px.line(data_frame=dataSet, y='AM/FM-based classification')
            ValuePlot.show()
        elif int(choice1) == 20:
            ValuePlot = px.line(data_frame=dataSet, y='class')
            ValuePlot.show()
