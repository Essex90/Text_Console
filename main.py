from tkinter import *
from tkinter import filedialog, ttk
import os


class Console():
    def __init__(self):

        title = 'Text Console'
        self.window = Tk()
        self.window.geometry('1024x800')
        self.window.title(title)

        self.tabs = {'tab': 0}

        self.tab_list = []
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(expand = True, fill= 'both')

    def run(self):
        self.window.mainloop()



if __name__ == '__main__':
    app = Console()
    app.run()