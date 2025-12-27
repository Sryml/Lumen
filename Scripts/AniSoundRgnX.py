import Bladex

import Language

language = Language.CheckFallback()

# *********************************
# *      Creacion de sonidos      *
# *********************************

GolpeArmaEscudoRgn=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoRgn')
GolpeArmaEscudoRgn.SendNotify=0
GolpeArmaArmaRgn=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaRgn')
GolpeArmaArmaRgn.SendNotify=0
TajoEmpalanteRgn=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-33.wav', 'TajoEmpalanteRgn')
TajoEmpalanteRgn.SendNotify=0
TajoCortanteRgn=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-44.wav', 'TajoCortanteRgn')
TajoCortanteRgn.SendNotify=0
TajoMutilacionRgn=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionRgn')
TajoMutilacionRgn.SendNotify=0
GolpeContundenteRgn=Bladex.CreateSound('../../sounds/golpe-maza-arm.wav', 'GolpeContundenteRgn')
GolpeContundenteRgn.SendNotify=0

EsfuerzoCortoRgn=Bladex.CreateSound('../../sounds/ataqueRgn.wav', 'EsfuerzoCortoRgn')
EsfuerzoCortoRgn.SendNotify=0
EsfuerzoCortoRgn.Volume=0.8
EsfuerzoCorto1Rgn=Bladex.CreateSound('../../sounds/ataqueRgn1.wav', 'EsfuerzoCorto1Rgn')
EsfuerzoCorto1Rgn.SendNotify=0
EsfuerzoCorto1Rgn.Volume=0.8
EsfuerzoCorto2Rgn=Bladex.CreateSound('../../sounds/ataqueRgn6.wav', 'EsfuerzoCorto2Rgn')
EsfuerzoCorto2Rgn.SendNotify=0
EsfuerzoCorto2Rgn.Volume=0.8
EsfuerzoCorto3Rgn=Bladex.CreateSound('../../sounds/ataqueRgn3.wav', 'EsfuerzoCorto3Rgn')
EsfuerzoCorto3Rgn.SendNotify=0
EsfuerzoCorto3Rgn.Volume=0.8
EsfuerzoCorto4Rgn=Bladex.CreateSound('../../sounds/ataqueRgn4.wav', 'EsfuerzoCorto4Rgn')
EsfuerzoCorto4Rgn.SendNotify=0
EsfuerzoCorto4Rgn.Volume=0.8
EsfuerzoCorto5Rgn=Bladex.CreateSound('../../sounds/ataqueRgn5.wav', 'EsfuerzoCorto5Rgn')
EsfuerzoCorto5Rgn.SendNotify=0
EsfuerzoCorto5Rgn.Volume=0.8
EsfuerzoCorto6Rgn=Bladex.CreateSound('../../sounds/ataqueRgn2.wav', 'EsfuerzoCorto6Rgn')
EsfuerzoCorto6Rgn.SendNotify=0
EsfuerzoCorto6Rgn.Volume=0.8
SesgadoCorto=Bladex.CreateSound('../../sounds/sesgado-corto.wav', 'SesgadoCorto')
SesgadoCorto.SendNotify=0
SesgadoCorto.Volume=0.6
SesgadoLargo=Bladex.CreateSound('../../sounds/sesgado-largo.wav', 'SesgadoLargo')
SesgadoLargo.SendNotify=0
SesgadoLargo.Volume=0.6
SesgadoCortoGrave=Bladex.CreateSound('../../sounds/sesgado-corto-grave.wav', 'SesgadoCortoGrave')
SesgadoCortoGrave.SendNotify=0
SesgadoCortoGrave.Volume=0.6
SesgadoLargoGrave=Bladex.CreateSound('../../sounds/sesgado-largo-grave.wav', 'SesgadoLargoGrave')
SesgadoLargoGrave.SendNotify=0
SesgadoCortoGrave.Volume=0.6
SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=0
SesgadoCortoGrave.Volume=0.6
SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=0
SesgadoCortoGrave.Volume=0.6
EsfuerzoGolpeFrontalRgn=Bladex.CreateSound('../../sounds/ataque-largoRgn.wav', 'EsfuerzoGolpeFrontalRgn')
EsfuerzoGolpeFrontalRgn.SendNotify=0
EsfuerzoGolpeLateralRgn=Bladex.CreateSound('../../sounds/ataque-largoRgn1.wav', 'EsfuerzoGolpeLateralRgn')
EsfuerzoGolpeLateralRgn.SendNotify=0
EsfuerzoGolpeCabezaRgn=Bladex.CreateSound('../../sounds/ataque-largoRgn2.wav', 'EsfuerzoGolpeCabezaRgn')
EsfuerzoGolpeCabezaRgn.SendNotify=0
EsfuerzoGolpeAtrasRgn=Bladex.CreateSound('../../sounds/ataque-largoRgn3.wav', 'EsfuerzoGolpeAtrasRgn')
EsfuerzoGolpeAtrasRgn.SendNotify=0
EsfuerzoRgnMediano=Bladex.CreateSound('../../sounds/ataque-largoRgn4.wav', 'EsfuerzoRgnMediano')
EsfuerzoRgnMediano.SendNotify=0
EsfuerzoGolpeArribaRgn=Bladex.CreateSound('../../sounds/ataque-largoRgn5.wav', 'EsfuerzoGolpeArribaRgn')
EsfuerzoGolpeArribaRgn.SendNotify=0

MuerteRagnar1=Bladex.CreateSound('../../sounds/muerteRgn.wav', 'MuerteRagnar1')
MuerteRagnar1.SendNotify=0
MuerteRagnar2=Bladex.CreateSound('../../sounds/muerteRgn1.wav', 'MuerteRagnar2')
MuerteRagnar2.SendNotify=0
MuerteRagnar3=Bladex.CreateSound('../../sounds/muerteRgn2.wav', 'MuerteRagnar3')
MuerteRagnar3.SendNotify=0
MuerteRagnar4=Bladex.CreateSound('../../sounds/muerteRgn3.wav', 'MuerteRagnar4')
MuerteRagnar4.SendNotify=0

MuerteRagnar=Bladex.CreateSound('../../sounds/ragnar-die.wav', 'MuerteRagnar')
MuerteRagnar.SendNotify=0
HeridaRagnar=Bladex.CreateSound('../../sounds/ragnar-hurt.wav', 'HeridaRagnar')
HeridaRagnar.SendNotify=0


HeridaRagnar1=Bladex.CreateSound('../../sounds/heridaRgn1.wav', 'HeridaRagnar1')
HeridaRagnar1.SendNotify=0
HeridaRagnar2=Bladex.CreateSound('../../sounds/heridaRgn2.wav', 'HeridaRagnar2')
HeridaRagnar2.SendNotify=0
HeridaRagnar3=Bladex.CreateSound('../../sounds/heridaRgn3.wav', 'HeridaRagnar3')
HeridaRagnar3.SendNotify=0

RisaRagnar=Bladex.CreateSound('../../sounds/risa-ragnar.wav', 'RisaRagnar')
RisaRagnar.MinDistance=10000
RisaRagnar.MaxDistance=25000
InsultoRagnar=Bladex.CreateSound('../../sounds/'+language+'/insultoRgn.wav', 'InsultoRagnar')
InsultoRagnar.MinDistance=15000
InsultoRagnar.MaxDistance=25000

InsultoRagnar=Bladex.CreateSound('../../sounds/'+language+'/insultoRgn.wav', 'InsultoRagnar')
InsultoRagnar.MinDistance=15000
InsultoRagnar.MaxDistance=25000


AndarRagnar1=Bladex.CreateSound('../../sounds/mov-armadura-5.wav', 'AndarRagnar1')
AndarRagnar1.SendNotify=0
AndarRagnar1.Volume=0.3
AndarRagnar1.MinDistance=5000
AndarRagnar1.MaxDistance=15000
AndarRagnar2=Bladex.CreateSound('../../sounds/mov-armadura-6.wav', 'AndarRagnar2')
AndarRagnar2.SendNotify=0
AndarRagnar2.Volume=0.3
AndarRagnar2.MinDistance=5000
AndarRagnar2.MaxDistance=15000

CaidaRagnar1=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaRagnar1')
CaidaRagnar1.SendNotify=0
CaidaRagnar1.Volume=0.8
CaidaRagnar1.MinDistance=1000
CaidaRagnar1.MaxDistance=25000

CaidaRagnar2=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaRagnar2')
CaidaRagnar2.SendNotify=0
CaidaRagnar2.Volume=0.8
CaidaRagnar2.MinDistance=1000
CaidaRagnar2.MaxDistance=25000

DesangreRagnar1=Bladex.CreateSound('../../sounds/desangre2.wav', 'DesangreRagnar1')
DesangreRagnar1.SendNotify=0
DesangreRagnar1.Volume=0.8
DesangreRagnar1.MinDistance=1000
DesangreRagnar1.MaxDistance=25000
DesangreRagnar2=Bladex.CreateSound('../../sounds/desangre4.wav', 'DesangreRagnar2')
DesangreRagnar2.SendNotify=0
DesangreRagnar2.Volume=0.8
DesangreRagnar2.MinDistance=1000
DesangreRagnar2.MaxDistance=25000




print "Sonidos para Ragnar creados..."