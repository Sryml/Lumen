import pocimac
import Torchs

## pocima en la escena funesta

o=Bladex.CreateEntity("pofunesta","Pocima50",111726.822000,7230.723000,-34521.094000,"Physic")
o.Scale=1.000000
o.Orientation=0.584950,0.288828,0.644902,0.398137
pocimac.CreatePotion("pofunesta")


## pocima 100 tras trampa flechas

dwarfpocima100a=Bladex.CreateEntity("dwarfpocima100a","Pocima100",-62172.458377,-9206.368936,-112756.747498,"Physic")
dwarfpocima100a.Scale=1.000000
dwarfpocima100a.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("dwarfpocima100a")


## pocima junto a palanca abre barrotes horizontales 

o=Bladex.CreateEntity("po50","Pocima50",-142301.378684,-8405.239702,-46681.950034)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("po50")

#pocima100 hacia el final

dwarfpocima100b=Bladex.CreateEntity("dwarfpocima100b","Pocima100",-224318.893632,-15205.629530,-5840.274948,"Physic")
dwarfpocima100b.Scale=1.000000
dwarfpocima100b.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("dwarfpocima100b")


#pocima100 en la biblioteca

dwarfpocima100c=Bladex.CreateEntity("dwarfpocima100c","Pocima100",-262540.970837,-27409.467547,69071.716703,"Physic")
dwarfpocima100c.Scale=1.000000
dwarfpocima100c.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("dwarfpocima100c")


#pocima100 en la sala de aranias

dwarfpocima100x=Bladex.CreateEntity("dwarfpocima100x","Pocima100",548.588516,-6209.693303,3699.894169,"Physic")
dwarfpocima100x.Scale=1.000000
dwarfpocima100x.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("dwarfpocima100x")

###APAGADO MAGICO DE LA P.... ANTORCHA
############################################

Apagala1Sec = Bladex.GetSector(-145000, -15000, 14000)
Apagala1Sec.OnEnter = Apagala

Apagala2Sec = Bladex.GetSector(-187000, -15000, 23500)
Apagala2Sec.OnEnter = Apagala