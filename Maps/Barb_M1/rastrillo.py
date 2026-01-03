import Sparks
import Locks
import Sounds
import AuxFuncs
import darfuncs
import Stars
import Objects

#---------------------rastrillo---



o=Bladex.CreateEntity("rastrillo1","Rastrillo",-86940.984000,-29341.231000,182983.704000)
o.Static=0
o.Scale=0.878663
o.Orientation=0.573509,0.573509,0.413628,-0.413628

Sparks.SetMetalSparkling("rastrillo1")
#Sparks.SetMetalSparkling("rastrillo2")


################REJA DE ACCESO AL SEGUNDO PISO DE LA CASA DEL JEFE#############
###############################################################################


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja3=Bladex.CreateEntity("Reja3","Rastrillo",-56187.948237,-35532.067430,144479.267747)
reja3.Static=1
reja3.Scale=0.749342
reja3.Orientation=0.705384,0.705384,-0.049325,0.049325
Sparks.SetMetalSparkling("Reja3")

reja3din=Objects.CreateDinamicObject("Reja3")

##funciones abrir-cerrar##
"""
def Abrereja69():

	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 1000)
	vel_finales=(1000.0, 500)

	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(reja3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrareja69():

	desplazamientos=(1800.0, 1800.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(1000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(reja3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
"""
##### Abrir el rastrillo al USAR LLAVE


cerradurp3=Locks.PlaceLock("cerradurp3","Cerraduracutre",(-54342.952939,-33828.016591,143064.408630),(0.390278,0.390278,0.589646,-0.589646),2.5)
cerradurp3.key="llave3"


cerradurp3.OnUnLockFunc=Abrereja69
cerradurp3.OnUnLockArgs=()

cerradurp3.OnLockFunc=Cierrareja69
cerradurp3.OnLockArgs=()

darfuncs.SetHint(cerradurp3.obj,"Rusted Lock")

o=Bladex.CreateEntity("llave3","Llavecutre",-40267.526631,-29426.797572,147055.112600)
o.Static=0
o.Scale=1.0
o.Orientation=0.000000,0.999929,0.003787,-0.011255
darfuncs.SetHint(o,"Rusted Key")
Stars.Twinkle("llave3")