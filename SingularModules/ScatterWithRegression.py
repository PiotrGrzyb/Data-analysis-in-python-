import pandas
import plotly.express as px


def main():
    telescopeDataSet = pandas.read_csv('../magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']

    fig = px.scatter(telescopeDataSet, x="fWidth", y="fLength", trendline="ols", trendline_color_override="red")
    fig1 = px.scatter(telescopeDataSet, x="fSize", y="fConc", trendline="ols", trendline_color_override="red")
    fig2 = px.scatter(telescopeDataSet, x="fAlpha", y="fDist", trendline="ols", trendline_color_override="red")
    fig3 = px.scatter(telescopeDataSet, x="fM3Long", y="fM3Trans", trendline="ols", trendline_color_override="red")
    fig4 = px.scatter(telescopeDataSet, x="fConc", y="fConc1", trendline="ols", trendline_color_override="red")
    fig5 = px.scatter(telescopeDataSet, x="fLength", y="fDist", trendline="ols", trendline_color_override="red")

    fig5.show()



if __name__ == '__main__':
    main()
