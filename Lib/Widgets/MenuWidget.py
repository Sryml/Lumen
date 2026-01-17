#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#
# Change list:
# * Refactor text UI
#

import Lumenx
import BUIx
import Bladex
import Raster
import ScorerWidgets
import WidgetsExtra
import SpinWidget
import TextFXWidget
import pdb
#import Bldb
import BInput
#import IDebug
import BBLib
import MenuText
import sys
import string
import Language
import os
import Menu
import GameText
import traceback
import types

import netgame
import PanelFillerCommon
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition

# by Sryml
from Lumenx import printx

B_FrameWidget = BUIx.B_FrameWidget
B_TextWidget = BUIx.B_TextWidget
FontColor = Language.FontColor
#

#if netgame.GetNetState()==0:
#  import Scorer
global isQuitting
isQuitting = 0

NoteOptionY = 1 - 0.24
BackButtonY = 1 - 0.208 # 100
BackGamepadButtonY = 1 - 0.146 # 70
AcceptBackY = 1 - 0.083 # 40

class Stack:
  def __init__(self):
    #print "Stack.__init__()"
    self.Items=[]

  def __del__(self):
    #print "Stack.__del__()"
    pass

  def nItems(self):
    return len(self.Items)

  def Push(self,item):
    self.Items.append(item)

  def Pop(self):
    self.Items=self.Items[:-1]

  def Top(self):
    try:
      return self.Items[-1]
    except:
      return None

  def Reset(self):
    self.Items=[]




class MenuStack(Stack):
  def __init__(self,final_callback):
    Stack.__init__(self)
    self.FinalCallBack=final_callback

  def Push(self,menu_item):
    #print "MenuStack Pushing",menu_item,"with refcount",sys.getrefcount(menu_item)
    s=self.Top()
    if not s:
      Bladex.SetAppMode("Menu")
    Bladex.SetRootWidget(menu_item.GetPointer())
    Stack.Push(self,menu_item)
    menu_item.Menudesc.get("OnEnter", lambda x: 0)(menu_item) # by Sryml
    #print "RefCount (pushed)",sys.getrefcount(menu_item)

  def Pop(self):
    if isQuitting:
      Bladex.Quit()
    #print "MenuStack.Popping",self.Top(),"with refcount",sys.getrefcount(self.Top())
    # by Sryml
    s=self.Top()
    if s:
      s.Menudesc.get("OnLeave", lambda x: 0)(s)
    #
    Stack.Pop(self)
    s=self.Top()
    if s:
      Bladex.SetRootWidget(s.GetPointer())
    else:
      #print "Final CallBack"
      self.FinalCallBack()



class B_MenuFocusManager:
  def __init__(self):
    #print "B_MenuFocusManager.__init__()"
    self.MenuItems=[]
    self.Focus=None # Voy a llevar el foco aqu� en vez de dejarselo al C.

  def __del__(self):
    #print "B_MenuFocusManager.__del__()"
    self.Focus=None
    self.MenuItems=[]

  def AddMenuElement(self,menu_element):
    #print "B_MenuFocusManager.AddMenuElement()  (init)->",menu_element, sys.getrefcount(self)
    self.MenuItems.append(menu_element)
    self.Focus=menu_element
    #print "B_MenuFocusManager.AddMenuElement()  (end)->", sys.getrefcount(self)


  def GetFocus(self):
    return self.Focus


  def SetFocus(self,menu_element):
    accepts_focus=0
    try:
      accepts_focus=menu_element.AcceptsFocus()
    except:
      pass

    if accepts_focus==1:
      old_foc=self.GetFocus()
      if menu_element==old_foc:
        return 1
      if old_foc:
        old_foc.SetHasFocus(0)
      menu_element.SetHasFocus(1)
      self.Focus=menu_element
      return 1

    return 0



  def SetFocus_Idx(self,menu_element_idx):
    try:
      menu_element=self.MenuItems[menu_element_idx]
      self.SetFocus(menu_element)
      if menu_element.FocusCallBack:
        menu_element.FocusCallBack(menu_element) # Added by Sryml
    except:
      print "Error setting focus to index",menu_element_idx



  def NextFocus(self):
    try:
      old_focus=self.GetFocus()
      index=self.MenuItems.index(old_focus)
      list=self.MenuItems[index+1:]+self.MenuItems[:index]
      for i in list:
        if self.SetFocus(i):
          if i.FocusCallBack: # by Sryml
            i.FocusCallBack(i)
          return
    except:
      print "B_MenuFocusManager::NextFocus() -> Exception ocurred."
      pass



  def PrevFocus(self):
    try:
      old_focus=self.GetFocus()
      index=self.MenuItems.index(old_focus)

      l1=self.MenuItems[:index]
      l2=self.MenuItems[index+1:]
      l1.reverse()
      l2.reverse()
      list=l1+l2

      for i in list:
        if self.SetFocus(i):
          if i.FocusCallBack: # by Sryml
            i.FocusCallBack(i)
          return

    except:
      print "B_MenuFocusManager::PrevFocus() -> Exception ocurred."
      pass

  def FinalRelease(self):
##    print "B_MenuFocusManager.FinalRelease()"
    for i in self.MenuItems:
      try:
        i.FinalRelease()
      except:
        pass



# -----------------------------------------
# by Sryml: start
# -----------------------------------------
class B_MenuFrameWidget(B_MenuFocusManager, B_FrameWidget):
    def __init__(self, Parent, Name, Width, Height, VertPos=0):
        B_FrameWidget.__init__(self, Parent, Name, Width, Height)
        B_MenuFocusManager.__init__(self)
        self.VertPos = VertPos
        self.thisown = 1
        self.SetAutoScale(1)

    def __del__(self):
        for i in self.MenuItems:
            i.SetDrawFunc(None)

        B_FrameWidget.__del__(self)
        B_MenuFocusManager.__del__(self)

    def AddMenuElement(
        self,
        menu_element,
        sep=0,
        HPos=0.5,
        HIndicator=B_FrameWidget.B_FR_HRelative,
        HAnchor=B_FrameWidget.B_FR_HCenter,
        VIndicator=B_FrameWidget.B_FR_AbsoluteTop,
    ):
        B_MenuFocusManager.AddMenuElement(self, menu_element)

        if Lumenx.GetGameVersion() == Lumenx.CLASSIC_VER:
            self.AddWidget(  # type: ignore
                menu_element,
                HPos,
                self.VertPos + sep,
                HIndicator,
                HAnchor,
                VIndicator,
                B_FrameWidget.B_FR_Top,
            )
        else:
            if sep in (Menu.BackOptionVSep, Menu.BackGamepadOptionVSep, Menu.GamepadButtonVSep, Menu.NoteOptionVSep):
                YPos = BackButtonY
                if sep == Menu.BackGamepadOptionVSep:
                    YPos = BackGamepadButtonY
                elif sep == Menu.GamepadButtonVSep:
                    YPos = AcceptBackY
                    menu_element.SetScale(0.7)
                elif sep == Menu.NoteOptionVSep:
                    YPos = NoteOptionY
                self.AddWidget(  # type: ignore
                    menu_element,
                    HPos,
                    YPos,
                    HIndicator,
                    HAnchor,
                    B_FrameWidget.B_FR_VRelative,
                    B_FrameWidget.B_FR_Top,
                )
            else:
                self.AddWidget(  # type: ignore
                    menu_element,
                    HPos,
                    self.VertPos + sep,
                    HIndicator,
                    HAnchor,
                    B_FrameWidget.B_FR_AbsoluteTop,
                    B_FrameWidget.B_FR_Top,
                )

        self.VertPos = self.VertPos + menu_element.GetSize()[1] + sep
# -----------------------------------------
# by Sryml: end
# -----------------------------------------


# MenuDescr es un diccionario con los siguientes campos para describir el men�:
# "Name",            Nombre del men�.
# "Kind",            Clase de elemento, es una clase. Si no existe se usa B_MenuItemText.
# "FrameKind",       Clase del marco del elemento, es una clase. Si no existe se usa B_MenuTree.
# "ListDescr",       Lista de MenuDesc, puede no existir.
# "Command",         Si ListDscr est� vac�a o no existe, trata de ejecutar este.
# "VSep",            Separaci�n con el elemento anterior, si es el primero es el margen vertical.
# "Font",            Fuente para el elemento.
# "Options",         Lista de opciones para un elemento de tipo B_MenuItemOption.
# "SelOptionFunc",   Llama a esta funci�n para saber la opci�n seleccionada para un elemento
#                    de tipo B_MenuItemOption. Tiene que devolver una de las opciones de Options.
#                    Si no existe esta funci�n, toma la primera.
# "Actions",         Lista para las acciones que se pueden definir en la p�gina de teclado.
# "Position",        Lista que indica c�mo colocar los men�s.
# "PositionEx",      Lista que indica c�mo colocar los men�s, ampliaci�n.
# "Size",            Lista con el ancho y el alto.
# "BackGround",      Imagen de fondo.
# "PageDscrs",       Lista de Descripci�n de p�ginas.
# "PageDscr",        Descripci�n de p�ginas, es una diccionario con los siguientes campos:
#                    "PrevLabel",   Etiqueta a la p�gina anterior.
#                    "NextLabel",   Etiqueta a la p�gina siguiente.
#                    "Title",       T�tulo de la p�gina. (Obligatorio).
# "SpinValues",      Tupla con tres valores para configurar un SpinWidget: inferior, superior, pasos.
# "SpinGetValue"     Funci�n que le dice al SpinWidget c�mo obtener su valor inicial.
# "SpinSetValueEnd"  Funci�n que llama un SpinWidget al salir de contexto.
# "SpinOnChange"     Funci�n que llama un SpinWidget al cambiarse el valor

class B_MenuTreeItem:
  def __init__(self,MenuDescr,StackMenu):
    #print "MenuTreeItem.__init__()"
    self.SetAlpha(0.5)
    self.StackMenu=StackMenu
    self.MenuDescr=MenuDescr
    self.FocusCallBack = MenuDescr.get("FocusCallBack") # by Sryml

  def __del__(self):
    #print "MenuTreeItem.__del__()"
    pass

  def __str__(self):
    print "B_MenuTreeItem widget with descriptor",self.MenuDescr

  def IncMenuItem(self):
      try:
        command=self.MenuDescr["LeftCommand"]
        command(self)
      except KeyError:
        pass


  def DecMenuItem(self):
      try:
        command=self.MenuDescr["RightCommand"]
        command(self)
      except KeyError:
        pass

  def ActivateItem(self,activate):
    if activate==1:
      NewFrame=self.CreateFrame()
      if NewFrame:
        self.StackMenu.Push(NewFrame)
        return 1
      else:
        try:
          command=self.MenuDescr["Command"]
          command(self)
          return 1
        except:
          return 0
    elif activate==0:
      w=self.StackMenu.Top()
      try:
        w.FinalRelease()
      except:
        pass
      self.StackMenu.Pop()
      #del(w)


  def CreateFrame(self):
      # by Sryml
      l_dscr = self.MenuDescr.get("ListDescr", [])
      if l_dscr == []:
          # printx("l_dscr == []")
          return None

      frame_class = self.MenuDescr.get("FrameKind", B_MenuTree)
      try:
          return frame_class(self, self.MenuDescr, self.StackMenu)
      except:
          printx("Error Creating frame of class", frame_class)
          traceback.print_exc()
      #




# -----------------------------------------
# by Sryml: start
# -----------------------------------------
class B_MenuTree(B_MenuFrameWidget):
    def __init__(self, Parent, Menudesc, StackMenu, VertPos=0):
        vw, vh = Raster.GetSize()
        Width, Height = Menudesc.get("Size", (vw, vh))

        SizeFor = Menudesc.get("SizeFor")
        if Width == "auto" and Height != "auto":
            if not SizeFor or Lumenx.GetGameVersion() in SizeFor:
                ratio = vh / float(vw)
                Width = int(Height / ratio)
                Width = Width % 2 and Width + 1 or Width
            else:
                Width, Height = vw, vh
        elif Width != "auto" and Height == "auto":
            if not SizeFor or Lumenx.GetGameVersion() in SizeFor:
                ratio = vw / float(vh)
                Height = int(Width / ratio)
                Height = Height % 2 and Height + 1 or Height
            else:
                Width, Height = vw, vh
        elif Width == "auto" and Height == "auto":
            Width, Height = vw, vh

        B_MenuFrameWidget.__init__(
            self, Parent, "MenuTree" + Menudesc["Name"], Width, Height, VertPos  # type: ignore
        )

        self.Menudesc = Menudesc

        ValidIndex = 0
        isValidIndex = 0
        for i in Menudesc["ListDescr"]:
            m_class = i.get("Kind", B_MenuItemTextNoFX)
            wSubMenu = m_class(self, i, StackMenu)
            if not isValidIndex:
                if wSubMenu.AcceptsFocus():
                    isValidIndex = 1
                else:
                    ValidIndex = ValidIndex + 1

            vsep = i.get("VSep", 0)
            if type(vsep) == types.StringType:
              try:
                if vsep[-1] == "%":
                  vsep = int(float(vsep[:-1]) * Height) # type: ignore
                elif vsep[-2:] == "em":
                  vsep = int(wSubMenu.GetSize()[1] * float(vsep[:-2]))
                else:
                  printx("Invalid VSep value:", vsep)
                  vsep = 0
              except:
                vsep = 0
                traceback.print_exc()

            HPos = 0.5
            HIndicator = B_FrameWidget.B_FR_HRelative
            HAnchor = B_FrameWidget.B_FR_HCenter
            VIndicator = i.get("VIndicator", B_FrameWidget.B_FR_AbsoluteTop)

            PosDscr = i.get("Position", i.get("PositionEx"))
            if PosDscr:
                HPos = PosDscr[0]
                HIndicator = PosDscr[1]
                HAnchor = PosDscr[2]

            B_MenuFrameWidget.AddMenuElement(
                self, wSubMenu, vsep, HPos, HIndicator, HAnchor, VIndicator
            )

        if Menudesc.has_key("iFocus"):
            self.SetFocus_Idx(Menudesc["iFocus"])
        else:
            self.SetFocus_Idx(ValidIndex)

    def __del__(self):
        # print "B_MenuTree.__del__()"
        B_MenuFrameWidget.__del__(self)

    def __str__(self):
        printx("B_MenuTree widget with Frame", self.Name())


class B_MenuItemTextNoFX(B_TextWidget, B_MenuTreeItem):
    def __init__(
        self, Parent, MenuDescr, StackMenu, font_server=ScorerWidgets.font_server
    ):
        self.Focusable = MenuDescr.get("Focusable", 1)
        self.Text = MenuDescr.get("Text", MenuDescr["Name"])
        self.Color = MenuDescr.get("Color", None)
        self.Alpha = MenuDescr.get("Alpha", 1.0)

        Font = MenuDescr.get("Font", Language.FontCommon)
        isVisible = MenuDescr.get("Visible", 1)
        Scale = MenuDescr.get("FontScale", Language.MFontScale["L"])

        B_TextWidget.__init__(
            self, Parent, "SubMenu" + MenuDescr["Name"], self.Text, font_server, Font
        )
        self.SetCanvas(Parent.GetSize())
        B_MenuTreeItem.__init__(self, MenuDescr, StackMenu)  # type: ignore

        self.Parent = Parent

        self.SetAlpha(self.Alpha)
        self.SetVisible(isVisible)
        self.SetScale(Scale)
        MenuDescr.get("PostInitCommand", lambda x: 0)(self)

        self.SetDrawFunc(self.Draw)

    def __str__(self):
        printx("B_MenuItemTextNoFX widget with text", self.GetTextData())

    def Draw(self, x, y, time):
        if self.GetVisible() == 0:
            return

        if self.Color:
            r, g, b = self.Color
        else:
            foc = self.GetHasFocus()
            if foc:
                r, g, b = FontColor.Focused
            elif not self.Focusable:
                r, g, b = FontColor.Unfocusable
            else:
                r, g, b = FontColor.Unfocused

        a = self.Alpha

        if self.GetColor() != (r, g, b):
            self.SetColor(r, g, b)
        if self.GetAlpha() != a:
            self.SetAlpha(a)

        if self.GetTextData() != self.Text:
            self.SetText(self.Text)
            if self.ScaleFrame:
                self.ScaleFrame.RecalcLayout()
            else:
                self.Parent.RecalcLayout()
        else:
            self.DefDraw(x, y, time)

    def ActivateItem(self, activate):
        if activate == 1:
            if not self.AcceptsFocus():
                return 0
            self.MenuDescr.get("Command", lambda x: 0)(self)
            NewFrame = self.CreateFrame()
            if NewFrame:
                self.StackMenu.Push(NewFrame)
            return 1
            # else:
                # command = self.MenuDescr.get("Command")
                # if command:
                #     command(self)
                #     return 1
                # return 0
        elif activate == 0:
            w = self.StackMenu.Top()
            try:
                w.FinalRelease()
            except:
                pass
            self.StackMenu.Pop()

    def AcceptsFocus(self):
        if self.GetVisible() == 0:
            return 0
        return self.Focusable

    def FinalRelease(self):
        self.Parent = None

class B_MenuItemTextNoFXNoFocus(B_MenuItemTextNoFX):
  def __init__(
      self, Parent, MenuDescr, StackMenu, font_server=ScorerWidgets.font_server
  ):
      B_MenuItemTextNoFX.__init__(self, Parent, MenuDescr, StackMenu)
      self.Focusable = 0

  def AcceptsFocus(self):
    return 0

class B_MenuItemOption(B_MenuItemTextNoFX):
    def __init__(
        self, Parent, MenuDescr, StackMenu, font_server=ScorerWidgets.font_server
    ):
        self.Options = MenuDescr.get("Options")
        if not self.Options:
            self.Options = ["No option defined"]

        SelOption = MenuDescr.get("SelOptionFunc")
        if SelOption is not None:
          self.SelOption = SelOption()
        else:
          SelOption = MenuDescr.get("SelOptionFunc2", lambda x: 0)
          self.SelOption = SelOption(self)

        B_MenuItemTextNoFX.__init__(self, Parent, MenuDescr, StackMenu)

        self.OptionText = self.Text
        self.Text = self.OptionText + " < " + MenuText.GetMenuText(self.Options[self.SelOption]) + " >"

    def __del__(self):
        pass
        # printx("B_MenuItemOption.__del__()",self.Name())

    def ActivateItem(self, activate):
        check_pass = None
        val = 1
        if self.MenuDescr.has_key("CheckPass"):
            check_pass = self.MenuDescr["CheckPass"]
            val = check_pass()

        if activate in (1, -1) and (val == 1):
          self.SelOption = self.SelOption + activate
          self.SelOption = self.SelOption % len(self.Options)

          self.Text = self.OptionText + " < " + MenuText.GetMenuText(self.Options[self.SelOption]) + " >"

          command = self.MenuDescr.get("Command", None)
          if command:
            command(self.Options[self.SelOption])
          command = self.MenuDescr.get("Command2", None)
          if command:
            command(self.Options[self.SelOption], self)

        elif activate == 0:
          self.StackMenu.Pop()

    def IncMenuItem(self):
        self.ActivateItem(1)

    def DecMenuItem(self):
        self.ActivateItem(-1)

    def SetSelOption(self, option):
      self.SelOption=option
      self.Text = self.OptionText + " < " + MenuText.GetMenuText(self.Options[self.SelOption]) + " >"


class B_MenuSpin(SpinWidget.B_SpinWidget,B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu,font_server=ScorerWidgets.font_server):
    w,h = MenuDescr.get("Size",(300,19))
    defaultValue = MenuDescr.get("DefaultValue", -1)

    self.Focusable = MenuDescr.get("Focusable", 1)
    self.Text = MenuDescr.get("Text", MenuDescr["Name"])
    self.Color = MenuDescr.get("Color", None)
    self.Alpha = MenuDescr.get("Alpha", 1.0)

    Font = MenuDescr.get("Font", Language.FontCommon)
    isVisible = MenuDescr.get("Visible", 1)
    Scale = MenuDescr.get("FontScale", Language.MFontScale["L"])

    SpinWidget.B_SpinWidget.__init__(self,Parent,self.Text,w,h,font_server,Font,defaultValue)
    B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)

    # self.SetAlpha(self.Alpha) # B_FrameWidget do not work
    self.SetVisible(isVisible)

    self.WText.SetScale(Scale)
    self.DefaultText.SetScale(Scale)
    self.Spin.Text.SetScale(Scale)
    self.Spin.LeftArrow.SetScale(Scale)
    self.Spin.RightArrow.SetScale(Scale)
    self.RecalcLayout()
    self.Spin.RecalcLayout()

    try:
      l,u,s=MenuDescr["SpinValues"]
      SpinWidget.B_SpinWidget.SetLimits(self,l,u)
      SpinWidget.B_SpinWidget.SetSteps(self,s)
    except KeyError:
      pass

    try:
      self.SetValueEnd=MenuDescr["SpinSetValueEnd"]
    except KeyError:
      self.SetValueEnd=None

    if MenuDescr.has_key("SpinOnChange"):
        self.SpinOnChange = MenuDescr["SpinOnChange"]
    else:
        self.SpinOnChange = None

    try:
      val_func=MenuDescr["SpinGetValue"]
      val=val_func()
      SpinWidget.B_SpinWidget.SetValue(self,val)
    except KeyError:
      pass


  def IncMenuItem(self):
    self.IncrementValue()
    value = self.GetValue()
    if self.SpinOnChange:
       self.SpinOnChange(value)


  def DecMenuItem(self):
    self.DecrementValue()
    value = self.GetValue()
    if self.SpinOnChange:
       self.SpinOnChange(value)


  def FinalRelease(self):
    if self.SetValueEnd is not None:
      self.SetValueEnd(self.GetValue())

  def AcceptsFocus(self):
      if self.GetVisible() == 0:
          return 0
      return self.Focusable

class B_MenuItemText(TextFXWidget.B_TextFXWidget,B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu,font_server=ScorerWidgets.font_server):
    #print "B_MenuItemText.__init__()",MenuDescr["Name"]
    Font = MenuDescr.get("Font", Language.FontCommon)
    Scale = MenuDescr.get("FontScale", Language.MFontScale["L"])

    TextFXWidget.B_TextFXWidget.__init__(self,Parent,"SubMenu"+MenuDescr["Name"],MenuDescr["Name"],font_server,Font)
    B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)

    self.SetScale(Scale)

  def __del__(self):
##    print "B_MenuItemText.__del__()",self.Name()
    TextFXWidget.B_TextFXWidget.__del__(self)
    B_MenuTreeItem.__del__(self)

  def __str__(self):
    print "B_MenuItemText widget with text",self.GetTextData()

# -----------------------------------------
# by Sryml: end
# -----------------------------------------

#if Bladex.GetMapType() > 0:
#  class B_VariableFocusTextMenuItem(B_MenuItemText):
#    def AcceptsFocus(self):
#      return 0
#else:
#  class B_VariableFocusTextMenuItem(B_MenuItemText):
#    def __str__(self):
#      print "B_MenuItemText widget with text",self.GetTextData()



class B_MenuItemTextNoFocus(B_MenuItemText):
  def AcceptsFocus(self):
    return 0





class B_MenuItemPage(B_MenuFrameWidget):
  def __init__(self,Parent,PageDscr,MenuDescr,StackMenu):
    #print "Creating B_MenuItemPage()"
    #IDebug.set_trace()
    #Bldb.set_trace()
    #pdb.set_trace()
    self.TitleText=PageDscr["Title"]  #Tienen que tener t�tulo
    B_MenuFrameWidget.__init__(self,Parent,"MenuItemPage "+self.TitleText)
    #B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)
    font=Language.FontTitle # Provisional
    font_server=ScorerWidgets.font_server    # Provisional

    self.BackgroundImage=None
    try:
      self.BackgroundImage=PageDscr["Background"]
    except KeyError:
      pass

    self.PrevLabel="Prev"
    try:
      self.PrevLabel=PageDscr["PrevLabel"]
    except KeyError:
      pass

    self.Title=BUIx.B_TextWidget(self,"Title MenuItemPage "+self.TitleText,self.TitleText,font_server,Language.FontTitle)
    self.Title.SetAlpha(0.8)
    self.Title.SetColor(252,247,167)
    self.Title.SetScale(Language.MFontScale["L"])
    self.AddWidget(self.Title,10,10,
                   BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)


    # Truco, cada PageDscr puede tener un font, pero los B_MenuItemText lo leen de MenuDescr
    try:
      font=PageDscr["Font"]
      MenuDescr["Font"]=font
    except KeyError:
      pass

    self.PrevItem=B_MenuItemText(self,self.TitleText+self.PrevLabel,self.PrevLabel,None,StackMenu)
    self.PrevItem.SetAlpha(1.0)
    self.PrevItem.SetColor(252,247,167)
    B_MenuFocusManager.AddMenuElement(self,self.PrevItem)
    self.AddWidget(self.PrevItem,10,10,
                   BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


    self.NextLabel="Next"
    try:
      self.NextLabel=PageDscr["NextLabel"]
    except KeyError:
      pass

    self.NextItem=B_MenuItemText(self,self.TitleText+self.NextLabel,self.NextLabel,None,StackMenu)
    self.NextItem.SetAlpha(1.0)
    self.NextItem.SetColor(252,247,167)
    B_MenuFocusManager.AddMenuElement(self,self.NextItem)
    self.AddWidget(self.NextItem,10,10,
                   BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


    self.ContinueItem=B_MenuItemText(self,self.TitleText+" Continue","Continue",None,StackMenu)
    self.ContinueItem.SetAlpha(1.0)
    self.ContinueItem.SetColor(252,247,167)
    B_MenuFocusManager.AddMenuElement(self,self.ContinueItem)
    self.AddWidget(self.ContinueItem,0.4,10,
                   BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_Left,
                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

    self.BackItem=B_MenuItemText(self,self.TitleText+" Back","Back",None,StackMenu)
    self.BackItem.SetAlpha(0.5)
    self.BackItem.SetColor(252,247,167)
    B_MenuFocusManager.AddMenuElement(self,self.BackItem)
    self.AddWidget(self.BackItem,0.4,10,
                   BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_Right,
                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

    #self.SetDrawFunc(self.Draw)
    self.Description="No Description"
    try:
      self.Description=PageDscr["Description"]
    except KeyError:
      pass

    self.DescriptionItem=B_MenuItemTextNoFocus(self,self.TitleText+" Description",self.Description,None,StackMenu)
    B_MenuFocusManager.AddMenuElement(self,self.DescriptionItem)
    self.DescriptionItem.SetAlpha(1.0)
    self.DescriptionItem.SetColor(252,247,167)
    self.AddWidget(self.DescriptionItem,25,0.7,
                   BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                   BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)


    try:
      BackgroundImage=PageDscr["BackGround"]
      self.BackgroundItem=WidgetsExtra.B_ImageWidget(self,self.TitleText+" Background",BackgroundImage)
      self.AddWidget(self.BackgroundItem,0.5,0.5,
                   BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                   BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)
    except KeyError:
      pass

    B_MenuFocusManager.SetFocus(self,self.ContinueItem)


  def __del__(self):
    #print "Destroying ",self
    pass

  def __str__(self):
    print "B_MenuItemPage",self.TitleText


  def SetVisible(self,v):
    B_MenuFrameWidget.SetVisible(self,v)


#  def Draw(self,x,y,time):
#    if self.GetVisible()==0:
#      return
#    foc=self.GetHasFocus()
#    if foc:
#      self.SetColor(240,240,240)
#    else:
#      self.SetColor(240,10,10)
#
#    self.DefDraw(x,y,time)




class B_MenuItemPages(BUIx.B_TextWidget,B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu):
    Font = MenuDescr.get("Font", Language.FontCommon)
    Scale = MenuDescr.get("FontScale", Language.MFontScale["L"])
    font_server=ScorerWidgets.font_server    # Provisional
    BUIx.B_TextWidget.__init__(self,Parent,"B_MenuItemPages","B_MenuItemPages Text",font_server,Font)
    B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)
    self.Pages=[]
    self.ActivePage=None
    self.SetDrawFunc(self.Draw)
    self.SetSizeChangedFunc(self.SizeChanged)
    PageDscrs=MenuDescr["PageDscrs"]
    for i in PageDscrs:
      self.AddPage(Parent,i,MenuDescr,StackMenu)
    self.SetActivePage(self.Pages[0])
    self.thisown=1

  def __del__(self):
    print "Deleting",self
    #del(self.Pages)


  def AddPage(self,Parent,pagedscr,MenuDescr,StackMenu):
    page=B_MenuItemPage(Parent,640,480,pagedscr,MenuDescr,StackMenu)
    self.Pages.append(page)


  def SetActivePage(self,page):
    if self.ActivePage:
      self.ActivePage.SetVisible(0)
    self.ActivePage=page
    if self.ActivePage:
      self.ActivePage.SetVisible(1)
      Bladex.SetRootWidget(self.ActivePage.GetPointer())

  def NextPageAux(self,desp):
    old_page=self.ActivePage
    index=self.Pages.index(old_page)
    index=index+desp
    index=index%len(self.Pages)
    self.SetActivePage(self.Pages[index])

  def NextPage(self):
    self.NextPageAux(1)

  def PrevPage(self):
    self.NextPageAux(-1)


  def GetPointer(self):
    if self.ActivePage:
      return self.ActivePage.GetPointer()
    else:
      return self.GetPointer()


  def AcceptsFocus(self):
    return 0

  def GetFocus(self):
    return self

  def NextFocus(self):
    if self.ActivePage:
      self.ActivePage.NextFocus()
    else:
      pass

  def PrevFocus(self):
    if self.ActivePage:
      self.ActivePage.PrevFocus()
    else:
      pass


  def ActivateItem(self,act):
    #print "B_MenuItemPages.ActivateItem()"
    if act and self.ActivePage:
      wTemp=self.ActivePage.GetFocus()
      #pdb.set_trace()
      if not wTemp.ActivateItem(1):
        if self.ActivePage.GetFocus()==self.ActivePage.PrevItem:
          self.PrevPage()
        elif self.ActivePage.GetFocus()==self.ActivePage.NextItem:
          self.NextPage()
    else:
      self.SetActivePage(None)
      B_MenuTreeItem.ActivateItem(self,act)


  def __str__(self):
    print "class B_MenuItemPages with",len(self.Pages),"pages"


  def Draw(self,x,y,time):
    if self.ActivePage:
      self.ActivePage.Draw(x,y,time)
    else:
      self.SetColor(100,100,240)
      self.SetAlpha(0.5)
      BUIx.B_TextWidget.DefDraw(self,100,100,time)


  def SizeChanged(self,reshz,resvt):
    for i in self.Pages:
      i.SizeChanged(reshz,resvt)

  def CreateFrame(self):
    return None



BackImageBitmap = BBLib.B_BitMap24()
BackImageBitmap.ReadFromFile("../../Data/menu_wide.jpg")

class B_BackImageWidget(BUIx.B_RectWidget):

	def __init__(self,Parent,MenuDescr,StackMenu):
		self.image = MenuDescr.get("Image", BackImageBitmap) # type: BBLib.B_BitMap24
		self.vidw = 1
		self.vidh = 1
		BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],self.vidw,self.vidh)
		self.Selected=0
		self.Solid=0
		self.Border=0
		self.Dimension = self.image.GetDimension()
		self.SetDrawFunc(self.Draw)

	def Draw(self,x,y,time):
		Raster.SetPosition(0,0)
		Raster.DrawImage(self.Dimension[0], self.Dimension[1], "RGB", "Cover", self.image.GetData()) # by Sryml
		self.DefDraw(x,y,time)

	def FinalRelease(self):
		pass # BUIx.B_RectWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 0

class B_BackBlank(BUIx.B_RectWidget):

	def __init__(self,Parent,MenuDescr,StackMenu):
		self.Bitmap  = BBLib.B_BitMap24()
		self.Bitmap.ReadFromFile("../../Data/Black.jpg")
		self.vidw = 1
		self.vidh = 1
		BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],self.vidw,self.vidh)
		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)

	def Draw(self,x,y,time):
		Raster.SetPosition(0,0)
		Raster.DrawImage(640,480,"BGR","Stretch",self.Bitmap.GetData())
		self.DefDraw(x,y,time)

	def FinalRelease(self):
		BUIx.B_RectWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 0


def SetCombosText(arg):
  import PanelFillerCombos
  return PanelFillerCombos.FillCombosText(arg)

def SetAbilitiesText(arg):
  import PanelFillerAbilities
  return PanelFillerAbilities.FillAbilitiesText(arg)

def SetSpecialsText(arg):
  import PanelFillerSpecials
  return PanelFillerSpecials.FillSpecialsText(arg)

def SetGamepadDisconnectFunc(isDisconnect):
    import Scorer
    global wDisconnectGamepadBox

    if isDisconnect == 1:
        wDisconnectGamepadBox=BUIx.B_TextWidget(Scorer.wMessageFrame,"MessageWidget","\n\n\n\n\n",ScorerWidgets.font_server,Language.FontTitle)
        wDisconnectGamepadBox.SetColor(255,255,255)
        wDisconnectGamepadBox.SetSolid(1)
        wDisconnectGamepadBox.SetText(" "+MenuText.GetMenuText("Gamepad disconnected")+" ")
        wDisconnectGamepadBox.SetJustification(BUIx.B_TextWidget.B_TEXT_HCenter)
        wDisconnectGamepadBox.SetBackgroundAlpha(0.0)
        wDisconnectGamepadBox.SetBackgroundColor(0,0,0)
        wDisconnectGamepadBox.SetAlpha(1)
        # if not GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
        #     scale = 0.8
        # else:
        #     scale = 2
        # wDisconnectGamepadBox.SetScale(scale)
        wDisconnectGamepadBox.SetScale(Language.MFontScale["L"])

        Scorer.wMessageFrame.AddWidget(wDisconnectGamepadBox,0.5,50,
              BUIx.B_FrameWidget.B_FR_HRelative,
              BUIx.B_FrameWidget.B_FR_HCenter,
              BUIx.B_FrameWidget.B_FR_AbsoluteBottom,
              BUIx.B_FrameWidget.B_FR_Bottom)

    elif isDisconnect == 0:
        Scorer.wMessageFrame.SetAlpha(0)
        Scorer.wMessageFrame.RemoveWidget("MessageWidget",0)


    Scorer.wMessageFrame.RecalcLayout()

class B_BackWeapon(BUIx.B_FrameWidget):

	#def __init__(self,Parent,MenuDescr,StackMenu):
	def __init__(self,Parent,Menudesc,StackMenu,VertPos=0):
		import Language
		import GotoMapVars
		self.image = 1
		self.NumImages = 6
		self.PanelWidgets = []
		self.PanelWidgetsName = []

		self.Text = 0
		self.NumTexts = 4

		self.TextsAvail = [0, 0, 0, 0]

		self.vidw = 1
		self.vidh = 1

		self.addone = 0

		char = Bladex.GetEntity("Player1")
		print char.Kind

		Raster.UnifyRenderBuffers()

		if "ORCMURAL"    in GotoMapVars.BaList:
			self.TextsAvail[1] = 1
		if "ISLANDMURAL" in GotoMapVars.BaList:
			self.TextsAvail[2] = 1
		if  "NEJEVMURAL" in GotoMapVars.BaList:
			self.TextsAvail[3] = 1

		# Range Vars
		Inventory = Bladex.GetEntity("Player1").GetInventory()

		if (not Inventory.nTablets > 0) and not (1 in GotoMapVars.PlacedTablets) and not (self.TextsAvail[1] or self.TextsAvail[2] or self.TextsAvail[3]):
			self.addone = 1
		if  "SALATABLILLAS" in GotoMapVars.BaList or (1 in GotoMapVars.PlacedTablets) or (Inventory.nTablets > 0):
			self.addone = 0
			self.TextsAvail[0] = 1

		language = PanelFillerCommon.GetLanguageFallback()
		print language

		self.Specials  = BBLib.B_BitMap24()
		self.Specials.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillaspecials_hi_empty.jpg")

		self.Items  = BBLib.B_BitMap24()
		self.Items.ReadFromFile("../../Data/TB/" + language +"/Items/plantillaGitems_hi.jpg")

		self.Weapons  = BBLib.B_BitMap24()
		self.Weapons.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillaweapons_hi_empty.jpg")


		self.Habilities  = BBLib.B_BitMap24()
		self.Habilities.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillahabilities_hi_empty.jpg")

		self.MapText  = BBLib.B_BitMap24()

		if not self.MapText.ReadFromFile("../../Data/TB/" + language + "/" + char.Kind + "/" + Bladex.GetCurrentMap() + "_hi.jpg"):
			if not self.MapText.ReadFromFile("../../Data/TB/" + language + "/"  + Bladex.GetCurrentMap() + "_hi.jpg"):
				if not self.MapText.ReadFromFile("../../Data/TB/" + language + "/" + char.Kind + "/" + Bladex.GetCurrentMap() + ".jpg"):
					self.MapText.ReadFromFile("../../Data/TB/" + language + "/"  + Bladex.GetCurrentMap() + ".jpg")

		if string.lower(Bladex.GetCurrentMap()) == "tower_m16":
			inv = Bladex.GetEntity("Player1").GetInventory()
			for i in range(inv.nWeapons):
				if (Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2") or (Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2Barbarian"):
					self.MapText.ReadFromFile("../../Data/TB/" + language + "/"  + "conTower_m16_hi.jpg")
				else:
					self.MapText.ReadFromFile("../../Data/TB/" + language + "/"  + "sinTower_m16_hi.jpg")


		self.Tablets  = BBLib.B_BitMap24()
		if (Inventory.nTablets > 0) or (1 in GotoMapVars.PlacedTablets):
			self.Tablets.ReadFromFile("../../Data/TB/"+ language  + "/tablillas_hi.jpg")

		self.Text1 = BBLib.B_BitMap24()
		if self.TextsAvail[1]:
			self.Text1.ReadFromFile("../../Data/TB/" + language  + "/muralorc_hi.jpg")
		self.Text2 = BBLib.B_BitMap24()
		if self.TextsAvail[2]:
			self.Text2.ReadFromFile("../../Data/TB/" + language  + "/muralisla1_hi.jpg")
		self.Text3 = BBLib.B_BitMap24()
		if self.TextsAvail[3]:
			self.Text3.ReadFromFile("../../Data/TB/" + language  + "/muralnejev_hi.jpg")


		BUIx.B_FrameWidget.__init__(self,Parent,Menudesc["Name"],self.vidw,self.vidh)

		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)

		self.SndCorreGema=Bladex.CreateSound("../../Sounds/golpe-generico2.wav","Chanje")
		self.SndCorreGema.Volume=2.0
		self.SndCorreGema.MinDistance=1000000.0
		self.SndCorreGema.MaxDistance=2000000

		if self.addone == 0:
			while not self.TextsAvail[self.Text]:
				self.Text = self.Text + 1
				if self.Text > self.NumTexts - 1:
					self.Text = 0

		self.SetupPanelWidgets()

	def AddButtonTexts(self, language):
		sys.path.append('../../SCRIPTS/Combos/' + language)
		import PanelButtonsLoca
		index = 0
		elem = "Button"
		for text in PanelButtonsLoca.buttons:
			name = language + elem + text
			font = PanelFillerCommon.CheckFontChineseFallback(elem)
			buttonWidget=PanelFillerCommon.InitWidget(self, name, text, font, elem)
			posX = PanelFillerCommon.CheckButtonOffset(index, buttonTextPosition[0] + (buttonOffset[0] * index))
			posY = buttonTextPosition[1]
			posX = PanelFillerCommon.CorrectPosX(posX)
			posY = PanelFillerCommon.CorrectPosY(posY)
			self.AddWidget(buttonWidget,posX,posY,relative,center,relativev,left)
			index = index + 1

	def RemovePanelWidgets(self):
		for elem in self.PanelWidgetsName:
			self.RemoveWidget(elem, 0)
		self.PanelWidgets = []
		self.PanelWidgetsName = []

	def SetupPanelWidgets(self):
		currImage = self.GetCurrentImage()
		self.RemovePanelWidgets()
		if currImage == 0:
			SetSpecialsText(self)
		elif currImage == 1:
			SetCombosText(self)
		elif currImage == 2:
			SetAbilitiesText(self)
		self.AddButtonTexts(PanelFillerCommon.GetLanguageFallback())

	def GetCurrentImage(self):
		import GotoMapVars
		currImage = self.image
		char = Bladex.GetEntity("Player1")
		Map = string.lower(Bladex.GetCurrentMap())

		Specials = 1

		Inventory = char.GetInventory()

		HaveCrush = 0

		for i in range(Inventory.nWeapons):
			Weapon = Inventory.GetWeapon(i)
			RootWeapon = Bladex.GetEntity(Weapon)
			if RootWeapon.Kind == "CrushHammer":
				HaveCrush = 1

		if Map in GotoMapVars.BackLevelNames:
			Specials = 0
		else:
			if (Map in GotoMapVars.LevelNames and GotoMapVars.LevelNames.index(Map) > 6) or ((char.Kind == "Dwarf_N") and HaveCrush):
				Specials = 0
		if self.image < Specials:
			currImage = (self.NumImages - (1 + self.addone))

		if self.image > (self.NumImages - (1 + self.addone)):
			currImage = Specials
		return currImage

	def Draw(self,x,y,time):

		Raster.SetTextShadow(4, 4)
		import string
		import Menu

		# x,y = Raster.GetSize()
		# Raster.SetPosition((x - 640)/2, (y - 480)/2)


		# Horizontal buttons range checking
		self.image = self.GetCurrentImage()

		# Vertical -Text- options range checking
		if self.Text < 0:
			self.Text = self.NumTexts - 1

		if self.Text > self.NumTexts - 1:
			self.Text = 0

		# Set logic conditions
		if self.image == 0:
			w, h = self.Specials.GetDimension()
			Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Specials.GetData())
		if self.image == 1:
			w, h = self.Habilities.GetDimension()
			Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Weapons.GetData())
		if self.image == 2:
			w, h = self.Weapons.GetDimension()
			Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Habilities.GetData())
		if self.image == 3:
			w, h = self.Items.GetDimension()
			Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Items.GetData())
		if self.image == 4:
			w, h = self.MapText.GetDimension()
			Raster.DrawImage(w, h,"RGB","ScaledCentered2",self.MapText.GetData())
		if self.image == 5:
			if self.Text == 0:
				w, h = self.Tablets.GetDimension()
				Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Tablets.GetData())
			if self.Text == 1:
				w, h = self.Text1.GetDimension()
				Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Text1.GetData())
			if self.Text == 2:
				w, h = self.Text2.GetDimension()
				Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Text2.GetData())
			if self.Text == 3:
				w, h = self.Text3.GetDimension()
				Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Text3.GetData())

		if  ((self.image == 5)):
		# and
		#	(
		#		(self.TextsAvail[1]) or
		#		(self.TextsAvail[2]) or
		#		(self.TextsAvail[3])
		#	)):
			Menu.TBUDSoundAble = 1
		else:
			Menu.TBUDSoundAble = 0

		Raster.SetPosition(0,0)
		self.DefDraw(0,0,time)

	def FinalRelease(self):
		BUIx.B_FrameWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 1

	def IncMenuItem(self):
		self.SndCorreGema.PlayStereo()
		self.image = self.image + 1
		self.SetupPanelWidgets()

	def DecMenuItem(self):
		self.SndCorreGema.PlayStereo()
		self.image = self.image - 1
		self.SetupPanelWidgets()

	def GetFocus(self):
	    return self

	def ActivateItem(self,activate):
		import Menu
		Menu.ActivateMenu()
		return

	def NextFocus(self):
		if self.image == 5:
			self.Text = self.Text + 1
			count = 0
			while not self.TextsAvail[self.Text]:
				if count == len(self.TextsAvail):
					break
				self.Text = self.Text + 1
				if self.Text > self.NumTexts - 1:
					self.Text = 0
				count = count + 1

	def PrevFocus(self):
		if self.image == 5:
			self.Text = self.Text - 1
			count = 0
			while not self.TextsAvail[self.Text]:
				if count == len(self.TextsAvail):
					break
				self.Text = self.Text - 1
				if self.Text < 0:
					self.Text = self.NumTexts - 1
				count = count + 1

	def __del__(self):
		import Menu
		Menu.TBUDSoundAble = 1

class B_BackFeatures(BUIx.B_RectWidget):

	def __init__(self,Parent,MenuDescr,StackMenu):
		path = "../../Data/Demo/"+ Language.Current + "/"
		if not os.path.exists(path + "DEMO-SCREEN.jpg"):
			path = "../../Data/Demo/EnglishUS/"
		self.Bitmap  = BBLib.B_BitMap24()
		self.Bitmap.ReadFromFile(path + "DEMO-SCREEN.jpg")
		self.CurrentBitmap = BBLib.B_BitMap24()
		self.CurrentBitmap = self.Bitmap
		self.vidw = 1
		self.vidh = 1
		BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],self.vidw,self.vidh)
		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)
		self.Time2Exit=None
		global isQuitting
		isQuitting = 0

	def Draw(self,x,y,time):
		global isQuitting
		isQuitting = 1
		if self.Time2Exit==None:
			self.Time2Exit=time
		if time-self.Time2Exit>10.0:
			Bladex.Quit()
		Raster.SetPosition(0,0)
		Raster.DrawImage(4256,2394,"RGB","Stretch",self.CurrentBitmap.GetData())
		self.DefDraw(x,y,time)

	def FinalRelease(self):
		BUIx.B_RectWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 0
