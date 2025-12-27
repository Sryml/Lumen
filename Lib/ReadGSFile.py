





import re
import sys
import string
#import win32dbg


GSPattern=r"[^a-zA-Z0-9.:\\\-_/]*"

def __ReadGSLine(fileobject):
  Line=fileobject.readline()
  if(Line==None):  # Estoy en EOF
    raise EOFError

  return string.strip(Line)


def __ReadGhostSector(fileobject):
  Line=__ReadGSLine(fileobject)
  GSDesc={}
  GSDesc["Vertex"]=[]

  # Primero busco el BeginGhostSector
  BeginNotFound=1
  while BeginNotFound:
    Line=__ReadGSLine(fileobject)

    res=re.split(GSPattern,Line)
    if res[0]=="BeginGhostSector":
      break

  Line=__ReadGSLine(fileobject)
  res=re.split(GSPattern,Line)
  while res[0]!="EndGhostSector":
    Tag=res[0]
    if Tag=="Name":
      GSDesc["Name"]=res[1]
    elif Tag=="FloorHeight":
      GSDesc["FloorHeight"]=-1000*string.atof(res[1])
    elif Tag=="RoofHeight":
      GSDesc["RoofHeight"]=-1000*string.atof(res[1])
    elif Tag=="Vertex":
      GSDesc["Vertex"].append( (1000*string.atof(res[1]),-1000*string.atof(res[2])) )
    elif Tag=="Grupo":
      GSDesc["Grupo"]=res[1]
    elif Tag=="Sonido":
      GSDesc["Sonido"]=res[1]
    elif Tag=="Volumen":
      GSDesc["Volumen"]=string.atof(res[1])
    elif Tag=="VolumenBase":
      GSDesc["VolumenBase"]=string.atof(res[1])
    elif Tag=="DistanciaMinima":
      GSDesc["DistanciaMinima"]=string.atof(res[1])
    elif Tag=="DistanciaMaxima":
      GSDesc["DistanciaMaxima"]=string.atof(res[1])
    elif Tag=="DistMaximaVertical":
      GSDesc["DistMaximaVertical"]=string.atof(res[1])
    elif Tag=="Escala":
      GSDesc["Escala"]=string.atof(res[1])
    Line=__ReadGSLine(fileobject)
    res=re.split(GSPattern,Line)

  return GSDesc






def ReadGhostSectorFile(filename):
  print filename
#  win32dbg.set_trace()
  f=open(filename,"rt")
  ret=[]
  CurrLine=__ReadGSLine(f)
  while CurrLine!="":
    res=re.split(GSPattern,CurrLine)
    if res[0]=="NumGhostSectors":
      for i in range(int(res[1])):
        dsc=__ReadGhostSector(f)
        ret.append(dsc)
        #print "Dsc: ",dsc
        #print "Bladex.AddGhostSector(\"",dsc["Name"],"\", ",
        #print dsc["FloorHeight"],",",
        #print dsc["RoofHeight"],",",
        #print dsc["Vertex"],
        #print ")"
    CurrLine=__ReadGSLine(f)
  f.close()
  return ret




def ProcessGhostSectorFile(filename):
  try:
    import Bladex
    res=ReadGhostSectorFile(filename)
    for igs in res:
      Bladex.AddGhostSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
      Bladex.SetGhostSectorSound(igs["Name"],igs["Sonido"],igs["Volumen"],igs["VolumenBase"],
                               igs["DistanciaMinima"],igs["DistanciaMaxima"],igs["DistMaximaVertical"],
                               igs["Escala"])

  except KeyError:
    print "Error processing",filename,"Unknown attribute"
  except:
    print "Error processing",filename





if __name__ == '__main__':
  res=ReadGhostSectorFile("DesPrb2.sf")
  print res
