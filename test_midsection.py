import wx
from wx.lib.scrolledpanel import ScrolledPanel
# import matplotlib.backends.backend_wxagg
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.widgets import Cursor

from pdb import set_trace
# import wx.lib.plot as plt
import matplotlib.pyplot as plt
import numpy as np
import mpld3

# class PlotCanvas(plt.PlotCanvas):
    # def __init__(self, parent, size):
        # plt.PlotCanvas.__init__(self, parent, style=wx.SIMPLE_BORDER, size=size)
        # self.data = [(1,2), (2,3), (3,5), (4,6), (5,8), (6,8), (10,10)]
        # line = plt.PolyLine(self.data, legend='', colour='pink', width=2)
        # gc = plt.PlotGraphics([line], 'Line Graph', 'X Axis', 'Y Axis')
        # self.Draw(gc, xAxis=(0,15), yAxis=(0,15))


class MidsectionImport(wx.Panel):
    def __init__(self, midsecHeader=None, *args, **kwargs):
        super(MidsectionImport, self).__init__(*args, **kwargs)
        self.midsecHeader = midsecHeader
        self.headerLbl = "Header"
        self.testLbl1 = "test label1"
        self.testLbl2 = "test label2"
        self.testLbl3 = "test label3"
        self.testLbl4 = "test label4"
        self.tipLbl = "velocity:       111 m\narea:        222 m^2\nsomething:   1234 u"
        self.tipLbl2 = "velocity:       999 m\narea:        888 m^2\nsomething:   7777 u"


        self.InitUI()


    def InitUI(self):
        self.panelSizerH = wx.BoxSizer(wx.HORIZONTAL)
        self.panelSizerV = wx.BoxSizer(wx.VERTICAL)
        self.tableSizerV = wx.BoxSizer(wx.VERTICAL)
        

        self.SetSizer(self.panelSizerV)

        self.table = ScrolledPanel(self)
        self.table.SetSizer(self.tableSizerV)
        self.table.SetupScrolling(False, True)

        self.panelSizerH.Add((40, -1), 0, wx.EXPAND)
        self.panelSizerH.Add(self.table, 1, wx.EXPAND)
        self.panelSizerH.Add((40, -1), 0, wx.EXPAND)

        self.panel2SizerH = wx.BoxSizer(wx.HORIZONTAL)

        

        self.canvasPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        self.canvaSizerV = wx.BoxSizer(wx.VERTICAL)
        self.canvasPanel.SetSizer(self.canvaSizerV)

        # self.fig, self.ax = plt.figure()
        if self.midsecHeader != None:
            self.midsectionHeader, self.fig, self.ax, self.tags, self.depths, self.tagmarkLineList, self.depthTagList, \
                    self.depthList = self.midsecHeader.GeneratePlot()
            self.annot = self.ax.annotate("_anno_", xy=(20,0.8), xytext=(50,50),textcoords="offset points", \
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
            self.annot.set_visible(True)

            self.canvas = FigureCanvas(self.canvasPanel, -1, self.fig)
            self.fig.canvas.mpl_connect('button_press_event', self.onMouseClickAx2)
            self.fig.canvas.mpl_connect('motion_notify_event', self.onMouseOverAx2)
            self.canvaSizerV.Add(self.canvas, 1, wx.EXPAND)


        self.panel2SizerH.Add((40, -1), 0, wx.EXPAND)
        self.panel2SizerH.Add(self.canvasPanel, 1, wx.EXPAND)
        self.panel2SizerH.Add((40, -1), 0, wx.EXPAND)



        self.panelSizerV.Add((-1, 80), 0, wx.EXPAND)
        self.panelSizerV.Add(self.panelSizerH, 1, wx.EXPAND)
        self.panelSizerV.Add((-1, 80), 0, wx.EXPAND)
        self.panelSizerV.Add(self.panel2SizerH, 1, wx.EXPAND)
        self.panelSizerV.Add((-1, 80), 0, wx.EXPAND)


        self.panel0 = wx.Panel(self.table, style=wx.SIMPLE_BORDER)
        self.panel0.SetBackgroundColour('Grey')
        self.panel1 = wx.Panel(self.table, style=wx.SIMPLE_BORDER)
        self.panel2 = wx.Panel(self.table, style=wx.SIMPLE_BORDER)
        self.panel3 = wx.Panel(self.table, style=wx.SIMPLE_BORDER)
        self.panel4 = wx.Panel(self.table, style=wx.SIMPLE_BORDER)

        sizerH0 = wx.BoxSizer(wx.HORIZONTAL)
        sizerH1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerH2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerH3 = wx.BoxSizer(wx.HORIZONTAL)
        sizerH4 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel0.SetSizer(sizerH0)
        self.panel1.SetSizer(sizerH1)
        self.panel2.SetSizer(sizerH2)
        self.panel3.SetSizer(sizerH3)
        self.panel4.SetSizer(sizerH4)

        
        self.testTxt0_1 = wx.StaticText(self.panel0, 1, label=self.headerLbl)
        self.testTxt0_2 = wx.StaticText(self.panel0, 1, label=self.headerLbl)
        self.testTxt0_3 = wx.StaticText(self.panel0, 1, label=self.headerLbl)
        self.testTxt0_4 = wx.StaticText(self.panel0, 1, label=self.headerLbl)

        sizerH0.Add(self.testTxt0_1, 1, wx.EXPAND)
        sizerH0.Add(self.testTxt0_2, 1, wx.EXPAND)
        sizerH0.Add(self.testTxt0_3, 1, wx.EXPAND)
        sizerH0.Add(self.testTxt0_4, 1, wx.EXPAND)

        self.testTxt1_1 = wx.StaticText(self.panel1, 1, label=self.testLbl1)
        self.font1 = wx.Font(28, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.font2 = wx.Font(48, wx.ROMAN, wx.NORMAL, wx.BOLD)
        self.testTxt1_1.SetFont(self.font1)
        self.toolTip = wx.ToolTip(self.tipLbl)
        self.testTxt1_1.SetToolTip(self.toolTip)

        self.colour = self.testTxt1_1.GetBackgroundColour()



        self.testTxt1_1.Bind(wx.EVT_LEFT_UP, self.onLeftUp)
        self.testTxt1_1.Bind(wx.EVT_RIGHT_UP, self.onRightUp)
        self.testTxt1_1.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)
        # self.testTxt1_1.Bind(wx.EVT_RIGHT_DOWN, self.onRightDown)

        self.testTxt1_2 = wx.StaticText(self.panel1, 1, label=self.testLbl1)
        self.testTxt1_3 = wx.StaticText(self.panel1, 1, label=self.testLbl1)
        self.testTxt1_4 = wx.StaticText(self.panel1, 1, label=self.testLbl1)

        sizerH1.Add(self.testTxt1_1, 1, wx.EXPAND)
        sizerH1.Add(self.testTxt1_2, 1, wx.EXPAND)
        sizerH1.Add(self.testTxt1_3, 1, wx.EXPAND)
        sizerH1.Add(self.testTxt1_4, 1, wx.EXPAND)
       

        self.testTxt2_1 = wx.StaticText(self.panel2, 1, label=self.testLbl2)
        self.testTxt2_2 = wx.StaticText(self.panel2, 1, label=self.testLbl2)
        self.testTxt2_3 = wx.StaticText(self.panel2, 1, label=self.testLbl2)
        self.testTxt2_4 = wx.StaticText(self.panel2, 1, label=self.testLbl2)

        
        sizerH2.Add(self.testTxt2_1, 1, wx.EXPAND)
        sizerH2.Add(self.testTxt2_2, 1, wx.EXPAND)
        sizerH2.Add(self.testTxt2_3, 1, wx.EXPAND)
        sizerH2.Add(self.testTxt2_4, 1, wx.EXPAND)

        self.testTxt3_1 = wx.StaticText(self.panel3, 1, label=self.testLbl3)
        self.testTxt3_2 = wx.StaticText(self.panel3, 1, label=self.testLbl3)
        self.testTxt3_3 = wx.StaticText(self.panel3, 1, label=self.testLbl3)
        self.testTxt3_4 = wx.StaticText(self.panel3, 1, label=self.testLbl3)

        sizerH3.Add(self.testTxt3_1, 1, wx.EXPAND)
        sizerH3.Add(self.testTxt3_2, 1, wx.EXPAND)
        sizerH3.Add(self.testTxt3_3, 1, wx.EXPAND)
        sizerH3.Add(self.testTxt3_4, 1, wx.EXPAND)


        self.testTxt4_1 = wx.StaticText(self.panel4, 1, label=self.testLbl4)
        self.testTxt4_2 = wx.StaticText(self.panel4, 1, label=self.testLbl4)
        self.testTxt4_3 = wx.StaticText(self.panel4, 1, label=self.testLbl4)
        self.testTxt4_4 = wx.StaticText(self.panel4, 1, label=self.testLbl4)

        sizerH4.Add(self.testTxt4_1, 1, wx.EXPAND)
        sizerH4.Add(self.testTxt4_2, 1, wx.EXPAND)
        sizerH4.Add(self.testTxt4_3, 1, wx.EXPAND)
        sizerH4.Add(self.testTxt4_4, 1, wx.EXPAND)


        self.tableSizerV.Add(self.panel0, 1, wx.EXPAND)
        self.tableSizerV.Add(self.panel1, 1, wx.EXPAND)
        self.tableSizerV.Add(self.panel2, 1, wx.EXPAND)
        self.tableSizerV.Add(self.panel3, 1, wx.EXPAND)
        self.tableSizerV.Add(self.panel4, 1, wx.EXPAND)



        self.testTxt1_1.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt1_1.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt1_2.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt1_2.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt1_3.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt1_3.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt1_4.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt1_4.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        
        self.testTxt2_1.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt2_1.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt2_2.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt2_2.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt2_3.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt2_3.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt2_4.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt2_4.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)

        self.testTxt3_1.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt3_1.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt3_2.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt3_2.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt3_3.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt3_3.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt3_4.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt3_4.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)

        self.testTxt4_1.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt4_1.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt4_2.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt4_2.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt4_3.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt4_3.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        self.testTxt4_4.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.testTxt4_4.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)

    def onMouseOverAx2(self, event):
        print("===================Ax2 mouse over===========")
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.midsecHeader.Fill_ax2_light(x, y, self.tags, self.depths, self.tagmarkLineList, self.depthTagList, self.depthList)
            self.Layout()
            self.Refresh()
            # print("{}, {}".format(x, y))
            
    def onMouseClickAx2(self, event):
        print("===================Ax2 mouse click===========")
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.midsecHeader.Fill_ax2_dark(x, y, self.tags, self.depths, self.tagmarkLineList, self.depthTagList, self.depthList)
            self.Layout()
            self.Refresh()
            # print("{}, {}".format(x, y))
            # print("ax: {}".format(self.ax))
            


    def onMouseClickPlt(self, event):
        print("===================plt mouse click===========")

    def onMouseOver(self, event):
        obj = event.GetEventObject().GetParent()
        obj.SetBackgroundColour('Green')
        obj.Refresh()
        event.Skip()

    def onMouseLeave(self, event):
        obj = event.GetEventObject().GetParent()
        obj.SetBackgroundColour(self.colour)
        obj.Refresh()
        event.Skip()


    def onLeftUp(self, event):
        obj = event.GetEventObject()
        tooltip = obj.GetToolTip()
        tooltip.SetTip(self.tipLbl2)
        event.Skip()

    def onRightUp(self, event):
        obj = event.GetEventObject()
        tooltip = obj.GetToolTip()
        tooltip.SetTip(self.tipLbl)
        event.Skip()

    def onLeftDown(self, event):
        obj = event.GetEventObject()
        obj.SetForegroundColour('Blue')
        obj.Refresh()
        event.Skip()

    def onRightDown(self, event):
        obj = event.GetEventObject()
        obj.SetForegroundColour('Red')
        obj.SetFont(self.font2)
        print('on right down')
        obj.Refresh()
        event.Skip()

def main():
    app = wx.App()

    frame = wx.Frame(None, size=(800, 1200))
    midPanel = MidsectionImport(frame)

    frame.Show()

    app.MainLoop()


if __name__ == "__main__":
    main()

