import plotly.express as px


def scatterRegression(dataSet=None, choice=None):
    if int(choice) == 1:
        print("[1] x=fWidth, y=fLength")
        print("[2] x=fSize, y=fConc")
        print("[3] x=fAlpha, y=fDist")
        print("[4] x=fM3Long, y=fM3Trans")
        print("[5] x=fConc, y=fConc1")
        print("[6] x=fLength, y=fDist")
        choice = input("What plot to open?: ")
        if int(choice) == 1:
            fig = px.scatter(dataSet, x="fWidth", y="fLength", trendline="ols", trendline_color_override="red")
            fig.show()
        elif int(choice) == 2:
            fig1 = px.scatter(dataSet, x="fSize", y="fConc", trendline="ols", trendline_color_override="red")
            fig1.show()
        elif int(choice) == 3:
            fig2 = px.scatter(dataSet, x="fAlpha", y="fDist", trendline="ols", trendline_color_override="red")
            fig2.show()
        elif int(choice) == 4:
            fig3 = px.scatter(dataSet, x="fM3Long", y="fM3Trans", trendline="ols", trendline_color_override="red")
            fig3.show()
        elif int(choice) == 5:
            fig4 = px.scatter(dataSet, x="fConc", y="fConc1", trendline="ols", trendline_color_override="red")
            fig4.show()
        elif int(choice) == 6:
            fig5 = px.scatter(dataSet, x="fLength", y="fDist", trendline="ols", trendline_color_override="red")
            fig5.show()
    else:
        print("[1] x=The diameter of the optic disc, y=Exudates7")
        print("[2] x=Microaneurysms1, y=Exudates1")
        print("[3] x=The diameter of the optic disc, y=Microaneurysms1")
        print("[4] x=Euclidean distance of the center of macula, y=Exudates2")
        print("[5] x=Microaneurysms3, y=Exudates3")
        print("[6] x=The diameter of the optic disc, y=Exudates5")
        choice = input("What plot to open?: ")
        if int(choice) == 1:
            fig = px.scatter(dataSet, x="The diameter of the optic disc", y="Exudates7", trendline="ols", trendline_color_override="red")
            fig.show()
        elif int(choice) == 2:
            fig1 = px.scatter(dataSet, x="Microaneurysms1", y="Exudates1", trendline="ols", trendline_color_override="red")
            fig1.show()
        elif int(choice) == 3:
            fig2 = px.scatter(dataSet, x="The diameter of the optic disc", y="Microaneurysms1", trendline="ols", trendline_color_override="red")
            fig2.show()
        elif int(choice) == 4:
            fig3 = px.scatter(dataSet, x="Euclidean distance of the center of macula", y="Exudates2", trendline="ols", trendline_color_override="red")
            fig3.show()
        elif int(choice) == 5:
            fig4 = px.scatter(dataSet, x="Microaneurysms3", y="Exudates3", trendline="ols", trendline_color_override="red")
            fig4.show()
        elif int(choice) == 6:
            fig5 = px.scatter(dataSet, x="The diameter of the optic disc", y="Exudates5", trendline="ols", trendline_color_override="red")
            fig5.show()
