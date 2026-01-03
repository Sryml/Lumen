import Bladex
import Reference
import GotoMapVars

GoodShield	= []
BadShield	= []
Tablillas	= []



o=Bladex.CreateEntity("Kelbegen","Escudo8",-90134.749000,10000,1985.339000)
o.Scale=16
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Kelbegen","Tablilla1",-90134.749000,10000,1985.339000)
o.Scale=32
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

###

o=Bladex.CreateEntity("Tell-Hallaf","Escudo8",-70379.699000,10000,-1797.824000)
o.Scale=16
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Tell-Hallaf","Tablilla2",-70379.699000,10000,-1797.824000)
o.Scale=32
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

###

o=Bladex.CreateEntity("Ephira","Escudo8",-68459.210000,10000,12682.204000)
o.Scale=16
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Ephira","Tablilla3",-68459.210000,10000,12682.204000)
o.Scale=32
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)


###

o=Bladex.CreateEntity("Nejev","Escudo8",-41234.284000,10000,39172.076000)
o.Scale=16
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)


o=Bladex.CreateEntity("Nejev","Tablilla4",-41234.284000,10000,39172.076000)
o.Scale=32
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

##

o=Bladex.CreateEntity("Nemrut","Escudo8",-30310.393000,10000,3890.441000)
o.Scale=16
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Nemrut","Tablilla5",-30310.393000,10000,3890.441000)
o.Scale=32
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

###

o=Bladex.CreateEntity("Al-Farum","Escudo8",-29326.827000,10000,45394.131000)
o.Scale=16
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
GoodShield.append(o.Name)

o=Bladex.CreateEntity("Al-Farum","Tablilla6",-29326.827000,10000,45394.131000)
o.Scale=32
o.Orientation=0.997564,0.069756,0.000000,0.000000
o.RemoveFromWorld()
BadShield.append(o.Name)

##

# Ask Jose Luis about this, do not know how this stuff goes
o=Bladex.CreateEntity("Ianna","BladeSword2",28275.839000,10000,37737.520000)
#o=Bladex.CreateEntity("Ianna","Escudo8",28275.839000,10000,37737.520000)
o.Scale=34.204850
#o.Scale=16 # No object
o.Orientation=0.769421,0.559017,0.202733,-0.233218
#o.Orientation=0.997564,0.069756,0.000000,0.000000 # No object
#o.RemoveFromWorld()
GoodShield.append(o.Name)

#o=Bladex.CreateEntity("NoName0","BladeSword2",30024.165190,6645.251519,38281.893258)
#o.Scale=34.204850
#o.Orientation=0.769421,0.559017,0.202733,-0.233218
#o.RemoveFromWorld()
#BadShield.append(o.Name)

#########################	TORRE DE DAL-GURAK

##

o=Bladex.CreateEntity("Dal-Gurak","Escudon",48858.410000,10000,33152.115000)
o.Scale=12
o.Orientation=0.998630,0.052336,0.000000,0.000000
BadShield.append(o.Name)
#____________________________________
