




import BUIx
import Raster
import MenuWidget

#import Bldb





class B_TabButton(MenuWidget.B_MenuItemTextNoFX):
  def __init__(self,Parent,MenuDescr,StackMenu):
    MenuWidget.B_MenuItemTextNoFX.__init__(self,Parent,MenuDescr,StackMenu)


  def __del__(self):
    MenuWidget.B_MenuItemTextNoFX.__del__()

  def ActivateItem(self,activate):
    #print "B_MenuItemOption.ActivateItem()"
    if activate==1:
      print "B_TabButton::ActivateItem(), Hola Caracola"
    elif activate==0:
      self.StackMenu.Pop()





class B_TabWidget(BUIx.B_FrameWidget):
  def __init__(self,Parent,Menudesc,StackMenu):
    print "B_TabWidget __init__()"
    #Bldb.set_trace()
    Width,Height=Raster.GetSize()
    try:
      Width,Height=Menudesc["Size"]
    except:
      pass

    BUIx.B_FrameWidget.__init__(self,Parent,"TabWidget"+Menudesc["Name"],Width,Height)
    print "About to create self.TabButtons"
    self.TabButtons=MenuWidget.B_MenuFrameWidget(self,"TabButtons"+Menudesc["Name"],150,Height)
    self.AddWidget(self.TabButtons,
                   0,0,
                   BUIx.B_Widget.B_FR_AbsoluteRight,BUIx.B_Widget.B_FR_Right,
                   BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top)

    print "About to create self.TabClient"
    self.TabClient=BUIx.B_FrameWidget(self,"TabClient"+Menudesc["Name"],Width-150,Height)
    self.AddWidget(self.TabClient,
                   0,0,
                   BUIx.B_Widget.B_FR_AbsoluteLeft,BUIx.B_Widget.B_FR_Left,
                   BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top)

    print "About to create Tabs"
    for i in Menudesc["ListDescr"]:
      print i
      wTab=B_TabButton(self,i,StackMenu)
      self.AddTab(wTab)

    print "B_TabWidget End __init__()"



  def __AddButton(self,but_name):
    Descr_tmp={"Name":but_name}
    #Bldb.set_trace()
    menu_element=B_TabButton(self,Descr_tmp,None)

    self.TabButtons.AddMenuElement(menu_element)



  def __AddClient(self,but):
    menu_element=B_MenuItemText(self,Descr_tmp,None)
    self.TabButtons.AddMenuElement(menu_element)


  def AddTab(self,tab): #Tab es un B_FrameWidget
    name=tab.Name()
    print "B_TabWidget::AddTab()",name,type(name)
    self.__AddButton(name[:10])
    #self.__AddClient()

  def GetFocus(self):
    return self.TabButtons.GetFocus()

  def NextFocus(self):
     self.TabButtons.NextFocus()

  def PrevFocus(self):
     self.TabButtons.PrevFocus()




