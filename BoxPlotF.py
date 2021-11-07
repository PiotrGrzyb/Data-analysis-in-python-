import pandas
import plotly.express as px


def box(dataSet=None, choice=None):
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
        choice1 = input("Which attribute box plot to show ")
        if int(choice1) == 1:
            fLenghtBox = px.box(data_frame=dataSet, y='fLength')
            fLenghtBox.show()
        elif int(choice1) == 2:
            fWidthBox = px.box(data_frame=dataSet, y='fWidth')
            fWidthBox.show()
        elif int(choice1) == 3:
            fSizeBox = px.box(data_frame=dataSet, y='fSize')
            fSizeBox.show()
        elif int(choice1) == 4:
            fConcBox = px.box(data_frame=dataSet, y='fConc')
            fConcBox.show()
        elif int(choice1) == 5:
            fConc1Box = px.box(data_frame=dataSet, y='fConc1')
            fConc1Box.show()
        elif int(choice1) == 6:
            fAsymBox = px.box(data_frame=dataSet, y='fAsym')
            fAsymBox.show()
        elif int(choice1) == 7:
            fM3LongBox = px.box(data_frame=dataSet, y='fM3Long')
            fM3LongBox.show()
        elif int(choice1) == 8:
            fM3TransBox = px.box(data_frame=dataSet, y='fM3Trans')
            fM3TransBox.show()
        elif int(choice1) == 9:
            fAlphaBox = px.box(data_frame=dataSet, y='fAlpha')
            fAlphaBox.show()
        elif int(choice1) == 10:
            fDistBox = px.box(data_frame=dataSet, y='fDist')
            fDistBox.show()
        elif int(choice1) == 11:
            classBox = px.box(data_frame=dataSet, y='class')
            classBox.show()
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
        choice1 = input("Which attribute box plot to show ")

        if int(choice1) == 1:
            Box = px.box(data_frame=dataSet, y='Quality')
            Box.show()
        elif int(choice1) == 2:
            Box = px.box(data_frame=dataSet, y='Pre-screeening')
            Box.show()
        elif int(choice1) == 3:
            Box = px.box(data_frame=dataSet, y='Microaneurysms1')
            Box.show()
        elif int(choice1) == 4:
            Box = px.box(data_frame=dataSet, y='Microaneurysms2')
            Box.show()
        elif int(choice1) == 5:
            Box = px.box(data_frame=dataSet, y='Microaneurysms3')
            Box.show()
        elif int(choice1) == 6:
            Box = px.box(data_frame=dataSet, y='Microaneurysms4')
            Box.show()
        elif int(choice1) == 7:
            Box = px.box(data_frame=dataSet, y='Microaneurysms5')
            Box.show()
        elif int(choice1) == 8:
            Box = px.box(data_frame=dataSet, y='Microaneurysms6')
            Box.show()
        elif int(choice1) == 9:
            Box = px.box(data_frame=dataSet, y='Exudates1')
            Box.show()
        elif int(choice1) == 10:
            Box = px.box(data_frame=dataSet, y='Exudates2')
            Box.show()
        elif int(choice1) == 11:
            Box = px.box(data_frame=dataSet, y='Exudates3')
            Box.show()
        elif int(choice1) == 12:
            Box = px.box(data_frame=dataSet, y='Exudates4')
            Box.show()
        elif int(choice1) == 13:
            Box = px.box(data_frame=dataSet, y='Exudates5')
            Box.show()
        elif int(choice1) == 14:
            Box = px.box(data_frame=dataSet, y='Exudates6')
            Box.show()
        elif int(choice1) == 15:
            Box = px.box(data_frame=dataSet, y='Exudates7')
            Box.show()
        elif int(choice1) == 16:
            Box = px.box(data_frame=dataSet, y='Exudates8')
            Box.show()
        elif int(choice1) == 17:
            Box = px.box(data_frame=dataSet, y='Euclidean distance of the center of macula')
            Box.show()
        elif int(choice1) == 18:
            Box = px.box(data_frame=dataSet, y='The diameter of the optic disc')
            Box.show()
        elif int(choice1) == 19:
            Box = px.box(data_frame=dataSet, y='AM/FM-based classification')
            Box.show()
        elif int(choice1) == 20:
            Box = px.box(data_frame=dataSet, y='class')
            Box.show()
