import dust
import whrandom
import Sounds
# comienza (-21578,  -6764, -19318)
# termina  (-94482, -10568, -66622)
# termina  (-65963, -10318, -57829)
########################################################

Temblon_s=Sounds.CreateEntitySound("../../Sounds/terremoto-piedras.wav","desprendimiento1")
Temblon_s.Volume=1; Temblon_s.MinDistance=2000; Temblon_s.MaxDistance=90000;

Piedruna=Sounds.CreateEntitySound("../../Sounds/M-RUMBLE-ROCA.wav","desprendimiento3")
Piedruna.Volume=1; Piedruna.MinDistance=2000; Piedruna.MaxDistance=90000;

Tiembla_ = 0


SActivaTembluno   = Bladex.GetSector(-21578, -6764, -19318)
SActivaTembluno.OnEnter   = Telmbluno_Com

SDActivaTembluno2 = Bladex.GetSector(-37802.11, -8901.54, -38635.20)
SDActivaTembluno2.OnEnter = Telmbluno_Off



# comienza (-92473, 3484, -72630)
# termina  (-104342, -10315, -4120)
####################################################
#	PRIMER TEMBLOR DE LA CIUDAD

XSActivaTembluno   = Bladex.GetSector(109202.370201, 6429.27706907, -12302.4726494)
XSActivaTembluno.OnEnter   = XTelmbluno_Com

XSActivaTemblunoA   = Bladex.GetSector(105283.470864, 5982.10045541, -47922.7975046)
XSActivaTemblunoA.OnEnter   = XTelmbluno_Com

XSDActivaTembluno1 = Bladex.GetSector(84809.7873309, 1377.87458661, -26190)
XSDActivaTembluno1.OnEnter = XTelmbluno_Off



########################################################
###	TRAS LA PRIMERA PUERTA

YSActivaTembluno   = Bladex.GetSector(-12000.00, -2031.02992528, -46588.3931787)
YSActivaTembluno.OnEnter   = YTelmbluno_Com

YSDActivaTembluno1 = Bladex.GetSector(-22000.0, -2856.59641012, -37000.0)
YSDActivaTembluno1.OnEnter = YTelmbluno_Off



########################################################


ZSActivaTembluno   = Bladex.GetSector(-96376.0847711, -9369.77359202, -57937.8646381)
ZSActivaTembluno.OnEnter   = ZTelmbluno_Com

ZSDActivaTembluno1 = Bladex.GetSector(-122492.529305, -8560.64123353, -68086.9968806)
ZSDActivaTembluno1.OnEnter = ZTelmbluno_Off

########################################################


ASActivaTembluno   = Bladex.GetSector(-133682.359857, -1698.40856057, -34915.5955536)
ASActivaTembluno.OnEnter   = ATelmbluno_Com

ASDActivaTembluno1 = Bladex.GetSector(-91678.9242366, -3893.6920549, -17357.220923)
ASDActivaTembluno1.OnEnter = ATelmbluno_Off