import numpy as np
import pandas as pd

# Raw data from report
dfopen_raw = pd.read_excel(
    '', 'Sheet1')
dfclosed_raw = pd.read_excel(
    '', 'Sheet2')

# dict of active cit's and teller id's
df_cit_list = pd.read_excel(
    '')
df_teller_list = pd.read_excel(
    '')

# Values where CIT matches on active CIT list
dfopen = pd.merge(dfopen_raw, df_cit_list)
dfclosed = pd.merge(dfclosed_raw, df_cit_list)

# Tasks Closed by Researcher
dfclosed_researchers = pd.merge(dfclosed, df_teller_list)
df_researcher_count = dfclosed_researchers[['Researcher','Loan_ID']]
df_researcher_count = df_researcher_count.groupby(df_researcher_count['Researcher']).count()
