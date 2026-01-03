##                                                                     ##
 ###                   SONIDOS PARA LOS PERSONAJES                   ###
  ####                                                             ####
   ###################################################################


#####################################
#               __                  #
#  | | |\  | | |    | |  _|_  | O   #
#  |/  |  \| | | _  +-+   |   +/|\) #
#  |\  |   | | |__| | |   |    / \  #
#                                   #
#####################################

_Pasito=Bladex.CreateSound("../../Sounds/Paso-Podrido.wav","Pasito")
_Pasito.MinDistance =   1000
_Pasito.MaxDistance =  10000
_Pasito.Volume      =  1.0


_Pasito1=Bladex.CreateSound("../../Sounds/Paso-Podrido-1.wav","Pasito1")
_Pasito1.MinDistance =   1000
_Pasito1.MaxDistance =  10000
_Pasito1.Volume      =  1.0

_Espadacab=Bladex.CreateSound("../../Sounds/espada-caballero.wav","Espadacab")
_Espadacab.MinDistance =   1000
_Espadacab.MaxDistance =  10000
_Espadacab.Volume      =  1.0


_RozeCab=Bladex.CreateSound("../../Sounds/correajes-88.wav","RozeCab")
_RozeCab.MinDistance =   1000
_RozeCab.MaxDistance =  10000
_RozeCab.Volume      =  1.0

_RozeCab1=Bladex.CreateSound("../../Sounds/correajes-88b.wav","RozeCab1")
_RozeCab1.MinDistance =   1000
_RozeCab1.MaxDistance =  10000
_RozeCab1.Volume      =  1.0


_XclamaCab1=Bladex.CreateSound("../../Sounds/esfuerzo-traidor-corto.wav","XclamaCab1")
_XclamaCab1.MinDistance =   1000
_XclamaCab1.MaxDistance =  10000
_XclamaCab1.Volume      =  1.0


LOOP_KNIGHT = (692.0/20.0)

def SonidosDelKavayero():
	Bladex.AddScheduledFunc(Bladex.GetTime()+LOOP_KNIGHT, SonidosDelKavayero,())

	Bladex.AddScheduledFunc(Bladex.GetTime()+163.0/20, _Pasito.Play,(16039, -8388,-11988, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+410.0/20, _Pasito1.Play,(16039, -8388,-11988, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+420.0/20, _Espadacab.Play,(16039, -8388,-11988, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+ 75.0/20.0, _RozeCab.Play,(16039, -8388,-11988, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+148.0/20.0, _RozeCab1.Play,(16039, -8388,-11988, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+182.0/20.0, _RozeCab.Play,(16039, -8388,-11988, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+360.0/20.0, _RozeCab1.Play,(16039, -8388,-11988, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+392.0/20.0, _RozeCab.Play,(16039, -8388,-11988, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+418.0/20.0, _RozeCab1.Play,(16039, -8388,-11988, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+552.0/20.0, _RozeCab.Play,(16039, -8388,-11988, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+250.0/20.0, _XclamaCab1.Play,(16039, -8388,-11988, 0))


####################################
#              __   _   __         #
#  |\  |    | |  | | | |    _ o    #
#  | | | /\ | |--| |/  |-  (\/O\}  #
#  |/  |/  \| |  | |\  |     / \   #
#                                  #
####################################

LOOP_DWARF = (1606.0/60.0)

_Bostezo =Bladex.CreateSound("../../Sounds/bostezo-enano.wav","Bostezo")
_Bostezo.MinDistance =   1000
_Bostezo.MaxDistance =  10000
_Bostezo.Volume      =  1.0


_unabirra =Bladex.CreateSound("../../Sounds/interrogancia-enano.wav","unabirra")
_unabirra.MinDistance =   1000
_unabirra.MaxDistance =  10000
_unabirra.Volume      =  1.0


_Takebirra =Bladex.CreateSound("../../Sounds/coger-jarra.wav","Takebirra")
_Takebirra.MinDistance =   1000
_Takebirra.MaxDistance =  10000
_Takebirra.Volume      =  1.0


_SePoneEnPedo =Bladex.CreateSound("../../Sounds/drink2.wav","SePoneEnPedo")
_SePoneEnPedo.MinDistance =   1000
_SePoneEnPedo.MaxDistance =  10000
_SePoneEnPedo.Volume      =  1.0

_NyamNyam =Bladex.CreateSound("../../Sounds/relame-enano.wav","NyamNyam")
_NyamNyam.MinDistance =   1000
_NyamNyam.MaxDistance =  10000
_NyamNyam.Volume      =  1.0


_PosaBirra =Bladex.CreateSound("../../Sounds/posar-jarra.wav","PosaBirra")
_PosaBirra.MinDistance =   1000
_PosaBirra.MaxDistance =  10000
_PosaBirra.Volume      =  1.0

_SeTira =Bladex.CreateSound("../../Sounds/caida-pie.wav","SeTira")
_SeTira.MinDistance =   1000
_SeTira.MaxDistance =  10000
_SeTira.Volume      =  0.5


_HaceFiaca =Bladex.CreateSound("../../Sounds/bostezo-enano2.wav","HaceFiaca")
_HaceFiaca.MinDistance =   1000
_HaceFiaca.MaxDistance =  10000
_HaceFiaca.Volume      =  1.0


def SonidosDelEnano():
	Bladex.AddScheduledFunc(Bladex.GetTime()+LOOP_DWARF, SonidosDelEnano,())

	Bladex.AddScheduledFunc(Bladex.GetTime()+228.0/60.0, _Bostezo.Play,(11563, -827,9813, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+677.0/60.0, _unabirra.Play,(11563, -827,9813, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+745.0/60.0, _Takebirra.Play,(11563, -827,9813, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+823.0/60.0, _SePoneEnPedo.Play,(11563, -827,9813, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+983.0/60.0, _NyamNyam.Play,(11563, -827,9813, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+1060.0/60.0, _PosaBirra.Play,(11563, -827,9813, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+1187.0/60.0, _SeTira.Play,(11563, -827,9813, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+1251.0/60.0, _HaceFiaca.Play,(11563, -827,9813, 0))

###############################################
#  _   _   _   _   _   _     _         o      #
# | \ | | | | | \ | | | | | | | |\|  ()@()    #
# | / |_| |/  | / |_| |/  | |_| | | () @ ()   #
# | \ | | |\  | \ | | |\  | | | | |   / \ +   #
# |_/ | | | | |_/ | | | | | | | | |  () ()|   #
#                                    /\ /\|   #
###############################################

LOOP_BARB = (1789.0/60.0)

_CogePedron             = Bladex.CreateSound("../../Sounds/barb-coge-piedra2.wav","CogePedron")
_CogePedron.MinDistance =   1000
_CogePedron.MaxDistance =  10000
_CogePedron.Volume      =  1.0

_EsfuerzoPedron             = Bladex.CreateSound("../../Sounds/esfuerzos_barb_corto_1.wav","EsfuerzoPedron")
_EsfuerzoPedron.MinDistance =   1000
_EsfuerzoPedron.MaxDistance =  10000
_EsfuerzoPedron.Volume      =  1.0

_Pedrada             =Bladex.CreateSound("../../Sounds/sesgado-corto.wav","Pedrada")
_Pedrada.MinDistance =   1000
_Pedrada.MaxDistance =  10000
_Pedrada.Volume      =  1.0

_chofPiedra             =Bladex.CreateSound("../../Sounds/m-chopagua1.wav","chofPiedra")
_chofPiedra.MinDistance =   1000
_chofPiedra.MaxDistance =  10000
_chofPiedra.Volume      =  1.0

_CojeEspada             = Bladex.CreateSound("../../Sounds/m-desenfunda-piedra.wav","CojeEspada")
_CojeEspada.MinDistance =   1000
_CojeEspada.MaxDistance =  10000
_CojeEspada.Volume      =  1.0


_GritaElCondenado             = Bladex.CreateSound("../../Sounds/esfuerzos_barb_corto_2.wav","GritaElCondenado")
_GritaElCondenado.MinDistance =   1000
_GritaElCondenado.MaxDistance =  10000
_GritaElCondenado.Volume      =  1.0

_Espadazo             = Bladex.CreateSound("../../Sounds/Sesgado2.wav","Espadazo")
_Espadazo.MinDistance =   1000
_Espadazo.MaxDistance =  10000
_Espadazo.Volume      =  1.0

_GolpeHierba             = Bladex.CreateSound("../../Sounds/Golpe_Hierba.wav","GolpeHierba")
_GolpeHierba.MinDistance =   1000
_GolpeHierba.MaxDistance =  10000
_GolpeHierba.Volume      =  1.0

_DejaEspada             = Bladex.CreateSound("../../Sounds/hachaa.wav","DejaEspada")
_DejaEspada.MinDistance =   1000
_DejaEspada.MaxDistance =  10000
_DejaEspada.Volume      =  1.0

_Cansadito             = Bladex.CreateSound("../../Sounds/bostezo-enano2.wav","Cansadito")
_Cansadito.MinDistance =   1000
_Cansadito.MaxDistance =  10000
_Cansadito.Volume      =  1.0


def SonidosDelBarbaro():
	Bladex.AddScheduledFunc(Bladex.GetTime()+LOOP_BARB, SonidosDelBarbaro,())

	Bladex.AddScheduledFunc(Bladex.GetTime()+463.0/60.0, _CogePedron.Play       ,(-99, -616,-3233, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+665.0/60.0, _EsfuerzoPedron.Play   ,(-99, -616,-3233, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+687.0/60.0, _Pedrada.Play          ,(-99, -616,-3233, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+777.0/60.0, _chofPiedra.Play       ,(-99, -616,-3233, 0))


	Bladex.AddScheduledFunc(Bladex.GetTime()+877.0/60.0, _CojeEspada.Play       ,(-99, -616,-3233, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1162.0/60.0, _GritaElCondenado.Play ,(-99, -616,-3233, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1178.0/60.0, _Espadazo.Play         ,(-99, -616,-3233, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1190.0/60.0, _GolpeHierba.Play      ,(-99, -616,-3233, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+1307.0/60.0, _DejaEspada.Play       ,(-99, -616,-3233, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+1615.0/60.0, _Cansadito.Play        ,(-99, -616,-3233, 0))


#######################################
#                                     #
#                              |  0\  #
#   _        _  __  _          +-((   #
#  |_| |\/| |_|  / | | |\|        ))  #
#  | | |  | | | -- |_| | |        ||  #
#                                     #
#######################################


LOOP_AMZ = (1273.0/60.0)

_LevantatePiba             = Bladex.CreateSound("../../Sounds/Mov-amazona-2.wav","LevantatePiba")
_LevantatePiba.MinDistance =   1000
_LevantatePiba.MaxDistance =  10000
_LevantatePiba.Volume      =  1.0

_PisaLaPiba1               = Bladex.CreateSound("../../Sounds/07-pas51.wav","PisaLaPiba1")
_PisaLaPiba1.MinDistance   =   1000
_PisaLaPiba1.MaxDistance   =  10000
_PisaLaPiba1.Volume        =  1.0

_PisaLaPiba2               = Bladex.CreateSound("../../Sounds/07-pas52.wav","PisaLaPiba2")
_PisaLaPiba2.MinDistance   =   1000
_PisaLaPiba2.MaxDistance   =  10000
_PisaLaPiba2.Volume        =  1.0


_Flechazo                  = Bladex.CreateSound("../../Sounds/disparo_arco.wav","Flechazo")
_Flechazo.MinDistance      =   1000
_Flechazo.MaxDistance      =  10000
_Flechazo.Volume           =  1.0

_Tensado                   = Bladex.CreateSound("../../Sounds/m-creakcuerda-44.wav","Tensado")
_Tensado.MinDistance       =   1000
_Tensado.MaxDistance       =  10000
_Tensado.Volume            =  1.0

_ApoyoPiba                 = Bladex.CreateSound("../../Sounds/Mov-amazona-1.wav","ApoyoPiba")
_ApoyoPiba.MinDistance     =   1000
_ApoyoPiba.MaxDistance     =  10000
_ApoyoPiba.Volume          =  1.0

_TakePiba                  = Bladex.CreateSound("../../Sounds/coger-arco.wav","TakePiba")
_TakePiba.MinDistance      =   1000
_TakePiba.MaxDistance      =  10000
_TakePiba.Volume           =  1.0

_SacafPiba                 = Bladex.CreateSound("../../Sounds/desenfundar-flecha1.wav","SacafPiba")
_SacafPiba.MinDistance     =   1000
_SacafPiba.MaxDistance     =  10000
_SacafPiba.Volume          =  1.0


def SonidosDeLaAmazona():
	Bladex.AddScheduledFunc(Bladex.GetTime()+LOOP_AMZ, SonidosDeLaAmazona,())

	Bladex.AddScheduledFunc(Bladex.GetTime()+190.0/60.0, _LevantatePiba.Play      ,(14881,-1082,22235, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+243.0/60.0, _PisaLaPiba1.Play        ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+285.0/60.0, _PisaLaPiba2.Play        ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+414.0/60.0, _PisaLaPiba1.Play        ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+562.0/60.0, _PisaLaPiba2.Play        ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+715.0/60.0, _PisaLaPiba1.Play        ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+763.0/60.0, _PisaLaPiba2.Play        ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+847.0/60.0, _PisaLaPiba1.Play        ,(14881,-1082,22235, 0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+332.0/60.0, _TakePiba.Play           ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+565.0/60.0, _SacafPiba.Play          ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+605.0/60.0, _Tensado.Play            ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+636.0/60.0, _Flechazo.Play           ,(14881,-1082,22235, 0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+765.0/60.0, _TakePiba.Play           ,(14881,-1082,22235, 0))


#########################################
#     ___                               #
#    | __|   |\                         #
#    |   |   |\   Music                 #
#   0    |   |    Superfragilistic      #
#       0   0                           #
#                                       #
#########################################

VOLUMEN_MUSICA = 1

Bladex.AddMusicEventMP3( "suspenselento",  "../../Sounds/seleccion-personaje.MP3", 2.0, 1.0, VOLUMEN_MUSICA, 10000, 1, -1 )
Bladex.AddScheduledFunc(Bladex.GetTime(),Bladex.ExeMusicEvent,(Bladex.GetMusicEvent("suspenselento"),))