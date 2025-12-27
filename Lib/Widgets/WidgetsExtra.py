


import BUIx
import BVideo
import Raster
import BBLibc
import math
import sys


class B_VideoWidget(BUIx.B_RectWidget):
  def __init__(self,Parent,Name,video):
    self.Vid=BVideo.B_Video()
    self.Vid.SetVideo(video)
    self.vidw,self.vidh=self.Vid.GetDimension()
    BUIx.B_RectWidget.__init__(self,Parent,Name,self.vidw,self.vidh)
    self.Selected=0
    self.Solid=0
    self.Border=0
    self.SetDrawFunc(self.Draw)

  def __del__(self):
    pass


  def Draw(self,x,y,time):
    Raster.SetPosition(x,y)
    Raster.DrawImage(self.vidw,self.vidh,"BGR","UpsideDown",self.Vid.GetData(time))
    self.DefDraw(x,y,time)




class B_ImageWidget(BUIx.B_RectWidget):
  def __init__(self,Parent,Name,image):
    self.Bitmap=BBLib.B_BitMap24()
    self.Bitmap.ReadFromBMP(image)
    self.vidw,self.vidh=self.Bitmap.GetDimension()
    BUIx.B_RectWidget.__init__(self,Parent,Name,self.vidw,self.vidh)
    self.Selected=0
    self.Solid=0
    self.Border=0
    self.SetDrawFunc(self.Draw)

  def __del__(self):
    pass

  def Draw(self,x,y,time):
    Raster.SetPosition(x,y)
    Raster.DrawImage(self.vidw,self.vidh,"RGB","Normal",self.Bitmap.GetData())
    self.DefDraw(x,y,time)


class B_FlashBitmapWidget(BUIx.B_BitmapWidget):
  def __init__(self,Parent,Name,width,height,BitmapName,FileName):
    BUIx.B_BitmapWidget.__init__(self,Parent,Name,width,height,BitmapName,FileName)
    self.SetDrawFunc(self.Draw)
    self.Flashing=0
    self.MinAlpha= 0.0
    self.MaxAlpha= 1.0
    self.Continuous= 0

  def Draw(self,x,y,time):
    if self.GetVisible()==0:
      return

    if self.Flashing!=0:
      alpha=self.GetAlpha()
      alpha_range= self.MaxAlpha-self.MinAlpha
      if self.Continuous:
        self.SetAlpha(0.5+0.5*(math.cos(time*self.Flashing))*alpha_range+self.MinAlpha)
      else:	
        self.SetAlpha(max(0.0, math.cos(time*self.Flashing))*alpha_range+self.MinAlpha)
      self.DefDraw(x,y,time)
      self.SetAlpha(alpha)
    else:
      self.DefDraw(x,y,time)


  def SetFlash(self,fl):
    self.Flashing=fl


  def GetFlash(self):
    return self.Flashing

class B_FlashBarWidget(BUIx.B_BarWidget):
  def __init__(self,Parent,Name,width,height):
    BUIx.B_BarWidget.__init__(self,Parent,Name,width,height)
    self.SetDrawFunc(self.Draw)
    self.Flashing=0    
    self.NormalColor= (0,0,0)
    self.DeltaColor= (0,0,0)
    self.Continuous= 0
    
  def Draw(self,x,y,time):
    if self.GetVisible()==0:
      return

    if self.Flashing!=0:      
      if self.Continuous:
        a= 0.5+0.5*math.cos(time*self.Flashing)
      else:
        a= max(0.0, math.cos(time*self.Flashing))
      BUIx.B_BarWidget.SetColor(self,
                                self.NormalColor[0]+self.DeltaColor[0]*a, 
                                self.NormalColor[1]+self.DeltaColor[1]*a, 
                                self.NormalColor[2]+self.DeltaColor[2]*a)
      self.DefDraw(x,y,time)
      BUIx.B_BarWidget.SetColor(self,self.NormalColor[0], self.NormalColor[1], self.NormalColor[2])
    else:
      self.DefDraw(x,y,time)

  def SetFlash(self,fl):
    self.Flashing=fl

  def GetFlash(self):
    return self.Flashing

  def SetColor(self,r,g,b):
    # change the delta to preserve the flash color    
    #import pdb
    #pdb.set_trace()
    dc= (r-self.NormalColor[0],g-self.NormalColor[1],b-self.NormalColor[2])
    self.DeltaColor= (min (self.DeltaColor[0]-dc[0], 255-r), 
                      min (self.DeltaColor[1]-dc[1], 255-g), 
                      min (self.DeltaColor[2]-dc[2], 255-b))
    
    self.NormalColor= (r,g,b)
    BUIx.B_BarWidget.SetColor(self,r,g,b)
    
  def SetFlashColor(self,r,g,b):        
    # Store as a delta
    #import pdb
    #pdb.set_trace()
    self.DeltaColor= (r-self.NormalColor[0], g-self.NormalColor[1], b-self.NormalColor[2])

  def GetFlashColor(self):
    return (self.NormalColor[0]+self.DeltaColor[0], 
            self.NormalColor[1]+self.DeltaColor[1], 
            self.NormalColor[2]+self.DeltaColor[2])


class B_FlashTextWidget(BUIx.B_TextWidget):
  def __init__(self,Parent,Name,Text,font_server,font):
    BUIx.B_TextWidget.__init__(self,Parent,Name,Text,font_server,font)
    self.SetDrawFunc(self.Draw)
    self.Flashing=0


  def Draw(self,x,y,time):
    if self.GetVisible()==0:
      return

    if self.Flashing!=0:
      alpha=self.GetAlpha()
      self.SetAlpha(math.cos(time*self.Flashing))
      self.DefDraw(x,y,time)
      self.SetAlpha(alpha)
    else:
      self.DefDraw(x,y,time)


  def SetFlash(self,fl):
    self.Flashing=fl


  def GetFlash(self):
    return self.Flashing




