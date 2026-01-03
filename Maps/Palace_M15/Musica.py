import Bladex
import ReadGSFile




res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])



# Funcion: ApagaMusicaAlEntrar(trsector_name, entity_name)

# Funcion: EnciendeMusicaGenericaAntes(trsector_name, entity_name)

# Funcion: EnciendeMusicaGenericaDespues(trsector_name, entity_name)

# Funcion: EnciendeMusicaSuspense(trsector_name, entity_name)

# Funcion: EnciendeMusicaMiserere(trsector_name, entity_name)



Bladex.SetTriggerSectorFunc("GenAnt1",      "OnEnter", EnciendeMusicaGenericaAntes)
Bladex.SetTriggerSectorFunc("GenAnt2",      "OnEnter", EnciendeMusicaGenericaAntes)
Bladex.SetTriggerSectorFunc("GenAnt3",      "OnEnter", EnciendeMusicaGenericaAntes)
Bladex.SetTriggerSectorFunc("GenAnt4",      "OnEnter", EnciendeMusicaGenericaAntes)
Bladex.SetTriggerSectorFunc("GenAnt5",      "OnEnter", EnciendeMusicaGenericaAntes)
Bladex.SetTriggerSectorFunc("Silencio1",    "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("Silencio2",    "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("Silencio3",    "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("Silencio4",    "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("GenDes1",      "OnEnter", EnciendeMusicaGenericaDespues)
Bladex.SetTriggerSectorFunc("GenDes2",      "OnEnter", EnciendeMusicaGenericaDespues)
Bladex.SetTriggerSectorFunc("GenDes3",      "OnEnter", EnciendeMusicaGenericaDespues)
Bladex.SetTriggerSectorFunc("Suspense1",    "OnEnter", EnciendeMusicaSuspense)
Bladex.SetTriggerSectorFunc("Suspense2",    "OnEnter", EnciendeMusicaSuspense)
Bladex.SetTriggerSectorFunc("Miserere",     "OnEnter", EnciendeMusicaMiserere)
