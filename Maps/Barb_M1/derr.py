###################
#     Sonidos     #
###################

derrumbesuelopiedra=Bladex.CreateSound("../../Sounds/Stone-floor-collapse.wav", "DerrumbeSueloPiedra")
derrumbesuelopiedra.Volume=1
derrumbesuelopiedra.MinDistance=5000
derrumbesuelopiedra.MaxDistance=40000

derrumbesueloagua=Bladex.CreateSound("../../Sounds/impact-watersplash.wav", "DerrumbeSueloAgua")
derrumbesueloagua.Volume=1
derrumbesueloagua.MinDistance=5000
derrumbesueloagua.MaxDistance=40000


#############################################
#     Derrumbamiento SUELO MADERA           #
#############################################

derr1=Bladex.GetSector(-166000,-14900,215500)
derr1.Active=0
derr2=Bladex.GetSector(-166000,-14900,213000)
derr2.Active=0
derr3=Bladex.GetSector(-168000,-14900,212500)
derr3.Active=0
derr4=Bladex.GetSector(-162500,-14900,213200)
derr4.Active=0

derr1.InitBreak((0, 150, 0), (2650, 0, 1500), (310, 0.0, 650))
derr2.InitBreak((0, 150, 0), (2650, 0, 1500), (310, 0.0, 650))
derr3.InitBreak((0, 150, 0), (2650, 0, 1500), (310, 0.0, 650))
derr4.InitBreak((0, 150, 0), (2650, 0, 1500), (310, 0.0, 650))


###sector que activa la rotura
sectorderr=Bladex.GetSector(-165000,-15900,213000)


sectorderr.OnWalkOn=Derrumba


#--------------------DERRUMBAMIENTO-CASA-TORRE----------------





#--------------------DERRUMBAMIENTO-CASA-JEFE----------------



#sderr4=Bladex.GetSector(-77000,-35600,159000)
#sderr4.Active=0

#sderr5=Bladex.GetSector(-77000,-35600,155000)
#sderr5.Active=0