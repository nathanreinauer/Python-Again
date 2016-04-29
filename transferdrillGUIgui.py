
from wx import *
from datetime import *
import os.path
import shutil

# Today - 24 hours = "yesterday"
yesterday = datetime.now() - timedelta(days=1)


                

class windowClass(wx.Frame):


    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(size=(470,175),*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        self.SetTitle('File Transfer Manager')
        self.Show(True)

        self.dlg2 = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE)
        self.dlg = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE)
        self.srcPath = self.dlg.GetPath()
        self.destPath = self.dlg.GetPath()

            

        # Menu bar
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)
        
        # File menu
        fileButton = wx.Menu()
        menuBar.Append(fileButton, 'File')

        # File - Check/Transfer
        checkItem = wx.MenuItem(fileButton, wx.ID_ANY,"Check/Transfer Files...")
        fileButton.AppendItem(checkItem)
        self.Bind(wx.EVT_MENU, self.Message, checkItem)

        # File - Quit
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT,"Quit")
        fileButton.AppendItem(exitItem)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        # Directory box labels
        srcText = wx.StaticText(panel, -1, "Browse for source directory...",(10,10))
        destText = wx.StaticText(panel, -1, "Browse for destination directory...",(10,57))

        # Directory text boxes
        self.control1 = wx.TextCtrl(panel,size=(200, -1),pos=(10,27))
        self.control2 = wx.TextCtrl(panel,size=(200, -1),pos=(10,74))

        # Browse buttons
        srcBtn = wx.Button(panel, label="Browse",pos=(217,26))
        srcBtn.Bind(wx.EVT_BUTTON, self.onDir1)
        
        destBtn = wx.Button(panel, label="Browse",pos=(217,73))
        destBtn.Bind(wx.EVT_BUTTON, self.onDir2)

        # Check button
        checkBtn = wx.Button(panel, label="Check/Transfer",size=(110,73),pos=(325,26))
        # checkBtn = Enable(False)
        checkBtn.Bind(wx.EVT_BUTTON, self.Message)

    def counting(self):
        count = 0
        # Figure out how many files are new
        for file in os.listdir(self.srcPath):
            mod = self.modTime(self.srcPath+"//"+file)

            if yesterday < mod:
                count = count+1
        return count

    def modTime(self, filePath):
        t = os.path.getmtime(filePath)
        return datetime.fromtimestamp(t)

    def Message(self, e):

        if self.srcPath or self.destPath == None:
            print "Whoops!"
        else:
            checkBox = wx.MessageDialog(None, 'There are currently '+str(self.counting())+
                                        ' new files in the source folder. Copy them to the destination folder?',
                                        caption='Caption',style=YES_NO|CENTRE, pos=DefaultPosition)
            checkAnswer = checkBox.ShowModal()
            if checkAnswer == wx.ID_YES:
                self.Transfer()
            checkBox.Destroy()

    def Quit(self, e):
        self.Close()

    def Transfer(self):
        for file in os.listdir(self.srcPath):
            mod = self.modTime(self.srcPath+"//"+file)

            # Copy the files that were modified in the last 24 hours
            if yesterday < mod:
                shutil.copy((self.srcPath+"//"+file), self.destPath)
                print self.srcPath+"//"+file+" successfully copied."

            # Ignore older files
            elif yesterday > mod:
                print "File skipped."
                    
        print "Operation completed."

    def TextBox1(self, path):
        self.control1.ChangeValue(path)

    def TextBox2(self, path):
        self.control2.ChangeValue(path)
        
    # Browse source folder dialog
    def onDir1(self, event):

        if self.dlg.ShowModal() == wx.ID_OK:

            self.TextBox1(self.srcPath)
        self.dlg.Destroy()
        

    # Browse destination folder dialog
    def onDir2(self, event):
##        dlg = wx.DirDialog(self, "Choose a directory:",
##                           style=wx.DD_DEFAULT_STYLE
##                           )
        if self.dlg2.ShowModal() == wx.ID_OK:
            #self.destPath = dlg.GetPath()
            self.TextBox2(self.destPath)
        self.dlg2.Destroy()

        
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()
        



