

import string
# Para las pruebas fuera de Blade
import sys
sys.path.append("C:/Blade/Lib")


import BHTMLLib
import shutil
import Bladex


import CharStats
char=Bladex.GetEntity("Player1")
inv=char.GetInventory()


class B_StatusPage(BHTMLLib.B_HTMLDocBody):
  def __init__(self,filename,stats):
    BHTMLLib.B_HTMLDocBody.__init__(self,filename,"Estado")
    self.Stats=stats


  def CreateHTML(self):
    self.GenerateHeader()
    self.GenerateBody(scroll="no")
    self.Paragraph("Estado")

    self.Paragraph(char.Name)
    LifeText="Life: %d/%d"%(char.Life,CharStats.GetCharMaxLife(char.CharType,char.Level))
    self.Paragraph(LifeText)
    self.Paragraph("Level:"+str(char.Level))
    self.Paragraph("Type:"+str(char.CharType))
    self.CloseBody()
    self.CloseHTML()






class B_CharStatus:
  def __init__(self,filepath,title,background):
    self.FilePath=filepath
    self.Background=background
    self.Status=None
    self.Skills=None
    self.Weapons=None
    self.Objects=None


  def CreateHTML(self):
    shutil.copyfile(self.FilePath+"/"+BHTMLLib.GetEnvValue("Language")+"/CharStatus/CharStatus.html",
                    self.FilePath+"/CharStatus.html")
    shutil.copyfile(self.FilePath+"/"+BHTMLLib.GetEnvValue("Language")+"/CharStatus/CharStatusMenu.html",
                    self.FilePath+"/CharStatusMenu.html")

    StatusPage=B_StatusPage(self.FilePath+"StatusPage.html",None)
    StatusPage.CreateHTML()
    StatusPage.WriteHTMLFile()


    SkillsPage=BHTMLLib.B_HTMLDocBody(self.FilePath+"SkillsPage.html","Habilidades")
    SkillsPage.GenerateHeader()
    SkillsPage.GenerateBody(scroll="no")
    SkillsPage.Paragraph("Habilidades")
    SkillsPage.CloseBody()
    SkillsPage.CloseHTML()
    SkillsPage.WriteHTMLFile()


    WeaponsPage=BHTMLLib.B_HTMLDocBody(self.FilePath+"WeaponsPage.html","Armas")
    WeaponsPage.GenerateHeader()
    WeaponsPage.GenerateBody(scroll="no")
    WeaponsPage.Paragraph("Armas")
    for i in range(inv.nWeapons):
      WeaponsPage.Paragraph(inv.GetWeapon(i))
    for i in range(inv.nShields):
      WeaponsPage.Paragraph(inv.GetShield(i))
    WeaponsPage.CloseBody()
    WeaponsPage.CloseHTML()
    WeaponsPage.WriteHTMLFile()


    ObjectsPage=BHTMLLib.B_HTMLDocBody(self.FilePath+"ObjectsPage.html","Objetos")
    ObjectsPage.GenerateHeader()
    ObjectsPage.GenerateBody(scroll="no")
    ObjectsPage.Paragraph("Objetos")
    for i in range(inv.nObjects):
      WeaponsPage.Paragraph(inv.GetObject(i))
    ObjectsPage.CloseBody()
    ObjectsPage.CloseHTML()
    ObjectsPage.WriteHTMLFile()


