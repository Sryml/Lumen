import Bladex
import ReadGSFile




res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])



# Funcion: ApagaMusicaAlEntrar(trsector_name, entity_name)

# Funcion: EnciendeSuspenseRapido(trsector_name, entity_name)

# Funcion: EnciendeMusicaCapilla(trsector_name, entity_name)

# Funcion: DesactivaEnciendeMusicaCapilla(trsector_name, entity_name)

# Funcion: EnciendeSuspenseLento(trsector_name, entity_name)

# Funcion: EnciendeMusicaZonaCaos(trsector_name, entity_name)

# Funcion: EnciendeMusicaTorre(trsector_name, entity_name)

# Funcion: EnciendeRagnarCuchillas(trsector_name, entity_name)

# Funcion: EnciendeTrampa(trsector_name, entity_name)

# Funcion: EnciendeMusicaPendulos(trsector_name, entity_name)



Bladex.SetTriggerSectorFunc("SuspenseRapido1", "OnEnter", EnciendeSuspenseRapido)
Bladex.SetTriggerSectorFunc("SuspenseRapido2", "OnEnter", EnciendeSuspenseRapido)
Bladex.SetTriggerSectorFunc("Silencio1", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("Silencio2", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("SuspenseRapido3", "OnEnter", EnciendeSuspenseRapido)
Bladex.SetTriggerSectorFunc("Silencio3", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("MusicaCapilla1", "OnEnter", EnciendeMusicaCapilla)
Bladex.SetTriggerSectorFunc("MusicaCapilla2", "OnEnter", DesactivaEnciendeMusicaCapilla)
Bladex.SetTriggerSectorFunc("SuspenseLento1", "OnEnter", EnciendeSuspenseLento)
Bladex.SetTriggerSectorFunc("SuspenseLento2", "OnEnter", EnciendeSuspenseLento)
Bladex.SetTriggerSectorFunc("Silencio4", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("MusicaZonaCaos1", "OnEnter", EnciendeMusicaZonaCaos)
Bladex.SetTriggerSectorFunc("MusicaZonaCaos2", "OnEnter", EnciendeMusicaZonaCaos)
Bladex.SetTriggerSectorFunc("MusicaTorre1", "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("MusicaTorre2", "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("Silencio5", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("Silencio6", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("MusicaTorre3", "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("MusicaTorre4", "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("Silencio7", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("MusicaTorre5", "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("Silencio8", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("RagnarCuchillas", "OnEnter", EnciendeRagnarCuchillas)
Bladex.SetTriggerSectorFunc("TrampaTechoPinchos", "OnEnter", EnciendeTrampa)
Bladex.SetTriggerSectorFunc("TrampaFlechas1", "OnEnter", EnciendeTrampa)
Bladex.SetTriggerSectorFunc("TrampaFlechas2", "OnEnter", EnciendeTrampa)
Bladex.SetTriggerSectorFunc("MusicaZonaCaos3", "OnEnter", EnciendeMusicaZonaCaos)
Bladex.SetTriggerSectorFunc("MusicaPendulos", "OnEnter", EnciendeMusicaPendulos)
