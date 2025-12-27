


import BUIx
import DistortFX





class B_TextFXWidget(BUIx.B_TextWidget): #,DistortFX.B_DistortFX):
  def __init__(self,Parent,name,text,font_server,font,dist_size=45,color=(255,10,10)):
    #DistortFX.B_DistortFX.__init__(self,dist_size,color)
    BUIx.B_TextWidget.__init__(self,Parent,name,text,font_server,font)
    self.SetDrawFunc(self.Draw)
    self.SetAlpha(1.0)

  def SetText(self,text):
    BUIx.B_TextWidget.SetText(self,text)
    self.FilterUpdated=0
    self.SelectionFilterUpdated=0
    self.Filter=None
    self.SelectionFilter=None
