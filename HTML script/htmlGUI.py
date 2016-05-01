
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

headContent = (
"""
<head>
Stay tuned for our amazing summer sale!
</head>
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
        self.logo = PhotoImage(file='tour_logo.gif')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0,column=0,rowspan=2)
        ttk.Label(self.frame_header,text='Thanks for exploring!',style='Header.TLabel').grid(row=0,column=1)
        ttk.Label(self.frame_header, wraplength=300,
                  text=("We're glad you chose Explore California for your recent adventure!  "
                        "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row=1,column=1)

        # Body 
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()
        
        # Body content (labels)
        ttk.Label(self.frame_content,text='Name:').grid(row=0,column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content,text='Email:').grid(row=0,column=1, padx=5, sticky='sw')    
        ttk.Label(self.frame_content,text='Comments:').grid(row=2,column=0,padx=5, sticky='sw')

        # Body content (textboxes)
        self.entry_name=ttk.Entry(self.frame_content,width=24, font=('Arial',10))
        self.entry_email=ttk.Entry(self.frame_content,width=24, font=('Arial',10))
        self.text_body=Text(self.frame_content,width=50,height=10, font=('Arial',10))

        # Placement of textboxes
        self.entry_name.grid(row=1,column=0)
        self.entry_email.grid(row=1,column=1)
        self.text_body.grid(row=3,column=0,columnspan=2)

        # Buttons
        ttk.Button(self.frame_content,text='Submit', command=self.submit).grid(row=4,column=0,padx=5, sticky='e')
        ttk.Button(self.frame_content,text='Clear',command=self.clear).grid(row=4,column=1,padx=5,sticky='w')

#-------------------------FUNCTIONS-------------------------#

        # Function that creates and writes html file
    def createHTML(name, content):
        file = open(name, "w")
        file.write(content)
        file.close()
        print("Operation completed.")
        
        # Prints contents of textboxes to the shell on Submit click
    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('<html> '+headContent+' <body> {} </body> </html>'.format(self.text_body.get(1.0,'end')))
        
        # Clears textboxes after submitting
        self.clear()

        # Confirmation of submission via dialog box
        messagebox.showinfo(title='Summer Sales Content',message='Body content submitted.')

        # Clears all textboxes on Clear click
    def clear(self):
        self.entry_name.delete(0,'end')
        self.entry_email.delete(0,'end')
        self.text_body.delete(1.0,'end')
        
# Run program          
def main():            
    
    root = Tk()
    guihtml = GUIhtml(root)
    root.mainloop()
    
if __name__ == "__main__": main()
