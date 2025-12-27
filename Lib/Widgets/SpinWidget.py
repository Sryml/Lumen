



import BUIx
import DistortFX
import types
import MenuText






class B_SpinWidgetAux(BUIx.B_FrameWidget):
  def __init__(self,Parent,Name,Width,Height,font_server,font):
    BUIx.B_FrameWidget.__init__(self,Parent,Name,Width,Height)
    self.LeftArrow=BUIx.B_TextWidget(self,"SpinLArrow "+Name,"<",font_server,font)
    self.AddWidget(self.LeftArrow,1,0.5,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                                      BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)
    self.LeftArrow.SetColor(252,247,167)
    self.LeftArrow.SetAlpha(1)

    self.RightArrow=BUIx.B_TextWidget(self,"SpinRArrow "+Name,">",font_server,font)
    self.AddWidget(self.RightArrow,1,0.5,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                                        BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)
    self.RightArrow.SetColor(252,247,167)
    self.RightArrow.SetAlpha(1)

    self.Text=BUIx.B_TextWidget(self,"SpinTextAux "+Name,"0",font_server,font) # 0 == self.Value
    self.AddWidget(self.Text,0.5,0.5,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                                   BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)
    self.Text.SetColor(252,247,167)
    self.Text.SetAlpha(1)

    self.LowLimit=0
    self.UpLimit=10
    self.Steps=10
    self.Value=0
    self.__SetIncrement()
    self.AdjustArrows()



  def SetLimits(self,low,up):
    if low>up:
      return

    self.LowLimit=low
    self.UpLimit=up
    self.__SetIncrement()

    if self.Value<low:
      self.Value=low
    elif self.Value>up:
      self.Value=up

    self.UpdateDisplayValue()


  def SetSteps(self,steps):
    if steps<0:
      return

    self.Steps=steps
    self.__SetIncrement()

    self.UpdateDisplayValue()


  def __SetIncrement(self):
    self.Increment=(self.UpLimit-self.LowLimit)/self.Steps


  def AdjustArrows(self):
    if self.Value<=self.LowLimit:
      self.LeftArrow.SetVisible(0)
    else:
      self.LeftArrow.SetVisible(1)

    if self.Value>=self.UpLimit:
      self.RightArrow.SetVisible(0)
    else:
      self.RightArrow.SetVisible(1)



  def IncrementValue(self):
    self.Value=self.Value+self.Increment
    if self.Value>self.UpLimit:
      self.Value=self.UpLimit

    self.UpdateDisplayValue()


  def DecrementValue(self):
    self.Value=self.Value-self.Increment
    if self.Value<self.LowLimit:
      self.Value=self.LowLimit

    self.UpdateDisplayValue()


  def UpdateDisplayValue(self):
    if type(self.Value)==types.FloatType:
      str_tmp="%.2f" % self.Value
      self.Text.SetText(str_tmp)
    else:
      self.Text.SetText(str(self.Value))
    self.RecalcLayout()
    self.AdjustArrows()


  def SetValue(self,value):
    if value>=self.LowLimit and value<=self.UpLimit and value!=self.Value:
      self.Value=value
      self.UpdateDisplayValue()




class B_SpinWidget(BUIx.B_FrameWidget):
  def __init__(self,Parent,Name,Width,Height,font_server,font,default_value):
    BUIx.B_FrameWidget.__init__(self,Parent,Name,Width,Height)
    self.Text=BUIx.B_TextWidget(self,"SpinLArrow "+Name,Name,font_server,font)
    self.AddWidget(self.Text,1,0.5,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                                   BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)
    self.DefaultText=BUIx.B_TextWidget(self,"DefaultText", Name,font_server,font)
    self.DefaultText.SetText("(" + MenuText.GetMenuText("Default") + ")")

    self.AddWidget(self.DefaultText,90,0.5,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                                   BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)

    self.Spin=B_SpinWidgetAux(self,"SpinText "+Name,80,Width,font_server,font) # 50 a ojo (Estoy hasta los c######).
    self.AddWidget(self.Spin,1,0.5,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                                   BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)
    self.SetDrawFunc(self.Draw)

    self.DefaultValue=default_value


  def SetLimits(self,low,up):
    self.Spin.SetLimits(low,up)


  def SetSteps(self,steps):
    self.Spin.SetSteps(steps)


  def IncrementValue(self):
    self.Spin.IncrementValue()

  def DecrementValue(self):
    self.Spin.DecrementValue()

  def SetValue(self,value):
    self.Spin.SetValue(value)

  def GetValue(self):
    return self.Spin.Value

  def Draw(self,x,y,time):
    foc=self.GetHasFocus()
    self.Text.SetAlpha           (1.0)
    self.Spin.Text.SetAlpha      (1.0)
    self.Spin.LeftArrow.SetAlpha (1.0)
    self.Spin.RightArrow.SetAlpha(1.0)
    if(self.DefaultValue==self.GetValue()):
      self.DefaultText.SetAlpha    (1.0)
    else:
      self.DefaultText.SetAlpha    (0.0)

    if foc:
      self.Text.SetColor           (252,247,167)
      self.Spin.Text.SetColor      (252,247,167)
      self.Spin.LeftArrow.SetColor (252,247,167)
      self.Spin.RightArrow.SetColor(252,247,167)
      self.DefaultText.SetColor    (252,247,167)
    else:
      self.Text.SetColor           (207,144,49)
      self.Spin.Text.SetColor      (207,144,49)
      self.Spin.LeftArrow.SetColor (207,144,49)
      self.Spin.RightArrow.SetColor(207,144,49)
      self.DefaultText.SetColor    (207,144,49)
    self.DefDraw(x,y,time)






class B_SpinFXWidget(B_SpinWidget): #,DistortFX.B_DistortFX):
  def __init__(self,Parent,Name,Width,Height,font_server,font,dist_size=45,color=(255,10,10)):
    B_SpinWidget.__init__(self,Parent,Name,Width,Height,font_server,font)
    #DistortFX.B_DistortFX.__init__(self,dist_size,color)
    self.SetDrawFunc(self.Draw)

  def IncrementValue(self):
    v1=self.GetValue()
    B_SpinWidget.IncrementValue(self)
    if v1!=self.GetValue():
      self.FilterUpdated=0
      self.SelectionFilterUpdated=0
      self.Filter=None
      self.SelectionFilter=None

  def DecrementValue(self):
    v1=self.GetValue()
    B_SpinWidget.DecrementValue(self)
    if v1!=self.GetValue():
      self.FilterUpdated=0
      self.SelectionFilterUpdated=0
      self.Filter=None
      self.SelectionFilter=None


