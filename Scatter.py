import pandas
import plotly.express as px


def main():
    telescopeDataSet = pandas.read_csv('../Data-analysis-in-python-/magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']

    fig = px.scatter(telescopeDataSet, x="class", y="fLength")
    fig.show()

    fig2 = px.scatter(telescopeDataSet, x="class", y="fWidth")
    #fig2.show()

    fig3 = px.scatter(telescopeDataSet, x="class", y="fSize")
    #fig3.show()

    fig4 = px.scatter(telescopeDataSet, x="class", y="fConc")
    #fig4.show()

    fig5 = px.scatter(telescopeDataSet, x="class", y="fConc1")
    #fig5.show()

    fig6 = px.scatter(telescopeDataSet, x="class", y="fAsym")
    #fig6.show()

    fig7 = px.scatter(telescopeDataSet, x="class", y="fM3Long")
    #fig7.show()

    fig8 = px.scatter(telescopeDataSet, x="class", y="fM3Trans")
    #fig8.show()

    fig9 = px.scatter(telescopeDataSet, x="class", y="fAlpha")
    #fig9.show()

    fig10 = px.scatter(telescopeDataSet, x="class", y="fDist")
    #fig10.show()

if __name__ == '__main__':
    main()
