import def_class
import Bladex
import Enm_Def
import Reference
#import Bldb


#Bladex.LoadSampledAnimation("../../Anm/Tkn_sleep.bmv","Tkn_sleep",1,"Knight_Traitor")
#Bladex.LoadSampledAnimation("../../Anm/Tkn_sleep.bmv","Tkn_sleep",1,"Knight_Traitor")
#Bladex.LoadSampledAnimation("../../Anm/Tkn_sleep_hit.bmv","Tkn_sleep_hit",1,"Knight_Traitor")
#Bladex.LoadSampledAnimation("../../Anm/Tkn_dth_sleep.bmv","Tkn_dth_sleep",0,"Knight_Traitor")

#####################
#     Carcelero     #
#####################

carcelero=Bladex.CreateEntity("Carcelero", "Knight_Traitor", -116575.0, 8575.0, 68700.0,"Person")
carcelero.Data=def_class.DrunkWarder(carcelero)
carcelero.Life=1
carcelero.Angle=0.0
carcelero.Blind=1
carcelero.Deaf=1


sectoriniccarc=Bladex.GetSector(-112000.0, 7000.0, 61700.0)
sectoriniccarc.OnEnter=IniciaCarcelero
carcelero.ImHurtFunc=Herido
carcelero.ImDeadFunc=Matado

Bladex.AddScheduledFunc(Bladex.GetTime()+0.12, carcelero.SetOnFloor, ())

sectorapagaronq=Bladex.GetSector(-95000.0, 17250.0, 70000.0)
sectorapagaronq.OnEnter=ApagaRonquidos
