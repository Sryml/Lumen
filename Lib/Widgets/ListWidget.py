


import Raster
import BUIx
import MenuWidget
import ScorerWidgets
import pdb
import Language



# Caracter flecha arriba: 189
# Caracter flecha abajo: 190

class B_ListWidget(MenuWidget.B_MenuFocusManager,BUIx.B_FrameWidget):
  def __init__(self,Parent,Menudesc,StackMenu,VertPos=0):

    width,height=Raster.GetSize()
    try:
      width,height=Menudesc["Size"]
      #print Menudesc["Size"]
    except:
      pass

    MenuWidget.B_MenuFocusManager.__init__(self)
    BUIx.B_FrameWidget.__init__(self,Parent,"List"+Menudesc["Name"],width,height)
    self.nElements=0
    self.Position=0
    self.ListItems=[]
    self.VertPos=0
    self.ListSize=0
    self.WidgetsVPos=[]
    self.WidgetsHeights=[]
    self.SetClipDraw(1)

    for i in Menudesc["ListDescr"]:
      m_class=MenuWidget.B_MenuItemTextNoFX
      try:
        m_class=i["Kind"]
      except:
        pass

      vsep=0
      try:
        vsep=i["VSep"]
      except:
        pass

      wSubMenu=m_class(self,i,StackMenu)
      self.AddMenuElement(wSubMenu, vsep)

    self.SetFocus_Idx(1)

    self.UpArrow=BUIx.B_TextWidget(self,"UpArrow",chr(189),ScorerWidgets.font_server,Language.LetrasMenu)
    self.AddWidget(self.UpArrow,50,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                                    BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    self.UpArrow.SetColor(207,144,49)
    self.UpArrow.SetAlpha(0.5)


    self.DownArrow=BUIx.B_TextWidget(self,"DownArrow",chr(190),ScorerWidgets.font_server,Language.LetrasMenu)
    self.AddWidget(self.DownArrow,50,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                                      BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
    self.DownArrow.SetColor(207,144,49)
    self.DownArrow.SetAlpha(0.5)



  def __del__(self):
##    print "B_ListWidget.__del__()",self.Name()
    for i in self.MenuItems:
      i.SetDrawFunc(None)

    MenuWidget.B_MenuFocusManager.__del__(self)
    BUIx.B_FrameWidget.__del__(self)


  def __str__(self):
    print "B_ListWidget",self.Name()


  def AdjustScrollArrows(self):
    if self.VertPos<0:
      self.UpArrow.SetAlpha(1)
    else:
      self.UpArrow.SetAlpha(0.4)

    w,h=self.GetSize()
    if self.ListSize+self.VertPos>h:
      self.DownArrow.SetAlpha(1)
    else:
      self.DownArrow.SetAlpha(0.4)


  def AddMenuElement(self,widget,sep=0,
                     HPos=0.5,HIndicator=BUIx.B_FrameWidget.B_FR_HRelative,HAnchor=BUIx.B_FrameWidget.B_FR_HCenter):
    MenuWidget.B_MenuFocusManager.AddMenuElement(self,widget)
    self.AddWidget(widget,117,self.ListSize,
                   BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    self.WidgetsVPos.append(self.ListSize)
    widget_height=widget.GetSize()[1]
    self.WidgetsHeights.append(widget_height)
    self.ListSize=self.ListSize+widget_height
    #if self.ListSize>self.GetSize()[1]:
    #  self.DoScroll(-1*widget_height)
    #  print "Calling ScrollUp(): ListSize=",self.ListSize,"widget_height=",widget_height
    self.SetFocus(widget.Name())
    #self.AdjustScrollArrows()  #No Funciona (?)


  def NextFocus(self):
    curr_focus=self.GetFocus()
    index=self.MenuItems.index(curr_focus)
    if index>=len(self.MenuItems)-1:
      self.AdjustScrollArrows()
      return

    MenuWidget.B_MenuFocusManager.NextFocus(self)
    wFoc=self.GetFocus()
    i=self.MenuItems.index(wFoc)
    if self.WidgetsVPos[i]+ self.WidgetsHeights[i] +self.VertPos >= self.GetSize()[1]:
      self.DoScroll(-self.WidgetsHeights[i])
    self.AdjustScrollArrows()


  def PrevFocus(self):
    curr_focus=self.GetFocus()
    index=self.MenuItems.index(curr_focus)
    if index<=0:
      self.AdjustScrollArrows()
      return

    MenuWidget.B_MenuFocusManager.PrevFocus(self)
    wFoc=self.GetFocus()
    i=self.MenuItems.index(wFoc)
    #print self.WidgetsVPos[i]+ self.WidgetsHeights[i] +self.VertPos ,self.GetSize()[1]
    if self.WidgetsVPos[i]+ self.WidgetsHeights[i]  +self.VertPos<=0:
      self.DoScroll(self.WidgetsHeights[i])
    self.AdjustScrollArrows()


  def RemoveWidget(self,widget):
    print "B_ListWidget::RemoveWidget() not implemented."
    pass


  def DoScroll(self,amount):
    for i in range(self.nWidgets()-2): # Me salto los dos �ltimos widgets, son las flechas
      self.MoveWidgetRel_Idx(i,0,amount)
    self.VertPos=self.VertPos+amount



  def GetTopIndex(self):
    pass

  def SetTopIndex(self,index):
    pass

  def EnsureVisible(self,index):
    pass

  def AcceptsFocus(self):
    if len(self.MenuItems) <= 1:
      return 0
    else:
      return 1


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
