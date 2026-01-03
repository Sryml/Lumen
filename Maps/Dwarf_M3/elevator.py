import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
###CREAMOS LA PLATAFORMA-OBJETO

plataformaelevador2=Bladex.CreateEntity("PlataformaElevador2", "PlataformaRail", -122937,-500,-91937)
plataformaelevador2.Static=0
plataformaelevador2.Scale=1.31
plataformaelevador2.Orientation=0.500000,0.500000,-0.500000,0.500000



##ESTABLECEMOS LA PROPIEDAD "DINAMICA" PARA LA PLATAFORMA OBJETO

plataformaelevador2movil=Objects.CreateDinamicObject("PlataformaElevador2")


##ESTABLECEMOS LOS SONIDOS QUE TENDR� EL ELEVADOR

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


##CREAMOS LA BARRA ELEVADORA QUE ESTARA INICIALMENTE EN POSICION CLOSED, ES DECIR, ARRIBA.

columnaelevador2=Doors.CreateDoor("ColumnaElevador2", (-122937, -1000, -92000), (0, -1, 0),500, 7500, Doors.OPENED)


##ESTABLECEMOS LOS TRAMOS DE MOVIMIENTO

columnaelevador2.opentype=Doors.AC_UNIF_DEC
columnaelevador2.o_init_vel=0
columnaelevador2.o_init_displ=1000
columnaelevador2.o_med_vel=-2000
columnaelevador2.o_med_displ=5000
columnaelevador2.o_end_vel=0
columnaelevador2.o_end_displ=1000

columnaelevador2.closetype=Doors.AC_UNIF_DEC
columnaelevador2.c_init_vel=0
columnaelevador2.c_init_displ=1000
columnaelevador2.c_med_vel=2000
columnaelevador2.c_med_displ=5000
columnaelevador2.c_end_vel=0
columnaelevador2.c_end_displ=1000


##A�ADIMOS enmarcha=0 COMO VARIABLE DE AMBITO GLOBAL ESTABLECIDA INICIALMENTE EN CERO, ES DECIR, LA PLATAFORMA ESTA PARADA :)


enmarcha=0


##DEFINIMOS COMO SER�N LAS FUNCIONES QUE RIJAN LOS MOVIMIENTOS DE BAJAR Y SUBIR, A�ADIENDO EN BajaElevador LA CONDICION




columnaelevador2.OnEndCloseFunc=EsperaYBajaElevador2
columnaelevador2.OnEndOpenFunc=Elevador2Arriba


##CREAMOS LAS PALANCAS

palanca1elevador2=Levers.PlaceLever("Palanca1Elevador2", Levers.LeverType3, (-120309.137737,-8638.822330,-88677.369961), (0.5,0.5,0.5,-0.5), 1.0)
palanca1elevador2.mode=1

palanca1elevador2.OnTurnOnFunc=SubeElevador2
palanca1elevador2.OnTurnOnArgs=()



#########
#########
#########THE END