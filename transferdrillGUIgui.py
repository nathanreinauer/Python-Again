
from wx import *

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(size=(470,175),*args, **kwargs)

        self.basicGUI()

    def onDir(self, event):
        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            print "You chose %s" % dlg.GetPath()
        dlg.Destroy()
        

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
        checkItem = wx.MenuItem(fileButton, wx.ID_EXIT,"Check/Transfer Files...")
        fileButton.AppendItem(checkItem)
        self.Bind(wx.EVT_MENU, self.Check, checkItem)

        # File - Quit
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT,"Quit")
        fileButton.AppendItem(exitItem)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        # Directory box labels
        srcText = wx.StaticText(panel, -1, "Browse for source directory...",(10,10))
        destText = wx.StaticText(panel, -1, "Browse for destination directory...",(10,57))

        self.control1 = wx.TextCtrl(self,size=(200, -1),pos=(10,27))
        self.control2 = wx.TextCtrl(self,size=(200, -1),pos=(10,74))

        # Browse button
        srcBtn = wx.Button(panel, label="Browse",pos=(217,26))
        srcBtn.Bind(wx.EVT_BUTTON, self.onDir)

        destBtn = wx.Button(panel, label="Browse",pos=(217,73))
        destBtn.Bind(wx.EVT_BUTTON, self.onDir)

        # Check button
        checkBtn = wx.Button(panel, label="Check/Transfer",size=(110,73),pos=(325,26))
        # (doesn't work yet) checkBtn.bind(wx.EVT_BUTTON, self.Quit, exitItem)





##        checkBox = wx.MessageDialog(None, 'There are currently '+newFiles+' in the source folder. Copy them to the destination folder?',wx.YES_NO)
##        checkAnswer = checkBox.ShowModal()
##        checkBox.Destroy()
##        if checkBox.ShowModal()==wx.ID_OK: # or ID_YES? Something that means yes
##            Run transfer function


    def Quit(self, e):
        self.Close()

    def Check(self, e):
        self.Close() # This will open OK/Cancel dialog and display the number of new files

    def Transfer(self, e):
        self.Close() # This will run the transfer if they click OK to dialog

        
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()
        



