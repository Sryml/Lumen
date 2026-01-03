"""
############################################################################################################

APARICION SE�OR OSCURO

En esta escena tenemos 5 camaras:

1. Anakardo_Camera01.cam
	Va desde el frame 0 hasta el 125 y esta quieta.

2. Anakardo_Camera02.cam
	Va desde el frame 126 hasta el 249. Tambien esta quieta.

3. Anakardo_Camera03.cam
	Va desde el frame 250 hasta el 455.

Durante estas primeras 3 camaras se ve al viejo soltando una parrafada.

4. Anakardo_Camera04.cam
	Va desde el frame 456 hasta el 667

5. Anakardo_Camera05.cam
	Desde el frame 668 hasta el 968


PERSONAJES.

Viejo: Vejete.bod (Vejete)

	su animacion es: Vejete_pinchado.bmv y va desde el frame 0 hasta el 717, pero debes hacerlo desaparecer completamente en el frame 629. Tratalo como un actor, ya que no esta creado como personaje.
Eventos asociados a el: En el frame 534 debes soltar un chorro de sangre hacia su frente, ya que es pinchado por el anakardo.


Anakardo sin Viejo: Ank2.bod (Ank2)

	Su animacion es: Ank2_pincha_viejo.bmv y va desde el frame 0 hasta el 666 (como no tenia que ser un numero diabolico). Tratalo como actor.
Hasta el frame 389 este bicho es invisible, y empieza a aparecer en el frame 390, pero no lo hace inmidiatamente, sino que hace una transicion hasta que lo hace por completo en el frame 450 (metele algun efecto de glow o algo, de todas formas el efecto de aparicion depende de que le guste a JoseLuis).
En el frame 529, al golpear el anacardo con sus pinchos en la mesa, debe romperla en pedazos.



Anakardo Con viejo: Ank.bod (DarkLord)

	Su animacion es: Ank_pincha_viejo.bmv y va desde el frame 668 hasta el 968. Debes hacer invisible al anterior Bod (Ank2.bod) en el frame 668, y hacer visible a este en el mismo frame.
Utiliza un Actor ya que cuando termine su animacion, haras un cambio de camara a la espalda del personaje jugador y ya lo puedes cambiar por un bod enemigo, en el frame 968.
En el frame 765 del pecho del bicho (donde esta el viejo) empieza a soltar particulas de salgre a borbotones (mientras que esta temblando); y dejalas de emitir en el frame 880 (cuidado que las particulas no lleguen a camara o si no se parara el sistema.

############################################################################################################
"""

import darfuncs
import Bladex
import dust


CreaAltar()

#Bladex.ReadBitMap("../../Data/KeyGlow.bmp","OjoVejete")

OjoBrillo = [0,0,0.025]

#LocuraSangrienta(char.Position[0],char.Position[1],char.Position[2])

#DropBlood(char.Position[0],char.Position[1],char.Position[2],0,0,0)


CreaViejoVerde()



_PasoAnacardo1=Bladex.CreateSound("../../Sounds/paso-mino-piedra3.wav","PasoAnacardo1")
_PasoAnacardo1.Volume      =       1.0
_PasoAnacardo1.MinDistance =   50000.0
_PasoAnacardo1.MaxDistance = 1000000.0


_PasoAnacardo2=Bladex.CreateSound("../../Sounds/paso-mino-piedra.wav","PasoAnacardo2")
_PasoAnacardo2.Volume      =       1.0
_PasoAnacardo2.MinDistance =   50000.0
_PasoAnacardo2.MaxDistance = 1000000.0


_SesgadoTeJodes=Bladex.CreateSound("../../Sounds/Sesgado1.wav","SesgadoTeJodes")
_SesgadoTeJodes.Volume      =       1.0
_SesgadoTeJodes.MinDistance =   50000.0
_SesgadoTeJodes.MaxDistance = 1000000.0

_EmpalaVejete=Bladex.CreateSound("../../Sounds/pinchito.wav","EmpalaVejete")
_EmpalaVejete.Volume      =       1.0
_EmpalaVejete.MinDistance =   50000.0
_EmpalaVejete.MaxDistance = 1000000.0

_SesgadoGore=Bladex.CreateSound("../../Sounds/sesgado-gore.wav","SesgadoGore")
_SesgadoGore.Volume      =       1.0
_SesgadoGore.MinDistance =   50000.0
_SesgadoGore.MaxDistance = 1000000.0

_FusionCool=Bladex.CreateSound("../../Sounds/fusion-viejete.wav","FusionCool")
_FusionCool.Volume      =       1.0
_FusionCool.MinDistance =   50000.0
_FusionCool.MaxDistance = 1000000.0

_BrilloOjos=Bladex.CreateSound("../../Sounds/fireball-swing.wav","BrilloOjos")
_BrilloOjos.Volume      =       1.0
_BrilloOjos.MinDistance =   50000.0
_BrilloOjos.MaxDistance = 1000000.0

_absorcion=Bladex.CreateSound("../../Sounds/absorcion.wav", "Absorcion")
_absorcion.Volume=1.0
_absorcion.MinDistance=150000
_absorcion.MaxDistance=500000
