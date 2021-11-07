import pandas
import plotly.express as px


def scatter(dataSet=None, choice=None):
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
        choice1 = input("Which attribute scatter plot to show ")
        if int(choice1) == 1:
            Scatter = px.scatter(dataSet, x="class", y="fLength")
            Scatter.show()
        elif int(choice1) == 2:
            Scatter = px.scatter(dataSet, x="class", y="fWidth")
            Scatter.show()
        elif int(choice1) == 3:
            Scatter = px.scatter(dataSet, x="class", y="fSize")
            Scatter.show()
        elif int(choice1) == 4:
            Scatter = px.scatter(dataSet, x="class", y="fConc")
            Scatter.show()
        elif int(choice1) == 5:
            Scatter = px.scatter(dataSet, x="class", y="fConc1")
            Scatter.show()
        elif int(choice1) == 6:
            Scatter = px.scatter(dataSet, x="class", y="fAsym")
            Scatter.show()
        elif int(choice1) == 7:
            Scatter = px.scatter(dataSet, x="class", y="fM3Long")
            Scatter.show()
        elif int(choice1) == 8:
            Scatter = px.scatter(dataSet, x="class", y="fM3Trans")
            Scatter.show()
        elif int(choice1) == 9:
            Scatter = px.scatter(dataSet, x="class", y="fAlpha")
            Scatter.show()
        elif int(choice1) == 10:
            Scatter = px.scatter(dataSet, x="class", y="fDist")
            Scatter.show()
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
        choice1 = input("Which attribute scatter plot to show ")

        if int(choice1) == 1:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Quality')
            Scatter.show()
        elif int(choice1) == 2:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Pre-screeening')
            Scatter.show()
        elif int(choice1) == 3:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Microaneurysms1')
            Scatter.show()
        elif int(choice1) == 4:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Microaneurysms2')
            Scatter.show()
        elif int(choice1) == 5:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Microaneurysms3')
            Scatter.show()
        elif int(choice1) == 6:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Microaneurysms4')
            Scatter.show()
        elif int(choice1) == 7:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Microaneurysms5')
            Scatter.show()
        elif int(choice1) == 8:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Microaneurysms6')
            Scatter.show()
        elif int(choice1) == 9:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Exudates1')
            Scatter.show()
        elif int(choice1) == 10:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Exudates2')
            Scatter.show()
        elif int(choice1) == 11:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Exudates3')
            Scatter.show()
        elif int(choice1) == 12:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Exudates4')
            Scatter.show()
        elif int(choice1) == 13:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Exudates5')
            Scatter.show()
        elif int(choice1) == 14:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Exudates6')
            Scatter.show()
        elif int(choice1) == 15:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Exudates7')
            Scatter.show()
        elif int(choice1) == 16:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Exudates8')
            Scatter.show()
        elif int(choice1) == 17:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='Euclidean distance of the center of macula')
            Scatter.show()
        elif int(choice1) == 18:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='The diameter of the optic disc')
            Scatter.show()
        elif int(choice1) == 19:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='AM/FM-based classification')
            Scatter.show()
        elif int(choice1) == 20:
            Scatter = px.scatter(data_frame=dataSet, x="class", y='class')
            Scatter.show()
