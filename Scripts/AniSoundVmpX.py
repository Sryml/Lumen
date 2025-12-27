import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************


GolpeArmaEscudoVmp=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoVmp')
GolpeArmaEscudoVmp.SendNotify=1
GolpeArmaArmaVmp=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaVmp')
GolpeArmaArmaVmp.SendNotify=1
TajoEmpalanteVmp=Bladex.CreateSound('../../sounds/corte-carne.wav', 'TajoEmpalanteVmp')
TajoEmpalanteVmp.SendNotify=1
TajoCortanteVmp=Bladex.CreateSound('../../sounds/corte-carne-2.wav', 'TajoCortanteVmp')
TajoCortanteVmp.SendNotify=1
TajoMutilacionVmp=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionVmp')
TajoMutilacionVmp.SendNotify=1
GolpeContundenteVmp=Bladex.CreateSound('../../sounds/golpe-maza-carne.wav', 'GolpeContundenteVmp')
GolpeContundenteVmp.SendNotify=1


Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')
Enfundar.SendNotify=0
EsfuerzoCortoVmp=Bladex.CreateSound('../../sounds/AtaqueVmp1.wav', 'EsfuerzoCortoVmp')
EsfuerzoCortoVmp.SendNotify=0
EsfuerzoCortoVmp.Volume=0.8
EsfuerzoCorto1Vmp=Bladex.CreateSound('../../sounds/AtaqueVmp2.wav', 'EsfuerzoCorto1Vmp')
EsfuerzoCorto1Vmp.SendNotify=0
EsfuerzoCorto1Vmp.Volume=0.8
EsfuerzoCorto2Vmp=Bladex.CreateSound('../../sounds/AtaqueVmp3.wav', 'EsfuerzoCorto2Vmp')
EsfuerzoCorto2Vmp.SendNotify=0
EsfuerzoCorto2Vmp.Volume=0.8
EsfuerzoCorto3Vmp=Bladex.CreateSound('../../sounds/AtaqueVmp4.wav', 'EsfuerzoCorto3Vmp')
EsfuerzoCorto3Vmp.SendNotify=0
EsfuerzoCorto3Vmp.Volume=0.8
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
MuerteVmp1=Bladex.CreateSound('../../sounds/MuerteVmp.wav', 'MuerteVmp1')
MuerteVmp1.SendNotify=0
HeridaVmp1=Bladex.CreateSound('../../sounds/HeridaVmp1.wav', 'HeridaVmp1')
HeridaVmp1.SendNotify=0
HeridaVmp2=Bladex.CreateSound('../../sounds/HeridaVmp2.wav', 'HeridaVmp2')
HeridaVmp2.SendNotify=0

DesapareceVmp=Bladex.CreateSound('../../sounds/desaparece-vamp1.wav', 'DesapareceVmp')
DesapareceVmp.SendNotify=0
DesapareceVmp.Volume=1
DesapareceVmp.MinDistance=1000
DesapareceVmp.MaxDistance=25000

CaidaVmp1=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaVmp1')
CaidaVmp1.SendNotify=0
CaidaVmp1.Volume=0.3
CaidaVmp2=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaVmp2')
CaidaVmp2.SendNotify=0
CaidaVmp2.Volume=0.3

RespiracionVmp1=Bladex.CreateSound('../../sounds/respiracionVmp1.wav', 'RespiracionVmp1')
RespiracionVmp1.SendNotify=0
RespiracionVmp1.Volume=0.5
RespiracionVmp1.MinDistance=1000
RespiracionVmp1.MaxDistance=16000
RespiracionVmp2=Bladex.CreateSound('../../sounds/respiracionVmp2.wav', 'RespiracionVmp12')
RespiracionVmp2.SendNotify=0
RespiracionVmp2.Volume=0.5
RespiracionVmp2.MinDistance=1000
RespiracionVmp2.MaxDistance=16000

RespiracionVmp3=Bladex.CreateSound('../../sounds/respiracionVmp3.wav', 'RespiracionVmp3')
RespiracionVmp3.SendNotify=0
RespiracionVmp3.Volume=0.5
RespiracionVmp3.MinDistance=1000
RespiracionVmp3.MaxDistance=16000
RespiracionVmp4=Bladex.CreateSound('../../sounds/respiracionVmp4.wav', 'RespiracionVmp4')
RespiracionVmp4.SendNotify=0
RespiracionVmp4.Volume=0.5
RespiracionVmp4.MinDistance=1000
RespiracionVmp4.MaxDistance=16000

AguadoVmp1=Bladex.CreateSound('../../sounds/Aguado1.wav', 'AguadoVmp1')
AguadoVmp1.SendNotify=0
AguadoVmp1.Volume=0.5
AguadoVmp1.MinDistance=1000
AguadoVmp1.MaxDistance=25000
AguadoVmp2=Bladex.CreateSound('../../sounds/Aguado2.wav', 'AguadoVmp2')
AguadoVmp2.SendNotify=0
AguadoVmp2.Volume=0.5
AguadoVmp2.MinDistance=1000
AguadoVmp2.MaxDistance=25000
AguadoVmp3=Bladex.CreateSound('../../sounds/Aguado3.wav', 'AguadoVmp3')
AguadoVmp3.SendNotify=0
AguadoVmp3.Volume=0.5
AguadoVmp3.MinDistance=1000
AguadoVmp3.MaxDistance=25000

RoceVmp1=Bladex.CreateSound('../../sounds/mov-troll-2.wav', 'RoceVmp1')
RoceVmp1.SendNotify=0
RoceVmp1.MinDistance=1000
RoceVmp1.MaxDistance=25000
RoceVmp2=Bladex.CreateSound('../../sounds/mov-troll-1.wav', 'RoceVmp2')
RoceVmp2.SendNotify=0
RoceVmp2.MinDistance=1000
RoceVmp2.MaxDistance=25000


InsultoVmp=Bladex.CreateSound('../../sounds/insultoVmp.wav', 'InsultoVmp')
InsultoVmp.SendNotify=0




print "Sonidos para el vampiro creados..."
