


#---------------------poner sol--------------------------------------------------------------

Bladex.SetSun(1,1,1.5,1)




#-------------------------LUCES----------------------------------

#-------------------------LUZ DEL-ROTO-AGUA-VENENOSA---------------------------------
luz1=Bladex.CreateEntity("Luz1","Entity Spot",-53998.680116,-2991.954951,-18197.746435)
luz1.Color=124,131,186
luz1.Intensity=1
luz1.Precission=0.04
luz1.CastShadows=0
luz1.Visible=0
luz1.Flick=0


#-------------------------LUZ DEL-AGUA-VENENOSA---------------------------------
luz2=Bladex.CreateEntity("Luz2","Entity Spot",-54000,-1300,500)
luz2.Color=101,139,16
luz2.Intensity=8
luz2.Precission=0.09
luz2.CastShadows=0
luz2.Visible=0
luz2.Flick=1

#-------------------------LUZ DEL-AGUA-SAGRADA---------------------------------

luz3=Bladex.CreateEntity("Luz2","Entity Spot",8037.755217,-1578.716652,-25077.563290)
#luz3.Color=53,125,147
luz3.Color=58,158,197
luz3.Intensity=6
luz3.Precission=0.09
luz3.CastShadows=0
luz3.Visible=0
luz3.Flick=0
#-------------------------LUZ DEL-CHORRO-SAGRADO--------------------------

luz4=Bladex.CreateEntity("Luz2","Entity Spot",7946.362016,-3082.103118,-4287.858452)
luz4.Color=96,128,164
luz4.Intensity=2
luz4.Precission=0.04
luz4.CastShadows=0
luz4.Visible=0
luz4.Flick=0

#-------------------------ROTO DEL INICIO----------------------------------

luz5=Bladex.CreateEntity("Luz1","Entity Spot",-43000,0,-118500)
luz5.Color=74,74,74
luz5.Intensity=5
luz5.CastShadows=0
luz5.Precission=0.06
luz5.Visible=0
luz5.Flick=0

