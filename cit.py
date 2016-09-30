


# # Open and Closed CIT Report

import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

fileList = [f for f in listdir(r'') if isfile(
    join(r'', f))]
dfopen = pd.read_excel(
    r'{}'.format(fileList[0]), sheetname='Open CIT Detail')
dfclosed = pd.read_excel(
    r'{}'.format(fileList[0]), sheetname='Completed MTD')


def dir_todf(files):
    if len(fileList) == 1:
        pass
    else:
        for i in range(1, len(fileList)):
            df_stepopen = pd.read_excel(r'{}'.format(
                fileList[i]), sheetname='Open CIT Detail').dropna(axis=0, how='all').dropna(axis=1, how='all')
            df_stepclosed = pd.read_excel(r'{}'.format(
                fileList[i]), sheetname='Completed MTD').dropna(axis=0, how='all').dropna(axis=1, how='all')
            global dfopen
            dfopen = pd.concat([dfopen, df_stepopen])
            global dfclosed
            dfclosed = pd.concat([dfclosed, df_stepclosed])
            print(i)

dir_todf(fileList)


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
plt.style.use('ggplot')


total_open_tasks = dfopen['Account Number'].count()
tasks_opened_prior_day = dfopen['Account Number'][dfopen['CIT Created Date']==dfopen['COPYDATE']].count()
total_oos = dfopen['Account Number'][dfopen['Days Past Target']>0].count()
percent_open_tasks_oos = total_open_tasks / total_oos



summary_data = {'Total open tasks': [total_open_tasks],'Tasks opened from prior day': [tasks_opened_prior_day],'Total tasks OOS': [total_oos]}
open_tasks_summary = pd.DataFrame(summary_data,columns=['Total open tasks','Tasks opened from prior day','Total tasks OOS'])
open_tasks_summary

tasks_closed_prior_day = dfclosed['Account Number'][dfclosed['CIT Completed Date']==dfclosed['COPYDATE']].count()
instd_closed_prior_day = dfclosed['Account Number'][dfclosed['CIT Completed Date']==dfclosed['COPYDATE']][dfclosed['Days Past Target']<=0].count()
oos_closed_prior_day = dfclosed['Account Number'][dfclosed['CIT Completed Date']==dfclosed['COPYDATE']][dfclosed['Days Past Target']>0].count()
percent_closed_instd_prior_day = instd_closed_prior_day / tasks_closed_prior_day
percent_closed_oos_prior_day = oos_closed_prior_day / tasks_closed_prior_day


graph_summary_data = pd.DataFrame({'Tasks opened prior day': [tasks_opened_prior_day],'Tasks closed prior day':tasks_closed_prior_day,'Total tasks OOS': [total_oos],'OOS closed prior day': oos_closed_prior_day},columns=['Tasks opened prior day','Tasks closed prior day','Total tasks OOS','OOS closed prior day'])
graph_summary_data

graph_summary_data.ix[0].plot(kind='bar',color='indianred')
total_oospi = pd.Series({'Total open tasks':total_open_tasks,'Toal tasks OOS':total_oos})

import seaborn as sns
total_oospi = pd.DataFrame({'Total open tasks':[total_open_tasks],'Toal tasks OOS':[total_oos]})
total_oospi.plot(kind='barh',alpha=0.5)

tasks_closed_prior_day = dfclosed['CIT Task Number'][dfclosed['CIT Completed Date']==dfclosed['COPYDATE']].count()

tasks_closed_prior_day

pd.DataFrame(dfclosed[dfclosed['CIT Completed Date']==dfclosed['COPYDATE']]).groupby(['CIT Task Number'])['Account Number'].count()
