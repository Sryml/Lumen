


import Raster
import BImagex


class B_DistortFX:
  def __init__(self,dist_size=45,color=(255,10,10)):
    self.Filter=None
    self.SelectionFilter=None
    self.FilterUpdated=0      # 0 Si hay que recalcular el filtro
    self.SelectionFilterUpdated=0
    self._foc=0               # Indica si tiene el foco
    self.FilterIncX=0
    self.FilterIncY=2
    self.DistSize=dist_size
    self.R=color[0]
    self.G=color[1]
    self.B=color[2]
    

  def __del__(self):
    print "B_TextFXWidget.__del__()",self.Name()
    if self.Filter is not None:
      self.Filter.ClearBuffer()
    #if self.SelectionFilter is not None:
    #  self.SelectionFilter.ClearBuffer()


  def __str__(self):
    print "B_TextFXWidget widget with text",self.GetTextData()

  def CreateDistorsion(self,x,y,time=0):
    w,h=self.GetSize()
    self.SelectionFilter=BImagex.B_SideDistortFilter()
    self.SetColor(self.R,self.G,self.B)
    self.FilterIncX=self.FilterIncX+6
    self.FilterIncY=2
    self.SelectionFilter.SetDistance(self.FilterIncX)
    self.DefDraw(x,y,time)
    self.SelectionFilter.SetImageBuffer(w+2*self.FilterIncX,h+2*self.FilterIncY)

    bud_address=self.SelectionFilter.GetImageBuffer()
    Raster.GetImage(x-self.FilterIncX,y-self.FilterIncY,w+2*self.FilterIncX,h+2*self.FilterIncY,
                  "RGB","",self.SelectionFilter.GetBufferSize(),bud_address)

    self.SelectionFilter.CopyToBuffer2()
    self.SelectionFilter.Apply()
    #self.SelectionFilter.GetFromBuffer2("Substract")


  def CreateBlur(self,x,y,time=0,width=0,height=0):
    if width!=0 and height!=0:
      w,h=width,height
    else:
      w,h=self.GetSize()
    self.Filter=BImagex.B_GridSubFilter()

    if self.AcceptsFocus():
      self.SetColor(self.R,self.G,self.B)
    else:    
      self.SetColor(self.R * 0.23,self.G * 0.23,self.B * 0.23)

    self.Filter.SetCoefficients([ 0 , 1 , 1 , 1 , 0 ,
                                  0 , 1 , 1 , 1 , 0 ,
                                  0 , 1 , 1 , 1 , 0 ,
                                  0 , 1 , 1 , 1 , 0 ,
                                  0 , 1 , 1 , 1 , 0])
    self.DefDraw(x,y,time)
    self.Filter.SetImageBuffer(w+4,h+4)

    bud_address=self.Filter.GetImageBuffer()
    Raster.GetImage(x-2,y-2,w+4,h+4,"RGB","",self.Filter.GetBufferSize(),bud_address)
    #self.Filter.Apply()


  def Draw(self,x,y,time):
    if self.GetVisible()==0:
      return

    foc=self.GetHasFocus()
    if foc!=self._foc:
      self.SelectionFilterUpdated=0
      self.FilterIncX=0

    self._foc=foc
    w,h=self.GetSize()

    if not foc:
      if self.SelectionFilterUpdated:
        Raster.SetPosition(x-self.FilterIncX,y-self.FilterIncY)
        Raster.DrawImage(w+2*self.FilterIncX,h+2*self.FilterIncY,"RGB","Native",self.SelectionFilter.GetImageBuffer())
        return
    else:
      if self.FilterUpdated:
        Raster.SetPosition(x-2,y-2)
        Raster.DrawImage(w+4,h+4,"RGB","Native",self.Filter.GetImageBuffer())
        return

    self.SetAlpha(1.0)
    if not foc:
      self.CreateDistorsion(x,y,time)
      if self.Filter is None:
        self.CreateBlur(x,y,time)
      sfw,sfh=self.Filter.GetDimension()
      self.SelectionFilter.CopySubBuffer(self.FilterIncX-2,0,sfw,sfh,self.Filter.GetImageBuffer(),"AddInc")
      self.SelectionFilter.GetFromBuffer2("Substract")#AddInc")#
      Raster.SetPosition(x-self.FilterIncX,y-self.FilterIncY)
      Raster.DrawImage(w+2*self.FilterIncX,h+2*self.FilterIncY,"RGB","Native",self.SelectionFilter.GetImageBuffer())

      if self.FilterIncX>self.DistSize:
        self.SelectionFilterUpdated=1
      else:
        self.SelectionFilterUpdated=0

    else:
      self.CreateBlur(x,y,time)
      Raster.SetPosition(x-2,y-2)
      Raster.DrawImage(w+4,h+4,"RGB","Native",self.Filter.GetImageBuffer())

      self.FilterUpdated=1
