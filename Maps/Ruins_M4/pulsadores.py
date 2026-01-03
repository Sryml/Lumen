import Bladex
import Button
import Objects
import AuxFuncs
import Sounds
import darfuncs



### Sonidos

clickbarra=Sounds.CreateEntitySound("../../Sounds/trap-clicked.wav", "ClickBarra")
clickbarra.Volume=0.5
clickbarra.MinDistance=2000
clickbarra.MaxDistance=15000

barradesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "BarraDeslizando")
barradesliz.Volume=0.7
barradesliz.Pitch=0.7
barradesliz.MinDistance=2000
barradesliz.MaxDistance=15000

estacasdesliz=Sounds.CreateEntitySound("../../Sounds/alud.wav", "EstacasDeslizando")
estacasdesliz.Volume=1.0
estacasdesliz.Pitch=0.6
estacasdesliz.MinDistance=2000
estacasdesliz.MaxDistance=15000



### Objetos

est1=Bladex.CreateEntity("Estaca1","EstacaFernando",24250.000000,-1300.000000,26000.000000)
est1.Scale=1.000000
est1.Orientation=0.579228,0.579228,-0.405580,0.405580

est2=Bladex.CreateEntity("Estaca2","EstacaFernando",24687.500000,-2200.000000,25562.500000)
est2.Scale=1.000000
est2.Orientation=0.122788,0.122788,0.696364,-0.696364

est3=Bladex.CreateEntity("Estaca3","EstacaFernando",25125.000000,-2200.000000,25125.000000)
est3.Scale=1.000000
est3.Orientation=0.707107,0.707107,0.000000,0.000000

est4=Bladex.CreateEntity("Estaca4","EstacaFernando",25562.500000,-2200.000000,24687.500000)
est4.Scale=1.000000
est4.Orientation=0.541675,0.541675,0.454519,-0.454519

est5=Bladex.CreateEntity("Estaca5","EstacaFernando",26000.000000,-1300.000000,24250.000000)
est5.Scale=1.000000
est5.Orientation=0.707107,0.707107,0.000000,0.000000

est1din=Objects.CreateDinamicObject("Estaca1")
est2din=Objects.CreateDinamicObject("Estaca2")
est1din.Timer=est2din.Timer="Timer30"


puls1=Bladex.CreateEntity("puls1","Bloque",35900.000000,410.000000,0.000000)
puls1.Scale=1.172579
puls1.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(puls1,"Trigger")

puls2=Bladex.CreateEntity("puls2","Bloque",0.000000,410.000000,-35900.000000)
puls2.Scale=1.172579
puls2.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(puls2,"Trigger")

puls3=Bladex.CreateEntity("puls3","Bloque",-37900.000000,410.000000,0.000000)
puls3.Scale=1.172579
puls3.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(puls3,"Trigger")

puls4=Bladex.CreateEntity("puls4","Bloque",0.000000,410.000000,35900.000000)
puls4.Scale=1.172579
puls4.Orientation=0.500000,0.500000,-0.500000,0.500000
darfuncs.SetHint(puls4,"Trigger")

pulsadores=Button.CreateButtonCombination(0,AbreLaberinto,"")
pulsadores.AddButton("puls1",2,(-1,0,0),400,0,0,1)
pulsadores.AddButton("puls2",2,(0,0,1),400,0,0,1)
pulsadores.AddButton("puls3",2,(1,0,0),400,0,0,1)
pulsadores.AddButton("puls4",2,(0,0,-1),400,0,0,1)

puls1.Frozen=1
puls2.Frozen=1
puls3.Frozen=1
puls4.Frozen=1

barracareto=Bladex.CreateEntity("barracareto","BarraCareto",24000.000000,-250.000000,25500.000000)
barracareto.Scale=1.244716
barracareto.Orientation=0.653282,0.653282,-0.270598,0.270598

barranarizon=Bladex.CreateEntity("barranarizon","BarraNarizon",24500.000000,-250.000000,25000.000000)
barranarizon.Scale=1.244716
barranarizon.Orientation=0.653282,0.653282,-0.270598,0.270598

barrapajaro=Bladex.CreateEntity("barrapajaro","BarraPajaro",25000.000000,-250.000000,24500.000000)
barrapajaro.Scale=1.244716
barrapajaro.Orientation=0.653282,0.653282,-0.270598,0.270598

barraelefante=Bladex.CreateEntity("barraelefante","BarraElefante",25500.000000,-250.000000,24000.000000)
barraelefante.Scale=1.244716
barraelefante.Orientation=0.653282,0.653282,-0.270598,0.270598

barracaretodin=Objects.CreateDinamicObject("barracareto")
barranarizondin=Objects.CreateDinamicObject("barranarizon")
barrapajarodin=Objects.CreateDinamicObject("barrapajaro")
barraelefantedin=Objects.CreateDinamicObject("barraelefante")
barracaretodin.Timer=barranarizondin.Timer=barrapajarodin.Timer=barraelefantedin.Timer="Timer30"


######## Funcion: MueveEstaca5()

######## Funcion: MueveEstacas34()

######## Funcion: AbreEstacasLaberinto()

######## Funcion: AbreLaberinto()

######## Funcion: ActivaBajaBarra(button_name,type,x=0,y=0,z=0,xc=0,yc=0,zc=0,wcx=0,wcy=0,wcz=0,wdx=0,wdy=0,wdz=0)

######## Funcion: BajaBarra(barra_name)


puls1.UseFunc=ActivaBajaBarra
puls2.UseFunc=ActivaBajaBarra
puls3.UseFunc=ActivaBajaBarra
puls4.UseFunc=ActivaBajaBarra
puls1.HitFunc=ActivaBajaBarra
puls2.HitFunc=ActivaBajaBarra
puls3.HitFunc=ActivaBajaBarra
puls4.HitFunc=ActivaBajaBarra
