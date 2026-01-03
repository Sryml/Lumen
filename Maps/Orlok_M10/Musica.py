import Bladex
import ReadGSFile



res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


cuevasvisitadas=0
fortificacionvisitada=0


# Funcion: ApagaMusicaAlEntrar(trsector_name, entity_name)

# Funcion: EnciendeMusicaValles(trsector_name, entity_name)

# Funcion: EnciendeMusicaDesfiladero(trsector_name, entity_name)

# Funcion: EnciendeMusicaCuevas(trsector_name, entity_name)

# Funcion: EnciendeMusicaFortificacion(trsector_name, entity_name)

# Funcion: EnciendeMusicaSustoDKN(trsector_name, entity_name)

# Funcion: DesactivaEncendidoMusicaSustoDKN(trsector_name, entity_name)

# Funcion: EnciendeMusicaEncuentraLLave(trsector_name, entity_name)

# Funcion: EnciendeMusicaEncuentraOrbe(trsector_name, entity_name)


Bladex.SetTriggerSectorFunc("ValleInt1",         "OnEnter", EnciendeMusicaValles)
Bladex.SetTriggerSectorFunc("ValleInt2",         "OnEnter", EnciendeMusicaValles)
Bladex.SetTriggerSectorFunc("ValleInt3",         "OnEnter", EnciendeMusicaValles)
Bladex.SetTriggerSectorFunc("ValleInt4",         "OnEnter", EnciendeMusicaValles)
Bladex.SetTriggerSectorFunc("ValleInt5",         "OnEnter", EnciendeMusicaValles)
Bladex.SetTriggerSectorFunc("ValleInt6",         "OnEnter", EnciendeMusicaValles)
Bladex.SetTriggerSectorFunc("ValleInt7",         "OnEnter", EnciendeMusicaValles)
Bladex.SetTriggerSectorFunc("DesfiladeroAnt1",   "OnEnter", EnciendeMusicaDesfiladero)
Bladex.SetTriggerSectorFunc("DesfiladeroAnt2",   "OnEnter", EnciendeMusicaDesfiladero)
Bladex.SetTriggerSectorFunc("DesfiladeroAnt3",   "OnEnter", EnciendeMusicaDesfiladero)
Bladex.SetTriggerSectorFunc("DesfiladeroAnt4",   "OnEnter", EnciendeMusicaDesfiladero)
Bladex.SetTriggerSectorFunc("Silencio1",         "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("Silencio2",         "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("Silencio3",         "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("Cuevas1",           "OnEnter", EnciendeMusicaCuevas)
Bladex.SetTriggerSectorFunc("Cuevas2",           "OnEnter", EnciendeMusicaCuevas)
Bladex.SetTriggerSectorFunc("Cuevas3",           "OnEnter", EnciendeMusicaCuevas)
#Bladex.SetTriggerSectorFunc("DesfiladeroPost",   "OnEnter", EnciendeMusicaDesfiladero)
Bladex.SetTriggerSectorFunc("Fortificacion1",    "OnEnter", EnciendeMusicaFortificacion)
#Bladex.SetTriggerSectorFunc("Fortificacion2",    "OnEnter", EnciendeMusicaFortificacion)
Bladex.SetTriggerSectorFunc("SustoDKN",          "OnEnter", EnciendeMusicaSustoDKN)
Bladex.SetTriggerSectorFunc("DesactivaSustoDKN", "OnEnter", DesactivaEncendidoMusicaSustoDKN)
Bladex.SetTriggerSectorFunc("EncuentraLlave",    "OnEnter", EnciendeMusicaEncuentraLLave)
Bladex.SetTriggerSectorFunc("EncuentraOrbe",     "OnEnter", EnciendeMusicaEncuentraOrbe)
