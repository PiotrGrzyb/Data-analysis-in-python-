import pandas
import plotly.express as px


def main():
    telescopeDataSet = pandas.read_csv('../magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']

    fLenghtLine = px.line(data_frame=telescopeDataSet, y='fLength')
    fWidthLine = px.line(data_frame=telescopeDataSet, y='fWidth')
    fSizeLine = px.line(data_frame=telescopeDataSet, y='fSize')
    fConcLine = px.line(data_frame=telescopeDataSet, y='fConc')
    fConc1Line = px.line(data_frame=telescopeDataSet, y='fConc1')
    fAsymLine = px.line(data_frame=telescopeDataSet, y='fAsym')
    fM3LongLine = px.line(data_frame=telescopeDataSet, y='fM3Long')
    fM3TransLine = px.line(data_frame=telescopeDataSet, y='fM3Trans')
    fAlphaLine = px.line(data_frame=telescopeDataSet, y='fAlpha')
    fDistLine = px.line(data_frame=telescopeDataSet, y='fDist')
    classLine = px.line(data_frame=telescopeDataSet, y='class')

    fDistLine.show()


if __name__ == '__main__':
    main()
