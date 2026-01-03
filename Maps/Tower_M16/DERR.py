import Bladex



###################
#     Sonidos     #
###################

derrumbesuelopiedra=Bladex.CreateSound("../../Sounds/Stone-floor-collapse.wav", "DerrumbeSueloPiedra")
derrumbesuelopiedra.Volume=1
derrumbesuelopiedra.MinDistance=12000
derrumbesuelopiedra.MaxDistance=60000

derrumbesueloagua=Bladex.CreateSound("../../Sounds/impact-watersplash.wav", "DerrumbeSueloAgua")
derrumbesueloagua.Volume=1
derrumbesueloagua.MinDistance=12000
derrumbesueloagua.MaxDistance=60000


#############################################
#     Derrumbamiento SUELO LAVA             #
#############################################

derr1=Bladex.GetSector(57500, 20500, -11400)
derr1.Active=0
derr2=Bladex.GetSector(58500, 20700, -23500)
derr2.Active=0
derr3=Bladex.GetSector(58500, 20700, -29000)
derr3.Active=0



derr1.InitBreak((0, 900, 0), (2500, 0, 0), (300, 0.0, 1850))
derr2.InitBreak((0, 900, 0), (2500, 0, 0), (600, 0.0, 1850))
derr3.InitBreak((0, 900, 0), (2500, 0, 0), (220, 0.0, 1850))

###sector que activa la rotura?????
sectorderr=Bladex.GetSector(58500, 18700, -29000)

sectorderr.OnWalkOn=Derrumba