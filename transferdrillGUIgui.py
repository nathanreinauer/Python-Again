
from wx import *
from datetime import *
import os.path

### Path to each folder
##srcPath = os.path.expanduser('~\Desktop\Customer Orders')
##destPath = os.path.expanduser('~\Desktop\Home Office')

### Number of files in Customer Orders
##newFiles = len([f for f in os.listdir(srcPath)if os.path.isfile(os.path.join(srcPath, f))])

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




    def Message(self, e):
        # Number of files in Customer Orders
        newFiles = len([f for f in os.listdir(self.srcPath)if os.path.isfile(os.path.join(self.srcPath, f))])
        checkBox = wx.MessageDialog(None, 'There are currently '+str(newFiles)+
                                    ' new files in the source folder. Copy them to the destination folder?',
                                    caption='Caption',style=YES_NO|CENTRE, pos=DefaultPosition)
        checkAnswer = checkBox.ShowModal()
        if checkAnswer == wx.ID_YES:
            print "Here's where transfer happens."
            self.Transfer()
        checkBox.Destroy()

    def Quit(self, e):
        self.Close()

    def Transfer(self):
        self.Close() # This will run the transfer if they click OK to dialog

    def TextBox1(self, path):
        self.control1.ChangeValue(path)

    def TextBox2(self, path):
        self.control2.ChangeValue(path)
        
    # Browse source folder dialog
    def onDir1(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.srcPath = dlg.GetPath()
            self.TextBox1(self.srcPath)
        dlg.Destroy()
        

    # Browse destination folder dialog
    def onDir2(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.destPath = dlg.GetPath()
            self.TextBox2(self.destPath)
        dlg.Destroy()

        
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()
        



