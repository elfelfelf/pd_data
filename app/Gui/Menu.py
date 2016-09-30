from tkinter import *
from tkinter import ttk

class MenuBar(object):

    def __init__(self, master):
        self.menubar = Menu(master)
        master.option_add('*tearOff', False)
        master.config(menu=self.menubar)
        
        self.file = Menu(self.menubar)
        self.view = Menu(self.menubar)
        self.run = Menu(self.menubar)

        self.project = Menu(self.menubar)
        self.tools = Menu(self.project)

        self.dataset = Menu(self.menubar)
        self.import_data = Menu(self.dataset)
        self.export_data = Menu(self.dataset)
        self.preprocess = Menu(self.dataset)

        self.macro = Menu(self.menubar)
        
        self.menubar.add_cascade(menu=self.file, label='File')
        self.menubar.add_cascade(menu=self.view, label='View')
        self.menubar.add_cascade(menu=self.run, label='Run')
        self.menubar.add_cascade(menu=self.project, label='Project')
        self.project.add_cascade(menu=self.tools, label='Tools')
        self.menubar.add_cascade(menu=self.dataset, label='Dataset')
        self.dataset.add_command(label='Create New Dataset...')
        self.dataset.add_cascade(menu=self.import_data, label='Import Data')
        self.dataset.add_cascade(menu=self.export_data, label='Export')
        self.dataset.add_cascade(menu=self.preprocess, label='Preprocessing')

        self.menubar.add_cascade(menu=self.macro, label='Macro')

        self.file.add_command(label='New Project File...')
        self.file.add_separator()
        self.file.add_command(label='Open...')
        self.file.add_command(label='Save')
        self.file.add_command(label='Save As...')
        self.file.add_separator()
        self.file.add_command(label='Project Settings...')
        self.file.add_command(label='System Credentials...')
        self.file.add_command(label='Preferences...')
        self.file.add_separator()
        self.file.add_command(label='Exit')
        self.view.add_command(label='Event Window...')
        self.view.add_command(label='Project Explorer...')
        self.view.add_command(label='Dataset Editor...')
        self.view.add_command(label='Macro Editor...')
        self.view.add_command(label='Report Editor...')
        self.run.add_command(label='Current Project')
        self.run.add_command(label='Macro...')
        self.run.add_command(label='Report Automation...')
        self.project.add_command(label='Datasets...')
        self.project.add_command(label='Macros...')
        self.project.add_command(label='Reports...')
        self.project.add_separator()
        self.tools.add_command(label='Task Scheduler...')
        self.project.add_command(label='Manage Data Sources...')

        self.import_data.add_command(label='Spreadsheet File...')
        self.import_data.add_command(label='From Database...')
        self.import_data.add_command(label='From File Directory...')
        self.export_data.add_command(label='Dataset to Excel...')
        self.export_data.add_command(label='Automated Report...')
        self.dataset.add_separator()
        self.dataset.add_command(label='New Dataset Query...')
        self.dataset.add_command(label='Pivot Table...')
        self.preprocess.add_command(label='Normalize...')
        self.preprocess.add_command(label='Data Types...')
        self.preprocess.add_command(label='Date and Time Formats...')
        self.preprocess.add_command(label='Text and Regex...')
        self.preprocess.add_command(label='CoreLogic Datatypes...')
        self.preprocess.add_command(label='Machine Learning...')
        self.dataset.add_command(label='Visualize...')
        self.macro.add_command(label='New Macro...')
        self.macro.add_command(label='Event Logs...')
        self.macro.add_command(label='Manage Client Systems...')
        self.macro.add_command(label='Macro Properties...')

    def new_project_file(self):
        pass



def test_menubar():

    root = Tk()
    MenuBar(root)
    root.mainloop()

test_menubar()
