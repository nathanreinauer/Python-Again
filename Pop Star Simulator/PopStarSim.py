
import wx

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(size=(400,515),*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()
        
        fileButton = wx.Menu()
        editButton = wx.Menu()
        importItem = wx.Menu()
        newItem = wx.Menu()


        fileButton.Append(wx.ID_ANY,'New Song\t(New enough according to the lawyers, anyway)')
        
        importItem.Append(wx.ID_ANY,'Import drum machine')
        importItem.Append(wx.ID_ANY,'Import 3-note piano loop')
        importItem.Append(wx.ID_ANY,"Help: What are 'instruments'?")

        

        fileButton.AppendMenu(wx.ID_ANY,'Import Instrument...',importItem)

        

        toolBar = self.CreateToolBar()
        quitToolButton = toolBar.AddLabelTool(wx.ID_ANY,'Quit',
                                              wx.Bitmap('mic.bmp'))
        importToolButton = toolBar.AddLabelTool(wx.ID_ANY,'Import',
                                                wx.Bitmap('guitar.bmp'))

        quitToolButton = toolBar.AddLabelTool(wx.ID_ANY,'Quit',
                                              wx.Bitmap('key.bmp'))
        importToolButton = toolBar.AddLabelTool(wx.ID_ANY,'Import',
                                                wx.Bitmap('dj.bmp'))

        
        toolBar.Realize()
        self.Bind(wx.EVT_TOOL, self.Quit, quitToolButton)

        
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT,"Quit\t(Work at Sbarro's instead)")
        exitItem.SetBitmap(wx.Bitmap('quit.png'))
        fileButton.AppendItem(exitItem)

        
        exitItem.SetBitmap(wx.Bitmap('quit.png'))
        
        editButton.Append(wx.ID_ANY,'Fire drummer for being too drunk/high')
        editButton.Append(wx.ID_ANY,'Fire drummer for being better looking than singer')
        editButton.Append(wx.ID_ANY,'Fire drummer for being late to practice again')
        editButton.Append(wx.ID_ANY,'Fire drummer for being too sober')

        
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)


        nameBox = wx.TextEntryDialog(None, 'What is your band called?','Welcome!','Johnny No-Name & the Cheese Graters')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()


        yesNoBox = wx.MessageDialog(None, 'Are you prepared to wallow in obscurity for .005 cents a play on Spotify?','Making sure you\'re up for this...',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()


        #if yesNoAnswer == wx.ID_NO:
         #   userName = 'Loser!'

        chooseOneBox = wx.SingleChoiceDialog(None, 'Choose a genre...',
                                             'Genre',
                                             ['Pop','Rock','I don\'t believe in labels, man','Acoustic versions of radio hits on YouTube'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        a = wx.TextCtrl(panel, pos=(3,50), size=(378,300))
        a.SetValue("Generic Party Song #14")

        aweText = wx.StaticText(panel, -1, "Welcome to Pop Star Simulator!", pos=(3,3))
        #aweText.SetForegroundColour('#67cddc')
        #aweText.SetBackgroundColour('black')

        rlyAweText = wx.StaticText(panel, -1, "Let's write some lyrics:",(3,30))
        #rlyAweText.SetForegroundColour(favColor)
        #rlyAweText.SetBackgroundColour('black')


            

        self.SetTitle('Welcome, '+userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()

        
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()
        



