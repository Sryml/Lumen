import Sounds
import Bladex
import ReadGSFile




res=ReadGSFile.ReadGhostSectorFile("ruinssnd.sf")
for igs in res:
  Bladex.AddGhostSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
  Bladex.SetGhostSectorSound(igs["Name"],igs["Sonido"],igs["Volumen"],igs["VolumenBase"],
                             igs["DistanciaMinima"],igs["DistanciaMaxima"],igs["DistMaximaVertical"],igs["Escala"])




############ SONIDOS AMBIENTE CATACUMBAS ZONA OESTE


aderrumbe1=Bladex.CreateSound("../../Sounds/blom3.wav","Blom3")
aderrumbe1.Volume=0.8
aderrumbe1.MinDistance=500
aderrumbe1.MaxDistance=15000
aderrumbe1.BaseVolume=1.0

######## Funcion: ActivaDerrumbe(sectorindex,entityname)

s1=Bladex.GetSector(-68000,5000,-33000)
s1.OnEnter=ActivaDerrumbe


rocaseco1=Bladex.CreateSound("../../Sounds/rocas-eco.wav","Eco1")
rocaseco1.Volume=0.1
rocaseco1.MinDistance=500
rocaseco1.MaxDistance=15000
rocaseco1.BaseVolume=1.0

######## Funcion: ActivaRocaseco1(sectorindex,entityname)

s2=Bladex.GetSector(-77500,5000,-11750)
s2.OnEnter=ActivaRocaseco1


ambcat1=Sounds.CreatePeriodicSound("../../Sounds/blom5.wav", "ambcat1",20,10,(-64500, 15000, 8500))
ambcat1.sound.Volume=0.5
ambcat1.sound.MinDistance=500
ambcat1.sound.MaxDistance=15000
ambcat1.sound.BaseVolume=1.0
ambcat1.sound.SendNotify=0
ambcat1.PlayPeriodic()


ambcat2=Sounds.CreatePeriodicSound("../../Sounds/blom3.wav", "ambcat2",20,5,(-65000, 15000, 25500))
ambcat2.sound.Volume=0.5
ambcat2.sound.MinDistance=500
ambcat2.sound.MaxDistance=15000
ambcat2.sound.BaseVolume=1.0
ambcat2.sound.SendNotify=0
ambcat2.PlayPeriodic()


ambcat3=Sounds.CreatePeriodicSound("../../Sounds/blom3.wav", "ambcat3",20,10,(-30000, 15000, 13750))
ambcat3.sound.Volume=0.5
ambcat3.sound.MinDistance=500
ambcat3.sound.MaxDistance=15000
ambcat3.sound.BaseVolume=1.0
ambcat3.sound.SendNotify=0
ambcat3.PlayPeriodic()


ecoagua1=Bladex.CreateSound("../../Sounds/blom2.wav","Eco1")
ecoagua1.Volume=0.1
ecoagua1.MinDistance=500
ecoagua1.MaxDistance=15000
ecoagua1.BaseVolume=1.0

######## Funcion: ActivaEcoagua1(sectorindex,entityname)

s3=Bladex.GetSector(-69250,11000,750)
s3.OnEnter=ActivaEcoagua1




############ SONIDOS AMBIENTE CATACUMBAS ZONA SUR


ambcat4=Sounds.CreatePeriodicSound("../../Sounds/blom3.wav", "ambcat4",20,5,(-25500, 15000, -49750))
ambcat4.sound.Volume=0.5
ambcat4.sound.MinDistance=500
ambcat4.sound.MaxDistance=15000
ambcat4.sound.BaseVolume=1.0
ambcat4.sound.SendNotify=0
ambcat4.PlayPeriodic()


acido=Bladex.CreateSound("../../Sounds/blom2.wav","Acido")
acido.Volume=1
acido.MinDistance=500
acido.MaxDistance=15000
acido.BaseVolume=1.0

######## Funcion: ActivaAcido(sectorindex,entityname)

s4=Bladex.GetSector(-11250,8000,-50000)
s4.OnEnter=ActivaAcido




############ SONIDOS AMBIENTE CATACUMBAS ZONA ESTE


pozo1=Bladex.CreateSound("../../Sounds/rocas-eco.wav","Pozo1")
pozo1.Volume=1
pozo1.MinDistance=500
pozo1.MaxDistance=15000
pozo1.BaseVolume=1.0

######## Funcion: SuenaPozo(sectorindex,entityname)

s5=Bladex.GetSector(43560,7835,-47871)
s5.OnEnter=SuenaPozo


ambcat5=Sounds.CreatePeriodicSound("../../Sounds/blom3.wav", "ambcat5",20,5,(11000,15000,-59000))
ambcat5.sound.Volume=0.7
ambcat5.sound.MinDistance=500
ambcat5.sound.MaxDistance=15000
ambcat5.sound.BaseVolume=1.0
ambcat5.sound.SendNotify=0
ambcat5.PlayPeriodic()


ambcat6=Sounds.CreatePeriodicSound("../../Sounds/blom1.wav", "ambcat6",20,5,(51000,15000,-16000))
ambcat6.sound.Volume=1
ambcat6.sound.MinDistance=500
ambcat6.sound.MaxDistance=15000
ambcat6.sound.BaseVolume=1.0
ambcat6.sound.SendNotify=0
ambcat6.PlayPeriodic()


ambcat7=Sounds.CreatePeriodicSound("../../Sounds/rocas-eco.wav", "ambcat7",25,10,(48750,15000,10000))
ambcat7.sound.Volume=1
ambcat7.sound.MinDistance=500
ambcat7.sound.MaxDistance=15000
ambcat7.sound.BaseVolume=1.0
ambcat7.sound.SendNotify=0
ambcat7.PlayPeriodic()


ambcat8=Sounds.CreatePeriodicSound("../../Sounds/rocas-eco.wav", "ambcat8",20,10,(64000,15000,38000))
ambcat8.sound.Volume=0.7
ambcat8.sound.MinDistance=500
ambcat8.sound.MaxDistance=15000
ambcat8.sound.BaseVolume=1.0
ambcat8.sound.SendNotify=0
ambcat8.PlayPeriodic()


puente1=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "puente1",8,4,(61750, 3000, 55750))
puente1.sound.Volume=0.7
puente1.sound.MinDistance=500
puente1.sound.MaxDistance=5000
puente1.sound.BaseVolume=1.0
puente1.sound.SendNotify=0
puente1.PlayPeriodic()


puente2=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "puente2",10,5,(61750, 3000, 55750))
puente2.sound.Volume=1
puente2.sound.MinDistance=500
puente2.sound.MaxDistance=5000
puente2.sound.BaseVolume=1.0
puente2.sound.SendNotify=0
puente2.PlayPeriodic()


puente3=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-3.wav", "puente3",12,6,(61750, 3000, 55750))
puente3.sound.Volume=1
puente3.sound.MinDistance=500
puente3.sound.MaxDistance=5000
puente3.sound.BaseVolume=1.0
puente3.sound.SendNotify=0
puente3.PlayPeriodic()




############ SONIDOS AMBIENTE TEMPLO CENTRAL


espiritu1=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "Espiritu1",12,6,(0, -10000, 0))
espiritu1.sound.Volume=1
espiritu1.sound.MinDistance=5000
espiritu1.sound.MaxDistance=25000
espiritu1.sound.BaseVolume=1.0
espiritu1.sound.SendNotify=0
espiritu1.PlayPeriodic()


espiritu2=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "Espiritu2",10,5,(0, -10000, 0))
espiritu2.sound.Volume=1
espiritu2.sound.MinDistance=5000
espiritu2.sound.MaxDistance=25000
espiritu2.sound.BaseVolume=1.0
espiritu2.sound.SendNotify=0
espiritu2.PlayPeriodic()




############ SONIDOS AMBIENTE HALCONES


halcon1=Sounds.CreatePeriodicSound("../../Sounds/pajaro1.wav", "Halcon1",40,20,(0, -30000, -20000))
halcon1.sound.Volume=1
halcon1.sound.MinDistance=10000
halcon1.sound.MaxDistance=30000
halcon1.sound.BaseVolume=1.0
halcon1.sound.SendNotify=0
halcon1.PlayPeriodic()


halcon2=Sounds.CreatePeriodicSound("../../Sounds/pajaro2.wav", "Halcon2",30,15,(-20000, -30000, 0))
halcon2.sound.Volume=1
halcon2.sound.MinDistance=10000
halcon2.sound.MaxDistance=30000
halcon2.sound.BaseVolume=1.0
halcon2.sound.SendNotify=0
halcon2.PlayPeriodic()


halcon3=Sounds.CreatePeriodicSound("../../Sounds/pajaro1.wav", "Halcon3",40,20,(0, -30000, 20000))
halcon3.sound.Volume=1
halcon3.sound.MinDistance=10000
halcon3.sound.MaxDistance=30000
halcon3.sound.BaseVolume=1.0
halcon3.sound.SendNotify=0
halcon3.PlayPeriodic()


halcon4=Sounds.CreatePeriodicSound("../../Sounds/pajaro2.wav", "Halcon4",30,15,(20000, -30000, 0))
halcon4.sound.Volume=1
halcon4.sound.MinDistance=10000
halcon4.sound.MaxDistance=30000
halcon4.sound.BaseVolume=1.0
halcon4.sound.SendNotify=0
halcon4.PlayPeriodic()




############ SONIDOS GOTAS TRAMPAS Y POZO


t1g1=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "trampa1gota1",6,3,(46500, 12000, 19500))
t1g1.sound.Volume=0.7
t1g1.sound.MinDistance=1000
t1g1.sound.MaxDistance=7000
t1g1.sound.BaseVolume=1.0
t1g1.sound.SendNotify=0
t1g1.PlayPeriodic()


t1g2=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "trampa1gota2",8,4,(45000, 12000, 21000))
t1g2.sound.Volume=1
t1g2.sound.MinDistance=1000
t1g2.sound.MaxDistance=7000
t1g2.sound.BaseVolume=1.0
t1g2.sound.SendNotify=0
t1g2.PlayPeriodic()


t1g3=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-3.wav", "trampa1gota3",10,5,(47500, 12000, 21500))
t1g3.sound.Volume=1
t1g3.sound.MinDistance=1000
t1g3.sound.MaxDistance=7000
t1g3.sound.BaseVolume=1.0
t1g3.sound.SendNotify=0
t1g3.PlayPeriodic()


pozog1=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "pozogota1",6,3,(47000, 11000, -49000))
pozog1.sound.Volume=0.7
pozog1.sound.MinDistance=1000
pozog1.sound.MaxDistance=7000
pozog1.sound.BaseVolume=1.0
pozog1.sound.SendNotify=0
pozog1.PlayPeriodic()


pozog2=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "pozogota2",8,4,(48500, 11000, -47500))
pozog2.sound.Volume=1
pozog2.sound.MinDistance=1000
pozog2.sound.MaxDistance=7000
pozog2.sound.BaseVolume=1.0
pozog2.sound.SendNotify=0
pozog2.PlayPeriodic()


pozog3=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-3.wav", "pozogota3",10,5,(50000, 11000, -49000))
pozog3.sound.Volume=1
pozog3.sound.MinDistance=1000
pozog3.sound.MaxDistance=7000
pozog3.sound.BaseVolume=1.0
pozog3.sound.SendNotify=0
pozog3.PlayPeriodic()


t2g1=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "trampa2gota1",6,3,(-72500, 11000, -500))
t2g1.sound.Volume=0.7
t2g1.sound.MinDistance=1000
t2g1.sound.MaxDistance=7000
t2g1.sound.BaseVolume=1.0
t2g1.sound.SendNotify=0
t2g1.PlayPeriodic()


t2g2=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "trampa2gota2",8,4,(-74500, 11000, 1500))
t2g2.sound.Volume=1
t2g2.sound.MinDistance=1000
t2g2.sound.MaxDistance=7000
t2g2.sound.BaseVolume=1.0
t2g2.sound.SendNotify=0
t2g2.PlayPeriodic()


t2g3=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-3.wav", "trampa2gota3",10,5,(-72500, 11000, 2500))
t2g3.sound.Volume=1
t2g3.sound.MinDistance=1000
t2g3.sound.MaxDistance=7000
t2g3.sound.BaseVolume=1.0
t2g3.sound.SendNotify=0
t2g3.PlayPeriodic()




#### sectores fantasmas para probar el EAX

#res=ReadGSFile.ReadGhostSectorFile("eax.sf")
#for igs in res:
#  Bladex.AddGhostSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
#  Bladex.SetGhostSectorSound(igs["Name"],igs["Sonido"],igs["Volumen"],igs["VolumenBase"],
#                             igs["DistanciaMinima"],igs["DistanciaMaxima"],igs["DistMaximaVertical"],igs["Escala"])
