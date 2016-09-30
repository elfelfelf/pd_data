
import pandas as pd
import numpy as np
import easygui as gui




class Df():
    
    def data_in(file_gui=True,source='file', filepath=None, db=None, table=None,
                filetype='xl', worksheet=0, query=None):        
        '''create new pandas dataframe from data source'''

        if source == 'file':
            
            if file_gui == True:
                filepath = gui.fileopenbox()
            
            if filetype == 'xl':
                dataframe = pd.read_excel(filepath,sheet_name=worksheet)
            
            elif filetype == 'csv':
                dataframe = pd.read_csv(file_path)
        
        elif source == 'db':
            dataframe = pd.read_sql_table(table,db.engine)
            
        elif source == 'query':
            dataframe = pd.read_sql_query(query,db.engine)
            return dataframe
            
    
    def data_out(filetype='xl'):
        pass
        
        


class open_cit_closed_mtd(Df):
    
    def __init__(self):
        pass
    
    def query(loan_id=None,task_category=None, task_number='all', task_status='A',
              OOS=True, createdby_daterange=None, created_daterange=None,
              completed_daterange=None, target_daterange=None,
              assigned_tellerid=None, assigned_tellername=None, task_area=None,
              days_past_target=None,investor=None,account_status=None,servicing_status=None,
              investor_code=None,state=None, product_group=None, spoc_tellerid=None,
              spoc_tellername=None, copydate=None):
                  pass