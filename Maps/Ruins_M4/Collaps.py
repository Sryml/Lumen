import Bladex


MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8
MESSAGE_SETSTATICWEPONMODE=13



###################
#     Sonidos     #
###################

derrumbesuelopiedra=Bladex.CreateSound("../../Sounds/Stone-floor-collapse.wav", "DerrumbeSueloPiedra")
derrumbesuelopiedra.Volume=1
derrumbesuelopiedra.MinDistance=5000
derrumbesuelopiedra.MaxDistance=40000

derrumbesueloagua=Bladex.CreateSound("../../Sounds/impact-watersplash.wav", "DerrumbeSueloAgua")
derrumbesueloagua.Volume=1
derrumbesueloagua.MinDistance=5000
derrumbesueloagua.MaxDistance=40000



#################################
#     Derrumbamientos subt.     #
#################################

### Pinchos del derr. cercano al inicio

pinchoderr3=Bladex.CreateEntity("PinchoDerr3","PinchoMiguel",47803.130000,11500.000000,22039.610000,"Weapon")
pinchoderr3.Scale=1.000000
pinchoderr3.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr4=Bladex.CreateEntity("PinchoDerr4","PinchoMiguel",47266.180000,11500.000000,21144.820000,"Weapon")
pinchoderr4.Scale=1.000000
pinchoderr4.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr5=Bladex.CreateEntity("PinchoDerr5","PinchoMiguel",46711.558000,11500.000000,20435.989000,"Weapon")
pinchoderr5.Scale=1.000000
pinchoderr5.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr6=Bladex.CreateEntity("PinchoDerr6","PinchoMiguel",46402.994000,11500.000000,18951.883000,"Weapon")
pinchoderr6.Scale=1.000000
pinchoderr6.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr7=Bladex.CreateEntity("PinchoDerr7","PinchoMiguel",47057.053000,11500.000000,19609.138000,"Weapon")
pinchoderr7.Scale=1.000000
pinchoderr7.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr8=Bladex.CreateEntity("PinchoDerr8","PinchoMiguel",47270.725000,11500.000000,18803.176000,"Weapon")
pinchoderr8.Scale=1.000000
pinchoderr8.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr9=Bladex.CreateEntity("PinchoDerr9","PinchoMiguel",47915.674000,11500.000000,19505.536000,"Weapon")
pinchoderr9.Scale=1.000000
pinchoderr9.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr10=Bladex.CreateEntity("PinchoDerr10","PinchoMiguel",46139.749000,11500.000000,19791.128000,"Weapon")
pinchoderr10.Scale=1.000000
pinchoderr10.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr11=Bladex.CreateEntity("PinchoDerr11","PinchoMiguel",45660.650000,11500.000000,19115.744000,"Weapon")
pinchoderr11.Scale=1.000000
pinchoderr11.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr12=Bladex.CreateEntity("PinchoDerr12","PinchoMiguel",45320.074000,11500.000000,19940.229000,"Weapon")
pinchoderr12.Scale=1.000000
pinchoderr12.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr13=Bladex.CreateEntity("PinchoDerr13","PinchoMiguel",45910.851000,11500.000000,20482.319000,"Weapon")
pinchoderr13.Scale=1.000000
pinchoderr13.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr14=Bladex.CreateEntity("PinchoDerr14","PinchoMiguel",46346.823000,11500.000000,21173.642000,"Weapon")
pinchoderr14.Scale=1.000000
pinchoderr14.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr15=Bladex.CreateEntity("PinchoDerr15","PinchoMiguel",46967.538000,11500.000000,21800.390000,"Weapon")
pinchoderr15.Scale=1.000000
pinchoderr15.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr16=Bladex.CreateEntity("PinchoDerr16","PinchoMiguel",47190.751000,11500.000000,22419.870000,"Weapon")
pinchoderr16.Scale=1.000000
pinchoderr16.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr17=Bladex.CreateEntity("PinchoDerr17","PinchoMiguel",46403.572000,11500.000000,22481.694000,"Weapon")
pinchoderr17.Scale=1.000000
pinchoderr17.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr18=Bladex.CreateEntity("PinchoDerr18","PinchoMiguel",46010.769000,11500.000000,21872.575000,"Weapon")
pinchoderr18.Scale=1.000000
pinchoderr18.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr19=Bladex.CreateEntity("PinchoDerr19","PinchoMiguel",45064.483000,11500.000000,20706.213000,"Weapon")
pinchoderr19.Scale=1.000000
pinchoderr19.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr20=Bladex.CreateEntity("PinchoDerr20","PinchoMiguel",45583.823000,11500.000000,21342.685000,"Weapon")
pinchoderr20.Scale=1.000000
pinchoderr20.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr21=Bladex.CreateEntity("PinchoDerr21","PinchoMiguel",45496.506000,11500.000000,22272.725000,"Weapon")
pinchoderr21.Scale=1.000000
pinchoderr21.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr22=Bladex.CreateEntity("PinchoDerr22","PinchoMiguel",44912.227000,11500.000000,21815.265000,"Weapon")
pinchoderr22.Scale=1.000000
pinchoderr22.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr23=Bladex.CreateEntity("PinchoDerr23","PinchoMiguel",44516.898000,11500.000000,21154.468000,"Weapon")
pinchoderr23.Scale=1.000000
pinchoderr23.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr24=Bladex.CreateEntity("PinchoDerr24","PinchoMiguel",44153.785000,11500.000000,21857.310000,"Weapon")
pinchoderr24.Scale=1.000000
pinchoderr24.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr25=Bladex.CreateEntity("PinchoDerr25","PinchoMiguel",44296.069000,11500.000000,20165.703000,"Weapon")
pinchoderr25.Scale=1.000000
pinchoderr25.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr26=Bladex.CreateEntity("PinchoDerr26","PinchoMiguel",44723.832000,11500.000000,19312.651000,"Weapon")
pinchoderr26.Scale=1.000000
pinchoderr26.Orientation=0.596368,0.596368,-0.379928,0.379928

pinchoderr26a=Bladex.CreateEntity("PinchoDerr26a","PinchoMiguel",48250.069000,11500.000000,21200.703000,"Weapon")
pinchoderr26a.Scale=1.000000
pinchoderr26a.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr26b=Bladex.CreateEntity("PinchoDerr26b","PinchoMiguel",47650.832000,11500.000000,20150.651000,"Weapon")
pinchoderr26b.Scale=1.000000
pinchoderr26b.Orientation=0.596368,0.596368,-0.379928,0.379928




"""
### Pinchos del derr. opuesto al inicio

pinchoderr27=Bladex.CreateEntity("PinchoDerr27","PinchoMiguel",-73763.125000,11000.000000,4034.313000,"Weapon")
pinchoderr27.Scale=1.000000
pinchoderr27.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr28=Bladex.CreateEntity("PinchoDerr28","PinchoMiguel",-72578.401000,11000.000000,3568.248000,"Weapon")
pinchoderr28.Scale=1.000000
pinchoderr28.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr29=Bladex.CreateEntity("PinchoDerr29","PinchoMiguel",-71638.989000,11000.000000,3027.215000,"Weapon")
pinchoderr29.Scale=1.000000
pinchoderr29.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr30=Bladex.CreateEntity("PinchoDerr30","PinchoMiguel",-73343.172000,11000.000000,3263.003000,"Weapon")
pinchoderr30.Scale=1.000000
pinchoderr30.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr31=Bladex.CreateEntity("PinchoDerr31","PinchoMiguel",-72532.798000,11000.000000,2705.359000,"Weapon")
pinchoderr31.Scale=1.000000
pinchoderr31.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr32=Bladex.CreateEntity("PinchoDerr32","PinchoMiguel",-74755.967000,11000.000000,3702.932000,"Weapon")
pinchoderr32.Scale=1.000000
pinchoderr32.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr33=Bladex.CreateEntity("PinchoDerr33","PinchoMiguel",-75568.089000,11000.000000,3098.530000,"Weapon")
pinchoderr33.Scale=1.000000
pinchoderr33.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr34=Bladex.CreateEntity("PinchoDerr34","PinchoMiguel",-74365.240000,11000.000000,2896.032000,"Weapon")
pinchoderr34.Scale=1.000000
pinchoderr34.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr35=Bladex.CreateEntity("PinchoDerr35","PinchoMiguel",-73617.277000,11000.000000,2391.358000,"Weapon")
pinchoderr35.Scale=1.000000
pinchoderr35.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr36=Bladex.CreateEntity("PinchoDerr36","PinchoMiguel",-75098.572000,11000.000000,2451.600000,"Weapon")
pinchoderr36.Scale=1.000000
pinchoderr36.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr37=Bladex.CreateEntity("PinchoDerr37","PinchoMiguel",-75817.232000,11000.000000,1895.928000,"Weapon")
pinchoderr37.Scale=1.000000
pinchoderr37.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr38=Bladex.CreateEntity("PinchoDerr38","PinchoMiguel",-74562.287000,11000.000000,1914.393000,"Weapon")
pinchoderr38.Scale=1.000000
pinchoderr38.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr39=Bladex.CreateEntity("PinchoDerr39","PinchoMiguel",-75305.643000,11000.000000,1034.018000,"Weapon")
pinchoderr39.Scale=1.000000
pinchoderr39.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr40=Bladex.CreateEntity("PinchoDerr40","PinchoMiguel",-74994.323000,11000.000000,-9.715000,"Weapon")
pinchoderr40.Scale=1.000000
pinchoderr40.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr41=Bladex.CreateEntity("PinchoDerr41","PinchoMiguel",-74390.395000,11000.000000,786.271000,"Weapon")
pinchoderr41.Scale=1.000000
pinchoderr41.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr42=Bladex.CreateEntity("PinchoDerr42","PinchoMiguel",-74359.956000,11000.000000,-849.362000,"Weapon")
pinchoderr42.Scale=1.000000
pinchoderr42.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr43=Bladex.CreateEntity("PinchoDerr43","PinchoMiguel",-73939.996000,11000.000000,-78.897000,"Weapon")
pinchoderr43.Scale=1.000000
pinchoderr43.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr44=Bladex.CreateEntity("PinchoDerr44","PinchoMiguel",-73319.506000,11000.000000,-995.893000,"Weapon")
pinchoderr44.Scale=1.000000
pinchoderr44.Orientation=0.707107,0.707107,0.000000,0.000000

pinchoderr45=Bladex.CreateEntity("PinchoDerr45","PinchoMiguel",-72172.571000,11000.000000,-1409.650000,"Weapon")
pinchoderr45.Scale=1.000000
pinchoderr45.Orientation=0.405580,0.405580,-0.579228,0.579228

pinchoderr46=Bladex.CreateEntity("PinchoDerr46","PinchoMiguel",-72760.919000,11000.000000,-487.333000,"Weapon")
pinchoderr46.Scale=1.000000
pinchoderr46.Orientation=0.405580,0.405580,-0.579228,0.579228

######### Funcion: DeactivatePinchoOnHit

######### Funcion: ActivatePinchos

ActivatePinchos()
"""




### Funcionamiento

dersubcerinic=Bladex.GetSector(47000.0, 7600.0, 21000.0)
dersubcerinic.Active=0

dersubopinic=Bladex.GetSector(-73000.0, 6100.0, 1000.0)
dersubopinic.Active=0

dersubcerinic.InitBreak((0.0, 300.0, 0.0), (1800.0, 0.0, -500.0), (300.0, 0.0, 1200.0))
dersubopinic.InitBreak((0.0, 300.0, 0.0), (1800.0, 0.0, -500.0), (300.0, 0.0, 1200.0))

sectordersubcerinic=Bladex.GetSector(47000.0, 7000.0, 21000.0)
sectordersubopinic=Bladex.GetSector(-73000.0, 5500.0, 1000.0)

######### Funcion: Cont2DerSubCerInic

######### Funcion: Cont2DerSubOpInic

######### Funcion: ContDerSubCerInic

######### Funcion: ContDerSubOpInic

######### Funcion: DerSubCerInic

######### Funcion: DerSubOpInic

sectordersubcerinic.OnEnter=DerSubCerInic
sectordersubopinic.OnEnter=DerSubOpInic




### Muerte al caer en los pinchos del derrumbamiento cercano al inicio

######## Funcion: MuertePinchos(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("TSPinchos", "OnEnter", MuertePinchos)




###############################################
#     Derrumbamiento pasarela lago laber.     #
###############################################

derpasarela1=Bladex.GetSector(58250.0, 500.0, 51500.0)
derpasarela1.Active=0

derpasarela2=Bladex.GetSector(57750.0, 500.0, 52500.0)
derpasarela2.Active=0

derpasarela1.InitBreak((0.0, 500.0, 0.0), (1200.0, 0.0, -300.0), (200.0, 0.0, 900.0))
derpasarela2.InitBreak((0.0, 500.0, 0.0), (-200.0, 0.0, 900.0), (1200.0, 0.0, 300.0))

sectorderpasarela=Bladex.GetSector(58000.0, 150.0, 52000.0)

######### Funcion: Cont2DerPasarela

######### Funcion: ContDerPasarela

######### Funcion: DerrumbaPasarela

sectorderpasarela.OnWalkOn=DerrumbaPasarela



##############################################
#     Derrumbamiento pasarela lago subt.     #
##############################################

derpasarelasub1=Bladex.GetSector(-5000.0, 9500.0, -54000.0)
derpasarelasub1.Active=0

derpasarelasub2=Bladex.GetSector(-5000.0, 9500.0, -55000.0)
derpasarelasub2.Active=0

derpasarelasub1.InitBreak((0.0, 1000.0, 0.0), (1200.0, 0.0, -300.0), (200.0, 0.0, 900.0))
derpasarelasub2.InitBreak((0.0, 1000.0, 0.0), (-200.0, 0.0, 900.0), (1200.0, 0.0, 300.0))

sectorderpasarelasub=Bladex.GetSector(-9000.0, 8000.0, -51000.0)

######### Funcion: Cont2DerPasarelaSub

######### Funcion: ContDerPasarelaSub

######### Funcion: DerrumbaPasarelaSub

sectorderpasarelasub.OnWalkOn=DerrumbaPasarelaSub



#############################
#     Muerte lago subt.     #
#############################

siseoacido=Bladex.CreateSound("../../Sounds/muerte-acida.wav", "SiseoAcido")
siseoacido.Volume=1
siseoacido.Scale=1.14
siseoacido.MinDistance=5000
siseoacido.MaxDistance=45000

surtgas1=Bladex.CreateSound("../../Sounds/gas.wav", "SurtidorGas1")
surtgas1.Volume=1.0
surtgas1.MinDistance=1000
surtgas1.MaxDistance=20000

surtgas2=Bladex.CreateSound("../../Sounds/gas.wav", "SurtidorGas2")
surtgas2.Volume=1.0
surtgas2.MinDistance=1000
surtgas2.MaxDistance=20000

surtgas3=Bladex.CreateSound("../../Sounds/gas.wav", "SurtidorGas3")
surtgas3.Volume=1.0
surtgas3.MinDistance=1000
surtgas3.MaxDistance=20000

surtgas4=Bladex.CreateSound("../../Sounds/gas.wav", "SurtidorGas4")
surtgas4.Volume=1.0
surtgas4.MinDistance=1000
surtgas4.MaxDistance=20000

sectorlanzavapores=Bladex.GetSector(23000.0, 7000.0, -54000.0)

sectorlagosub=Bladex.GetSector(-5000.0, 14150.0, -54000.0)


######### Funcion: VaporesAcido

######### Funcion: LanzaVaporesAcido

sectorlanzavapores.OnEnter=LanzaVaporesAcido


######### Funcion: FuegoVerdePlayer

######### Funcion: ContRevive

######### Funcion: ReviveEnLagoSub

######### Funcion: MuerteEnLagoSub

sectorlagosub.OnEnter=MuerteEnLagoSub



#########################################
#     Derrumbamiento piramide abajo     #
#########################################

derpirabajo1=Bladex.GetSector(-2000.0, -10000.0, -40000.0)
derpirabajo1.Active=0

derpirabajo2=Bladex.GetSector(0.0, -10000.0, -38000.0)
derpirabajo2.Active=0

derpirabajo1.InitBreak((0.0, 250.0, 0.0), (800.0, 0.0, -100.0), (100.0, 0.0, 500.0))
derpirabajo2.InitBreak((0.0, 250.0, 0.0), (-100.0, 0.0, 500.0), (800.0, 0.0, 100.0))

sectorderpirabajo=Bladex.GetSector(0.0, -12000.0, -40000.0)

######### Funcion: Cont2DerPirAbajo

######### Funcion: ContDerPirAbajo

######### Funcion: DerrumbaPirAbajo

sectorderpirabajo.OnWalkOn=DerrumbaPirAbajo



#############################################
#     Derrumbamiento piramide izquierda     #
#############################################

derpirizq1=Bladex.GetSector(-42000.0, -10000.0, 2000.0)
derpirizq1.Active=0

derpirizq1.InitBreak((0.0, 250.0, 0.0), (800.0, 0.0, -100.0), (100.0, 0.0, 500.0))

sectorderpirizq=Bladex.GetSector(-42000.0, -12000.0, 0.0)

######### Funcion: Cont2DerPirIzq

######### Funcion: ContDerPirIzq

######### Funcion: DerrumbaPirIzq

sectorderpirizq.OnWalkOn=DerrumbaPirIzq



########################
#     Muros falsos     #
########################

### Sonidos

sonidoroturamurofalso=Bladex.CreateSound("../../Sounds/single-boulder-impact.wav", "SonidoRoturaMuroFalso")

### Cementerio y Sala del tesoro

sectormurofalsoext=Bladex.GetSector(-28000.0, -1500.0, -50875.0)
sectormurofalsoext.Active=0
sectormurofalsoint=Bladex.GetSector(-55000.0, -1500.0, -37625.0)
sectormurofalsoint.Active=0
sectormurofalsotes=Bladex.GetSector(-29625.0, -1500.0, 23500.0)
sectormurofalsotes.Active=0

sectorrompemurofalsoext=Bladex.GetSector(-28000.0, -1500.0, -50500.0)
sectorrompemurofalsoint=Bladex.GetSector(-55000.0, -1500.0, -37250.0)
sectorrompemurofalsotes=Bladex.GetSector(-29250.0, -1500.0, 23500.0)

sectorrompemurofalsoext.ActiveSurface=0.0, 0.0, 1.0
sectorrompemurofalsoint.ActiveSurface=0.0, 0.0, 1.0
sectorrompemurofalsotes.ActiveSurface=1.0, 0.0, 0.0

sectormurofalsoext.InitBreak((0.0, 0.0, -250.0), (800.0, 200.0, 0.0), (-200.0, 800.0, 0.0))
sectormurofalsoint.InitBreak((0.0, 0.0, -250.0), (800.0, 200.0, 0.0), (-200.0, 800.0, 0.0))
sectormurofalsotes.InitBreak((-250.0, 0.0, 0.0), (0.0, 800.0, 200.0), (0.0, -200.0, 800.0))

######### Funcion: RompeMuroFalso

sectorrompemurofalsoext.OnHit=RompeMuroFalso
sectorrompemurofalsoint.OnHit=RompeMuroFalso
sectorrompemurofalsotes.OnHit=RompeMuroFalso
