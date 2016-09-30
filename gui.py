from tkinter import *
from tkinter import ttk



class Window(object):

    def __init__(self,master,window_title,geometry):

        self.window = Toplevel(master)
        self.window.title(window_title)
        self.window.geometry(geometry)


        pass

    def user_auth(self,header_text='',user_text='Username',password_text='Password:',
                  button_text='Submit'):

        self.head_frame = ttk.Frame(self.window)
        self.head_frame.pack()
        ttk.Label(self.head_frame, text = header_text).grid(row=0,column=0)

        ttk.Label(self.head_frame, text=user_text).grid(row=2,column=0)
        ttk.Label(self.head_frame, text=password_text).grid(row=4,column=0)

        self.head_frame.config(relief='groove')

        self.entry_user = ttk.Entry(self.head_frame, width = 24).grid(row=2,column=1)
        self.entry_password = ttk.Entry(self.head_frame, width = 24).grid(row=4,column=1)
        ttk.Button(self.head_frame, text=button_text).grid(row=6,column='0')





class User_Auth(object):

    def __init__(self, master):
        self.head_frame = ttk.Frame(master)
        self.head_frame.pack()
        ttk.Label(self.head_frame, text = 'CoreLogic Client Systems Automation').grid(row=0,column=0)

        self.body_frame = ttk.Frame(master)
        self.body_frame.pack()
        ttk.Label(self.body_frame, text='ISC/ User:').grid(row=2,column=0)
        ttk.Label(self.body_frame, text='LSAMS User ID').grid(row=4,column=0)
        ttk.Label(self.body_frame, text='LSAMS Password').grid(row=5,column=0)


        self.entry_isc = ttk.Entry(self.body_frame, width = 24).grid(row=2,column=1)
        self.entry_sys_user = ttk.Entry(self.body_frame, width = 24).grid(row=4,column=1)
        self.entry_sys_password = ttk.Entry(self.body_frame, width = 24).grid(row=5,column=1)

        self.template_textbox = Text(self.body_frame, width = 50, height = 10)
        ttk.Button(self.body_frame, text='Submit').grid(row=6,column='0')


def main():

    root = Tk()
    new = Window(root,'title','250x150')
    new.user_auth()
    root.mainloop()

if __name__ == '__main__':
    main()