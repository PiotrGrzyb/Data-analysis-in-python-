import pandas
import plotly.express as px


def main():
    telescopeDataSet = pandas.read_csv('../Data-analysis-in-python-/magic04(gamma-1, hardon-0).data')
    telescopeDataSet.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                                'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']

    fLenghtHis = px.histogram(data_frame=telescopeDataSet, x='fLength')
    fWidthHis = px.histogram(data_frame=telescopeDataSet, x='fWidth')
    fSizeHis = px.histogram(data_frame=telescopeDataSet, x='fSize')
    fConcHis = px.histogram(data_frame=telescopeDataSet, x='fConc')
    fConc1His = px.histogram(data_frame=telescopeDataSet, x='fConc1')
    fAsymHis = px.histogram(data_frame=telescopeDataSet, x='fAsym')
    fM3LongHis = px.histogram(data_frame=telescopeDataSet, x='fM3Long')
    fM3TransHis = px.histogram(data_frame=telescopeDataSet, x='fM3Trans')
    fAlphaHis = px.histogram(data_frame=telescopeDataSet, x='fAlpha')
    fDistHis = px.histogram(data_frame=telescopeDataSet, x='fDist')
    classHis = px.histogram(data_frame=telescopeDataSet, x='class')

    fAsymHis.show()


if __name__ == '__main__':
    main()
