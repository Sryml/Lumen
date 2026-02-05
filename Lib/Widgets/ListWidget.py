#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#
# Change list:
# * Refactor text UI
# * Refactor ListWidget
#


import Raster
import BUIx
import MenuWidget
import ScorerWidgets
import pdb
import Language

from Lumenx import printx

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None

# Caracter flecha arriba: 189
# Caracter flecha abajo: 190


class B_ListWidget(MenuWidget.B_MenuTree):
    def __init__(self, Parent, Menudesc, StackMenu, VertPos=0):
        self.FocusCallBack = Menudesc.get("FocusCallBack")

        self.WidgetsVPos = []
        self.WidgetsHeights = []
        self.MaxItems = 0
        self.VertScroll = 0

        MenuWidget.B_MenuTree.__init__(self, Parent, Menudesc, StackMenu, VertPos)
        self.SetAutoScale(0)
        self.SetClipDraw(1)
        
        self.nElements = len(self.MenuItems)
        self.ListSize = self.VertPos
        # self.Position = 0
        # self.ListItems = []

        # for i in Menudesc["ListDescr"]:
        #     m_class = i.get("Kind", MenuWidget.B_MenuItemTextNoFX)
        #     vsep = i.get("VSep", 0)

        #     wSubMenu = m_class(self, i, StackMenu)
        #     self.AddMenuElement(wSubMenu, vsep)
        # self.nElements = len(self.MenuItems)

        # self.SetFocus_Idx(1)
        ArrowHPos = Menudesc.get("ArrowHPos", 0.066)
        Scale = Menudesc.get("FontScale", Language.MFontScale["L"])

        self.UpArrow = BUIx.B_TextWidget(
            self,
            "UpArrow",
            Language.UpArrow,
            ScorerWidgets.font_server,
            Language.FontTitle,
        )
        self.UpArrow.SetScale(Scale)
        self.UpArrow.SetColor(207, 144, 49)
        self.UpArrow.SetAlpha(0.4)
        self.AddWidget(
            self.UpArrow,
            ArrowHPos,
            0,
            BUIx.B_FrameWidget.B_FR_HRelative,
            BUIx.B_FrameWidget.B_FR_Left,
            BUIx.B_FrameWidget.B_FR_AbsoluteTop,
            BUIx.B_FrameWidget.B_FR_Top,
        )

        self.DownArrow = BUIx.B_TextWidget(
            self,
            "DownArrow",
            Language.DownArrow,
            ScorerWidgets.font_server,
            Language.FontTitle,
        )
        self.DownArrow.SetScale(Scale)
        self.DownArrow.SetColor(207, 144, 49)
        self.DownArrow.SetAlpha(0.4)
        self.AddWidget(
            self.DownArrow,
            ArrowHPos,
            0,
            BUIx.B_FrameWidget.B_FR_HRelative,
            BUIx.B_FrameWidget.B_FR_Left,
            BUIx.B_FrameWidget.B_FR_AbsoluteBottom,
            BUIx.B_FrameWidget.B_FR_Bottom,
        )

        self.AdjustScrollArrows()

    # def __del__(self):
    ##    print "B_ListWidget.__del__()",self.Name()
    # for i in self.MenuItems:
    #     i.SetDrawFunc(None)

    # MenuWidget.B_MenuFocusManager.__del__(self)
    # BUIx.B_FrameWidget.__del__(self)

    def __str__(self):
        printx("B_ListWidget", self.Name())

    def AdjustScrollArrows(self):
        if self.VertScroll < 0:
            self.UpArrow.SetAlpha(1)
        else:
            self.UpArrow.SetAlpha(0.4)

        w, h = self.GetSize()
        if self.ListSize + self.VertScroll > h:
            self.DownArrow.SetAlpha(1)
        else:
            self.DownArrow.SetAlpha(0.4)

    def AddMenuElement(
        self,
        menu_element,
        vsep=0,
        HPos=0.5,
        HIndicator=BUIx.B_FrameWidget.B_FR_HRelative,
        HAnchor=BUIx.B_FrameWidget.B_FR_HCenter,
        VIndicator=BUIx.B_FrameWidget.B_FR_AbsoluteTop,
    ):
        self.WidgetsVPos.append(self.VertPos)
        MenuWidget.B_MenuFrameWidget.AddMenuElement(
            self, menu_element, vsep, HPos, HIndicator, HAnchor, VIndicator
        )
        widget_height = menu_element.GetSize()[1] * self.ViewScale
        self.WidgetsHeights.append(widget_height)
        if self.MaxItems == 0 and self.VertPos >= self.GetSize()[1]:
            self.MaxItems = len(self.MenuItems) - 1

    def AddMenuElement2(
        self,
        widget,
        sep=0,
        HPos=0.5,
        HIndicator=BUIx.B_FrameWidget.B_FR_HRelative,
        HAnchor=BUIx.B_FrameWidget.B_FR_HCenter,
    ):
        MenuWidget.B_MenuFocusManager.AddMenuElement(self, widget)
        self.AddWidget(
            widget,
            117,
            self.ListSize,
            BUIx.B_FrameWidget.B_FR_AbsoluteLeft,
            BUIx.B_FrameWidget.B_FR_Left,
            BUIx.B_FrameWidget.B_FR_AbsoluteTop,
            BUIx.B_FrameWidget.B_FR_Top,
        )
        self.WidgetsVPos.append(self.ListSize)
        widget_height = widget.GetSize()[1]
        self.WidgetsHeights.append(widget_height)
        self.ListSize = self.ListSize + widget_height
        if self.MaxItems == 0 and self.ListSize >= self.GetSize()[1]:
            self.MaxItems = len(self.WidgetsHeights) - 1
            # print "MaxItems:", self.MaxItems
        #  self.DoScroll(-1*widget_height)
        #  print "Calling ScrollUp(): ListSize=",self.ListSize,"widget_height=",widget_height
        # self.SetFocus(widget) #
        # self.AdjustScrollArrows()  #No Funciona (?)

    def NextFocus(self):
        # curr_focus=self.GetFocus()
        # index=self.MenuItems.index(curr_focus)
        # if index>=len(self.MenuItems)-1:
        #   self.AdjustScrollArrows()
        #   return

        MenuWidget.B_MenuFocusManager.NextFocus(self)
        wFoc = self.GetFocus()
        i = self.MenuItems.index(wFoc)
        #
        if self.nElements > self.MaxItems and i == 0:
            self.DoScroll2(0)
        #
        elif (
            self.WidgetsVPos[i] + self.WidgetsHeights[i] + self.VertScroll
            >= self.GetSize()[1]
        ):
            self.DoScroll(-self.WidgetsHeights[i])
        self.AdjustScrollArrows()

    def PrevFocus(self):
        # curr_focus=self.GetFocus()
        # index=self.MenuItems.index(curr_focus)
        # if index<=0:
        #   self.AdjustScrollArrows()
        #   return

        MenuWidget.B_MenuFocusManager.PrevFocus(self)
        wFoc = self.GetFocus()
        i = self.MenuItems.index(wFoc)
        # print self.WidgetsVPos[i]+ self.WidgetsHeights[i] +self.VertPos ,self.GetSize()[1]
        #
        if self.nElements > self.MaxItems and i == (self.nElements - 1):
            self.DoScroll2(-reduce(lambda x, y: x + y, self.WidgetsHeights[self.MaxItems :], 0))  # type: ignore
        #
        elif self.WidgetsVPos[i] + self.WidgetsHeights[i] + self.VertScroll <= 0:
            self.DoScroll(self.WidgetsHeights[i])
        self.AdjustScrollArrows()

    def RemoveWidget(self, widget):
        printx("B_ListWidget::RemoveWidget() not implemented.")
        pass

    def DoScroll(self, amount):
        for i in range(
            self.nElements
        ):  # Me salto los dos �ltimos widgets, son las flechas
            self.MoveWidgetRel_Idx(i, 0, amount)
        self.VertScroll = self.VertScroll + amount

    def DoScroll2(self, amount):
        for i in range(self.nElements):
            self.MoveWidgetTo_Idx(
                i,
                self.GetWidgetPosition(self.MenuItems[i].Name())[1],
                self.WidgetsVPos[i] + amount,
            )
        self.VertScroll = amount

    def GetTopIndex(self):
        pass

    def SetTopIndex(self, index):
        pass

    def EnsureVisible(self, index):
        pass

    def AcceptsFocus(self):
        return len(self.MenuItems) != 0


##  def Draw(self,x,y,time):
##    if self.GetVisible()==0:
##      return
##
##    #print "MenuItemText",self.Name()
##    foc=self.GetHasFocus()
##    if foc:
##      self.SetBorderColor(220,220,220)
##    else:
##      self.SetBorderColor(220,10,10)
##
##    self.DefDraw(x,y,time)
