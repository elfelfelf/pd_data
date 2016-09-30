# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:02:41 2015

@author: Chris
"""

from wrangle import munge as mg
import pandas as pd
import win32com.client

#df = pd.read_excel(r'C:\Users\Chris\Documents\f\Open and Closed CIT MTD testfile.xls')
#mg.clean(df)

def select(dataframe,*args):
    collist = []
    for i, k in enumerate(args):
        collist.append(k)
    dataframe = dataframe[collist]
    return dataframe
def show(df):
    df = pd.DataFrame(df)
    writer = pd.ExcelWriter(r'', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    workbook.close()
    xlApp  = win32com.client.Dispatch("Excel.Application")
    xlApp.Visible = True
    wb = xlApp.Workbooks.Open(r'')
    wb = xlApp.ActiveWorkbook
    val = input('-c to close workbook...: ')
    if val == '-c':
        wb.Save()
        wb.Close()
        xlApp.Quit()

#df.dropna(how='any',axis=1,thresh=2,inplace=True)
