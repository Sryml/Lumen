import darfuncs
import Objects



#-------------------------LUCES----------------------------------

#-------------------------LUZ DEL-GENERADOR----------------------------------

luz1=Bladex.CreateEntity("Luzg1","Entity Spot",-4000,2600,-20500)
luz1.Color=80,40,10
luz1.Intensity=4
luz1.Precission=0.1
luz1.Visible=0
luz1.CastShadows=0
luz1.Flick=0

luz1b=Bladex.CreateEntity("Luzg2","Entity Spot",-4000,2600,-10500)
luz1b.Color=80,40,10
luz1b.Intensity=3
luz1b.Precission=0.1
luz1b.Visible=0
luz1b.CastShadows=0
luz1b.Flick=0

#-------------------------LUZ DE-la-sala-de-las-tablillas-----

#luz2=Bladex.CreateEntity("Luz2","Entity Spot",-38000,4000,25000)
#luz2.Color=20,60,110
#luz2.Intensity=22
#luz2.Precission=0.3
#luz2.Visible=0
#luz2.CastShadows=0
#luz2.Flick=0

#-------------------------LUZ DEL-GENERADOR-DE-LOS-BAGNOS--------

luz3=Bladex.CreateEntity("Luz3","Entity Spot",-36000,4600,-14000)
luz3.Color=80,110,110
luz3.Intensity=3
luz3.Precission=0.09
luz3.Visible=0
luz3.CastShadows=0
luz3.Flick=0

#-------------------------LUZ DEL-GENERADOR-DE-LA-TABLILLA--------

#1
#luz4=Bladex.CreateEntity("Luz4","Entity Spot",4500,6500,-12000)
#luz4.Color=79,98,79
#luz4.Intensity=5
#luz4.Precission=0.06
#luz4.Visible=0
#luz4.CastShadows=0
#luz4.Flick=0

#2
luz5=Bladex.CreateEntity("Luz5","Entity Spot",-3000,6500,-4000)
luz5.Color=80,40,10
luz5.Intensity=2
luz5.Precission=0.06
luz5.Visible=0
luz5.CastShadows=0
luz5.Flick=0


#luz del pozo
#2
luz6=Bladex.CreateEntity("Luz6","Entity Spot",1500,16000,5500)
luz6.Color=61,86,146
luz6.Intensity=3
luz6.Precission=0.06
luz6.Visible=0
luz6.CastShadows=0
luz6.Flick=0

#####################################################################################33
##
##	LUCES EN LA SALA DE LAS RUNAS
##
#######################################################################################


#1
luz7=Bladex.CreateEntity("Luz7","Entity Spot",-48750,12000,19250)
luz7.Color=61,86,146
luz7.Intensity=3
luz7.Precission=0.1
luz7.Visible=0
luz7.CastShadows=0
luz7.Flick=0

#2
luz8=Bladex.CreateEntity("Luz8","Entity Spot",-48500,12000,30750)
luz8.Color=61,86,146
luz8.Intensity=3
luz8.Precission=0.1
luz8.Visible=0
luz8.CastShadows=0
luz8.Flick=0

#3
luz9=Bladex.CreateEntity("Luz9","Entity Spot",-38250,12000,36750)
luz9.Color=61,86,146
luz9.Intensity=3
luz9.Precission=0.1
luz9.Visible=0
luz9.CastShadows=0
luz9.Flick=0

#4
luz10=Bladex.CreateEntity("Luz10","Entity Spot",-28000,12000,19250)
luz10.Color=61,86,146
luz10.Intensity=3
luz10.Precission=0.1
luz10.Visible=0
luz10.CastShadows=0
luz10.Flick=0

#5
luz11=Bladex.CreateEntity("Luz11","Entity Spot",-28000,12000,31000)
luz11.Color=61,86,146
luz11.Intensity=3
luz11.Precission=0.1
luz11.Visible=0
luz11.CastShadows=0
luz11.Flick=0

#6
luz10=Bladex.CreateEntity("Luz10","Entity Spot",-38250,12000,13000)
luz10.Color=61,86,146
luz10.Intensity=3
luz10.Precission=0.1
luz10.Visible=0
luz10.CastShadows=0
luz10.Flick=0

########################################################################

##	NOMBRES DE LAS RUNAS

########################################################################

runa1=Bladex.CreateEntity("Runa1","GhostPointer",-48750,12000,19250)
darfuncs.SetHint(runa1,"ARYAMAN")

runa2=Bladex.CreateEntity("Runa2","GhostPointer",-48500,12000,30750)
darfuncs.SetHint(runa2,"HAURVATAT")

runa3=Bladex.CreateEntity("Runa3","GhostPointer",-38250,12000,36750)
darfuncs.SetHint(runa3,"XSHATHRA")

runa4=Bladex.CreateEntity("Runa4","GhostPointer",-28000,12000,19250)
darfuncs.SetHint(runa4,"IANNA")

runa5=Bladex.CreateEntity("Runa5","GhostPointer",-28000,12000,31000)
darfuncs.SetHint(runa5,"AMERETAT")

runa6=Bladex.CreateEntity("Runa6","GhostPointer",-38250,12000,13000)
darfuncs.SetHint(runa6,"ARAMATI")