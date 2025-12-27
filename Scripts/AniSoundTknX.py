import Bladex
import Language

language = Language.CheckFallback()
# *********************************
# *      Creacion de sonidos      *
# *********************************

GolpeArmaEscudoTkn=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoTkn')
GolpeArmaEscudoTkn.SendNotify=0
GolpeArmaEscudoTkn.Volume=0.8
GolpeArmaArmaTkn=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaTkn')
GolpeArmaArmaTkn.SendNotify=0
GolpeArmaArmaTkn.Volume=0.8
TajoEmpalanteTkn=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-33.wav', 'TajoEmpalanteTkn')
TajoEmpalanteTkn.SendNotify=0
TajoEmpalanteTkn.Volume=0.8
TajoCortanteTkn=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-44.wav', 'TajoCortanteTkn')
TajoCortanteTkn.SendNotify=0
TajoCortanteTkn.Volume=0.8
TajoMutilacionTkn=Bladex.CreateSound('../../sounds/mutilacion4-44.wav', 'TajoMutilacionTkn')
TajoMutilacionTkn.SendNotify=0
TajoMutilacionTkn.Volume=0.8
GolpeContundenteTkn=Bladex.CreateSound('../../sounds/golpe-maza-arm.wav', 'GolpeContundenteTkn')
GolpeContundenteTkn.SendNotify=0
GolpeContundenteTkn.Volume=0.8

KnightKeepStill=Bladex.CreateSound('../../sounds/'+language+'/knight-keepstill.wav', 'KnightKeepStill')
KnightKeepStill.MinDistance=1000
KnightKeepStill.MaxDistance=25000


KnightKeepStill=Bladex.CreateSound('../../sounds/'+language+'/knight-keepstill.wav', 'KnightKeepStill')
KnightKeepStill.MinDistance=1000
KnightKeepStill.MaxDistance=25000



Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')
Enfundar.SendNotify=0

EsfuerzoCortoTkn=Bladex.CreateSound('../../sounds/ataqueTkn.wav', 'EsfuerzoCortoTkn')
EsfuerzoCortoTkn.SendNotify=0
EsfuerzoCortoTkn.Volume=0.8
EsfuerzoCortoTkn.MinDistance=1000
EsfuerzoCortoTkn.MaxDistance=25000
EsfuerzoCorto1Tkn=Bladex.CreateSound('../../sounds/ataqueTkn1.wav', 'EsfuerzoCorto1Tkn')
EsfuerzoCorto1Tkn.SendNotify=0
EsfuerzoCorto1Tkn.Volume=0.8
EsfuerzoCorto1Tkn.MinDistance=1000
EsfuerzoCorto1Tkn.MaxDistance=25000
EsfuerzoCorto2Tkn=Bladex.CreateSound('../../sounds/ataqueTkn2.wav', 'EsfuerzoCorto2Tkn')
EsfuerzoCorto2Tkn.SendNotify=0
EsfuerzoCorto2Tkn.Volume=0.8
EsfuerzoCorto2Tkn.MinDistance=1000
EsfuerzoCorto2Tkn.MaxDistance=25000
EsfuerzoCorto3Tkn=Bladex.CreateSound('../../sounds/ataqueTkn2.wav', 'EsfuerzoCorto3Tkn')
EsfuerzoCorto3Tkn.SendNotify=0
EsfuerzoCorto3Tkn.Volume=0.8
EsfuerzoCorto3Tkn.MinDistance=1000
EsfuerzoCorto3Tkn.MaxDistance=25000
EsfuerzoCorto4Tkn=Bladex.CreateSound('../../sounds/ataqueTkn4.wav', 'EsfuerzoCorto4Tkn')
EsfuerzoCorto4Tkn.SendNotify=0
EsfuerzoCorto4Tkn.Volume=0.8
EsfuerzoCorto4Tkn.MinDistance=1000
EsfuerzoCorto4Tkn.MaxDistance=25000
EsfuerzoCorto5Tkn=Bladex.CreateSound('../../sounds/ataqueTkn5.wav', 'EsfuerzoCorto5Tkn')
EsfuerzoCorto5Tkn.SendNotify=0
EsfuerzoCorto5Tkn.Volume=0.8
EsfuerzoCorto5Tkn.MinDistance=1000
EsfuerzoCorto5Tkn.MaxDistance=25000
EsfuerzoCorto6Tkn=Bladex.CreateSound('../../sounds/ataqueTkn6.wav', 'EsfuerzoCorto6Tkn')
EsfuerzoCorto6Tkn.SendNotify=0
EsfuerzoCorto6Tkn.Volume=0.8
EsfuerzoCorto6Tkn.MinDistance=1000
EsfuerzoCorto6Tkn.MaxDistance=25000
SesgadoCorto=Bladex.CreateSound('../../sounds/sesgado-corto.wav', 'SesgadoCorto')
SesgadoCorto.SendNotify=0
SesgadoCorto.Volume=0.8
SesgadoCorto.MinDistance=1000
SesgadoCorto.MaxDistance=25000
SesgadoLargo=Bladex.CreateSound('../../sounds/sesgado-largo.wav', 'SesgadoLargo')
SesgadoLargo.SendNotify=0
SesgadoLargo.Volume=0.8
SesgadoLargo.MinDistance=1000
SesgadoLargo.MaxDistance=25000
SesgadoCortoGrave=Bladex.CreateSound('../../sounds/sesgado-corto-grave.wav', 'SesgadoCortoGrave')
SesgadoCortoGrave.SendNotify=0
SesgadoCortoGrave.Volume=0.8
SesgadoCortoGrave.MinDistance=1000
SesgadoCortoGrave.MaxDistance=25000
SesgadoLargoGrave=Bladex.CreateSound('../../sounds/sesgado-largo-grave.wav', 'SesgadoLargoGrave')
SesgadoLargoGrave.SendNotify=0
SesgadoLargoGrave.Volume=0.8
SesgadoLargoGrave.MinDistance=1000
SesgadoLargoGrave.MaxDistance=25000
SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=0
SesgadoCortoAgudo.Volume=0.8
SesgadoCortoAgudo.MinDistance=1000
SesgadoCortoAgudo.MaxDistance=25000
SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=0
SesgadoLargoAgudo.Volume=0.8
SesgadoLargoAgudo.MinDistance=1000
SesgadoLargoAgudo.MaxDistance=25000
EsfuerzoGolpeFrontalTkn=Bladex.CreateSound('../../sounds/esfuerzo-largo-Tkn.wav', 'EsfuerzoGolpeFrontalTkn')
EsfuerzoGolpeFrontalTkn.SendNotify=0
EsfuerzoGolpeFrontalTkn.MinDistance=1000
EsfuerzoGolpeFrontalTkn.MaxDistance=25000
EsfuerzoGolpeLateralTkn=Bladex.CreateSound('../../sounds/esfuerzo-largo-Tkn2.wav', 'EsfuerzoGolpeLateralTkn')
EsfuerzoGolpeLateralTkn.SendNotify=0
EsfuerzoGolpeLateralTkn.MinDistance=1000
EsfuerzoGolpeLateralTkn.MaxDistance=25000
EsfuerzoGolpeCabezaTkn=Bladex.CreateSound('../../sounds/esfuerzo-largo-Tkn3.wav', 'EsfuerzoGolpeCabezaTkn')
EsfuerzoGolpeCabezaTkn.SendNotify=0
EsfuerzoGolpeCabezaTkn.MinDistance=1000
EsfuerzoGolpeCabezaTkn.MaxDistance=25000
EsfuerzoGolpeAtrasTkn=Bladex.CreateSound('../../sounds/esfuerzo-largo-Tkn4.wav', 'EsfuerzoGolpeAtrasTkn')
EsfuerzoGolpeAtrasTkn.SendNotify=0
EsfuerzoGolpeAtrasTkn.MinDistance=1000
EsfuerzoGolpeAtrasTkn.MaxDistance=25000

EsfuerzoTknMediano=Bladex.CreateSound('../../sounds/esfuerzo-mediano-Tkn.wav', 'EsfuerzoTknMediano')
EsfuerzoTknMediano.SendNotify=0
EsfuerzoTknMediano.MinDistance=1000
EsfuerzoTknMediano.MaxDistance=25000
EsfuerzoTknLargo=Bladex.CreateSound('../../sounds/esfuerzo-mediano-Tkn2.wav', 'EsfuerzoTknLargo')
EsfuerzoTknLargo.SendNotify=0
EsfuerzoTknLargo.MinDistance=1000
EsfuerzoTknLargo.MaxDistance=25000

EsfuerzoGolpeArribaBarb=Bladex.CreateSound('../../sounds/esfuerzo-largo-Tkn5.wav', 'EsfuerzoGolpeArribaTkn')
EsfuerzoGolpeArribaBarb.SendNotify=0
EsfuerzoGolpeArribaBarb.MinDistance=1000
EsfuerzoGolpeArribaBarb.MaxDistance=25000

MuerteTkn=Bladex.CreateSound('../../sounds/muerteTkn.wav', 'MuerteTkn')
MuerteTkn.SendNotify=0
MuerteTkn.MinDistance=1000
MuerteTkn.MaxDistance=25000

MuerteTkn2=Bladex.CreateSound('../../sounds/muerteTkn2.wav', 'MuerteTkn2')
MuerteTkn2.SendNotify=0
MuerteTkn2.MinDistance=1000
MuerteTkn2.MaxDistance=25000
MuerteTkn3=Bladex.CreateSound('../../sounds/muerteTkn3.wav', 'MuerteTkn3')
MuerteTkn3.SendNotify=0
MuerteTkn3.MinDistance=1000
MuerteTkn3.MaxDistance=25000
MuerteTkn4=Bladex.CreateSound('../../sounds/muerteTkn4.wav', 'MuerteTkn4')
MuerteTkn4.SendNotify=0
MuerteTkn4.MinDistance=1000
MuerteTkn4.MaxDistance=25000

HeridaTkn1=Bladex.CreateSound('../../sounds/heridaTkn1.wav', 'HeridaTkn1')
HeridaTkn1.SendNotify=0
HeridaTkn1.MinDistance=1000
HeridaTkn1.MaxDistance=25000
HeridaTkn2=Bladex.CreateSound('../../sounds/heridaTkn2.wav', 'HeridaTkn2')
HeridaTkn2.SendNotify=0
HeridaTkn2.MinDistance=1000
HeridaTkn2.MaxDistance=25000
HeridaTkn3=Bladex.CreateSound('../../sounds/heridaTkn3.wav', 'HeridaTkn3')
HeridaTkn3.SendNotify=0
HeridaTkn3.MinDistance=1000
HeridaTkn3.MaxDistance=25000

RespiraTkn1=Bladex.CreateSound('../../sounds/traidor-respira.wav', 'RespiraTkn1')
RespiraTkn1.SendNotify=0
RespiraTkn1.Volume=0.2
RespiraTkn1.MinDistance=1000
RespiraTkn1.MaxDistance=14000
RespiraTkn2=Bladex.CreateSound('../../sounds/traidor-respira2.wav', 'RespiraTkn2')
RespiraTkn2.SendNotify=0
RespiraTkn2.Volume=0.2
RespiraTkn2.MinDistance=1000
RespiraTkn2.MaxDistance=14000


RespiraTkn3=Bladex.CreateSound('../../sounds/traidor-respira.wav', 'RespiraTkn3')
RespiraTkn3.SendNotify=0
RespiraTkn3.Volume=0.2
RespiraTkn3.MinDistance=1000
RespiraTkn3.MaxDistance=14000
RespiraTkn4=Bladex.CreateSound('../../sounds/traidor-respira2.wav', 'RespiraTkn4')
RespiraTkn4.SendNotify=0
RespiraTkn4.Volume=0.2
RespiraTkn4.MinDistance=1000
RespiraTkn4.MaxDistance=14000


#RespiraTkn5=Bladex.CreateSound('../../sounds/mov-armadura-5.wav', 'RespiraTkn5')
#RespiraTkn5.SendNotify=0
#RespiraTkn5.Volume=0.3
#RespiraTkn5.MinDistance=5000
#RespiraTkn5.MaxDistance=15000
#RespiraTkn6=Bladex.CreateSound('../../sounds/mov-armadura-6.wav', 'RespiraTkn6')
#RespiraTkn6.SendNotify=0
#RespiraTkn6.Volume=0.3
#RespiraTkn6.MinDistance=5000
#RespiraTkn6.MaxDistance=15000

DesangreTkn1=Bladex.CreateSound('../../sounds/desangre1.wav', 'DesangreTkn1')
DesangreTkn1.SendNotify=0
DesangreTkn1.Volume=0.7
DesangreTkn1.MinDistance=1000
DesangreTkn1.MaxDistance=25000
DesangreTkn2=Bladex.CreateSound('../../sounds/desangre3.wav', 'DesangreTkn1')
DesangreTkn2.SendNotify=0
DesangreTkn2.Volume=0.7
DesangreTkn2.MinDistance=1000
DesangreTkn2.MaxDistance=25000


RisaTkn=Bladex.CreateSound('../../sounds/risaTkn.wav', 'RisaTkn')
#RisaTkn.SendNotify=0
RisaTkn.MinDistance=5000
RisaTkn.MaxDistance=30000
RisaTkn.Volume=0.7

AltoTkn=Bladex.CreateSound('../../sounds/insultoTkn.wav', 'AltoTkn')
AltoTkn.MinDistance=5000
AltoTkn.MaxDistance=30000
AltoTkn.Volume=0.7

CaidaTkn1=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaTkn1')
CaidaTkn1.SendNotify=0
CaidaTkn1.Volume=0.8
CaidaTkn1.MinDistance=1000
CaidaTkn1.MaxDistance=25000

CaidaTkn2=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaTkn2')
CaidaTkn2.SendNotify=0
CaidaTkn2.Volume=0.8
CaidaTkn2.MinDistance=1000
CaidaTkn2.MaxDistance=25000

AtaqueTkn=Bladex.CreateSound('../../sounds/aporel.wav', 'AtaqueTkn')
AtaqueTkn.SendNotify=0
AtaqueTkn.Volume=0.8
AtaqueTkn.MinDistance=1000
AtaqueTkn.MaxDistance=25000

AltoTkn2=Bladex.CreateSound('../../sounds/'+language+'/altoTkn.wav', 'AltoTkn2')
AltoTkn2.SendNotify=0
AltoTkn2.Volume=1
AltoTkn2.MinDistance=1000
AltoTkn2.MaxDistance=25000
AltoTkn2=Bladex.CreateSound('../../sounds/'+language+'/altoTkn.wav', 'AltoTkn2')
AltoTkn2.SendNotify=0
AltoTkn2.Volume=1
AltoTkn2.MinDistance=1000
AltoTkn2.MaxDistance=25000

AvisoTkn1=Bladex.CreateSound('../../sounds/avisoTkn.wav', 'AvisoTkn1')
AvisoTkn1.SendNotify=0
AvisoTkn1.Volume=1
AvisoTkn1.MinDistance=1000
AvisoTkn1.MaxDistance=25000




TajoMutilacionTkn=Bladex.CreateSound('../../sounds/mutilacion4-44.wav', 'TajoMutilacionTkn')

print "Sonidos para el caballero traidor creados..."
