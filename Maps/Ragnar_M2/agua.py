import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import GameText
import Scorer
import math

	
	
scam=Bladex.GetSector(-90800.626477, -8612.85728787, 70714.54)
scam.OnEnter=eSceneCam
		
	
#-----------------------AGUA------------------------------------------------
############
####### PILONCILLO DONDE LAS ANTORCHAS

agua_ANt=Bladex.CreateEntity("agua_ANt","Entity Water",-99000,-3900,39250)
agua_ANt.Reflection=1.3
agua_ANt.Color=5,4,4




agua_let=Bladex.CreateEntity("agua_let","Entity Water",-113000,14700,71250)
agua_let.Reflection=1.3
agua_let.Color=11,7,5

agua_let1=Bladex.CreateEntity("agua_let1","Entity Water",-102750,19000,69250)
agua_let1.Reflection=1.3
agua_let1.Color=5,4,4

agua_let2=Bladex.CreateEntity("agua_let2","Entity Water",-72500,9010,69250)
agua_let2.Reflection=1.3
agua_let2.Color=5,4,4

agua_let2=Bladex.CreateEntity("agua_let2","Entity Water",-72500,9010,71250)
agua_let2.Reflection=1.3
agua_let2.Color=5,4,4

agua_cho1=Bladex.CreateEntity("agua_cho1","Entity Water",-86500,9010,71000)
agua_cho1.Reflection=1.3
agua_cho1.Color=5,3,1


agua_cho2=Bladex.CreateEntity("agua_cho2","Entity Water",-79000,9010,63000)
agua_cho2.Reflection=1.3
agua_cho2.Color=3,2,1


agua_ele=Bladex.CreateEntity("agua_ele","Entity Water",-126050,9580,48500)
agua_ele.Reflection=0.9
agua_ele.Color=13,10,5

##########bajando a las mazmorras
agua_pilon=Bladex.CreateEntity("agua_pilon","Entity Water",-73500,18515,71000)
agua_pilon.Reflection=0.0
agua_pilon.Color=12,8,6


agua_pilon2=Bladex.CreateEntity("agua_pilon2","Entity Water",-77750,15750,59500)
agua_pilon2.Reflection=0.0
agua_pilon2.Color=12,8,6

#############almacen del kaos

agua_pilonk=Bladex.CreateEntity("agua_pilonk","Entity Water",-107750,1250,-86750)
agua_pilonk.Reflection=0.0
agua_pilonk.Color=8,8,8

agua_pilonk2=Bladex.CreateEntity("agua_pilonk2","Entity Water",-107750,1250,-89750)
agua_pilonk2.Reflection=0.0
agua_pilonk2.Color=8,8,6



Bladex.AddParticleGType("AguaC2","WaterParticle",1,60)

for i in range(60):
	r=90
	g=100
	b=100
	a=60
	size=80.0
	Bladex.SetParticleGVal("AguaC2",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma2","SmokeParticle",1,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=120
	g=120
	b=120
	#a=255*math.sqrt(1.0-aux)
	a=255
	size=500.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma2",i,r,g,b,a,size)


#char.Position = -45250, 2000,-30000


#FUENTE VIDA

###chorro1
CreateCascada1("chorro1",(-106750,200,-86750),(0.0, 0.0, -450.0),(-1000.0, 0.0, 0.0),(-106950,1250,-86750),15)

###chorro2
CreateCascada1("chorro2",(-106750,200,-89750),(0.0, 0.0, -450.0),(-1000.0, 0.0, 0.0),(-106950,1250,-89750),15)




