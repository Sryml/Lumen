

import string



class B_HTMLBase:
  def __init__(self,filename,title):
    self.FileName=filename
    self.Title=title
    self.FileName=filename
    self.HTMLText=[]

  def __del__(self):
    pass

  def Reset(self):
    self.HTMLText=[]

  def WriteHTMLFile(self):
      file=open(self.FileName,"w")
      text=string.joinfields(self.HTMLText)
      file.write(text)
      file.close()

  def CanAddTag(self):
    return 0

  def CanClose(self):
    return 0

  def _GenerateHeader(self):
    Text="<HTML>\n\n"
    Text=Text+"<HEAD>\n"
    Text=Text+"<TITLE>"+self.Title+"</TITLE>\n"
    Text=Text+"<meta name=\"GENERATOR\" content=\"Blade TravelBook\">\n"
    Text=Text+"</HEAD>\n\n"
    return Text

  def GenerateHeader(self):
    self.HTMLText.append(self._GenerateHeader())



  def _CloseHTML(self):
    Text="\n</HTML>\n"
    return Text

  def CloseHTML(self):
    if not self.CanClose():
      print "Documento no tiene BODY o FRAMESET correcto"
      return
    self.HTMLText.append(self._CloseHTML())
  


  def _WriteHyperLink(self,text,destiny,target=None):
    Text='<A HREF="'+destiny+'"'
    if target is not None:
      Text=Text+' TARGET="'+target+'" '
    Text=Text+'> '+text+'</A>'
    return Text

  def HyperLink(self,text,destiny,target=None):
    if not self.CanAddTag():
      print "HyperLink: Documento no tiene BODY o FRAMESET correcto"
      return
    self.HTMLText.append(self._WriteHyperLink(text,destiny,target))



  def _WriteImage(self,image,descr=None,text=None,align="BOTTOM"):
    Text='<IMG SRC="'+image+'"'

    if descr:
      Text=Text+'"  ALT="'+text+'"'

    if text:
      Text=Text+'ALIGN='+align

    Text=Text+'>'

    if text:
      Text=Text+text+'\n'
    return Text

  def Image(self,image,descr=None,text=None,align='BOTTOM'):
    if not self.CanAddTag():
      print "Image: Documento no tiene BODY o FRAMESET correcto"
      return
    self.HTMLText.append(self._WriteImage(image,descr,text,align))




  def _WriteImageLink(self,image,destiny,descr=None,text=None,align='BOTTOM'):
    Text=self._WriteImage(image,descr,text,align)
    Text=self._WriteHyperLink(Text,destiny)
    return Text

  def ImageLink(self,image,destiny,descr=None,text=None,align='BOTTOM'):
    if not self.CanAddTag():
      print "ImageLink: Documento no tiene BODY o FRAMESET correcto"
      return
    self.HTMLText.append(self._WriteImageLink(image,destiny,descr,text,align))




  def _WriteParagraph(self,text,align=None):
    Text='<P'
    if align is not None:
      Text=Text+' ALIGN='+align
    Text=Text+'>'+text+'</P>\n'
    return Text

  def Paragraph(self,text,align=None):
    if not self.CanAddTag():
      print "Paragraph: Documento no tiene BODY o FRAMESET correcto"
      return
    self.HTMLText.append(self._WriteParagraph(text,align))



  






class B_HTMLDocBody(B_HTMLBase):
  def __init__(self,filename,title):
    B_HTMLBase.__init__(self,filename,title)
    self.HasBody=0 # 0: no tiene, 1: Body empezado, 2: Body cerrado.

  def Reset(self):
    B_HTMLBase.Reset(self)
    self.HasBody=0

  def _GenerateBody(self,topmargin=None,background=None,scroll="auto",watermark=0):
    Text='<BODY SCROLL="'+scroll+'"'
    if background is not None:
      Text=Text+' BACKGROUND="'+background+'"'
      if watermark:
        Text=Text+' bgproperties="fixed"'
    if topmargin is not None:
      Text=Text+' TOPMARGIN="'+str(topmargin)+'"'
    Text=Text+'>\n\n'
    return Text

  def GenerateBody(self,topmargin=None,background=None,scroll="auto",watermark=0):
    if self.HasBody!=0:
      print "Error, Documento ya tiene BODY"
      return
    self.HasBody=1
    self.HTMLText.append(self._GenerateBody(topmargin,background,scroll,watermark))

  def _CloseBody(self):
    Text="\n</BODY>\n"
    return Text

  def CloseBody(self):
    if self.HasBody!=1:
      print "Error, Documento no tiene BODY inicializado"
      return
    self.HTMLText.append(self._CloseBody())
    self.HasBody=2

  def CanAddTag(self):
    return (self.HasBody==1)

  def CanClose(self):
    return (self.HasBody==2)






class B_HTMLDocFrames(B_HTMLBase):
  def __init__(self,filename,title):
    B_HTMLBase.__init__(self,filename,title)
    self.HasFrameSet=0 # 0: no tiene, 1: FrameSet empezado, 2: FrameSet cerrado.
    self.nFrames=0
    self.nFramesAdded=0

  def Reset(self):
    B_HTMLBase.Reset(self)
    self.HasFrameSet=0 # 0: no tiene, 1: FrameSet empezado, 2: FrameSet cerrado.
    self.nFrames=0
    self.nFramesAdded=0

  def _GenerateFrameSet(self,orientation,dimensions,frameborder=None,framespacing=None,border=None):
    Text="<FRAMESET"
    if frameborder is not None:
      Text=Text+" FRAMEBORDER="+str(frameborder)
    if framespacing is not None:
      Text=Text+" FRAMESPACING="+str(framespacing)
    if border is not None:
      Text=Text+" BORDER="+str(border)
    Text=Text+" "+orientation+"=\""

    dim_len=len(dimensions)
    dim_counter=0
    for i in dimensions:
      Text=Text+i
      dim_counter=dim_counter+1
      if dim_counter<dim_len: # Si no es la última, hay que poner una coma.
        Text=Text+", "
    Text=Text+"\">\n"
    self.nFrames=len(dimensions)
    return Text

  def GenerateFrameSet(self,orientation,dimensions,frameborder=None,framespacing=None,border=None):
    if self.HasFrameSet!=0:
      print "Error, Documento ya tiene FRAMESET"
      return
    self.HTMLText.append(self._GenerateFrameSet(orientation,dimensions,frameborder,framespacing,border))
    self.HasFrameSet=1

  def _CloseFrameSet(self):
    Text='\n</FRAMESET>\n'
    return Text

  def CloseFrameSet(self):
    if self.HasFrameSet!=1:
      print "Error, Documento no tiene FRAMESET inicializado"
      return
    if self.nFrames!=self.nFramesAdded:
      for i in range(self.nFramesAdded,self.nFrames):
        self.Frame("ERROR")

    self.HTMLText.append(self._CloseFrameSet())
    self.HasFrameSet=2

  def CanAddTag(self):
    return (self.HasFrameSet==1)

  def CanClose(self):
    return (self.HasFrameSet==2)

  def _WriteFrame(self,src,name=None,maginwidth=None,maginheight=None,scrolling=None,noresize=None,frameborder=None):
    if type(src)==type("string"):
      Text='<FRAME SRC="'+src+'" '
    else: # Asume que hereda de HTMLBase
      Text='<FRAME SRC="'+src.FileName+'" '
    if name is not None:
      Text=Text+' NAME="'+name+'"'
    
    if maginwidth is not None:
      Text=Text+' MARGINWIDTH="'+maginwidth+'"'

    if maginheight is not None:
      Text=Text+' MARGINHEIGHT="'+maginheight+'"'

    if scrolling is not None:
      Text=Text+' SCROLLING="'+scrolling+'"'

    if noresize is not None:
      Text=Text+' NORESIZE'

    if frameborder is not None and frameborder=="no":
      Text=Text+' FRAMEBORDER="no"'

    Text=Text+'> </FRAME>\n'
    return Text

  def Frame(self,src,name=None,maginwidth=None,maginheight=None,scrolling=None,noresize=None,frameborder=None):
    if not self.CanAddTag():
      print "Frame: Documento no tiene FRAMESET correcto."
      return
    if self.nFramesAdded<self.nFrames:
      self.HTMLText.append(self._WriteFrame(src,name,maginwidth,maginheight,scrolling,noresize,frameborder))
      self.nFramesAdded=self.nFramesAdded+1
    else:
      print "Error, no se puede añadir Frame."


TravelBookLanguage="Spanish"
TravelBookCharacter="Barbarian"

def GetEnvValue(val):
  if val=="Language":
    return TravelBookLanguage
  elif val=="Character":
    return TravelBookCharacter
  else:
    print "BHTMLLib.GetEnvValue() -> Error: Unknown environment string.",val







"""
if __name__ == '__main__':
  class B_TravelBook(B_HTMLDocBody):
    def __init__(self,filename,title):
      B_HTMLDocBody.__init__(self,filename,title)
      self.GenerateHeader()
      self.GenerateBody()
      self.HyperLink("Índice","C:/Tmp/TravelBook/Index.htm")
      self.ImageLink("C:/Tmp/fpcreate.gif","C:/Tmp/TravelBook/Index.htm")
      self.Paragraph("Latas de la competencia.","CENTER")
      self.Paragraph(self._WriteHyperLink("Let the sun shine!","C:/"),"CENTER")
      self.CloseBody()
      self.CloseHTML()


  class B_TravelBookFrame(B_HTMLDocFrames):
    def __init__(self,filename,title):
      B_HTMLDocFrames.__init__(self,filename,title)
      self.GenerateHeader()
      self.GenerateFrameSet("COLS",["20%","80%"])
      self.Frame("c:/tmp/FileName.html")
      self.Frame("c:/tmp/FileName.html")
      self.CloseFrameSet()
      self.CloseHTML()


  TrBook=B_TravelBook("c:/tmp/FileName.html","TravelBook")
  print TrBook.HTMLText
  TrBook.WriteHTMLFile()
  
  
  TrBookFrame=B_TravelBookFrame("c:/tmp/FileNameFrame.html","TravelBook")
  print TrBookFrame.HTMLText
  TrBookFrame.WriteHTMLFile()
"""


