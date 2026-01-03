##################################################################
# Puertas que se rompen
#
# YUio
##################################################################

import Reference
import Select
import Change
import Actions
import Sounds
#import AniSound

LifeGateA = 3
LifeGateB = 3
LifeGateC = 3
LifeGateD = 3

break_sound=Sounds.CreateEntitySound('../../Sounds/M-derribo-muro.wav', 'SonidoDesprendimiento')
break_sound.Volume=1.0
break_sound.MinDistance=10000
break_sound.MaxDistance=40000

hit_sound = [0,0]

hit_sound[0]=Sounds.CreateEntitySound('../../Sounds/golpe-2.wav', 'SonidoHit')
hit_sound[0].Volume=1.0
hit_sound[0].MinDistance=10000
hit_sound[0].MaxDistance=40000

hit_sound[1]=Sounds.CreateEntitySound('../../Sounds/golpe-3.wav', 'SonidoHit')
hit_sound[1].Volume=1.0
hit_sound[1].MinDistance=10000
hit_sound[1].MaxDistance=40000

n_hit_sound = 0

bgateA1=Bladex.GetSector(16000,-5000,72000)		### SECTORES QUE SE ROMPEN
bgateA2=Bladex.GetSector(16000,-5000,70500)
bgateB1=Bladex.GetSector(16000,-5000,96000)
bgateB2=Bladex.GetSector(16000,-5000,95000)
bgateC1=Bladex.GetSector(-67500,-5000,85000)
bgateC2=Bladex.GetSector(-67500,-5000,84000)
bgateD1=Bladex.GetSector(-37875,-6000,114500)
bgateA1.Active=0
bgateA2.Active=0
bgateB1.Active=0
bgateB2.Active=0
bgateC1.Active=0
bgateC2.Active=0
bgateD1.Active=0
bgateA1.InitBreak( (200,0,0),(0,1200,0),(0,1000,1200),'piedra pesada')		#PARAMETROS DE ROTURA
bgateA2.InitBreak( (200,0,0),(0,1200,80),(0,1200,400),'piedra pesada')
bgateB1.InitBreak( (200,0,0),(0,1200,0),(0,1000,1200),'piedra pesada')
bgateB2.InitBreak( (200,0,0),(0,1200,80),(0,1200,400),'piedra pesada')
bgateC1.InitBreak( (200,0,0),(0,1200,0),(0,1000,1200),'piedra pesada')
bgateC2.InitBreak( (200,0,0),(0,1200,80),(0,1200,400),'piedra pesada')
bgateD1.InitBreak( (200,0,0),(0,1200,0),(0,1000,1200),'piedra pesada')



bgateA=Bladex.GetSector(15500,-5000,71500)		#SECTOR DELANTE DEL ROTO
bgateB=Bladex.GetSector(15500,-5000,95500)
bgateC=Bladex.GetSector(-67000,-5000,84000)
bgateD=Bladex.GetSector(-37400,-5000,116000)

bgateA.ActiveSurface= -1.0, 0.0, 0.0			#NORMAL A LA CARA DEL SECTOR QUE SE ROMPE
bgateA.OnHit=revientaPuertaA
bgateB.ActiveSurface= -1.0, 0.0, 0.0
bgateB.OnHit=revientaPuertaB
bgateC.ActiveSurface= 1.0, 0.0, 0.0
bgateC.OnHit=revientaPuertaC
bgateD.ActiveSurface= 1.0, 0.0, 0.0
bgateD.OnHit=revientaPuertaD