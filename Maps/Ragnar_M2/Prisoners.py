import def_class
import Bladex
import Enm_Def
import whrandom


#############################################
#     Definicion de la clase Prisionero     #
#############################################

#Bladex.LoadSampledAnimation("../../Anm/Prs_agony01.bmv","Prs_agony01",1,"Prisoner_3")
#Bladex.LoadSampledAnimation("../../Anm/Prs_agony02.bmv","Prs_agony02",1,"Prisoner_3")
#Bladex.LoadSampledAnimation("../../Anm/Prs_rlx_01.bmv","Prs_rlx_01",1,"Prisoner_3")
#Bladex.LoadSampledAnimation("../../Anm/Prs_rlx_02.bmv","Prs_rlx_02",1,"Prisoner_3")
#Bladex.LoadSampledAnimation("../../Anm/Prs_dth.bmv","Prs_dth",0,"Prisoner_3")



#######################
#     Prisioneros     #
#######################

prisionerovivo1=Bladex.CreateEntity("PrisioneroVivo3", "Prisoner_3", -100500.0, 8750.0, 79500.0,"Person")
prisionerovivo1.Angle=-3.14159/2.0
prisionerovivo1.Data=def_class.Prisoner(prisionerovivo1)
prisionerovivo1.Life=1
prisionerovivo1.Blind=1

prisionerovivo2=Bladex.CreateEntity("PrisioneroVivo2", "Prisoner_5", -91000.0, 8750.0, 79500.0,"Person")
prisionerovivo2.Angle=3.14159/12.0
prisionerovivo2.Data=def_class.Prisoner(prisionerovivo2)
prisionerovivo2.Life=1
prisionerovivo2.Blind=1

prisioneromuerto=Bladex.CreateEntity("PrisioneroMuerto", "Prisoner_6", -88000.0, 8750.0, 83000.0,"Person")
prisioneromuerto.Angle=0.0
prisioneromuerto.Data=def_class.Prisoner(prisioneromuerto)
prisioneromuerto.Life=1
prisioneromuerto.Blind=1


prisionerovivo1.ImHurtFunc=PrsHerido
prisionerovivo1.ImDeadFunc=PrsMatado

prisionerovivo2.ImHurtFunc=PrsHerido
prisionerovivo2.ImDeadFunc=PrsMatado

prisioneromuerto.ImDeadFunc=PrsMatado

sectorinic=Bladex.GetSector(-112000.0, 7000.0, 58000.0)

sectorinic.OnEnter=IniciaPrisioneros
