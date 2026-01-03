
import Bladex

#*************************************************************************************************
#*******************************     Definiciones para Fires.py         **************************
#*************************************************************************************************

		
def EnciendeAltarFires(FireName,PosFire):
	llamarada=Bladex.CreateEntity(FireName, "Entity Particle System D1", PosFire[0],PosFire[1],PosFire[2])
	llamarada.ParticleType="Flame"
	llamarada.YGravity=-4000.0
	llamarada.Friction=0.12
	llamarada.PPS=300
	llamarada.Velocity=0.0, -2500.0, 0.0
	llamarada.RandomVelocity=45.0
	llamarada.Time2Live=14


def CreateFires():
	EnciendeAltarFires("Palacio_Camera_fuego1.cam",(100000,-1600,209000))
	EnciendeAltarFires("Palacio_Camera_fuego2.cam",(89000,-1600,209000))
	EnciendeAltarFires("Palacio_Camera_fuego3.cam",(99750,-1600,203250))
	EnciendeAltarFires("Palacio_Camera_fuego4.cam",(89000,-1600,203250))


