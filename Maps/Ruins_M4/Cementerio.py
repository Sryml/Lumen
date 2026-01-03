import Bladex
import B3DLib
import EnemyTypes
import Actions



##################
#     Varios     #
##################

Bladex.CreateTimer("Timer1",1.0)


######################
#     Particulas     #
######################

#
###
##### Estan definidas en Generadores.py
###
#


##########################
#     Funcionamiento     #
##########################

######### Funcion: RemueveTierra(pos, v1, v2, v3)

######### Funcion: Despierta(ent_name)

######### Funcion: GeneraEnemigo(enemigo)

######### Funcion: GeneraEnemigoEnEspera(ent_name, time)

######### Funcion: LevantaOtroEsqueleto(ent_name)

######### Funcion: EmpiezaLevantamientoEsqueletos(sec_idx, ent_name)

salidamaus=Bladex.GetSector(-44625.0, -2000.0, -42625.0)

salidamaus.OnEnter=EmpiezaLevantamientoEsqueletos


####################
#     Enemigos     #
####################

######### Funcion: CreaEsqueleto(n, x, y, z)

esq1=CreaEsqueleto(1, -44000.0, 1000.0, -36850.0, 0, "Garrote", "Escudo5")
esq2=CreaEsqueleto(2, -36384.0, 1000.0, -38702.9, 0, "Garrote", "")
esq3=CreaEsqueleto(3, -38614.6, 1000.0, -30643.8, 0, "Gladius", "")
esq4=CreaEsqueleto(4, -35284.8, 1000.0, -44090.0, 0, "Hacha", "Escudo5")
esq5=CreaEsqueleto(5, -46650.0, 1000.0, -33052.2, 1, "Hacha", "")
esq6=CreaEsqueleto(6, -32002.9, 1000.0, -35757.6, 1, "Gladius", "")
esq7=CreaEsqueleto(7, -41603.9, 1000.0, -33754.5, 1, "Garrote", "Escudo5")
esq8=CreaEsqueleto(8, -32149.1, 1000.0, -40954.4, 2, "Maza", "")
esq9=CreaEsqueleto(9, -38998.3, 1000.0, -41611.7, 2, "Hacha", "Escudo5")
esq10=CreaEsqueleto(10, -43157.0, 1000.0, -30326.9, 2, "Maza", "Escudo2")
