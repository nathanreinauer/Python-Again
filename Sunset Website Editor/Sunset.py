import webbrowser
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from tkinter import simpledialog
from datetime import date
from datetime import datetime
import os
import csv
import os.path
import shutil
import glob


conn = sqlite3.connect('movielist.db')
c = conn.cursor()

# Today - 24 hours = "yesterday"
twoMonths = time.time() - 5259486


class GUIhtml:

#-------------------------GUI-------------------------#

    def __init__(self, master):

        # Frame
        master.title('Sunset Movie Editor')
        master.resizable(False,False)
        master.configure(background='#fe001a')

        # Colors, fonts, etc.
        self.style = ttk.Style()
        self.style.configure('TFrame',background='#fe001a')
        self.style.configure('TButton',background='#fe001a')
        self.style.configure('TLabel',background='#fe001a', font=('Arial',11))
        self.style.configure('Header.TLabel',background='#fe001a',font=('Georgia',25,'bold'))

        # Header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # Header content
        ttk.Label(self.frame_header,text='Movie Editor',style='Header.TLabel',foreground='#ffffff').grid(row=0,column=1,pady=5)

        # Body 
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()

        # Labels / Text boxes / Placement
        ttk.Label(self.frame_content,text='Title',foreground='#ffffff').grid(row=3,column=0,pady=5, sticky='e')
        self.text_title=Text(self.frame_content,width=65,height=1)
        self.text_title.grid(row=3,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Dates',foreground='#ffffff').grid(row=4,column=0,pady=5, sticky='e')
        self.text_date2d=Text(self.frame_content,width=25,height=1)
        self.text_date2d.grid(row=4,column=1,columnspan=1,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Cast',foreground='#ffffff').grid(row=5,column=0,pady=5, sticky='e')
        self.text_cast=Text(self.frame_content,width=75,height=4, wrap=WORD)
        self.text_cast.grid(row=5,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Synopsis',foreground='#ffffff').grid(row=6,column=0,pady=5, sticky='e')
        self.text_summary=Text(self.frame_content,width=75,height=9, wrap=WORD)
        self.text_summary.grid(row=6,column=1,columnspan=3,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Runtime',foreground='#ffffff').grid(row=7,column=0,pady=5, sticky='e')
        self.text_runtime=Text(self.frame_content,width=20,height=1)
        self.text_runtime.grid(row=7,column=1,columnspan=2,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='youtube.com/watch?v=',foreground='#ffffff').grid(row=7,column=2,pady=5, sticky='e')
        self.text_trailer=Text(self.frame_content,width=15,height=1)
        self.text_trailer.grid(row=7,column=3,columnspan=2,padx=5, sticky='w')

        ttk.Label(self.frame_content,text='Image',foreground='#ffffff').grid(row=8,column=0,pady=5, sticky='e')
        self.text_image=Text(self.frame_content,width=30,height=1)
        self.text_image.grid(row=8,column=1,columnspan=1,padx=5, sticky='w')

        # Dropdown Menus
        self.contentBox = StringVar()		 
        self.combobox = ttk.Combobox(self.frame_content, textvariable = self.contentBox, state='readonly', width=30, postcommand = self.forComboBox)		  	 
        self.combobox.grid(row=12,column=1, sticky='e')
        self.contentBox.set('Select movie:')

        ttk.Label(self.frame_content,text='Rating',foreground='#ffffff').grid(row=8,column=2,pady=5, sticky='e')
        self.contentBox2 = StringVar()		 
        self.combobox2 = ttk.Combobox(self.frame_content, textvariable = self.contentBox2, state='readonly', width=15)		  	 
        self.combobox2.grid(row=8,column=3)
        self.combobox2.config(values = ('G', 'PG', 'PG-13', 'R'))
        self.contentBox2.set('Select:')

        s = ttk.Style()                    
        s.configure('Wild.TRadiobutton',background='#fe001a',foreground='#ffffff')

        # Radio buttons
        self.v = IntVar()
        self.radio2d=ttk.Radiobutton(self.frame_content, text="2D", style='Wild.TRadiobutton', variable=self.v, value=1, command=self.selected).grid(row=4,column=3,sticky='w')
        self.radio3d=ttk.Radiobutton(self.frame_content, text="3D", style='Wild.TRadiobutton', variable=self.v, value=2, command=self.selected).grid(row=4,column=3,sticky='')
        self.v.set(1)

        self.v2 = IntVar()
        self.radio2d=ttk.Radiobutton(self.frame_content, text="Dolby 5.1", style='Wild.TRadiobutton', variable=self.v2, value=1, command=self.selected2).grid(row=4,column=2,padx=10,sticky='w')
        self.radio3d=ttk.Radiobutton(self.frame_content, text="Dolby 7.1", style='Wild.TRadiobutton', variable=self.v2, value=2, command=self.selected2).grid(row=4,column=2,padx=35,sticky='e')
        self.v2.set(1)

        # Spinbox for Year
        self.var = StringVar()
        self.var.set(str(date.today().year))
        self.spin = Spinbox(self.frame_content, width=6,from_=1990, to=2090, textvariable=self.var)
        self.spin.grid(row=4, column=1, sticky='e')
    
        # Buttons
        ttk.Button(self.frame_content, text='Import Record',command=self.buttClick).grid(row=12,column=2,padx=5,pady=5,sticky='w')
        ttk.Button(self.frame_content, text='Add Record',command=self.addRecord).grid(row=12,column=3,padx=5,pady=5,sticky='w')

#-------------------------MENU ITEMS-------------------------#

        menubar = Menu(master)

        # File Menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Create HTML File", underline=7, accelerator='CTRL+H', command=self.submit)
        filemenu.add_command(label="Open Newest HTML File", underline=0, accelerator='CTRL+O', command=self.openNewest)
        filemenu.add_separator()
        filemenu.add_command(label="Import Last Record", underline=0, accelerator='CTRL+I', command=self.importLast)
        filemenu.add_command(label="Delete Current Record", underline=0, accelerator='CTRL+D', command=self.messageDeleteRec)
        filemenu.add_command(label="Clear All Fields", underline=0, accelerator='CTRL+F', command=self.clear)
        filemenu.add_separator()
        filemenu.add_command(label="Add Message to Home Page", underline=4, accelerator='CTRL+M', command=self.menuMessage)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", underline=0, accelerator='CTRL+Q',command=Quit)
        menubar.add_cascade(label="File", underline=0,menu=filemenu)

        # Accelerators
        menubar.master.bind('<Control-q>', Quit)
        menubar.master.bind('<Control-h>', self.submit)
        menubar.master.bind('<Control-o>', self.openNewest)
        menubar.master.bind('<Control-i>', self.importLast)
        menubar.master.bind('<Control-d>', self.messageDeleteRec)
        menubar.master.bind('<Control-f>', self.clear)
        menubar.master.bind('<Control-m>', self.menuMessage)
        
        
        # View Menu
        viewmenu = Menu(menubar, tearoff=0)
        dbmenu = Menu(viewmenu, tearoff=0)
        viewmenu.add_command(label="Watch Trailer", underline=0, command=self.watchTrailer)
        viewmenu.add_command(label="Visit SunsetTheatre.com", underline=6, command=self.visitSite)
        dbmenu.add_command(label="Text File", underline=0, command=lambda: self.viewDB('txt'))
        dbmenu.add_command(label="CSV File", underline=0, command=lambda: self.viewDB('csv'))
        viewmenu.add_cascade(label="View Database As...",underline=0, menu=dbmenu)
        menubar.add_cascade(label="View", underline=0, menu=viewmenu)


        # Help Menu
        master.config(menu=menubar)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="View Manual", underline=0, command=self.manual)
        helpmenu.add_command(label="Contact Tech Support", underline=0, command=self.techSupport)
        filemenu.add_separator()
        helpmenu.add_command(label="About", underline=0, command=self.about)
        menubar.add_cascade(label="Help", underline=0, menu=helpmenu)



#-------------------------MESSAGES------------------------#

    def wrongFormat(self):
        result = messagebox.showerror(title='Error!',message=
                            "Error: You must enter a valid date in the following format:\nMonth 0, 0000 (January 13, 2020 for example)")
        
    def closedMessage(self):
        result = str(simpledialog.askstring("Closed?", "It looks like you're missing a day!\nIf the theatre will be closed, enter a message below explaining which day(s) and why.\nOtherwise hit Cancel."))
        return str(result)

    def noTrailer(self):
        result = messagebox.showerror(title='Error!',message=
                            "Error: Trailer field must contain an 11 character video ID from YouTube!")

    def notFound(self):
        result = messagebox.showerror(title='Error!',message=
                            "Error: You must create 'index.html' file first!")
        
    def blankImport(self):
        result = messagebox.showerror(title='Error!',message=
                            "Error: You must choose a record to import from the dropdown menu!")

    def blankRec(self):
        result = messagebox.showerror(title='Error!',message=
                            "Error: Record could not be added because one or more required fields were left blank.")

    def messageAdded(self):
        result = messagebox.showinfo(title='Record Added!',message=
                            "Success! New record added to the database.")

    def messageDeleted(self):
        result = messagebox.showinfo(title='Record Deleted!',message=
                            "Success! Record deleted.")

    def messageDeleteRec(self, event=None):
        try:
            delRec = self.addEpoch()
            c.execute("SELECT ID, Title, Format FROM Movies WHERE Epoch = {}".format(delRec))
            x = c.fetchall()
            result = messagebox.askyesno(message='Are you sure you want to delete {} from the database?'.format(x),icon='question', title='Delete Record?')
            if result == True:
                self.deleteCurrent()
                self.messageDeleted()
            else:
                pass
        except:
            result = messagebox.showerror(title='Error!',message=
                            "Error: No such record exists. Make sure the 'Dates' field is correct.")

    def messageOverwrite(self):
        result = messagebox.askyesno(message='There is already a movie scheduled for those days! Overwrite?',icon='question', title='Record Already Exists!')
        if result == True:
            self.overwriteCurrent()
        else:
            pass

        
#-------------------------FUNCTIONS-------------------------#


#---------------MENU FUNCTIONS
        
    def menuMessage(self, event=None):

        # Dialog box asking for date, and then print the epoch in the text filename
        date = str(simpledialog.askstring("Special Message", "How long would you like the message to remain on the home page?\n(Please type a date in this exact format: 'June 3, 2016')."))
        if date == 'None':
            pass
        else:
            try:
                pattern = '%B %d, %Y'      
                epoch = int(time.mktime(time.strptime(date, pattern)))
                filename = 'message{}.txt'.format(epoch)

                # Get rid of previous message text files
                for file in glob.glob("message*.txt"):
                    os.remove(file)
                    
                # Open the new text file in Notepad with boilerplate instructions already inserted
                file = open(filename, 'a')
                file.write(
                    '<!--\n\nType the HTML code for your message below, and then save and close the text file.\n'
                    'The message will appear above the upcoming movies next time you update the website,\n'
                    'and will remain there until the date you specified.\n\n'
                    '(These instructions will not appear on the website.)\n\n-->')
                file.close()
                os.system('start '+filename)
            except:
                self.wrongFormat()

    def techSupport(self): # Create an email to me
        webbrowser.open("mailto:n8thegreatest@gmail.com?subject=Help&body=Heeelp!")

    def overwriteCurrent(self): # Overwrites an entry in the DB
        overRec = self.addEpoch()
        c.execute("DELETE FROM Movies WHERE Epoch = {}".format(overRec))
        conn.commit()
        self.addRecord()

    def deleteCurrent(self): # Deletes an entry in the DB
        delRec = self.addEpoch()
        c.execute("DELETE FROM Movies WHERE Epoch = {}".format(delRec))
        conn.commit()
        self.clear()

    def openNewest(self, event=None): # Opens last index.html file
        if os.path.isfile('index.html') == True:
            filename = 'index.html'
            os.system("start "+filename)
        else:
            self.notFound()

    def watchTrailer(self): # Opens trailer in YouTube
        if len(self.text_trailer.get("1.0", 'end-1c')) == 11:
            webbrowser.open('https://www.youtube.com/watch?v={}'.format(self.text_trailer.get("1.0", 'end-1c')))
        else:
            self.noTrailer()

    def visitSite(self): # Opens SunsetTheatre.com
        webbrowser.open('http://sunsettheatre.com')

    def viewDB(self, x): # Opens DB in Notepad or Excel
        data = c.execute("SELECT * FROM Movies")

        with open('output.{}'.format(x), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Record ID', 'Epoch', 'Dates', 'Format', 'Title', 'Runtime', 'Image', 'Trailer', 'Cast', 'Synopsis', 'Rating', 'Sound', 'Last Epoch', 'Closed'])
            writer.writerows(data)
        filename = 'output.{}'.format(x)
        os.system("start "+filename)
        
    def manual(self): # Opens User's Guide
        filename = 'userguide.pdf'
        os.system('start '+filename)

    def about(self): # Opens 'About' window
        result = messagebox.showinfo(title='About Movie Editor',message="Sunset Movie Editor \n Version 1.0\n Coded by Nate in 2016")

    def getLast(self, x): # SELECTS a field from the most recent record
        c.execute("SELECT {} FROM Movies ORDER BY ID DESC LIMIT 1;".format(x))
        return c.fetchall()

    def importLast(self, event=None): # Puts data from DB into the main form
        self.clear()
 
        title = str(self.getLast("Title"))[3:-4]
        self.text_title.insert(1.0, title)

        dates = str(self.getLast("Dates"))[3:-11]
        self.text_date2d.insert(1.0, dates)

        synopsis = str(self.getLast("Synopsis"))[3:-4] 
        self.text_summary.insert(1.0, synopsis)

        cast = str(self.getLast("Actors"))[3:-4] 
        self.text_cast.insert(1.0, cast)

        runtime = str(self.getLast("Runtime"))[3:-4] 
        self.text_runtime.insert(1.0, runtime)

        rating = str(self.getLast("Rating"))[3:-4] 
        self.contentBox2.set(rating)

        trailer = str(self.getLast("Trailer"))[3:-4]
        self.text_trailer.insert(1.0, trailer)

        image = str(self.getLast("Image"))[3:-4] 
        self.text_image.insert(1.0, image)

        year = str(self.getLast("Dates"))[-9:-5]
        self.var.set(year)
        
        format1 = str(self.getLast("Format"))[3:-4]
        if format1 == '3D':
            self.v.set(2)
        else:
            self.v.set(1)

        sound = str(self.getLast("Sound"))[3:-4]
        if sound == 'Dolby 7.1':
            self.v2.set(2)
        else:
            self.v2.set(1)

        
#---------------------------OTHER FUNCTIONS--------------------------


    # Get 'Date Modified' for a file
    def modTime(self, filePath):
        t = time.ctime(os.path.getctime(filePath))
        x = time.mktime(time.strptime(t, "%a %b %d %H:%M:%S %Y"));
        return x

    # Check if it's been two months or not
    def twoMonthsAgo(self, num, content):
        try:
            newest = max(glob.iglob('Backup\\HomePage\\*.html'), key=os.path.getctime)        
            if self.modTime(newest) < twoMonths:
                if num == 1:
                    self.backupCreate(content)
                    self.backupDB()
                if num == 2:
                    self.backupPast(content)                    
            else:
                pass
        except ValueError:
            if num == 1:
                self.backupCreate(content)
                self.backupDB()
            if num == 2:
                self.backupPast(content)

    # Radio Button functions
    def selected(self):
        return(self.v.get())

    def selected2(self):
        return(self.v2.get())
    
    # SELECT each field from a record in DB (based on what's in combobox)
    def getFromCombo(self, x):
        varID = (self.contentBox.get()).split(' ', 1)[0]
        c.execute(("SELECT {} FROM Movies WHERE ID ='{}'").format(x, varID))
        return c.fetchall()

    # Puts data from last 9 records of DB into combobox
    def forComboBox(self):
        c.execute("SELECT ID, Format, Title FROM Movies ORDER BY ID DESC LIMIT 0,9")
        combo = c.fetchall()
        self.combobox.config(values = combo)

    # "Import" button for combobox-- Gets DB records from "getTitle", etc. and puts them into text fields
    def buttClick(self):
        if self.contentBox.get() == ('Select movie:'):
            self.blankImport()

        self.clear()
 
        title = str(self.getFromCombo("Title"))[3:-4] 
        self.text_title.insert(1.0, title)

        dates = str(self.getFromCombo("Dates"))[3:-11]
        self.text_date2d.insert(1.0, dates)

        synopsis = str(self.getFromCombo("Synopsis"))[3:-4]
        self.text_summary.insert(1.0, synopsis)

        cast = str(self.getFromCombo("Actors"))[3:-4]
        self.text_cast.insert(1.0, cast)

        runtime = str(self.getFromCombo("Runtime"))[3:-4]
        self.text_runtime.insert(1.0, runtime)

        rating = str(self.getFromCombo("Rating"))[3:-4]
        self.contentBox2.set(rating)

        trailer = str(self.getFromCombo("Trailer"))[3:-4]
        self.text_trailer.insert(1.0, trailer)

        image = str(self.getFromCombo("Image"))[3:-4]
        self.text_image.insert(1.0, image)

        year = str(self.getFromCombo("Dates"))[-9:-5]
        self.var.set(year)
        
        format1 = str(self.getFromCombo("Format"))[3:-4]
        if format1 == '3D':
            self.v.set(2)
        else:
            self.v.set(1)

        sound = str(self.getFromCombo("Sound"))[3:-4]
        if sound == 'Dolby 7.1':
            self.v2.set(2)
        else:
            self.v2.set(1)

    # Converts TEXBOX dates into Epoch
    def addEpoch(self):
        if ',' in (self.text_date2d.get("1.0", 'end-1c')): # If there's a comma in the date...
            datesTemp = (self.text_date2d.get("1.0", 'end-1c')).split(',', 1)[0] # Grab the first day from date field, eg. "May 12"
            date_time = datesTemp[:]+', ' + str(self.spin.get())# Slice the ends off and add year from spinbox
            pattern = '%B %d, %Y' # Tell python what the date format is
        else: # If there's NO comma in the date...
            datesTemp = (self.text_date2d.get("1.0", 'end-1c')).split(' &', 1)[0] # Grab the first day from date field, eg. "May 12"
            date_time = datesTemp[:]+', ' + str(self.spin.get())# Slice the ends off and add year from spinbox
            pattern = '%B %d, %Y' # Tell python what the date format is         
        epoch = int(time.mktime(time.strptime(date_time, pattern)))# Convert date to Epoch using pattern
        return (epoch)

    # Figures out upcoming movies in DB
    def newMovies(self):
        epochNow = int(time.time())
        c.execute('SELECT ID FROM Movies WHERE LastEpoch > {};'.format(epochNow))
        return c.fetchall()

    # Extracts ID numbers from string resulting from newMovies()
    def newMovieVar(self, x):
        movieVar1 = ''
        movieVar2 = ''
        movieVar3 = ''
        movieVar4 = ''
        movieVar5 = ''
        try:
            mVar1 = str(self.newMovies())
            movVar1 = ''.join(c for c in mVar1 if c not in '()[],')
            movieVar1 = movVar1.split(' ', 1)[0]
        except:
            pass
        try:
            mVar1 = str(self.newMovies())
            movVar1 = ''.join(c for c in mVar1 if c not in '()[],')
            movieVar2 = movVar1.split(' ', 2)[1]
        except:
            pass
        try:
            mVar1 = str(self.newMovies())
            movVar1 = ''.join(c for c in mVar1 if c not in '()[],')
            movieVar3 = movVar1.split(' ', 3)[2]
        except:
            pass
        try:
            mVar1 = str(self.newMovies())
            movVar1 = ''.join(c for c in mVar1 if c not in '()[],')
            movieVar4 = movVar1.split(' ', 4)[3]
        except:
            pass
        try:
            mVar1 = str(self.newMovies())
            movVar1 = ''.join(c for c in mVar1 if c not in '()[],')
            movieVar5 = movVar1.split(' ', 5)[4]
        except:
            pass
        if x == 1:
            return movieVar1
        elif x == 2:
            return movieVar2
        elif x == 3:
            return movieVar3
        elif x == 4:
            return movieVar4
        else:
            return movieVar5

    # Grab past movies from DB
    def getPastMovies(self):
        epochNow =  int(time.time())
        epochThisYear = datetime.now().year # Current year
        pattern = '%Y' 
        epoch1 = int(time.mktime(time.strptime(str(epochThisYear), pattern)))-1 # January 1, Current Year / Had to subtract 1 (see getPastMoviesPage() for reason)
        c.execute("SELECT Dates, Title, Format FROM Movies WHERE LastEpoch < {} AND Epoch > {};".format(epochNow, epoch1))
        fetch = (c.fetchall())
        epoch2 = int(time.mktime(time.strptime(str(epochThisYear - 1), pattern))) # January 1, Previous Year
        if str(fetch) == '[]':
            c.execute("SELECT Dates, Title, Format FROM Movies WHERE LastEpoch < {} AND Epoch > {};".format(epochNow, epoch2))
            blarp = str(c.fetchall())
            blarp = "<!->" + blarp # Adds invisible code to the beginning of the list so listPastMovies can work in any situation
            return blarp
        else:
            c.execute("SELECT Dates, Title, Format FROM Movies WHERE LastEpoch < {} AND Epoch > {};".format(epochNow, epoch1))
            return c.fetchall()

    # This cuts up the string that comes from the DB and adds it to index.html
    def listPastMovies(self):
        epochThisYear = str(datetime.now().year)
        x = str(self.getPastMovies())
        if x[0:4] == '<!->':
            epochThisYear = str(int(epochThisYear) - 1) 
        pastList = str(self.getPastMovies()).replace("\\n", "")
        pastList1 = pastList.replace("', '2D'", "")
        pastList2 = pastList.replace(" ("+epochThisYear+")', '", ": <b>").replace("'), ('", "</b><br>")
        pastList3 = pastList2.replace(" ("+epochThisYear+")', \"",": <b>").replace("\"), ('", "</b><br>")
        pastList4 = pastList3.replace("[('","").replace("')]","</b><br>").replace("\")]","</b><br>").replace("', '2D", "").replace("\", '2D", "").replace("', '3D", " 3D <img src='http://www.sunsettheatre.com/images/realdlogosmall.jpg'>").replace("\", '3D", " 3D <img src='http://www.sunsettheatre.com/images/realdlogosmall.jpg'>")
        return (pastList4)

    # Grab past movies from DB for the Past Movies page based on the year
    # Had to subtract "1" from "epo" because otherwise any Jan 1st movies get cut off
    def getPastMoviesPage(self, year):
        if year == 2015:
            epo = 1420099200
            end = 1451635200
        if year == 2016:
            epo = 1451635200
            end = 1483257600
        if year == 2017:
            epo = 1483257600
            end = 1514793600
        if year == 2018:
            epo = 1514793600
            end = 1546329600
        if year == 2019:
            epo = 1546329600
            end = 1577865600
        if year == 2020:
            epo = 1577865600
            end = 1609488000
        if year == 2021:
            epo = 1609488000
            end = 1641024000
        if year == 2022:
            epo = 1641024000
            end = 1641024000
        if year == 2023:
            epo = 1672560000
            end = 1704096000
        today = int(time.time())
        if epo < today and end > today:
            end = today

        c.execute("SELECT Dates, Title, Format FROM Movies WHERE Epoch > '{}' AND Epoch < '{}';".format(epo -1 , end))
        return c.fetchall()

    # This cuts up the string that comes from the DB and adds it to pastmovies.html
    def addPast(self, year):
        thisyear = date.today().year
        if str(self.getPastMoviesPage(year)) == '[]' or year > thisyear:
            pastList4 = ''
            top = ''
        else:
            pastList = str(self.getPastMoviesPage(year)).replace("\\n", "")
            pastList1 = pastList.replace("', '2D'", "")
            pastList2 = pastList.replace(" ("+str(year)+")', '", ": <b>").replace("'), ('", "</b><br>")
            pastList3 = pastList2.replace(" ("+str(year)+")', \"",": <b>").replace("\"), ('", "</b><br>")
            pastList4 = pastList3.replace("[('","").replace("')]","</b><br>").replace("\")]","</b><br>").replace("', '2D", "").replace("\", '2D", "").replace("', '3D", " 3D <img src='http://www.sunsettheatre.com/images/realdlogosmall.jpg'>").replace("\", '3D", " 3D <img src='http://www.sunsettheatre.com/images/realdlogosmall.jpg'>")
            top = ('''<hr>

    <font size=5 font color=red><b>'''+str(year)+''':</b><br>

    <font color=yellow size="3">''')
        return (top + pastList4)
           
    # Re-order table to make sure the newest movies are always at the end
    def sortTable(self):
        try:
            c.execute('DROP TABLE Ordered;')
        except:
            pass
        c.execute('CREATE TABLE Ordered (ID INTEGER PRIMARY KEY, Epoch INTEGER UNIQUE, Dates TEXT, Format TEXT, Title TEXT, Runtime TEXT, Image TEXT, Trailer TEXT, Actors TEXT, Synopsis TEXT, Rating TEXT, Sound TEXT, LastEpoch INTEGER, Closed TEXT);')
        c.execute('INSERT INTO Ordered  (Epoch, Dates, Format, Title, Runtime, Image, Trailer, Actors, Synopsis, Rating, Sound, LastEpoch, Closed) SELECT Epoch, Dates, Format, Title, Runtime, Image, Trailer, Actors, Synopsis, Rating, Sound, LastEpoch, Closed FROM Movies ORDER BY Epoch;')
        c.execute('DROP TABLE Movies;')
        c.execute('ALTER TABLE Ordered RENAME TO Movies;')

    # Adds records into DB from text fields
    def addRecord(self):
        self.sortTable()
        try:
            try:
                newTitle = self.text_title.get("1.0", 'end-1c')
                newSynopsis = self.text_summary.get("1.0", 'end-1c')
                newCast = self.text_cast.get("1.0", 'end-1c')
                newRuntime = self.text_runtime.get("1.0", 'end-1c')
                newRating = self.contentBox2.get()
                newTrailer = self.text_trailer.get("1.0", 'end-1c')
                newDates = self.text_date2d.get("1.0", 'end-1c')+" ("+str(self.spin.get())+")"
                newImage = self.text_image.get("1.0", 'end-1c')
                if self.selected() == 2:
                    newFormat = "3D"
                else:
                    newFormat = "2D"
                newEpoch = (self.addEpoch())
                if self.selected2() == 2:
                    newSound = "Dolby 7.1"
                else:
                    newSound = "Dolby 5.1"
                if newDates.count(',') > 1:
                    newLastEpoch = newEpoch + 432000
                else:
                    newLastEpoch = newEpoch + 259200

                c.execute('SELECT * FROM Movies WHERE Epoch = "{}"'.format(newEpoch))
                fetch = (str(c.fetchall()))
                if fetch == '[]':
                    if newDates.count(',') == 0:
                        newClosed = str(self.closedMessage())
                    else:
                        newClosed = ''
                
                    c.execute('INSERT INTO Movies (Title, Synopsis, Actors, Runtime, Rating, Trailer, Dates, Image, Format, Epoch, Sound, LastEpoch, Closed) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}",{},"{}", {}, "{}");'
                              .format(newTitle, newSynopsis, newCast, newRuntime, newRating, newTrailer, newDates, newImage, newFormat, newEpoch, newSound, newLastEpoch, newClosed))
                    conn.commit()
                    self.messageAdded()
                else:
                    self.messageOverwrite()
            except sqlite3.IntegrityError:
                    self.messageOverwrite()
        except ValueError:
            self.blankRec()


    # Grabs record of recent movies and plugs it into HTML chunk, does some trickery to combine 2D and 3D movies
    # 2D and 3D have to be next to each other in DB to work, hence the sortTable() function
    def addChunk1(self, x):
        closed = str(self.latestClosed(x))[3:-4]
        if closed == '': # if "closed" comes back empty from the DB, do nothing
            closed = ''
        elif closed == 'None':
            closed = ''
        elif closed == 'on':
            closed = ''
        elif closed == None:
            closed = ''
        else:
            closed = '<FONT color=yellow size=3>'+closed+'<br><br>' # but if "closed" comes back with text in it, print that sucka on the website
        sound = str(self.latestSound(x))[9:-6]
        if str(self.latestFormat(x))[3:-4] == '2D':
            dates = ((str(self.latestDates(x))[3:-10]) + '<br>')
            dates3d = ''
        else:
            dates = ''
            dates3d = ((str(self.latestDates(x))[3:-10])+'<font color="DodgerBlue"> in 3D<img src="http://www.SunsetTheatre.com/images/blueglasses.jpg"><br>')
        if self.latestTitle(x) == self.latestTitle(x+1):
            title = str(self.latestTitle(x))[3:-4]
            dates = ((str(self.latestDates(x))[3:-10])+' in 2D<br>')
            dates3d = ('<font color="DodgerBlue">'+(str(self.latestDates(x+1))[3:-10])+' in 3D<img src="http://www.SunsetTheatre.com/images/blueglasses.jpg"><br>')
            closed = str(self.latestClosed(x+1))[3:-4]
            if closed == '': # if "closed" comes back empty from the DB, do nothing
                closed = ''
            elif closed == 'None':
                closed = ''
            elif closed == 'on':
                closed = ''
            elif closed == None:
                closed = ''
            else:
                closed = '<FONT color=yellow size=3>'+closed+'<br><br>' # but if "closed" comes back with text in it, print that sucka on the website
        elif self.latestTitle(x) == self.latestTitle(x-1):
            title = ''
        else:
            title = str(self.latestTitle(x))[3:-4]
        synopsis = str(self.latestSynopsis(x))[3:-4]
        cast = str(self.latestCast(x))[3:-4]
        runtime = str(self.latestRuntime(x))[3:-4]
        if str(self.latestRating(x))[3:-4] == 'PG-13':
            rating = 'PG13'
        else:
            rating = str(self.latestRating(x))[3:-4] 
        trailer = str(self.latestTrailer(x))[3:-4] 
        image = str(self.latestImage(x))[3:-4]
        if dates3d != '':
            reald = '<img src="http://www.sunsettheatre.com/images/spacer.jpg"><img src="http://www.sunsettheatre.com/images/spacer.jpg"><img src="http://www.sunsettheatre.com/images/realdlogo.jpg">'
        else:
            reald = ''


        newChunk = self.chunk.format((title),
            (dates),
            (dates3d),
            (cast),
            (synopsis),
            (runtime),
            (trailer),
            (image),
            (rating),
            (reald),
            (sound),
            (closed))
        if title == '':
            return ''
            
        else:
            return str(newChunk)

    def addMessage(self):
        for file in glob.glob("message*.txt"):
            messagefile = file
        mEpoch = (str(messagefile)[7:-4])
        today = int(time.time())
        if int(mEpoch) > today:
            mess = open(messagefile, 'r')
            message = mess.read()
            mess.close()
        else:
            message = ''
        return message

    # Gets records from DB based on most recent movies
    def latestFormat(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Format FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Format FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Format FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Format FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Format FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
    
    def latestSynopsis(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Synopsis FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Synopsis FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Synopsis FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Synopsis FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Synopsis FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
            
    def latestTitle(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Title FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Title FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Title FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Title FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Title FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()   

    def latestCast(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Actors FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Actors FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Actors FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Actors FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Actors FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()

    def latestRating(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Rating FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Rating FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Rating FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Rating FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Rating FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()

    def latestDates(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Dates FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Dates FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Dates FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Dates FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Dates FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()

    def latestRuntime(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Runtime FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Runtime FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Runtime FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Runtime FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Runtime FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()

    def latestTrailer(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Trailer FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Trailer FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Trailer FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Trailer FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Trailer FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()

    def latestImage(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Image FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Image FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Image FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Image FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Image FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()

    def latestEpoch(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Epoch FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Epoch FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Epoch FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Epoch FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Epoch FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()

    def latestSound(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Sound FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Sound FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Sound FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Sound FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Sound FROM Movies WHERE ID ='{}'").format(varID))
            return c.fetchall()
        
    def latestClosed(self, x):
        if x == 1:
            varID = (self.newMovieVar(1))
            c.execute(("SELECT Closed FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()
        elif x == 2:
            varID = (self.newMovieVar(2))
            c.execute(("SELECT Closed FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()
        elif x == 3:
            varID = (self.newMovieVar(3))
            c.execute(("SELECT Closed FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()
        elif x == 4:
            varID = (self.newMovieVar(4))
            c.execute(("SELECT Closed FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()
        else:
            varID = (self.newMovieVar(5))
            c.execute(("SELECT Closed FROM Movies WHERE ID ='{}';").format(varID))
            return c.fetchall()   



        # Creates and writes index.html file
    def createHTML(self, content):
        file = open("index.html", "w")
        file.write(content)
        file.close()

        # Creates and writes pastmovies.html file
    def createPast(self, content):
        file = open('pastmovies.html','w')
        file.write(content)
        file.close()

        # Creates and writes backup of index.html file
    def backupCreate(self, content):
        textname = (datetime.now().month, datetime.now().year)
        file = open("Backup\\HomePage\\index{}.html".format(textname), "w")
        file.write(content)
        file.close()

        # Creates and writes backup of pastmovies.html file
    def backupPast(self, content):
        textname = (datetime.now().month, datetime.now().year)
        file = open("Backup\\PastPage\\pastmovies{}.html".format(textname), "w")
        file.write(content)
        file.close()

        # Copies movielist.db and pastes it in Backup folder
    def backupDB(self):
        dbname = (datetime.now().month, datetime.now().year)
        shutil.copy2('movielist.db', 'Backup\\Database\\movielist{}.db'.format(dbname))
        
        # Takes content from text file for use in createHTML() function
    def submit(self, event=None):
        self.sortTable()
        message = self.addMessage()
        first = self.addChunk1(1)
        second = self.addChunk1(2)
        third = self.addChunk1(3)
        fourth = self.addChunk1(4)
        fifth = self.addChunk1(5)
        myfile = open('site.txt', 'r')
        data=myfile.read()
        myfile.close()
        self.createHTML((data.format(message, first, second, third, fourth, fifth, self.listPastMovies())))
        self.pastsubmit()
        self.twoMonthsAgo(1, (data.format(message, first, second, third, fourth, fifth, self.listPastMovies())))
            
        # Confirmation of submission via dialog box
        messagebox.showinfo(title='Web page created successfully!',message=
                            "Success! Now just upload this index.html file to the server.")

        # Takes content from text file for use in createPast() function
    def pastsubmit(self):
        year1 = self.addPast(2015)
        year2 = self.addPast(2016)
        year3 = self.addPast(2017)
        year4 = self.addPast(2018)
        year5 = self.addPast(2019)
        year6 = self.addPast(2020)
        year7 = self.addPast(2021)
        year8 = self.addPast(2022)
        year9 = self.addPast(2023)
        myfile = open('pastpage.txt', 'r')
        data=myfile.read()
        myfile.close()
        self.createPast(data.format(year1, year2, year3, year4, year5, year6, year7, year8, year9))
        self.twoMonthsAgo(2, data.format(year1, year2, year3, year4, year5, year6, year7, year8, year9))

        # Resets all fields
    def clear(self, event=None):
        self.text_title.delete(1.0,'end')
        self.text_cast.delete(1.0,'end')
        self.text_date2d.delete(1.0,'end')
        self.text_summary.delete(1.0,'end')
        self.text_trailer.delete(1.0,'end')
        self.text_runtime.delete(1.0,'end')
        self.text_image.delete(1.0,'end')
        self.contentBox2.set('Select:')
        self.v.set(1)
        self.v2.set(1)
        self.var.set(str(date.today().year))

        # Gets index.html template from text file
    def textChunk():
        myfile = open('chunk.txt', 'r')
        data = myfile.read()
        myfile.close()
        return data

        # Gets pastmovies.html template from text file
    def pastChunk():
        myfile = open('pastchunk.txt', 'r')
        data = myfile.read()
        myfile.close()
        return data

    chunk = str(textChunk())
    pastchunk = str(pastChunk())
    
root = Tk()
        
# Run program          
def main():
    guihtml = GUIhtml(root)
    today = int(time.time())
    if today > 1672560000:
        message = messagebox.showinfo(title='Update Needed!',message=
                                        'This program was designed to last until January 1st, 2024. At that time, the "Past Movies" page will break. Please contact Nathan to update the program before that time. If you are in 2024 and the Past Movies page is broken, use a recent backup of the page from the Updates folder and add the movies manually. The rest of the program should work fine.')
    root.mainloop()

def Quit(event=None):
    root.destroy()
    
if __name__ == "__main__": main()
