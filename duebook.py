import numpy as np
import pandas as pd
from tkinter.filedialog import askopenfilename
import datetime as dt
import re
import matplotlib.pyplot as plt
plt.style.use('ggplot')

### retrieve dataframe from selected file

###raw data
#open_raw = pd.DataFrame(pd.read_excel(filePath,'Open CIT Detail')).dropna(axis=0, how='all').dropna(axis=1,how='all')
#closed_raw = pd.DataFrame(pd.read_excel(filePath,'Completed MTD')).dropna(axis=0, how='all').dropna(axis=1,how='all')

open_raw = pd.DataFrame(pd.read_excel(r'','Open CIT Detail')).dropna(axis=0, how='all').dropna(axis=1,how='all')
closed_raw = pd.DataFrame(pd.read_excel(r'','Completed MTD')).dropna(axis=0, how='all').dropna(axis=1,how='all')

cit_list = pd.DataFrame(pd.read_excel('citlist.xlsx'))
cit_list = cit_list[cit_list['Include'] == 'Yes']
teller_list = pd.DataFrame(pd.read_excel('teller.xlsx'))


##filtered to used CIT's
dfopen = pd.DataFrame(pd.merge(open_raw,cit_list,on='CIT Task Number'))
dfclosed = pd.DataFrame(pd.merge(closed_raw,cit_list,on='CIT Task Number'))
open_tax_workflows = dfopen['Account Number'].count()
total_loans_out_of_compliance = dfopen['Days Past Target'][dfopen['Days Past Target'] > 0].count()
percentage_of_loans_out_of_compliance = total_loans_out_of_compliance / open_tax_workflows

closed_tasks_volume_timeline = dfclosed[['CIT Completed Date','Account Number']].groupby('CIT Completed Date').count()
closed_tasks_day_stats = pd.DataFrame(dfclosed[['CIT Completed Date','Account Number']].groupby('CIT Completed Date').count()).describe()

oos_closed = dfclosed[dfclosed['Days Past Target']>0]
oos_closed_day_stats = pd.DataFrame(oos_closed[['CIT Completed Date','Account Number']].groupby('CIT Completed Date').count()).describe()
in_std_closed = dfclosed[dfclosed['Days Past Target']<=0]
in_std_closed_day_stats = pd.DataFrame(in_std_closed[['CIT Completed Date','Account Number']].groupby('CIT Completed Date').count()).describe()

print('Open task workflows: {}'.format(open_tax_workflows))
print('Total loans out of compliance: {}'.format(total_loans_out_of_compliance))
print('Percentage of loans out of compliance: {}'.format(percentage_of_loans_out_of_compliance))
print(' ')
closed_tasks_day_summary = closed_tasks_day_stats.reindex(index=['mean','std','min','max']).rename(columns={'Account Number': 'Daily tasks closed'})
print(closed_tasks_day_summary)
print(' ')
print(closed_tasks_volume_timeline.rename(columns={'Account Number': 'Tasks Closed'}))
