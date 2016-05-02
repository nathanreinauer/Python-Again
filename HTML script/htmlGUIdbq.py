import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

conn = sqlite3.connect('Content Database.db')
c = conn.cursor()

class GUIhtml:

#-------------------------GUI-------------------------#

    def __init__(self, master):

        # Frame
        master.title('Summer Sales Editor')
        master.resizable(False,False)
        master.configure(background='#009999')

        # Colors, fonts, etc.
        self.style = ttk.Style()
        self.style.configure('TFrame',background='#009999')
        self.style.configure('TButton',background='#009999')
        self.style.configure('TLabel',background='#009999', font=('Arial',11))
        self.style.configure('Header.TLabel',background='#009999',font=('Arial',18,'bold'))

        # Header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # Header content
        ttk.Label(self.frame_header,text='Summer Sales',style='Header.TLabel',foreground='#ccffff').grid(row=0,column=1,pady=5)
        ttk.Label(self.frame_header, wraplength=350,
                  text=("Welcome to the super easy content editor for our Summer Sales page!"
                        " Enter your text below and press 'Post'."),foreground='#ccffff').grid(row=1,column=1,pady=5)

        # Body 
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()
        self.text_body=Text(self.frame_content,width=50,height=10,wrap=WORD)

        # Combobox
        self.contentBox = StringVar()
        self.combobox = ttk.Combobox(self.frame_content, textvariable = self.contentBox, state='readonly')
        self.combobox.pack()
        self.combobox.config(values = ('Clothes', 'Food', 'Movies', 'Toys', 'Sand'))
        self.contentBox.set('Select content:')
        self.combobox.grid(row=3,column=0,padx=5,pady=5, sticky='e')
        

        # Combobox Button
        ttk.Button(self.frame_content,text='Select',command=self.setContent).grid(row=3,column=1,padx=5,pady=5,sticky='w')

        # Placement of textbox
        self.text_body.grid(row=4,column=0,columnspan=2,padx=5)

        # Textbox Buttons
        ttk.Button(self.frame_content,text='Post', command=self.submit).grid(row=5,column=0,padx=5,pady=5, sticky='e')
        ttk.Button(self.frame_content,text='Clear',command=self.clear).grid(row=5,column=1,padx=5,pady=5,sticky='w')

#-------------------------FUNCTIONS-------------------------#

        # Inserts content into textbox
    def setContent(self):
        combo = self.getContent()
        self.text_body.insert(END,combo)

        # Grabs info from database on 'Select' button click
    def getContent(self):
        c.execute("SELECT HTML FROM Content WHERE conName ='{}'".format(self.contentBox.get()))
        return c.fetchall()


        # Creates and writes html file
    def createHTML(self, content):
        file = open("Company Website.html", "w")
        file.write(content)
        file.close()
        
        # Takes content from textbox for use in createHTML() function
    def submit(self):
        self.createHTML((
'''
<html>
<head>
    <title>
        Summer Sale
    </title>
</head>
<body>
    <h2>
        Stay tuned for our amazing summer sale!
    </h2>
    <p>
        {}
    </p>
</body>
</html>
'''.format(self.text_body.get(1.0,'end'))))
        
        # Clears textbox after submitting
        self.clear()

        # Confirmation of submission via dialog box
        messagebox.showinfo(title='Web page created successfully!',message=
                            "Success! Navigate to this script's parent directory to view your new page.")

        # Clears textbox on Clear click
    def clear(self):
        self.text_body.delete(1.0,'end')
            
# Run program          
def main():            
    
    root = Tk()
    guihtml = GUIhtml(root)
    root.mainloop()
    
if __name__ == "__main__": main()
