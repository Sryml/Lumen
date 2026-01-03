#---------------------poner sol--------------------------------------------------------------

Bladex.SetSun(1,1,0.8,-0.4)

luzsolida2=Bladex.CreateEntity("Luzsolida2","Entity Spot",212183.468895, -8110.256501473, 106836.811)
luzsolida2.Color=245,85,6
luzsolida2.Intensity=15
luzsolida2.CastShadows=0
luzsolida2.Precission=0.36
luzsolida2.Visible=0
luzsolida2.Flick=0

#######lampara en la zona de las vidrieras
luzant1=Bladex.CreateEntity("Luzant1","Entity Spot",361630.501000,-12092.165000,74679.904000)
luzant1.Color=245,125,6
luzant1.Intensity=15
luzant1.CastShadows=0
luzant1.Precission=0.36
luzant1.Visible=0
luzant1.Flick=0







############################################
def Apagala(sectorindex,entityname): 
	a = Bladex.GetEntity(entityname)
	print entityname
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingeAntorcha"


ApagalaSec = Bladex.GetSector(312607.184024, -379.925676625, 128155.646)
ApagalaSec.OnEnter = Apagala
"""
############################################
def Apagala2(sectorindex,entityname): 
	a = Bladex.GetEntity(entityname)
	print entityname
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingeAntorcha"


Apagala2Sec = Bladex.GetSector(296007.184024, 500.25676625, 118155.646)
Apagala2Sec.OnEnter = Apagala2
"""