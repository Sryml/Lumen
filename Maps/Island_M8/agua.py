
#----------------------------AGUA---------------------------------
import Water
import LavaDefDamage

mar=Bladex.CreateEntity("mar","Entity Water",-117000,24000,50000)
mar.Reflection=1
mar.Color=0,0,0

aljibe=Bladex.CreateEntity("aljibe","Entity Water",-43000,8300,-45000)
aljibe.Reflection=0.5
aljibe.Color=1,0,0

banio=Bladex.CreateEntity("banio","Entity Water",-35000,5900,-14000)
banio.Reflection=0.6
banio.Color=0,8,1



##generador de enemigos verde
gen1=LavaDefDamage.LAVA_AREA()
gen1.CreateLava ("gen" ,-3000,3600,-10000 ,"cala2",0.05)


#
#    Anteh gera asin :
#
# gen1=Bladex.CreateEntity("gen","Entity Lava",-3000,3600,-10000)
# gen1.Surface.TextureName = "cala2"
# gen1.Surface.Zoom        = 0.1
#
#
# aura e :
#
# gen1.CreateLava ("gen" ,-3000,3600,-10000 ,"cala2",0.01)
#

##muerte en el lago

Water.SetGs("lago.sf","lago")
Water.WaterHi = 24000

#----------------------------FUENTES---------------------------------