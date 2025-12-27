


import string
# Para las pruebas fuera de Blade
import sys
sys.path.append("C:\\Blade\\Lib")


import BHTMLLib
import shutil



class B_TrvBMenu(BHTMLLib.B_HTMLDocBody):
  def __init__(self,filename,title,depends_race=0,submenu_path="",background=None):
    BHTMLLib.B_HTMLDocBody.__init__(self,filename,title)
    self.Places=[]
    self.BackGround=background
    self.DependsOnRace=depends_race
    self.SubMenuPath=submenu_path


  def CreateHTML(self):
    self.GenerateHeader()
    self.GenerateBody(background=self.BackGround,watermark=1)

    for i in self.Places:
      self.Paragraph(self._WriteHyperLink(i[0],i[1],"MainArea"),"CENTER")

    self.CloseBody()
    self.CloseHTML()


  def AddPlace(self,placename,filename):
    for i in self.Places:
      if i==i[0]:
        return

    if self.DependsOnRace==0:
      self.Places.append((placename,"C:/Blade/Data/TravelBook/"+
                                    BHTMLLib.GetEnvValue("Language")+self.SubMenuPath+filename))
    else:
      self.Places.append((placename,"C:/Blade/Data/TravelBook/"+
                                    BHTMLLib.GetEnvValue("Language")+self.SubMenuPath+
                                    BHTMLLib.GetEnvValue("Character")+"/"+filename))


class B_TrvBText(BHTMLLib.B_HTMLDocBody):
  def __init__(self,filename="C:\\Blade\\Data\\TravelBook\\CreationText.html",title="Historia del reino",background=None):
    BHTMLLib.B_HTMLDocBody.__init__(self,filename,title)
    self.Places=[]
    self.BackGround=background

  def CreateHTML(self):
    self.GenerateHeader()
    self.GenerateBody(background=self.BackGround,watermark=1)

    self.Paragraph(self._WriteHyperLink("Características personaje","C:/"),"CENTER")
    self.CloseBody()
    self.CloseHTML()






class B_TrvBMain(BHTMLLib.B_HTMLDocFrames):
  def __init__(self,filename,title,background,submenu_path,depends_race=0):
    BHTMLLib.B_HTMLDocFrames.__init__(self,filename,title)
    self.Places=[]
    self.Background=background
    self.DependsRace=depends_race
    self.SubMenuPath=submenu_path

  def CreateHTML(self):
    # Primero creo los frames para el título, principal y botones de navegación
    self.GenerateHeader()
    self.GenerateFrameSet("ROWS",["64","*","64"],0,0,0)
    #self.GenerateFrameSet("ROWS",["%10","%80","%10"],0)

    idx=string.rfind(self.FileName,'.htm')
    BasePath=self.FileName[:idx]

    idx=string.rfind(self.Background,'.bmp')
    BaseBackground=self.Background[:idx]
    
    Title=BHTMLLib.B_HTMLDocBody(BasePath+"Titulo.html","Titulo")
    Title.GenerateHeader()
    Title.GenerateBody(scroll="no",background=BaseBackground+"_up.bmp")
    Title.Paragraph(self.Title)
    Title.CloseBody()
    Title.CloseHTML()
    Title.WriteHTMLFile()

    Foot=BHTMLLib.B_HTMLDocBody(BasePath+"Foot.html","Foot")
    Foot.GenerateHeader()
    Foot.GenerateBody(scroll="no",background=BaseBackground+"_down.bmp")
    #Foot.Paragraph("Foot")
    Foot.Paragraph(Foot._WriteHyperLink("Volver","C:/Blade/Data/TravelBook/TravelBook.html","_top"),"RIGHT")
    Foot.CloseBody()
    Foot.CloseHTML()
    Foot.WriteHTMLFile()    

    Main=BHTMLLib.B_HTMLDocFrames(BasePath+"Main.html","Main")
    Main.GenerateHeader()
    Main.GenerateFrameSet("COLS",["*","128"],0,0,0)
    #Main.GenerateFrameSet("COLS",["%80","%20"],0)

    # Creo el frame con el menú:
    CreationMenu=B_TrvBMenu(BasePath+"Menu.html","Menu",self.DependsRace,self.SubMenuPath,background=BaseBackground+"_right.bmp")
    for i in self.Places:
      CreationMenu.AddPlace(i[0],i[1])
    CreationMenu.CreateHTML()
    CreationMenu.WriteHTMLFile()

    # Ahora creo las distintas páginas:
    for i in self.Places:
      CreationElement=B_TrvBText(i[1],background=BaseBackground+"_left.bmp")
      CreationElement.CreateHTML()
      CreationElement.WriteHTMLFile()

    Main.Frame("c:/tmp/FileName.html","MainArea",frameborder="no",scrolling="no")
    Main.Frame(CreationMenu)
    Main.CloseFrameSet()
    Main.CloseHTML()
    Main.WriteHTMLFile()

    self.Frame(Title,frameborder="no",scrolling="no",)
    self.Frame(Main,frameborder="no",scrolling="no")
    self.Frame(Foot,frameborder="no",scrolling="no")

    self.CloseFrameSet()
    self.CloseHTML()

  def AddPlace(self,place,filename):
    self.Places.append((place,filename))













