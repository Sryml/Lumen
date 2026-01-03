import whrandom
import Bladex
import dust
import darfuncs

TemblorMalditoTerror=Bladex.CreateSound("../../Sounds/Stone-floor-collapse.wav", "TemblorMalditoTerror")
TemblorMalditoTerror.Volume=1
TemblorMalditoTerror.MinDistance=10000
TemblorMalditoTerror.MaxDistance=40000

TemblorMalditoTerror2=Bladex.CreateSound("../../Sounds/derrumbe.wav", "TemblorMalditoTerror2")
TemblorMalditoTerror2.Volume=1
TemblorMalditoTerror2.MinDistance=10000
TemblorMalditoTerror2.MaxDistance=40000

Surtidores = [
		(293294,-11867,-19647),  #exterior arriba antes de primer derrumbamiento
		(301758,-11848,-17537),  #idem
		(295341, 1393,  12695),  #justo antes primer puente
		( 31042, 4252, -21727),  #justo despues primer puente
		(295318, 7842, -29259),  #justo antes escena orcos
		(304353,33201, -53153),  #justo despues escena orcos
		(316342,35772,  -8606),  #justo antes puente rompible
		(283216,38039,  17413),  #en zona minorxxxx
		(333226,35120, -72011),  #en zona guardias
		(350481,35222, -69874),  #en zona guardias
		(372364,37496, -64122),  #en zona guardias
		(345059,39742, -93694),  #en zona guardias
		(368463,38667, -87474),  #en zona guardias
		(382312,45390, -61858),  # tras ultimo rastrillo
		(393382,49097, -46317),  # tras ultimo rastrillo
		(369573,13974,-31097),   # en zona twin golems
		(353822,20413,-56209),   # en zona twin golems
		]

SurtiActivados = 1
NivelTemblor   = 2


ActivaTemblorcito()

darfuncs.EnterSecEvent(320494.862267, 41862.1291972, -69516.7297415,Atenua1)
darfuncs.EnterSecEvent(391950.203616, 57860.6967173, -23956.6747875,Atenua2)
darfuncs.EnterSecEvent(421398,76854,-24945,Atenua3)