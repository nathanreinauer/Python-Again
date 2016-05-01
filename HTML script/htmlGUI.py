
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

headContent = (
"""
<html>
<head>
<title>Summer Sale</title>
</head>
<body>
<h1>
"""
)

class GUIhtml:

#-------------------------GUI-------------------------#

    def __init__(self, master):

        # Frame
        master.title('Summer Sales')
        master.resizable(False,False)
        master.configure(background='#e1d8b9')

        # Colors, fonts, etc.
        self.style = ttk.Style()
        self.style.configure('TFrame',background='#e1d8b9')
        self.style.configure('TButton',background='#e1d8b9')
        self.style.configure('TLabel',background='#e1d8b9', font=('Arial',11))
        self.style.configure('Header.TLabel',background='#e1d8b9', font=('Arial',18,'bold'))

        # Header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # Header content
##        self.logo = PhotoImage(file='tour_logo.gif')
##        ttk.Label(self.frame_header, image=self.logo).grid(row=0,column=0,rowspan=2)
        ttk.Label(self.frame_header,text='Summer Sales',style='Header.TLabel').grid(row=0,column=1)
        ttk.Label(self.frame_header, wraplength=381,
                  text=("Welcome to the super easy content editor for the Summer Sales page!"
                        " Enter your text below and press 'Submit'.")).grid(row=1,column=1)

        # Body 
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()
        
        # Body label
        self.text_body=Text(self.frame_content,width=50,height=10, font=('Arial',10))

        # Placement of textbox
        self.text_body.grid(row=3,column=0,columnspan=2)

        # Buttons
        ttk.Button(self.frame_content,text='Submit', command=self.submit).grid(row=4,column=0,padx=5, sticky='e')
        ttk.Button(self.frame_content,text='Clear',command=self.clear).grid(row=4,column=1,padx=5,sticky='w')

#-------------------------FUNCTIONS-------------------------#

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
        messagebox.showinfo(title='Summer Sales Content',message='Body text submitted.')

        # Clears textbox on Clear click
    def clear(self):
        self.text_body.delete(1.0,'end')
        
# Run program          
def main():            
    
    root = Tk()
    guihtml = GUIhtml(root)
    root.mainloop()
    
if __name__ == "__main__": main()
