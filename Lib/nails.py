#----------------------------------------------------------------------
#   Proposito : Futil intento de automatizar la trampa
#              de pinchos para las futuras generaciones
#
#   Culpable  : Jose Dario Halle Cano
#
#   ToDo      : Sonidos y Polvo
#----------------------------------------------------------------------

##--------------------------------------------------------
##---                      Ejemplo                     ---
##--------------------------------------------------------
##
##import nails
##
###  crea la trampa
##
##trampa =   nails.NailTrap(5000,2000,15000)
##
### Agrega las puertas
##trampa.AddSector(       19058, 10085, -4519 )
##trampa.AddSector(       19027, 10085, -1514 )
##trampa.AddSector(       18521, 10085, 1049  )
##
###define que sectores activaran la trampa
##trampa.ActivationSector(19027, 10085, -1514 )
##
### Agrega todo los objetos Pincho o afines asociados a la trampa
##trampa.AddPincho("Pinch1")
##trampa.AddPincho("Pinch2")
##trampa.AddPincho("Pinch3")
##trampa.AddPincho("Pinch4")
##trampa.AddPincho("Pinch5")
##trampa.AddPincho("Pinch6")
##
##------------------------------------------------------------------------


import Doors
import Bladex
import Room
import Sounds
import ObjStore

TP_Opened   = 0
TP_Working  = 1

################################################################################################################

Sonido_Trampa_Activada = Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'SonidoActivacion')
Sonido_Trampa_Activada.Volume=1
Sonido_Trampa_Activada.MinDistance=15000
Sonido_Trampa_Activada.MaxDistance=20000

Sonido_Trampa_Bajando    = Sounds.CreateEntitySound('../../Sounds/stone-slide-and-hit.wav', 'SonidoPiedra')
Sonido_Trampa_Bajando.Volume=1
Sonido_Trampa_Bajando.MinDistance=15000
Sonido_Trampa_Bajando.MaxDistance=20000

Sonido_Trampa_Subiendo   = Sounds.CreateEntitySound('../../Sounds/drawbridge-loop.wav', 'SonidoCadena1')
Sonido_Trampa_Subiendo.Volume=1
Sonido_Trampa_Subiendo.MinDistance=15000
Sonido_Trampa_Subiendo.MaxDistance=20000

Sonido_Trampa_Reactivada = Sounds.CreateEntitySound('../../Sounds/metal-lever3.wav', 'SonidoReactivacion')
Sonido_Trampa_Reactivada.Volume=1
Sonido_Trampa_Reactivada.MinDistance=15000
Sonido_Trampa_Reactivada.MaxDistance=20000

Sonido_Trampa_Hit        = Sounds.CreateEntitySound('../../Sounds/Stone-door-shut.wav', 'Hit2')
Sonido_Trampa_Hit.Volume=1
Sonido_Trampa_Hit.MinDistance=15000
Sonido_Trampa_Hit.MaxDistance=20000

################################################################################################################

TrapList={}








def MataAlJugador():
  char      = Bladex.GetEntity("Player1")
  #char.Life = 0

def EntroElIluso(sectorindex,entityname):
  # Muere estupido Iluso
  sec = TrapList[sectorindex]
  if sec.Active:
     if sec.State == TP_Opened:
        sec.CloseTrap()
        if entityname == "Player1":
          Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, MataAlJugador, (),"MataAlJugador")


#
# Clase que implementa una trampa de pinchos
#---------------------------------------------
class NailTrap:

  def __init__(self,Tam,Ups,Downs):
    self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
    ObjStore.ObjectsStore[self.ObjId]=self
    self.agujas      = [ ]
    self.sectores    = [ ]
    self.size        = Tam
    self.Active      = 1
    self.SpeedOn     = Downs
    self.SpeedOff    = Ups
    self.State       = TP_Opened
    self.SoundX      = None
    self.SoundY      = None
    self.SoundZ      = None
    self.ypos        = 0

  def persistent_id(self):
    return self.ObjId

  def __getstate__(self):
    return (1,
            self.ObjId,
            self.agujas,
            self.sectores,
            self.size,
            self.Active,
            self.SpeedOn,
            self.SpeedOff,
            self.State,
            self.SoundX,
            self.SoundY,
            self.SoundZ,
            self.ypos
           )

  def __setstate__(self,parm):
    if parm[0]==1:
      self.ObjId=parm[1]
      ObjStore.ObjectsStore[self.ObjId]=self
      self.agujas=parm[2]
      self.sectores=parm[3]
      self.size=parm[4]
      self.Active=parm[5]
      self.SpeedOn=parm[6]
      self.SpeedOff=parm[7]
      self.State=parm[8]
      self.SoundX=parm[9]
      self.SoundY=parm[10]
      self.SoundZ=parm[11]
      self.ypos=parm[12]
    else:
      print "Version mismatch in NailTrap"
      self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
      ObjStore.ObjectsStore[self.ObjId]=self
      self.agujas      = [ ]
      self.sectores    = [ ]
      self.size        = 1
      self.Active      = 1
      self.SpeedOn     = 0
      self.SpeedOff    = 0
      self.State       = 0
      self.SoundX      = 0
      self.SoundY      = 0
      self.SoundZ      = 0
      self.ypos        = 0


  def AddPincho(self,Name):
     self.agujas.append(Name)
     ob = Bladex.GetEntity(Name)
     self.ypos = ob.Position[1]

  def AbreteSesamus(self):
    self.OpenTrap()
    Bladex.AddScheduledFunc(Bladex.GetTime()+10.0, self.SeteaElValue, (),"SeteaElValue")

  def SeteaElValue(self):
    self.State = TP_Opened

  def PinchosSiguenTecho(self):

     for Puert in self.agujas:
        Pincho = Bladex.GetEntity(Puert)
        X      = Pincho.Position[0]
        Z      = Pincho.Position[2]
        D      = self.sectores[0].sld_area().Displacement
        Y      = self.ypos + D
        Pincho.Position = X,Y,Z

     if self.State <> TP_Opened:
        Bladex.AddScheduledFunc(Bladex.GetTime()+0.025, self.PinchosSiguenTecho, (),"PinchosSiguenTecho")


  def AddSector(self,x,y,z):

     Puerta_Pinchos=Doors.CreateDoor("PuertaPinchos"+`len(self.sectores)`, (x,y,z), (0,1,0), 50, self.size, Doors.OPENED)
     Puerta_Pinchos.Squezze = 1

     Puerta_Pinchos.opentype       = Doors.UNIF
     Puerta_Pinchos.o_med_vel      = -abs(self.SpeedOff)
     Puerta_Pinchos.o_med_displ    = self.size
     Puerta_Pinchos.OnEndOpenFunc  = ""

     Puerta_Pinchos.closetype      = Doors.AC
     Puerta_Pinchos.c_init_vel     = 0
     Puerta_Pinchos.c_init_displ   = self.size
     Puerta_Pinchos.c_med_vel      = abs(self.SpeedOn)
     Puerta_Pinchos.OnEndCloseFunc = ""

     if(len(self.sectores) == 0):
          Puerta_Pinchos.SetWhileOpenSound(Sonido_Trampa_Subiendo)
          Puerta_Pinchos.SetEndOpenSound(Sonido_Trampa_Reactivada)

          Puerta_Pinchos.SetWhileCloseSound(Sonido_Trampa_Bajando)
          Puerta_Pinchos.SetEndCloseSound(Sonido_Trampa_Hit)


     self.sectores.append(Puerta_Pinchos)

  def ActivationSector(self,x,y,z):

     Sec                                = Bladex.GetSector(x,y,z)
     Sec.OnEnter                        = EntroElIluso
     TrapList[Sec.Index]                = self
     self.SoundX                        = x
     self.SoundY                        = y
     self.SoundZ                        = z


  def OpenTrap(self):
      self.State = TP_Working
      # sectors
      for Puert in self.sectores:
        Puert.OpenDoor()


  def CloseTrap(self):
      self.State = TP_Working
      self.PinchosSiguenTecho()

      # Pinchos
      Sonido_Trampa_Activada.Play(self.SoundX,self.SoundY,self.SoundZ)

      # sectors
      for Puert in self.sectores:
        Puert.CloseDoor()
        Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, self.AbreteSesamus, (),"AbreteSesamus")



def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(
     TrapList,
    )
  p.dump(d)
  funcfile.close()


def LoadData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  p.persistent_load=GameStateAux.persistent_load
  d=p.load()
  funcfile.close()
  print d

  global TrapList

  TrapList    = d[0]

import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
