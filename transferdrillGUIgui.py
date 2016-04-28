
import wx

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(size=(500,200),*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()
        
        fileButton = wx.Menu()

        
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT,"Quit")
        fileButton.AppendItem(exitItem)

        
        menuBar.Append(fileButton, 'File')
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)





##        checkBox = wx.MessageDialog(None, 'There are currently '+newFiles+' in the source folder. Copy them to the destination folder?',wx.YES_NO)
##        checkAnswer = checkBox.ShowModal()
##        checkBox.Destroy()
##        if checkBox.ShowModal()==wx.ID_OK: # or ID_YES? Something that means yes
##            Run transfer function

        srcText = wx.StaticText(panel, -1, "Browse for source directory...", pos=(3,3))

        destText = wx.StaticText(panel, -1, "Browse for destination directory...",(3,30))


            

        self.SetTitle('Welcome!')
        self.Show(True)

    def Quit(self, e):
        self.Close()

        
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()
        



