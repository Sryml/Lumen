import Breakings
import Ontake
import pocimac
import Sparks

##########################################################3



#en cuerpo de guardia
o=Bladex.CreateEntity("NoName0","Axpear",-37750.529837,-5915.050946,-4309.931355,"Weapon")
o.Scale=1.000000
o.Orientation=0.303158,0.231673,0.561631,-0.734161
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("NoName1","Guadanya",-33254.949986,-5367.461991,-5896.554466,"Weapon")
o.Scale=1.000000
o.Orientation=0.483785,-0.485599,-0.608201,-0.400297
ItemTypes.ItemDefaultFuncs (o)


#en la torre rota
o=Bladex.CreateEntity("NoName8","LongSword",71568.542917,-15232.482364,-22054.390393,"Weapon")
o.Scale=1.000000
o.Orientation=0.963400,-0.027691,-0.260586,0.056462
ItemTypes.ItemDefaultFuncs (o)


#segundo piso torre
o=Bladex.CreateEntity("NoName9","Axpear",64250.671328,-3424.754958,-38605.500534,"Weapon")
o.Scale=1.000000
o.Orientation=0.103192,0.251373,0.657377,-0.702865
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("NoName10","Lanza",64340.717820,-3315.605562,-37676.205187,"Weapon")
o.Scale=1.000000
o.Orientation=0.640316,0.581311,-0.408279,0.292200
ItemTypes.ItemDefaultFuncs (o)



#trampa con orco jefe
o=Bladex.CreateEntity("tombmaz2","Maza2",-4798.432211,5902.751039,-35819.014151,"Weapon")
o.Scale=1.000000
o.Orientation=0.236530,0.673311,-0.665879,-0.217512
ItemTypes.ItemDefaultFuncs (o)




#zona secreta con zombies
o=Bladex.CreateEntity("tombmartillo","Martillo",96252.208979,8942.689614,15268.777832,"Weapon")
o.Scale=1.000000
o.Orientation=0.687117,0.719238,-0.082426,-0.061428
ItemTypes.ItemDefaultFuncs (o)

powp_PP=Bladex.CreateEntity("tombPWP","PowerPotion",92452.052058,8915.854084,16489.239254,"Physic")
powp_PP.Scale=1.000000
powp_PP.Orientation=0.363617,-0.064629,-0.927222,-0.062166
pocimac.CreatePowerPotion("tombPWP")



#tumbas de los nobles
o=Bladex.CreateEntity("tombCrushHammer","CrushHammer",44551.140844,-1885.549668,58913.603463,"Weapon")
o.Scale=1.000000
o.Orientation=0.999714,0.023915,0.000691,-0.000048
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("tombamuletfa","Amuletofantasma",34328.831229,-1834.169291,58066.556699,"Physic")
o.Scale=1.000000
o.Orientation=0.999922,-0.000192,0.012471,-0.000144
ItemTypes.ItemDefaultFuncs (o)




#en zona secreta
o=Bladex.CreateEntity("TombDeathsword","DeathSword",88206.663653,7968.226267,57452.145969,"Weapon")
o.Weapon=1
o.Scale=1.000000
o.Orientation=0.205829,-0.005371,0.978544,0.007585
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("TombEscudo1","Escudo1",91446.127909,7893.027106,54074.360618,"Weapon")
o.Weapon=1
o.Scale=1.000000
o.Orientation=0.634174,0.488738,-0.519645,-0.298207
ItemTypes.ItemDefaultFuncs (o)




#armaduras en la tumba
o=Bladex.CreateEntity("tombarmK","ArmaduraCaballeroLigera",38680.240498,3702.505647,11951.223384,"Physic")
o.Solid=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("tombarmD","ArmaduraEnanoLigera",38668.082564,3774.049787,-14382.696468,"Physic")
o.Solid=0
o.Scale=1.000000
o.Orientation=0.700331,0.713589,0.015919,-0.008536
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("tombaxe4","Hacha4",37471.980932,4716.491431,-15086.114352,"Weapon")
o.Scale=1.000000
o.Orientation=0.452319,0.275077,-0.632900,-0.564958
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("tombelfsw","Espadaelfica",38467.579596,3977.740652,11223.446006,"Weapon")
o.Scale=1.000000
o.Orientation=0.598419,0.595107,-0.391628,0.366563
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("tombescarm","Escudo1",37624.659601,4781.779930,11891.881622,"Weapon")
o.Scale=1.000000
o.Orientation=0.763593,0.002286,0.603332,-0.230026
ItemTypes.ItemDefaultFuncs (o)