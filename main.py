import wx
from functools import partial
import random

class Frame(wx.Frame):

    def __init__(self, *args, **kw):
        super(Frame, self).__init__(*args, **kw)

        self.CreateStatusBar()
        self.SetStatusText("This is an example program...")

        self.textCtrl = wx.TextCtrl(self)
        self.changeColorBtn = wx.Button(self, label="Change color")
        self.resetColorBtn = wx.Button(self, label="Reset color")
        self.changeColorBtn.Bind(event=wx.EVT_BUTTON, handler=partial(self.onChangeColor, target=self.textCtrl))
        self.resetColorBtn.Bind(event=wx.EVT_BUTTON, handler=partial(self.onResetColor, target=self.textCtrl))
        self._doLayout()

    def _makeMenuBar(self):
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)

    def _doLayout(self):
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(wx.StaticText(self, label="Click to change textCtrl color"), flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        vSizer.Add(self.textCtrl, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        vSizer.Add(self.changeColorBtn, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        vSizer.Add(self.resetColorBtn, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        hSizer.Add(vSizer, proportion=1, flag=wx.ALIGN_CENTER)

        hSizer.SetMinSize(200, 100)
        self.SetSizerAndFit(hSizer)

    def onExit(self, event):
        self.Close(True)
    
    def onChangeColor(self, event, target):
        colors = [wx.RED, wx.BLUE, wx.GREEN]

        target.BackgroundColour = random.choice(colors)
        target.ForegroundColour = wx.WHITE

    def onResetColor(self, event, target):
        target.BackgroundColour = wx.NullColour
        target.ForegroundColour = wx.NullColour

    def onAbout(self, event):
        about = wx.adv.AboutDialogInfo()
        about.Name = "Change wxTextCtrl colors example"
        about.Version = "0.1"
        about.Copyright = "(C) Emiliano Mesquita Drago"
        about.Description = "An example for changing wxTextCtrl colors"
        about.SetWebSite("https://github.com/mezka/wx-textctrlcolor-example.git")
        wx.adv.AboutBox(about)

if __name__ == '__main__':
    app = wx.App()
    frm = Frame(None, title='Change wxTextCtrl colors example')
    frm.Show()
    app.MainLoop()