import Bladex
import EnmGenRnd
import B3DLib
import ReadGSFile
import Doors
import Button
import Sounds
import Breakings
import Actions
import EnemyTypes




######################
#     Particulas     #
######################

Bladex.AddParticleGType("Tierra2x","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=210
	g=190
	b=140
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("Tierra2x",i,r,g,b,a,size)


Bladex.AddParticleGType("Tierra3x","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=40
	g=30
	b=0
	a=255*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra3x",i,r,g,b,a,size)


###################################################
#     Funciones complementarias del generador     #
###################################################




#######################
#     Generadores     #
#######################



res=ReadGSFile.ReadGhostSectorFile("cementerio.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1

	
generadorT1 = EnmGenRnd.CreateEnemiesGenerator(6, 2)
generadorT1.CallBak = CreaSkeletoDichoso
generadorT1.AddPoint((54000,6800 ,-3000),("TombGen11Skl_1", "Skeleton", "Espadaromana", 0, "Escudo5", 1), "Skl_appears1",4)
generadorT1.AddPoint((60500,6800 ,-2750),("TombGen11Skl_2", "Skeleton", "Espadaelfica", 0, "Escudo2", 1), "Skl_appears1",5)
generadorT1.AddPoint((70000,6800 ,-3500),("TombGen11Skl_3", "Skeleton", "Hacha4", 0, "Escudo2", 1), "Skl_appears1",6)
generadorT1.AddPoint((74750,6800 ,6500),("TombGen11Skl_4", "Skeleton", "Maza2", 0, "Escudo1", 1), "Skl_appears1",7)
generadorT1.AddPoint((68000,6800 ,3500),("TombGen11Skl_5", "Skeleton", "Hacha3", 0, "Escudo1", 1), "Skl_appears1",8)
generadorT1.AddPoint((62000,6800 ,750),("TombGen11Skl_6", "Skeleton", "HookSword", 0, "Escudo1", 1), "Skl_appears1",9)


generadorT1.InitGenFunc=SaltaTierraGen2
generadorT1.Activate()
generadorT1.FinishGenFunc=Abrir


#print("poniendo el trigger sector")
Bladex.SetTriggerSectorFunc("cementerio", "OnEnter", EntroEnTriggerSector)

#char.Life = 30000