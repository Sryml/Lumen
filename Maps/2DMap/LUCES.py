import Bladex
import Reference
import GotoMapVars

GoodShield	= []
BadShield	= []
Tablillas	= []

###	PRIMER MAPA BARBARO

o=Bladex.CreateEntity("Kashgar","Escudo8",-57636.530000,13900,-19374.975000,"Weapon")
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Kashgar","Escudon",-57636.530000,13900,-19374.975000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)


###	PRIMER MAPA CABALLERO

o=Bladex.CreateEntity("Tabriz","Escudo8",-79169.079000,13900,4672.719000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Tabriz","Escudon",-79169.079000,13900,4672.719000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)


###	PRIMER MAPA ENANO

o=Bladex.CreateEntity("Kazel-Zalam","Escudo8",-103963.620000,13900,-1505.120000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Kazel-Zalam","Escudon",-103963.620000,13900,-1505.120000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)


###PRIMER MAPA AMAZONA

o=Bladex.CreateEntity("Marakamda","Escudo8",-50083.984000,13900,-6576.963000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Marakamda","Escudon",-50083.984000,13900,-6576.963000)
o.Scale=5
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)





####	A ELEGIR ENTRE ESTOS DOS

o=Bladex.CreateEntity("Kelbegen","Escudo8",-90134.749000,13900,1985.339000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Kelbegen","Escudon",-90134.749000,13900,1985.339000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

o=Bladex.CreateEntity("Kelbegen","Tablilla1",-90134.749000,13900,1985.339000)
o.Scale=19
o.Orientation=0.995396,0.095846,0.000000,0.000000
o.RemoveFromWorld()
Tablillas.append(o.Name)

###

o=Bladex.CreateEntity("Tell-Hallaf","Escudo8",-70379.699000,13900,-1797.824000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Tell-Hallaf","Escudon",-70379.699000,13900,-1797.824000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

o=Bladex.CreateEntity("Tell-Hallaf","Tablilla2",-70379.699000,13900,-1797.824000)
o.Scale=19
o.Orientation=0.995396,0.095846,0.000000,0.000000
o.RemoveFromWorld()
Tablillas.append(o.Name)

###	SIGUIENTES POR ESTE ORDEN

o=Bladex.CreateEntity("Ephira","Escudo8",-68459.210000,14000,12682.204000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Ephira","Escudon",-68459.210000,14000,12682.204000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

o=Bladex.CreateEntity("Ephira","Tablilla3",-68459.210000,14000,12682.204000)
o.Scale=19
o.Orientation=0.995396,0.095846,0.000000,0.000000
o.RemoveFromWorld()
Tablillas.append(o.Name)

##

o=Bladex.CreateEntity("Karum","Escudo8",-58187.154000,13900,20706.704000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Karum","Escudon",-58187.154000,13900,20706.704000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)


###	DESDE AQUI PUEDES ELEGIR DOS CAMINOS
##################################################################################


###############################
###	PRIMER CAMINO 3 MAPAS
###############################

##

o=Bladex.CreateEntity("Shalatuwar","Escudo8",-39236.556000,13900,24243.602000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Shalatuwar","Escudon",-39236.556000,13900,24243.602000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)


###	A ELEGIR ENTRE ESTOS DOS

o=Bladex.CreateEntity("Orlok","Escudo8",-13828.658000,13900,23751.465000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Orlok","Escudon",-13828.658000,13900,23751.465000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

##


o=Bladex.CreateEntity("Nemrut","Escudo8",-30310.393000,13900,3890.441000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Nemrut","Escudon",-30310.393000,13900,3890.441000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

o=Bladex.CreateEntity("Nemrut","Tablilla5",-30310.393000,13900,3890.441000)
o.Scale=19
o.Orientation=0.995396,0.095846,0.000000,0.000000
o.RemoveFromWorld()
Tablillas.append(o.Name)



#################################
###	SEGUNDO CAMINO 3 MAPAS
#################################



o=Bladex.CreateEntity("Nejev","Escudo8",-41234.284000,13900,39172.076000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)


o=Bladex.CreateEntity("Nejev","Escudon",-41234.284000,13900,39172.076000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

o=Bladex.CreateEntity("Nejev","Tablilla4",-41234.284000,13900,39172.076000)
o.Scale=19
o.Orientation=0.995396,0.095846,0.000000,0.000000
o.RemoveFromWorld()
Tablillas.append(o.Name)


###	A ELEGIR ENTRE ESTOS DOS


o=Bladex.CreateEntity("Al-Farum","Escudo8",-29326.827000,13900,45394.131000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Al-Farum","Escudon",-29326.827000,13900,45394.131000)
o.Scale=6
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

o=Bladex.CreateEntity("Al-Farum","Tablilla6",-29326.827000,13900,45394.131000)
o.Scale=19
o.Orientation=0.995396,0.095846,0.000000,0.000000
o.RemoveFromWorld()
Tablillas.append(o.Name)

##

o=Bladex.CreateEntity("Xathra","Escudo8",-43869.492000,13900,56313.163000)
o.Scale=8
o.Orientation=0.998630,0.052336,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Xathra","Escudon",-43869.492000,13900,56313.163000)
o.Scale=6
o.Orientation=0.998630,0.052336,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

###########################	TEMPLO DE LA DIOSA

##

o=Bladex.CreateEntity("Ianna","Escudo8",28275.839000,13900,37737.520000)
o.Scale=8
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("NoName0","BladeSword2",30024.165190,6645.251519,38281.893258)
o.Scale=34.204850
o.Orientation=0.769421,0.559017,0.202733,-0.233218
o.RemoveFromWorld()
BadShield.append(o.Name)

#########################	TORRE DE DAL-GURAK

##

o=Bladex.CreateEntity("Dal-Gurak","Escudon",48858.410000,13900,33152.115000)
o.Scale=6
o.Orientation=0.998630,0.052336,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)




#____________________________________
