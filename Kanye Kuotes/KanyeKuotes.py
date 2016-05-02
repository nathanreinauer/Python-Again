import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

conn = sqlite3.connect('Kanye.db')
c = conn.cursor()

class GUIhtml:

#-------------------------GUI-------------------------#

    def __init__(self, master):

        # Frame
        master.title('Kanye Kuotes')
        master.resizable(False,False)
        master.configure(background='#b30000')

        # Colors, fonts, etc.
        self.style = ttk.Style()
        self.style.configure('TFrame',background='#b30000')
        self.style.configure('TButton',background='#b30000')
        self.style.configure('TLabel',background='#b30000', font=('Arial',11))
        self.style.configure('Header.TLabel',background='#b30000',font=('Arial',18,'bold'))

        # Header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # Header content
        ttk.Label(self.frame_header,text='Kanye West Quote Generator',style='Header.TLabel',foreground='#ffcccc').grid(row=0,column=1,pady=5)
        ttk.Label(self.frame_header, wraplength=350,
                  text=("Everyone knows Kanye West is a genius, and no one knows that better than the man himself."
                        " Click the button below to drop a nugget of wisdom from one of history's greatest minds."),foreground='#ffcccc').grid(row=1,column=1,pady=5)

        # Body 
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()
        self.text_body=Text(self.frame_content,width=50,height=7,wrap=WORD)

        # Generate Quote Button
        ttk.Button(self.frame_content,text='Get Quote',command=self.setContent).grid(row=3,column=1,padx=5,pady=5,sticky='w')

        # Placement of textbox
        self.text_body.grid(row=4,column=0,columnspan=2,padx=5, pady=5)

#-------------------------FUNCTIONS-------------------------#


        # Inserts content into textbox
    def setContent(self):
        self.clear()
        combo = self.getContent()
        combo = combo.replace('\\', '')
        self.text_body.insert(END,combo)

        # Grabs info from database on 'Select' button click
    def getContent(self):
        c.execute("SELECT Quote FROM Quotes WHERE ID ={}".format(random.randint(1,54)))
        fetch = (c.fetchall())
        return str(fetch)[3:-4]

        # Clears textbox
    def clear(self):
        self.text_body.delete(1.0,'end')
            
# Run program          
def main():            
    
    root = Tk()
    guihtml = GUIhtml(root)
    root.mainloop()
    
if __name__ == "__main__": main()
