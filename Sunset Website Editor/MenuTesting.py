import sqlite3
from wx import *
from datetime import *
import os.path
import shutil

# Today - 24 hours = "yesterday"
yesterday = datetime.now() - timedelta(days=1)

# Setting up SQLite
conn = sqlite3.connect('TranDB.db')
c = conn.cursor()

class windowClass(Frame):

    # Frame makin'
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(size=(470,175),*args, **kwargs)
        self.basicGUI()
        self.Center()
        
#------------------------WIDGETS & VARIABLES------------------------#

    def basicGUI(self):
        # Settin' it up
        panel = Panel(self)
        self.SetTitle('File Transfer Manager')
        self.Show(True)


#------------------------------


        # Menu bar
        menuBar = MenuBar()
        self.SetMenuBar(menuBar)
        
#-------# File menu
        fileButton = Menu()
        menuBar.Append(fileButton, 'File')

        # File - "Create HTML File"
        createItem = MenuItem(fileButton, ID_ANY,"Create HTML File")
        fileButton.Append(createItem)
        self.Bind(EVT_MENU, self.submit, createItem)


        # File - "Open Newest HTML File"
        openItem = MenuItem(fileButton, ID_ANY,"Open Newest HTML File")
        fileButton.Append(openItem)
        self.Bind(EVT_MENU, self.openHTML, openItem)

        # File - "Import Last Record"
        importItem = MenuItem(fileButton, ID_ANY,"Import Last Record")
        fileButton.Append(importItem)
        self.Bind(EVT_MENU, self.importLast, importItem)

        # File - "Clear All Fields"
        clearItem = MenuItem(fileButton, ID_ANY,"Clear All Fields")
        fileButton.Append(clearItem)
        self.Bind(EVT_MENU, self.clear, clearItem)
        
        # File - "Quit"
        exitItem = MenuItem(fileButton, ID_EXIT,"Quit")
        fileButton.Append(exitItem)
        self.Bind(EVT_MENU, self.Quit, exitItem)
        
#-------# View menu
        viewButton = Menu()
        menuBar.Append(viewButton, 'View')

        # View - "Watch Trailer"
        trailerItem = MenuItem(viewButton, ID_ANY,"Watch Trailer")
        viewButton.Append(trailerItem)
        self.Bind(EVT_MENU, self.Message, trailerItem)

        # View - "Visit SunsetTheatre.com"
        sunsetItem = MenuItem(viewButton, ID_ANY,"Visit SunsetTheatre.com")
        viewButton.Append(sunsetItem)
        self.Bind(EVT_MENU, self.visitSite, sunsetItem)

        # View - "Print Database To Text File"
        databaseItem = MenuItem(viewButton, ID_ANY,"View Database")
        viewButton.Append(databaseItem)
        self.Bind(EVT_MENU, self.printDB, databaseItem)

#-------# Help menu
        helpButton = Menu()
        menuBar.Append(helpButton, 'Help')

        # View - "View Manual"
        manualItem = MenuItem(helpButton, ID_ANY,"View Manual")
        helpButton.Append(manualItem)
        self.Bind(EVT_MENU, self.openManual, manualItem)

        # View - "Tech Support"
        supportItem = MenuItem(helpButton, ID_ANY,"Tech Support")
        helpButton.Append(supportItem)
        self.Bind(EVT_MENU, self.techSupport, supportItem)

        # View - "About"
        aboutItem = MenuItem(helpButton, ID_ANY,"About")
        helpButton.Append(aboutItem)
        self.Bind(EVT_MENU, self.about, aboutItem)

#---------------------------------------

        # Directory textbox labels
        srcText = StaticText(panel, -1, "Browse for source directory...",(10,10))
        destText = StaticText(panel, -1, "Browse for destination directory...",(10,57))

        # Directory textboxes
        self.control1 = TextCtrl(panel,size=(200, -1),pos=(10,27), style=TE_READONLY)
        self.control2 = TextCtrl(panel,size=(200, -1),pos=(10,74), style=TE_READONLY)

        # Browse buttons
        srcBtn = Button(panel, label="Browse",pos=(217,26))
        srcBtn.Bind(EVT_BUTTON, self.onDir1)
        destBtn = Button(panel, label="Browse",pos=(217,73))
        destBtn.Bind(EVT_BUTTON, self.onDir2)

        # Check/Transfer button
        checkBtn = Button(panel, label="Check/Transfer",size=(110,73),pos=(325,26))
        checkBtn.Bind(EVT_BUTTON, self.Message)


#------------------------FUNCTIONS------------------------#
        
    # SQL --- ADD INFO TO TABLE
    def insertCell(self, add):
        c.execute("INSERT INTO LastCheck (DateTime) VALUES (?)", (add,))
        conn.commit()

    # SQL --- RETRIEVE LAST RECORD
    def getCell(self):
        c.execute("SELECT * FROM LastCheck ORDER BY ID DESC LIMIT 1")
        return c.fetchall()
    
    # Figure out how many new files are in source directory
    def counting(self):
        count = 0
        for file in os.listdir(self.srcPath):
            mod = self.modTime(self.srcPath+"//"+file)
            if yesterday < mod:
                count = count+1
        return count
    
    # Get 'Date Modified' for a file
    def modTime(self, filePath):
        t = os.path.getmtime(filePath)
        return datetime.fromtimestamp(t)

    # Dialog box giving number of new files
    # and asking if you'd like to transfer them
    def Message(self, e):
        try:
            checkBox = MessageDialog(None, 'There are currently '+str(self.counting())+
                                        ' new files in the source folder. Copy them to the destination folder?',
                                        caption='Check or Transfer Files',style=YES_NO|CENTRE, pos=DefaultPosition)
            checkAnswer = checkBox.ShowModal()
            if checkAnswer == ID_YES:
                self.Transfer()
            checkBox.Destroy()
            timeNow = datetime.now().strftime("%a, %b %d %Y at %I:%M %p")
            self.insertCell(timeNow)
        except:
            print("You failed to specify one or more directories.")

    # Dialog box giving time of last file check
    def TimeMessage(self, e):
        timeBox = MessageDialog(None, 'The most recent File Check was performed on '+(str(self.getCell())[8:-3])+'.',
                                    caption='Last File Check',style=OK|CENTRE, pos=DefaultPosition)
        timeAnswer = timeBox.ShowModal()
        if timeAnswer == ID_OK:
            timeBox.Destroy()

    # Makes GUI close
    def Quit(self, e):
        self.Close()

    # Where the magic happens
    def Transfer(self):
        for file in os.listdir(self.srcPath):
            mod = self.modTime(self.srcPath+"//"+file)

            # Transfer the files that were modified in the last 24 hours
            if yesterday < mod:
                shutil.copy((self.srcPath+"//"+file), self.destPath)
                print(self.srcPath+"//"+file+" successfully copied.")

            # Ignore older files
            elif yesterday > mod:
                print("File skipped.")
        print("Operation completed.")

    # Adds directory paths to the textboxes
    def TextBox1(self, path):
        self.control1.ChangeValue(path)

    def TextBox2(self, path):
        self.control2.ChangeValue(path)
        
    # Dialog: Browse for source folder
    def onDir1(self, event):
        dlg = DirDialog(self, "Choose a directory:",
                           style=DD_DEFAULT_STYLE
                           )
        if dlg.ShowModal() == ID_OK:
            self.srcPath = dlg.GetPath()
            self.TextBox1(self.srcPath)
        dlg.Destroy()
        

    # Dialog: Browse for destination folder
    def onDir2(self, event):
        dlg = DirDialog(self, "Choose a directory:",
                           style=DD_DEFAULT_STYLE
                           )
        if dlg.ShowModal() == ID_OK:
            self.destPath = dlg.GetPath()
            self.TextBox2(self.destPath)
        dlg.Destroy()

# Do it up
def main():
    app = App()
    windowClass(None)

    app.MainLoop()

main()
        



