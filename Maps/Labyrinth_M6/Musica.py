import Bladex
import ReadGSFile




res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


anillointeriorvisto=0
torrecentralvista=0
alcantarillasvistas=0


# Funcion: ApagaMusicaAlEntrar(trsector_name, entity_name)

# Funcion: EnciendeMusicaTorre(trsector_name, entity_name)

# Funcion: EnciendeMusicaTablilla(trsector_name, entity_name)

# Funcion: EnciendeMusicaTrampaTablilla(trsector_name, entity_name)

# Funcion: EnciendeMusicaAnilloExterior(trsector_name, entity_name)

# Funcion: EnciendeMusicaAnilloInterior(trsector_name, entity_name)

# Funcion: EnciendeMusicaTorreCentral(trsector_name, entity_name)

# Funcion: EnciendeMusicaSalaTrono(trsector_name, entity_name)

# Funcion: EnciendeMusicaLlave(trsector_name, entity_name)

# Funcion: EnciendeMusicaAlcantarillas(trsector_name, entity_name)

# Funcion: EnciendeMusicaSusto(trsector_name, entity_name)

# Funcion: DesactivaEncendidoMusicaSusto(trsector_name, entity_name)


Bladex.SetTriggerSectorFunc("TorreOS",          "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("TorreON",          "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("TorreNO",          "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("TorreNE",          "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("TorreEN",          "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("TorreES",          "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("TorreSO",          "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("TorreSE",          "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("AlcantarillaS",    "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("AlcantarillaN",    "OnEnter", EnciendeMusicaAlcantarillas)
Bladex.SetTriggerSectorFunc("AlcantarillaC",    "OnEnter", EnciendeMusicaTorre)
Bladex.SetTriggerSectorFunc("ZonaTablilla",     "OnEnter", EnciendeMusicaTablilla)
Bladex.SetTriggerSectorFunc("TrampaTablilla",   "OnEnter", EnciendeMusicaTrampaTablilla)
Bladex.SetTriggerSectorFunc("AnilloIntPuertaO", "OnEnter", EnciendeMusicaAnilloInterior)
Bladex.SetTriggerSectorFunc("AnilloIntPuertaE", "OnEnter", EnciendeMusicaAnilloInterior)
Bladex.SetTriggerSectorFunc("AnilloExt1",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt2",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt3",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt4",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt5",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt6",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt7",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt8",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt9",       "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt10",      "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt11",      "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloExt12",      "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("AnilloInt1",       "OnEnter", EnciendeMusicaAnilloInterior)
Bladex.SetTriggerSectorFunc("AnilloInt2",       "OnEnter", EnciendeMusicaAnilloInterior)
Bladex.SetTriggerSectorFunc("AnilloInt3",       "OnEnter", EnciendeMusicaAnilloInterior)
Bladex.SetTriggerSectorFunc("Silencio1",        "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("EncuentraLlave",   "OnEnter", EnciendeMusicaLlave)
Bladex.SetTriggerSectorFunc("TorreCentral1",    "OnEnter", EnciendeMusicaTorreCentral)
Bladex.SetTriggerSectorFunc("TorreCentral2",    "OnEnter", EnciendeMusicaTorreCentral)
Bladex.SetTriggerSectorFunc("TorreCentral3",    "OnEnter", EnciendeMusicaTorreCentral)
Bladex.SetTriggerSectorFunc("TorreCentral4",    "OnEnter", EnciendeMusicaTorreCentral)
Bladex.SetTriggerSectorFunc("PuertaAzotea",     "OnEnter", EnciendeMusicaTorreCentral)
Bladex.SetTriggerSectorFunc("ExteriorAzotea",   "OnEnter", EnciendeMusicaAnilloExterior)
Bladex.SetTriggerSectorFunc("Susto",            "OnEnter", EnciendeMusicaSusto)
Bladex.SetTriggerSectorFunc("DesactivaSusto",   "OnEnter", DesactivaEncendidoMusicaSusto)
Bladex.SetTriggerSectorFunc("SalaTrono",        "OnEnter", EnciendeMusicaSalaTrono)
