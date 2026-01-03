import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import GameText


"""	
p=Bladex.CreateEntity("g1","GhostPointer",-29695.6788199, 3965.4, -61025.7630464)
p.Static=0
p.Scale=0.10
p.Orientation=0.312668,0.641065,0.307258,-0.629973
p.UseFunc = cogeT1
	
p=Bladex.CreateEntity("g2","GhostPointer",-28695.6788199, 3965.4, -61025.7630464)
p.Static=0
p.Scale=0.10
p.Orientation=0.312668,0.641065,0.307258,-0.629973
p.UseFunc = cogeT2
	
p=Bladex.CreateEntity("g3","GhostPointer",-27695.6788199, 3965.4, -61025.7630464)
p.Static=0
p.Scale=0.10
p.Orientation=0.312668,0.641065,0.307258,-0.629973
p.UseFunc = cogeT3

	
p=Bladex.CreateEntity("g4","GhostPointer",-26695.6788199, 3965.4, -61025.7630464)
p.Static=0
p.Scale=0.10
p.Orientation=0.312668,0.641065,0.307258,-0.629973
p.UseFunc = cogeT4

	
p=Bladex.CreateEntity("g5","GhostPointer",-25695.6788199, 3965.4, -61025.7630464)
p.Static=0
p.Scale=0.10
p.Orientation=0.312668,0.641065,0.307258,-0.629973
p.UseFunc = cogeT5

	
p=Bladex.CreateEntity("g6","GhostPointer",-24695.6788199, 3965.4, -61025.7630464)
p.Static=0
p.Scale=0.10
p.Orientation=0.312668,0.641065,0.307258,-0.629973
p.UseFunc = cogeT6
"""
#-----------------------AGUA------------------------------------------------

agua_inicio=Bladex.CreateEntity("agua_inicio","Entity Water",-38000,4520,-53000)
agua_inicio.Reflection=1.3
agua_inicio.Color=15,4,0

agua_segunda=Bladex.CreateEntity("agua_segunda","Entity Water",-26000,460,-17000)
agua_segunda.Reflection=1.3
agua_segunda.Color=15,4,0

agua_shiva1=Bladex.CreateEntity("agua_shiva1","Entity Water",-35000,1650,73000)
agua_shiva1.Reflection=1.3
agua_shiva1.Color=15,14,10

agua_shiva2=Bladex.CreateEntity("agua_shiva2","Entity Water",9000,-750,91000)
agua_shiva2.Reflection=1.3
agua_shiva2.Color=15,14,10

agua_port=Bladex.CreateEntity("agua_port","Entity Water",-26000,250,134000)
agua_port.Reflection=1.3
agua_port.Color=15,14,10

agua_chorros=Bladex.CreateEntity("agua_chorros","Entity Water",9800,5300,168000)
agua_chorros.Reflection=1.3
agua_chorros.Color=15,14,10

agua_puente=Bladex.CreateEntity("agua_puente","Entity Water",-6000,11300,221000)
agua_puente.Reflection=1.3
agua_puente.Color=15,14,10

agua_final=Bladex.CreateEntity("agua_final","Entity Water",-4000,-700,244000)
agua_final.Reflection=1
agua_final.Color=5,4,4
"""
agua_espiral=Bladex.CreateEntity("agua_espiral","Entity Water",20000,500,-258250)
agua_espiral.Reflection=1
agua_espiral.Color=5,4,4
"""
agua_cabeza=Bladex.CreateEntity("agua_cabeza","Entity Water",-61000,950,70250)
agua_cabeza.Reflection=-0.5
agua_cabeza.Color=1,2,2



#################################
########### pilones #############
#################################

agua_final1=Bladex.CreateEntity("agua_final1","Entity Water",89000,-1600,203000)
agua_final1.Reflection=1
agua_final1.Color=1,1,1

agua_final2=Bladex.CreateEntity("agua_final2","Entity Water",89000,-1600,209000)
agua_final2.Reflection=1
agua_final2.Color=1,1,1

agua_final3=Bladex.CreateEntity("agua_final3","Entity Water",99500,-1600,203000)
agua_final3.Reflection=1
agua_final3.Color=1,1,1

agua_final4=Bladex.CreateEntity("agua_final4","Entity Water",99500,-1600,209000)
agua_final4.Reflection=1
agua_final4.Color=1,1,1


#################################
########### cripta  #############
#################################

agua_cripta=Bladex.CreateEntity("agua_cripta","Entity Water",-24000,15500,96750)
agua_cripta.Reflection=-1.5
agua_cripta.Color=1,1,1




##############################
########### LUCES ############
##############################



#######################
##### LUZ EN FATEPUR

luzFAT=Bladex.CreateEntity("LuzFAT","Entity Spot",-15200,11600,220300)
luzFAT.Color=65,96,124
luzFAT.Intensity=15
luzFAT.CastShadows=0
luzFAT.Precission=0.1
luzFAT.Visible=0
luzFAT.Flick=0


luzFAT2=Bladex.CreateEntity("LuzFAT2","Entity Spot",7690.36197389, 10605.1475285, 210966.6388)
luzFAT2.Color=65,96,154
luzFAT2.Intensity=10
luzFAT2.CastShadows=0
luzFAT2.Precission=0.1
luzFAT2.Visible=0
luzFAT2.Flick=0

luzFAT3=Bladex.CreateEntity("LuzFAT3","Entity Spot",6128.09126378, 10592.2475506, 222703.326)
luzFAT3.Color=35,56,64
luzFAT3.Intensity=25
luzFAT3.CastShadows=0
luzFAT3.Precission=0.1
luzFAT3.Visible=0
luzFAT3.Flick=0

luzFAT4=Bladex.CreateEntity("LuzFAT4","Entity Spot",-22893.1562644, 10592.4855966, 211356.24)
luzFAT4.Color=35,56,84
luzFAT4.Intensity=5
luzFAT4.CastShadows=0
luzFAT4.Precission=0.1
luzFAT4.Visible=0
luzFAT4.Flick=0

#######################
##### LUZ EN EL AGUJERO DE LA SALITA FINAL DEL LABERINTO

luzaug=Bladex.CreateEntity("Luzaug","Entity Spot",20000,-15000,258000)
luzaug.Color=205,176,94
luzaug.Intensity=39
luzaug.CastShadows=0
luzaug.Precission=0.1
luzaug.Visible=0
luzaug.Flick=0

luzLAB0=Bladex.CreateEntity("LuzLAB1","Entity Spot",-4320,-6000,244700)
luzLAB0.Color=31,56,74
luzLAB0.Intensity=39
luzLAB0.CastShadows=0
luzLAB0.Precission=0.1
luzLAB0.Visible=0
luzLAB0.Flick=0


luzLAB1=Bladex.CreateEntity("LuzLAB1","Entity Spot",21900,-6000,237000)
luzLAB1.Color=61,76,94
luzLAB1.Intensity=39
luzLAB1.CastShadows=0
luzLAB1.Precission=0.1
luzLAB1.Visible=0
luzLAB1.Flick=0


luzLAB2=Bladex.CreateEntity("LuzLAB2","Entity Spot",27900,-6000,274300)
luzLAB2.Color=51,86,94
luzLAB2.Intensity=20
luzLAB2.CastShadows=0
luzLAB2.Precission=0.1
luzLAB2.Visible=0
luzLAB2.Flick=0


#######################
##### LUZ EN EL cambio de ritmo donde habia antorchas y esqueletos

luzpega=Bladex.CreateEntity("LuzPega","Entity Spot",3800,-4000,267800)
luzpega.Color=191,176,94
luzpega.Intensity=20
luzpega.CastShadows=0
luzpega.Precission=0.1
luzpega.Visible=0
luzpega.Flick=0