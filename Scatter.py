import pandas
import plotly.express as px


def main():
    telescopeDataSet = pandas.read_csv('../Data-analysis-in-python-/magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']

    #fig = px.scatter(telescopeDataSet, x="fLength", y="class", size="Energy", color="Beats Per Minute (BPM)",
    #                 hover_name="Title")

    fig = px.scatter(telescopeDataSet, x="class", y="fLength")
    fig.show()

if __name__ == '__main__':
    main()
