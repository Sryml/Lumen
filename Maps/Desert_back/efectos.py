import Raster
import darfuncs
import dust

Raster.SetDomeColor(185,165,155)


#o=Bladex.CreateEntity("NoName26","Baston3",-24256.840902,-1627.502721,16373.638250)
#o.Scale=1.000000
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.FiresIntensity=[ 98 ]
#o.Lights=[ (1.000000,0.080000,(251,6,0)) ]


#-----------------------AGUA------------------------------------------------

fuente_vida=Bladex.CreateEntity("fuente_vida","Entity Water",6875,-1100,-2625)
fuente_vida.Reflection=-1
fuente_vida.Color=5,10,10

fuente_veneno=Bladex.CreateEntity("fuente_veneno","Entity Water",-54000,-1000,-22000)
fuente_veneno.Reflection=-0.5
fuente_veneno.Color=5,10,10

#en bagno venenoso
agua_ven=Bladex.CreateEntity("agua_monolito","Entity Water",-54000,0,500)
agua_ven.Reflection=-1
agua_ven.Color=0,0,0


#  EN MONOLITO

####agua en trampa de la palabra de dios

agua_god=Bladex.CreateEntity("agua_god","Entity Water",-58000,34000,142000)
agua_god.Reflection=0
agua_god.Color=0,0,0

####agua en el canal exterior

agua_canal=Bladex.CreateEntity("agua_canal","Entity Water",4000,12000,84000)
agua_canal.Reflection=0
agua_canal.Color=0,0,0



banio_octogonal=Bladex.CreateEntity("baño_octogonal","Entity Water",8000,300,-24000)
banio_octogonal.Reflection=0.5
banio_octogonal.Color=0,9,13

oil_altar=Bladex.CreateEntity("oil_altar","Entity Water",-60000,-3300,41500)
oil_altar.Reflection=0
oil_altar.Color=0,0,0



####PIEDRAS VERDES

p=Bladex.CreateEntity("leeagua","PiedraInformativa",5470.825000,-3109.147000,42549.338000)
p.Scale=1.308209
p.Orientation=0.504344,0.504344,-0.495618,0.495618
#p.UseFunc = useInGhostAgua	# cambiar funcion 
#darfuncs.SetHint(p,"Water Oracle")


p=Bladex.CreateEntity("leefuego","PiedraInformativa",-64466.023000,-2549.868000,41861.157000)
p.Scale=1.549318
p.Orientation=0.495618,0.495618,0.504344,-0.504344
#p.UseFunc = useInGhostFuego	# cambiar funcion 
#darfuncs.SetHint(p,"Fire Oracle")


p=Bladex.CreateEntity("leebaston","PiedraInformativa",-24252.197000,-831.667000,11867.282000)
p.Scale=1.967222
p.Orientation=0.694659,0.719340,0.000000,0.000000
#p.UseFunc = useInGhostPuerta	# cambiar funcion 
#darfuncs.SetHint(p,"Door Oracle")


#####################################
#     El rollo de fuego sagrado     #
#####################################
#water_altar_completed = 0
#AlightAltar(0,0)


fsa = dust.RemueveTierraGen(-54250,-300,750  ,900,750, 256, "LargeFire",32,-1)
fsa[0].YGravity=-4000.0
fsa[0].Velocity= 0.0, -500.0, 0.0
fsa[1].YGravity=-4000.0
fsa[1].Velocity= 0.0, -500.0, 0.0