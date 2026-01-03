import Bladex
import ReadGSFile




res=ReadGSFile.ReadGhostSectorFile("musicas.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])



### Sectores silenciadores

# Funcion: ApagaMusicaAlEntrar(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("ap_entrada_princ_lab", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_entrada_lago_lab", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_puerta_piramide", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_entrada_subt1_mausoleo", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_entrada_subt2_mausoleo", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_entrada_subt_tesoro", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_entrada_subt_templo", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_subt_pozo", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_entrada_fuentes", "OnEnter", ApagaMusicaAlEntrar)
Bladex.SetTriggerSectorFunc("ap_puerta_mausoleo", "OnEnter", ApagaMusicaAlEntrar)


### Sectores musica exterior

# Funcion: EnciendeMusicaExteriorAntes(trsector_name, entity_name)

# Funcion: EnciendeMusicaExteriorDespues(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("enc1_entrada_princ_lab", "OnEnter", EnciendeMusicaExteriorAntes)
Bladex.SetTriggerSectorFunc("enc1_puerta_piramide", "OnEnter", EnciendeMusicaExteriorAntes)
Bladex.SetTriggerSectorFunc("enc1_entrada_fuentes", "OnEnter", EnciendeMusicaExteriorAntes)
Bladex.SetTriggerSectorFunc("enc1_puerta_mausoleo", "OnEnter", EnciendeMusicaExteriorAntes)
Bladex.SetTriggerSectorFunc("enc1_entrada_lago_lab", "OnEnter", EnciendeMusicaExteriorAntes)
Bladex.SetTriggerSectorFunc("enc1_entrada_lat_lago_lab", "OnEnter", EnciendeMusicaExteriorAntes)
Bladex.SetTriggerSectorFunc("enc2_entrada_lat_lago_lab", "OnEnter", EnciendeMusicaExteriorAntes)


### Sectores musica laberinto e interiores

# Funcion: EnciendeMusicaLabInt(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("enc2_entrada_princ_lab", "OnEnter", EnciendeMusicaLabInt)
Bladex.SetTriggerSectorFunc("enc3_entrada_princ_lab", "OnEnter", EnciendeMusicaLabInt)
Bladex.SetTriggerSectorFunc("enc1_subt_pozo", "OnEnter", EnciendeMusicaLabInt)
Bladex.SetTriggerSectorFunc("enc2_entrada_fuentes", "OnEnter", EnciendeMusicaLabInt)
Bladex.SetTriggerSectorFunc("enc1_entrada_subt_tesoro", "OnEnter", EnciendeMusicaLabInt)
Bladex.SetTriggerSectorFunc("enc1_salida_lago_lab", "OnEnter", EnciendeMusicaLabInt)
Bladex.SetTriggerSectorFunc("enc1_salida_lat_lago_lab", "OnEnter", EnciendeMusicaLabInt)
Bladex.SetTriggerSectorFunc("enc2_salida_lat_lago_lab", "OnEnter", EnciendeMusicaLabInt)


### Sectores musica subterraneos

# Funcion: EnciendeMusicaSubterraneos(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("enc2_entrada_lago_lab", "OnEnter", EnciendeMusicaSubterraneos)
Bladex.SetTriggerSectorFunc("enc2_puerta_piramide", "OnEnter", EnciendeMusicaSubterraneos)
Bladex.SetTriggerSectorFunc("enc2_subt_pozo", "OnEnter", EnciendeMusicaSubterraneos)
Bladex.SetTriggerSectorFunc("enc3_subt_pozo", "OnEnter", EnciendeMusicaSubterraneos)
Bladex.SetTriggerSectorFunc("enc1_entrada_subt1_mausoleo", "OnEnter", EnciendeMusicaSubterraneos)
Bladex.SetTriggerSectorFunc("enc1_entrada_subt2_mausoleo", "OnEnter", EnciendeMusicaSubterraneos)
Bladex.SetTriggerSectorFunc("enc2_entrada_subt_tesoro", "OnEnter", EnciendeMusicaSubterraneos)
Bladex.SetTriggerSectorFunc("enc1_entrada_subt_templo", "OnEnter", EnciendeMusicaSubterraneos)


### Sectores musica mausoleo

# Funcion: EnciendeMusicaMausoleo(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("enc2_entrada_subt1_mausoleo", "OnEnter", EnciendeMusicaMausoleo)
Bladex.SetTriggerSectorFunc("enc2_entrada_subt2_mausoleo", "OnEnter", EnciendeMusicaMausoleo)
Bladex.SetTriggerSectorFunc("enc2_puerta_mausoleo", "OnEnter", EnciendeMusicaMausoleo)


### Sectores musica templo final

# Funcion: EnciendeMusicaTemploFinal(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("enc2_entrada_subt_templo", "OnEnter", EnciendeMusicaTemploFinal)
