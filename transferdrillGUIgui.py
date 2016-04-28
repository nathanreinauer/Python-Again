
from wx import *

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(size=(500,200),*args, **kwargs)

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

        # Directory box labels
        srcText = wx.StaticText(panel, -1, "Browse for source directory...",(3,3))
        destText = wx.StaticText(panel, -1, "Browse for destination directory...",(3,50))

        # Browse button
        dirDlgBtn = wx.Button(panel, label="Browse",pos=(200,15))
        dirDlgBtn.Bind(wx.EVT_BUTTON, self.onDir)

        # Menu bar
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)
        
        # File menu
        fileButton = wx.Menu()
        menuBar.Append(fileButton, 'File')

        # File - Quit
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT,"Quit")
        fileButton.AppendItem(exitItem)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)



##        checkBox = wx.MessageDialog(None, 'There are currently '+newFiles+' in the source folder. Copy them to the destination folder?',wx.YES_NO)
##        checkAnswer = checkBox.ShowModal()
##        checkBox.Destroy()
##        if checkBox.ShowModal()==wx.ID_OK: # or ID_YES? Something that means yes
##            Run transfer function


    def Quit(self, e):
        self.Close()

        
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()
        



