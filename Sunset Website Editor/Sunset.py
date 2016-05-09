
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class GUIhtml:

#-------------------------GUI-------------------------#

    def __init__(self, master):

        # Frame
        master.title('Sunset Movie Editor')
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
        ttk.Label(self.frame_header,text='Movie Editor',style='Header.TLabel',foreground='#ccffff').grid(row=0,column=1,pady=5)
##        ttk.Label(self.frame_header, wraplength=350,
##                  text=("Enter movie information below."
##                        " Email me if you run into problems."),foreground='#ccffff').grid(row=1,column=1,pady=5)

        # Body 
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()

        # Labels / Text boxes / Placement
        ttk.Label(self.frame_content,text='Title',foreground='#ccffff').grid(row=3,column=0,pady=5, sticky='e')
        self.text_title=Text(self.frame_content,width=65,height=1)
        self.text_title.grid(row=3,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='2D Dates',foreground='#ccffff').grid(row=4,column=0,pady=5, sticky='e')
        self.text_date2d=Text(self.frame_content,width=25,height=1)
        self.text_date2d.grid(row=4,column=1,columnspan=1,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='3D Dates',foreground='#ccffff').grid(row=4,column=2,pady=5, sticky='e')
        self.text_date3d=Text(self.frame_content,width=25,height=1)
        self.text_date3d.grid(row=4,column=3,columnspan=1,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Cast',foreground='#ccffff').grid(row=5,column=0,pady=5, sticky='e')
        self.text_cast=Text(self.frame_content,width=75,height=2)
        self.text_cast.grid(row=5,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Synopsis',foreground='#ccffff').grid(row=6,column=0,pady=5, sticky='e')
        self.text_summary=Text(self.frame_content,width=75,height=9)
        self.text_summary.grid(row=6,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Runtime',foreground='#ccffff').grid(row=7,column=0,pady=5, sticky='e')
        self.text_runtime=Text(self.frame_content,width=20,height=1)
        self.text_runtime.grid(row=7,column=1,columnspan=2,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='youtube.com/watch?v=',foreground='#ccffff').grid(row=7,column=2,pady=5, sticky='e')
        self.text_trailer=Text(self.frame_content,width=15,height=1)
        self.text_trailer.grid(row=7,column=3,columnspan=2,padx=5, sticky='w')
        

##        # Placement of textbox
##        self.text_body.grid(row=3,column=0,columnspan=2,padx=5)

        # Buttons
        ttk.Button(self.frame_content,text='Update Website', command=self.submit).grid(row=12,column=1,padx=5,pady=5, sticky='e')
        ttk.Button(self.frame_content,text='Clear All',command=self.clear).grid(row=12,column=2,padx=5,pady=5,sticky='w')

#-------------------------FUNCTIONS-------------------------#

        # Creates and writes html file
    def createHTML(self, content):
        file = open("index.html", "w")
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
'''.format(self.text_body1.get(1.0,'end'))))
        
        # Clears textbox after submitting
        self.clear()

        # Confirmation of submission via dialog box
        messagebox.showinfo(title='Web page created successfully!',message=
                            "Success! Navigate to this script's parent directory to view your new page.")

        # Clears textbox on Clear click
    def clear(self):
        self.text_body1.delete(1.0,'end')
        
# Run program          
def main():            
    
    root = Tk()
    guihtml = GUIhtml(root)
    root.mainloop()
    
if __name__ == "__main__": main()
