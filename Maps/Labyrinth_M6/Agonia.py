import Bladex
import InitDataField
import AuxFuncs
import GameText
import EnemyTypes
import Reference
import Actions
import Enm_Def




### Creacion de objetos

# La llave se crea en el Puertas.py

mapa=Bladex.CreateEntity("Mapa","Pergamino",0,-2000,-15000)
mapa.Static=1
mapa.Scale=1.4
mapa.Orientation=0.707107,0.707107,0.000000,0.000000
mapa.RemoveFromWorld()



### Creacion de personajes

herido=Bladex.CreateEntity("Herido", "Knight_Traitor", 185,-1219,-16850,"Person")
herido.Data= Enm_Def.NPCPerson(herido)
herido.Blind=1
herido.Deaf=1
herido.MeshName="Mortimer"
herido.SetOnFloor()
herido.Data.Invincibility=2
herido.Data.Respond2Thrown=None
herido.Data.ChanceOfFuryOnHurt=0.0

######## Funcion: LanzaHeridoAgonizante()

LanzaHeridoAgonizante()



### Funcionamiento

######## Funcion: ReseteaCamaraAgonia(Camera,Frame)

######## Funcion: CambiaCamaraAgonia2(Camera,Frame)

######## Funcion: CambiaCamaraAgonia1(Camera,Frame)

######## Funcion: MusicaytextoAgonia()

######## Funcion: Muere(person)

######## Funcion: ApareceItem(entity_name)

######## Funcion: SueltaItem()

######## Funcion: CogeItems()

######## Funcion: IniciaAgonia(sector_index, entity_name)

sector_agonia1=Bladex.GetSector(0,-4000,-12000)
sector_agonia2=Bladex.GetSector(0,-4000,-14750)
sector_agonia3=Bladex.GetSector(0,-4000,-17000)
sector_agonia1.OnWalkOn=IniciaAgonia
sector_agonia2.OnWalkOn=IniciaAgonia
sector_agonia3.OnWalkOn=IniciaAgonia


######## Funcion: IniciaAgonia2(sector_index, entity_name)

