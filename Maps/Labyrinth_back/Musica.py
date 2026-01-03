import Bladex
import ReadGSFile




res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


alcantarillasvistas=0


# Funcion: EnciendeMusicaTablilla(trsector_name, entity_name)

# Funcion: EnciendeMusicaTrampaTablilla(trsector_name, entity_name)

# Funcion: EnciendeMusica1Anillo(trsector_name, entity_name)

# Funcion: EnciendeMusica2Anillo(trsector_name, entity_name)

# Funcion: EnciendeMusicaAlcantarillas(trsector_name, entity_name)

# Funcion: EnciendeMusicaApChaos(trsector_name, entity_name)


Bladex.SetTriggerSectorFunc("AlcantarillaS",     "OnEnter", EnciendeMusicaAlcantarillas)
Bladex.SetTriggerSectorFunc("AlcantarillaC",     "OnEnter", EnciendeMusicaAlcantarillas)
Bladex.SetTriggerSectorFunc("ZonaTablilla",      "OnEnter", EnciendeMusicaTablilla)
Bladex.SetTriggerSectorFunc("TrampaTablilla",    "OnEnter", EnciendeMusicaTrampaTablilla)
Bladex.SetTriggerSectorFunc("Musica1a",          "OnEnter", EnciendeMusica1Anillo)
Bladex.SetTriggerSectorFunc("Musica1b",          "OnEnter", EnciendeMusica1Anillo)
Bladex.SetTriggerSectorFunc("Musica2a",          "OnEnter", EnciendeMusica2Anillo)
Bladex.SetTriggerSectorFunc("Musica2b",          "OnEnter", EnciendeMusica2Anillo)
Bladex.SetTriggerSectorFunc("Musica2c",          "OnEnter", EnciendeMusica2Anillo)
