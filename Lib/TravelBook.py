

# Para las pruebas fuera de Blade
##import sys
##sys.path.append("C:\\Blade\\Lib")


import BHTMLLib
import TrvBookLib
import CharStatusLib




# Solamente depende de por donde hayas estado.
class B_CreationHistory(TrvBookLib.B_TrvBMenu):
  def __init__(self,filename,title):
    TrvBookLib.B_TrvBMenu.__init__(self,filename,title,0,"/CreationHistory/")


# Depende de por donde hayas estado y del personaje que se lleve.
class B_KingdomHistory(TrvBookLib.B_TrvBMenu):
  def __init__(self,filename,title):
    TrvBookLib.B_TrvBMenu.__init__(self,filename,title,1,"/KingdomHistory/")


# Solamente depende de por donde hayas estado.
class B_TravelNotes(TrvBookLib.B_TrvBMenu):
  def __init__(self,filename,title):
    TrvBookLib.B_TrvBMenu.__init__(self,filename,title,0,"/TravelNotes/")



#  ------------------------------------- Libro de viajes -------------------------------------

class B_TravelBook(BHTMLLib.B_HTMLDocBody):
  def __init__(self,filename="C:/Blade/Data\\TravelBook\\TravelBook.html",title="Libro de viaje"):
    BHTMLLib.B_HTMLDocBody.__init__(self,filename,title)
    self.CanViewKingdomHistory=0
    self.CanViewCreationHistory=0
    self.CanViewAnthem=0
    self.CanViewTravelNotes=0

  def CreateHTML(self):
    self.GenerateHeader()
    self.GenerateBody(150,"Bitmaps/menu principal sin textos.bmp",scroll="no")

    self.Paragraph(self._WriteHyperLink("Características personaje","C:/Blade/Data/TravelBook/CharStatus.html"),"CENTER")

    if self.CanViewKingdomHistory:
      self.Paragraph(self._WriteHyperLink("Historia del reino","C:/Blade/Data/TravelBook/KingdomFrame.html"),"CENTER")
    else:
      self.Paragraph("Historia del reino","CENTER")

    if self.CanViewCreationHistory:
      self.Paragraph(self._WriteHyperLink("Historia de la creación","C:/Blade/Data/TravelBook/CreationFrame.html"),"CENTER")
    else:
      self.Paragraph("Historia de la creación","CENTER")

    if self.CanViewAnthem:
      self.Paragraph(self._WriteHyperLink("El cantar de Blade","C:/"),"CENTER")
    else:
      self.Paragraph("El cantar de Blade","CENTER")

    if self.CanViewTravelNotes:
      self.Paragraph(self._WriteHyperLink("Notas del viaje","C:/"),"CENTER")
    else:
      self.Paragraph("Notas del viaje","CENTER")

    self.CloseBody()
    self.CloseHTML()





def AddCreationHistory(name,file):
  Creation.Reset()
  Creation.AddPlace(name,file)
  Creation.CreateHTML()
  Creation.WriteHTMLFile()


def AddKingdomHistory(name,file):
  Kingdom.Reset()
  Kingdom.AddPlace(name,file)
  Kingdom.CreateHTML()
  Kingdom.WriteHTMLFile()


def AddTravelNote(name,file):
  Notes.Reset()
  Notes.AddPlace(name,file)
  Notes.CreateHTML()
  Notes.WriteHTMLFile()


def CanViewCreationHistory():
  TravelBook.Reset()
  TravelBook.CanViewCreationHistory=1
  TravelBook.CreateHTML()
  TravelBook.WriteHTMLFile()

def CanViewKingdomHistory():
  TravelBook.Reset()
  TravelBook.CanViewKingdomHistory=1
  TravelBook.CreateHTML()
  TravelBook.WriteHTMLFile()

def CanViewAnthem():
  TravelBook.Reset()
  TravelBook.CanViewAnthem=1
  TravelBook.CreateHTML()
  TravelBook.WriteHTMLFile()

def CanViewTravelNotes():
  TravelBook.Reset()
  TravelBook.CanViewTravelNotes=1
  TravelBook.CreateHTML()
  TravelBook.WriteHTMLFile()





TravelBook=B_TravelBook()
TravelBook.CanViewCreationHistory=1
TravelBook.CanViewKingdomHistory=1
TravelBook.CreateHTML()
TravelBook.WriteHTMLFile()




Creation=B_CreationHistory("C:/Blade/Data/TravelBook/CreationMenu.html","Historia de la creación")
##Creation.AddPlace("Localización 1","DE LA CREACIÓN DE LA TIERRA Y LA EDAD DE ORO.html")
##Creation.AddPlace("Localización 2","DE LA LLEGADA DE ASHERAT.html")
Creation.CreateHTML()
Creation.WriteHTMLFile()



Kingdom=B_KingdomHistory("C:/Blade/Data/TravelBook/KingdomMenu.html","Historia del reino")
##Kingdom.AddPlace("Localización 1","Kashgar.html")
##Kingdom.AddPlace("Localización 2","Kelbegen.html")
Kingdom.CreateHTML()
Kingdom.WriteHTMLFile()



Notes=B_TravelNotes("C:/Blade/Data/TravelBook/NotesMenu.html","Historia del reino")
Notes.CreateHTML()
Notes.WriteHTMLFile()




CharStatus=CharStatusLib.B_CharStatus("C:/Blade/Data/TravelBook/","Estadísticas",None)
CharStatus.CreateHTML()


