import pocimac
import Actions
import Ontake

pocimac.CreateFood("come1")

pocimac.CreateFood("come2")

pocimac.CreateFood("come3")

pocimac.CreateFood("come4")

pocimac.CreateFood("come5")

pocimac.CreateFood("come6")




####################################################################################################
##
##		POCIMAS
##
####################################################################################################
#import Pocimac

#pocima de la zona de las aranias
o=Bladex.CreateEntity("barbcome48","PocimaTodo",7692.425998,-9881.271405,-95448.447670,"Physic")
o.Scale=1.000000
o.Orientation=0.794472,0.286805,-0.534778,0.023882
pocimac.CreatePotion("barbcome48")


#pocima sobre la torre
#barbpocima100a=Bladex.CreateEntity("barbpocima100a","Pocima100",-46447.234140,-24203.502641,45139.518841)
#barbpocima100a.Static=0
#barbpocima100a.Scale=1.000000
#barbpocima100a.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("barbpocima100a")

#pocima tras las cajas en la casa de 4 pisos
barbpocima100b=Bladex.CreateEntity("m1pocima100b","Pocima100",-170672.764849,-9703.594997,208320.633127)
barbpocima100b.Static=0
barbpocima100b.Scale=1.000000
barbpocima100b.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("m1pocima100b")

#pocima en la cuarta planta de la casa de 4 pisos
o=Bladex.CreateEntity("potptp","Pocima50",-158490.005186,-25992.325026,206350.086813,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("potptp")

#pocima en la casa redonda
o=Bladex.CreateEntity("potptp2","Pocima50",-156769.995750,-19593.833216,163834.129612,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("potptp2")

#pocima tras la reja al lado de la casa del jefe
barbpocima100c=Bladex.CreateEntity("m1pocima100c","Pocima100",-84893.446288,-27201.929665,183685.536780)
barbpocima100c.Static=0
barbpocima100c.Scale=1.000000
barbpocima100c.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("m1pocima100c")


##Pocima en el moco

pocimac.CreatePotion("pocimoco")

pocimac.CreatePotion("pociencas")

pocimac.CreatePotion("cocacolo")

###########################3	POGÜER POTION


powp_PP=Bladex.CreateEntity("BARBPWPOTION","PowerPotion",-124549.543000,3913.126000,54184.42500,"Physic")
powp_PP.Solid=1
powp_PP.Scale=1.0
powp_PP.Orientation=0.899560,-0.088879,-0.427573,0.008567
pocimac.CreatePowerPotion("BARBPWPOTION")
