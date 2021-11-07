import pandas
import plotly.express as px


def main():
    telescopeDataSet = pandas.read_csv('../magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']

    fLenghtBox = px.box(data_frame=telescopeDataSet, y='fLength')
    fWidthBox = px.box(data_frame=telescopeDataSet, y='fWidth')
    fSizeBox = px.box(data_frame=telescopeDataSet, y='fSize')
    fConcBox = px.box(data_frame=telescopeDataSet, y='fConc')
    fConc1Box = px.box(data_frame=telescopeDataSet, y='fConc1')
    fAsymBox = px.box(data_frame=telescopeDataSet, y='fAsym')
    fM3LongBox = px.box(data_frame=telescopeDataSet, y='fM3Long')
    fM3TransBox = px.box(data_frame=telescopeDataSet, y='fM3Trans')
    fAlphaBox = px.box(data_frame=telescopeDataSet, y='fAlpha')
    fDistBox = px.box(data_frame=telescopeDataSet, y='fDist')
    classBox = px.box(data_frame=telescopeDataSet, y='class')

    fLenghtBox.show()


if __name__ == '__main__':
    main()
