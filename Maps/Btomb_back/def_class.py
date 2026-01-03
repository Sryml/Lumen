import Bladex

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para rayos.py           **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

class ENERGIZA_EF:

  def __init__(self,vx,vy,vz):

    ### Luz ###
    self.Ojo=Bladex.CreateEntity(Bladex.GenerateEntityName(),"Entity Spot", vx,vy,vz )
    self.Ojo.Intensity=0
    self.Ojo.Color= 0, 128, 255
    self.Ojo.Precission=0.1
    self.Ojo.CastShadows=0
    self.Ojo.Visible=1
    self.Ojo.SizeFactor=1
    self.Ojo.Flick=0

    ### Ojo ###
    self.cOjo=Bladex.CreateEntity(Bladex.GenerateEntityName(),"Entity Spot", vx,vy,vz )
    self.cOjo.Color= 255, 255, 255
    self.cOjo.Intensity=0
    self.cOjo.Precission=0.1
    self.cOjo.CastShadows=0
    self.cOjo.Visible=1
    self.cOjo.SizeFactor=1
    self.cOjo.Flick=0
    self.cOjo.GlowTexture="GenericParticle"
    self.cOjo.GlowTestZ=0

    ### Particulas ###
    self.parts=Bladex.CreateEntity(Bladex.GenerateEntityName(), "Entity Particle System D1", vx, vy, vz)
    self.parts.ParticleType="Energiza"
    self.parts.Time2Live= 0    #*self.size_factor
    self.parts.YGravity=0
    self.parts.Friction=0
    self.parts.RandomVelocity=-50.0
    self.parts.RandomVelocity_V=0.0
    self.parts.PPS=128


  def SetEnergiza(self,intens):
    self.Ojo.Intensity  = intens
    self.Ojo.SizeFactor = intens

    if(intens<1.5):
      self.parts.Time2Live =  (intens/1.75)*25.0
      self.cOjo.SizeFactor=0
      self.cOjo.Intensity=0
    else:
      self.parts.Time2Live = ((2.0-intens)/0.25)*25.0
      self.cOjo.SizeFactor = intens-1.5
      self.cOjo.Intensity = intens-1.5
