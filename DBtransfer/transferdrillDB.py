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

class windowClass(wx.Frame):

    # Frame makin'
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(size=(470,175),*args, **kwargs)
        self.basicGUI()
        self.Center()
        
#------------------------WIDGETS & VARIABLES------------------------#

    def basicGUI(self):
        # Settin' it up
        panel = wx.Panel(self)
        self.SetTitle('File Transfer Manager')
        self.Show(True)

        # Menu bar
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)
        
        # File menu
        fileButton = wx.Menu()
        menuBar.Append(fileButton, 'File')

        # File - "Check/Transfer"
        checkItem = wx.MenuItem(fileButton, wx.ID_ANY,"Check/Transfer Files...")
        fileButton.AppendItem(checkItem)
        self.Bind(wx.EVT_MENU, self.Message, checkItem)

        # File - "Date/Time of Last Check"
        timeItem = wx.MenuItem(fileButton, wx.ID_ANY,"Time of Last Check")
        fileButton.AppendItem(timeItem)
        self.Bind(wx.EVT_MENU, self.TimeMessage, timeItem)

        # File - "Quit"
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT,"Quit")
        fileButton.AppendItem(exitItem)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        # Directory textbox labels
        srcText = wx.StaticText(panel, -1, "Browse for source directory...",(10,10))
        destText = wx.StaticText(panel, -1, "Browse for destination directory...",(10,57))

        # Directory textboxes
        self.control1 = wx.TextCtrl(panel,size=(200, -1),pos=(10,27), style=wx.TE_READONLY)
        self.control2 = wx.TextCtrl(panel,size=(200, -1),pos=(10,74), style=wx.TE_READONLY)

        # Browse buttons
        srcBtn = wx.Button(panel, label="Browse",pos=(217,26))
        srcBtn.Bind(wx.EVT_BUTTON, self.onDir1)
        destBtn = wx.Button(panel, label="Browse",pos=(217,73))
        destBtn.Bind(wx.EVT_BUTTON, self.onDir2)

        # Check/Transfer button
        checkBtn = wx.Button(panel, label="Check/Transfer",size=(110,73),pos=(325,26))
        checkBtn.Bind(wx.EVT_BUTTON, self.Message)


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
            checkBox = wx.MessageDialog(None, 'There are currently '+str(self.counting())+
                                        ' new files in the source folder. Copy them to the destination folder?',
                                        caption='Check or Transfer Files',style=YES_NO|CENTRE, pos=DefaultPosition)
            checkAnswer = checkBox.ShowModal()
            if checkAnswer == wx.ID_YES:
                self.Transfer()
            checkBox.Destroy()
            timeNow = datetime.now().strftime("%a, %b %d %Y at %I:%M %p")
            self.insertCell(timeNow)
        except:
            print "You failed to specify one or more directories."

    # Dialog box giving time of last file check
    def TimeMessage(self, e):
        timeBox = wx.MessageDialog(None, 'The most recent File Check was performed on '+(str(self.getCell())[8:-3])+'.',
                                    caption='Last File Check',style=OK|CENTRE, pos=DefaultPosition)
        timeAnswer = timeBox.ShowModal()
        if timeAnswer == wx.ID_OK:
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
                print self.srcPath+"//"+file+" successfully copied."

            # Ignore older files
            elif yesterday > mod:
                print "File skipped."
        print "Operation completed."

    # Adds directory paths to the textboxes
    def TextBox1(self, path):
        self.control1.ChangeValue(path)

    def TextBox2(self, path):
        self.control2.ChangeValue(path)
        
    # Dialog: Browse for source folder
    def onDir1(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.srcPath = dlg.GetPath()
            self.TextBox1(self.srcPath)
        dlg.Destroy()
        

    # Dialog: Browse for destination folder
    def onDir2(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.destPath = dlg.GetPath()
            self.TextBox2(self.destPath)
        dlg.Destroy()

# Do it up
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()
        



