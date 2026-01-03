import def_class
import Bladex
import Enm_Def
import whrandom


"""
agonia3prs=Bladex.CreateSound("../../Sounds/moan2.wav", "Agonia3Prs")
agonia3prs.Volume=1
agonia3prs.Scale=1.112
agonia3prs.MinDistance=500
agonia3prs.MaxDistance=45000
"""

#######################
#     Prisioneros     #
#######################

prisionerovivo1=Bladex.CreateEntity("PrisioneroVivo3", "Prisoner_3", 2483.16054789, 1599.94557022, 22341.7806222)
prisionerovivo1.Person=1
prisionerovivo1.Angle=-3.14159/2.0
prisionerovivo1.Data=def_class.Prisoner(prisionerovivo1) # , -1340.70859198, 1593.16343408, 21635.0091023
prisionerovivo1.Life=1
prisionerovivo1.Blind=1

prisionerovivo2=Bladex.CreateEntity("PrisioneroVivo2", "Prisoner_5", -1340.70859198, 1593.16343408, 21635.0091023)
prisionerovivo2.Person=1
prisionerovivo2.Angle=3.14159/12.0
prisionerovivo2.Data=def_class.Prisoner(prisionerovivo2)
prisionerovivo2.Life=1
prisionerovivo2.Blind=1

prisioneromuerto=Bladex.CreateEntity("PrisioneroMuerto", "Prisoner_6", -1178.12808277, 1593.36002018, 11850.6916542)
prisioneromuerto.Person=1
prisioneromuerto.Angle=0.0
prisioneromuerto.Data=def_class.Prisoner(prisioneromuerto)
prisioneromuerto.Life=1
prisioneromuerto.Blind=1


prisionerovivo1.ImHurtFunc=PrsHerido
prisionerovivo1.ImDeadFunc=PrsMatado

prisionerovivo2.ImHurtFunc=PrsHerido
prisionerovivo2.ImDeadFunc=PrsMatado

prisioneromuerto.ImDeadFunc=PrsMatado



##################################
#     Prisioneros quejandose     #
##################################


sectorinic=Bladex.GetSector(685.321844855, 1382.90525999, 16790.3314864)

sectorinic.OnEnter=IniciaPrisioneros
