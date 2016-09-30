from tkinter.filedialog import askopenfilename
import pandas as pd
import inflection as inf
pd.set_option('expand_frame_repr', False)

def main():
    pass

df = pd.read_excel(r'')

def from_file():
    fp = askopenfilename()
    dataframe = pd.read_excel(fp)

def headers(dataframe,pretty=False,citreport=False):
    if citreport==True: dataframe.columns = dataframe.columns.str.replace('CIT','')
    dataframe.columns = [inf.underscore(inf.parameterize(i)).strip() for i in dataframe.columns]
    if pretty==True: dataframe.columns = [inf.titleize(i) for i in dataframe.columns]

    return dataframe

def clean(dataframe,human=False):
    dataframe.dropna(axis=1,how='all',inplace=True)
    dataframe.dropna(axis=0,how='all',inplace=True)
    dataframe.reset_index(drop=True,inplace=True)
    found_headers = False

    if True in dataframe.columns.str.contains('Unnamed'):
        dataframe.columns = [str(i) for i in dataframe.ix[0]]
        dataframe.drop(dataframe.index[0],axis=0,inplace=True)
        dataframe.reset_index(drop=True,inplace=True)

    while found_headers == False:
        dataframe.reset_index(drop=True,inplace=True)
        if 'nan' in [str(i) for i in dataframe.columns]:
            dataframe.columns = [str(i) for i in dataframe.ix[0]]
            dataframe.drop(dataframe.index[0],axis=0,inplace=True)
            dataframe.reset_index(drop=True,inplace=True)
        else:
            found_headers = True

    return dataframe


clean(df)
headers(df)


if __name__ == '__main__':
    main()
