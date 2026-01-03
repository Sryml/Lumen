


#---------------------poner sol--------------------------------------------------------------

Bladex.SetSun(1,1,1.5,1)

#-------------------------LUCES----------------------------------

#-------------------------LUZ DEL-AGUA-VENENOSA---------------------------------

luz2=Bladex.CreateEntity("Luz2","Entity Spot",-54000,-1300,500)
luz2.Color=101,139,16
luz2.Intensity=8
luz2.Precission=0.09
luz2.CastShadows=0
luz2.Visible=0
luz2.Flick=1

#-------------------------LUZ DEL-AGUA----------------------------------

luz3=Bladex.CreateEntity("Luz2","Entity Spot",-24875,10000,60500)
luz3.Color=53,125,147
luz3.Intensity=3
luz3.Precission=0.09
luz3.CastShadows=0
luz3.Visible=0
luz3.Flick=0
#-------------------------LUZ DEL-HUECO----------------------------------

luz4=Bladex.CreateEntity("Luz2","Entity Spot",-24875,-17000,65750)
luz4.Color=142,103,49
luz4.Intensity=19
luz4.Precission=0.09
luz4.CastShadows=0
luz4.Visible=0
luz4.Flick=0
#-------------------------CRIPTA LUZ DE LA GEMA----------------------------------

#luz1=Bladex.CreateEntity("Luz1","Entity Spot",-24750,.17000,65750)
#luz1.Color=185,166,230
#luz1.Intensity=0.3

#-------------------------ROTO DEL INICIO----------------------------------

luz5=Bladex.CreateEntity("Luz1","Entity Spot",-43000,0,-118500)
luz5.Color=74,74,74
luz5.Intensity=5
luz5.CastShadows=0
luz5.Precission=0.06
luz5.Visible=0
luz5.Flick=0

#-------------------------LUZ DE LA TABLILLA----------------------------------

#luz6=Bladex.CreateEntity("Luz6","Entity Spot",-62750,1229,124250)
#luz6.Color=249,174,0
#luz6.Intensity=15
#luz6.Precission=0.035

#oo=Bladex.CreateEntity("NoName0","Tablilla6",-62454.575000,1376.411000,124172.607000)
#oo.Static=0
#oo.Scale=2.0
#oo.Orientation=0.408968,-0.606320,0.381369,0.565402
#oo.CastShadows=0

#-----------------------AGUA------------------------------------------------

#baño_octogonal=Bladex.CreateEntity("baño_octogonal","Entity Water",8000,400,-24000)
#baño_octogonal.Reflection=-1
#baño_octogonal.Color=5,10,15


##################################################################################################
###-----------------GEMAS EN EL INTERIOR DEL TEMPLO-----------------------------------------------

GemLight3=Bladex.CreateEntity("GemLight3","Entity Spot",-17875,-7800,30000)
GemLight3.Color =80,144,96
GemLight3.Intensity = 0.5
GemLight3.Precission = 0.06
GemLight3.CastShadows = 0
GemLight3.Visible = 0 
GemLight3.Flick = 0

GemLight4=Bladex.CreateEntity("GemLight4","Entity Spot",-31875,-7500,30000)
GemLight4.Color = 80,144,96
GemLight4.Intensity = 0.5
GemLight4.Precission = 0.06
GemLight4.CastShadows = 0
GemLight4.Visible = 0 
GemLight4.Flick = 0


RGemLight=Bladex.CreateEntity("RGemLight","Entity Spot",-32125,-4300,23250)
RGemLight.Color =80,144,96
RGemLight.Intensity = 0.8
RGemLight.Precission = 0.09
RGemLight.CastShadows = 0
RGemLight.Visible = 0 
RGemLight.Flick = 0

RGemLight2=Bladex.CreateEntity("RGemLight2","Entity Spot",-17625,-4300,23250)
RGemLight2.Color = 80,144,96
RGemLight2.Intensity = 0.8
RGemLight2.Precission = 0.09
RGemLight2.CastShadows = 0
RGemLight2.Visible = 0 
RGemLight2.Flick = 0


GemLight5=Bladex.CreateEntity("GemLight5","Entity Spot",-32125,-7800,56500)
GemLight5.Color =80,144,96
GemLight5.Intensity = 0.5
GemLight5.Precission = 0.06
GemLight5.CastShadows = 0
GemLight5.Visible = 0 
GemLight5.Flick = 0

GemLight6=Bladex.CreateEntity("GemLight6","Entity Spot",-17625,-7500,56500)
GemLight6.Color = 80,144,96
GemLight6.Intensity = 0.5
GemLight6.Precission = 0.06
GemLight6.CastShadows = 0
GemLight6.Visible = 0 
GemLight6.Flick = 0