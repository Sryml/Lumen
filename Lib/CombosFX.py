import Bladex
import GenFX
import netgame
import math

from LumenLib import AnimAux

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None



#################################
#     Creacion de funciones     #
#################################

#CABALLERO
#"Kgt_g_27kata_new" ESPADAROMANA

def Kgt_g_27kata_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 1000, 2, 0, 0.01, 10, 2.0)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 3000, 6, 0, 0.01, 10, 2.0)
	elif step==3:
		GenFX.ModifyParticles(ComboFX_prtlsys, 1000, 2, 0, 0.01, 10, 0.1)

#"Kgt_g_28new" GLADIUS

def Kgt_g_28new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 3000, 2, 0, 0.01, 10, 2.0)
	elif step==2:
		pers=Bladex.GetEntity(EntityName)
		GenFX.ModifyParticles(ComboFX_prtlsys, 3000, 200, 0, 0.2,10, 0.05)

#"Kgt_g_01_new" MAZA

def Kgt_g_01_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 1500, 0.5, 0, 0.01, 10, 0.6)

#"Kgt_g_32_5_3new" ELFSWORD

def Kgt_g_32_5_3new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 500, 2, 0, 0.01, 10, 2.5)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 4000, 5, 0, 0.1, 10, 1.0)
	elif step==3:
		GenFX.ModifyParticles(ComboFX_prtlsys, 6000, 1, 0, 0.1, 10, 0.6)

#"Kgt_g_21_6_s8new" MAZA2

def Kgt_g_21_6_s8new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 500, 2, 0, 0.01, 10, 2.5)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 4000, 5, 0, 0.1, 10, 1.0)
	elif step==3:
		GenFX.ModifyParticles(ComboFX_prtlsys, 6000, 6, 0, 0.5, 10, 0.3)

#"Kgt_g_s22low_new" HOOKSWORD

def Kgt_g_s22low_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 3500, 5, 0, 0.03, 10, 0.6)

#"Kgt_g_sb25_new" ESPADACURVA

def Kgt_g_sb25_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 1000, 350, 0, 0.5, 15, 2.0)
	elif step==2:
		pers=Bladex.GetEntity(EntityName)
		GenFX.ModifyParticles(ComboFX_prtlsys, 4000, 4, 0, 0.1,10, 0.6)

#"Kgt_g_s19_new" DAGESSE

def Kgt_g_s19_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 3500, 5, 0, 0.03, 10, 0.8)

#"Kgt_g_18_11_22_new" CIMITARRA

def Kgt_g_18_11_22_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 500, 2, 0, 0.01, 10, 2.5)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 4000, 5, 0, 0.1, 10, 1.0)
	elif step==3:
		GenFX.ModifyParticles(ComboFX_prtlsys, 6000, 4, 0, 0.3, 10, 0.35)

#"Kgt_g_b32kata_new" MAZA3

def Kgt_g_b32kata_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 1000, 4, 0, 0.01, 10, 2.5)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 1000, 2, 0, 0.1, 10, 0.4)

#"Kgt_g_22kata_23_new" DOUBLESWORD

def Kgt_g_22kata_23_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 1000, 4, 0, 0.01, 10, 2.5)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 3000, 10, 0, 0.3, 10, 0.4)

#"Kgt_g_09_07_s6low_new" ESPADAFILO

def Kgt_g_09_07_s6low_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 3000, 4, 0, 0.1, 10, 0.4)

#"Kgt_g_29_3new" ESPADA

def Kgt_g_29_3new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 4000, 8, 0, 0.1, 10, 0.5)

#"Kgt_g_magic" BLADESWORD

def Kgt_g_magic_FX(EntityName, EventName):
	global ComboFX_prtlsys1
	global ComboFX_prtlsys2
	global ComboFX_prtlsys3
	global ComboFX_prtlsys4
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	obj_name = inv.GetActiveWeapon()
	if step==1:
		ComboFX_prtlsys1=GenFX.AddParticles(pers.Name, "LittleEnergyDissip", 200, 1, 1, 0.05, 30, 2.5, -600)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys1, 800, 1, 1, 0.05, 30, 0.8)

		id_number = int(10.0*Bladex.GetTime())

		fx_ent1 = Bladex.CreateEntity("FX1%s" % (id_number,), "FXVert2", 0,0,0)
		fx_ent2 = Bladex.CreateEntity("FX2%s" % (id_number,), "FXVert2", 0,0,0)
		fx_ent3 = Bladex.CreateEntity("FX3%s" % (id_number,), "Entity Spot", 0,0,0)
		fx_ent3.CastShadows = 0
		fx_ent3.Flick = 0
		fx_ent3.Color = (190, 180, 255)
		fx_ent3.Intensity = 0.0
		fx_ent1.Scale = 1.5
		fx_ent1.Link(fx_ent2)
		prtlsys=GenFX.AddParticles(fx_ent1.Name, "LittleEnergyDissip", 350, 0, 0, 0.1, 17, 3.9+0.7) # FastEnergyConc
		prtlsys=GenFX.AddParticles(fx_ent2.Name, "BrillosBladeSword", 150, 5, 0, 0.01, 6, 3.9+0.7)

		TrackEntity = (AnimAux.TrackEntity, (obj_name, ("anchor", "1H_R", (0,0,0)), ("", "", (1,0,0,0)), ("anchor", "1H_R", (0,0,1))), {})
		animation = AnimAux.Animation(fx_ent1, 5.0, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(0, 1280, 1.3, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 1280, 0.7, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 0, 2.5, BeforeFrame=TrackEntity)
		
		channel = animation.AddChannel(Loop=-1)
		node = channel.AddNode(0, math.pi*2, 0.75, Handler=AnimAux.NODE_HANDLER.Rotation, BeforeFrame=TrackEntity)

		animation.run()
		#
		animation = AnimAux.Animation(fx_ent3, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(0, 1280, 0.8, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 1280, 2.0, BeforeFrame=TrackEntity)

		channel = animation.AddChannel()
		node = channel.AddNode(0.0, 8.0, 0.8, BeforeFrame=TrackEntity, Handler=AnimAux.NODE_HANDLER.Intensity)
		node = channel.AddNode(8.0, 0.0, 2.0, BeforeFrame=TrackEntity, Handler=AnimAux.NODE_HANDLER.Intensity)

		animation.run()

	elif step==4:
		prtlsys=GenFX.AddParticles(obj_name, "LittleEnergyDissip", 1000, 4, 0, 0.1, 20, 1.4)
	elif step==5:
		prtlsys=GenFX.AddParticles(obj_name, "BrillosBladeSword", 800, 60, 0, 0.1, 24, 0.15)
		# 残影
		obj = Bladex.CreateEntity(str(Bladex.GetTime()), "FXVert2", 0,0,0)

		animation = AnimAux.Animation(obj, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel(Loop=-1, Time2Live=0.28)
		node = channel.AddNode(Handler=AnimAux.NODE_HANDLER.AfterimageFX)
		node.Afterimage_Target = obj_name
		node.Afterimage_Interval = 0.019

		animation.run()

#"Kgt_g_magic2" BLADESWORD

def Kgt_g_magic2_FX(EntityName, EventName):
	global ComboFX_prtlsys1
	global ComboFX_prtlsys2
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	if step==1:
		ComboFX_prtlsys1=GenFX.AddParticles(pers.InvRight, "LittleEnergyDissip", 1000, 4, 0, 0.1, 30, 2.0)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys1, 1000, 4, 0, 0.1, 20, 1.75)
	elif step==3:
		ComboFX_prtlsys2=GenFX.AddParticles(pers.InvRight, "LittleEnergyDissip", 6000, 60, 0, 0.05, 20, 0.1)

# FIRESWORD      
def Kgt_g_s28kata_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "Llamita", 1000, 10, 0, 0.1, 20, 1.3, -3000)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 3000, 0, 20, 0.1, 20, 0.3)

# ICESWORD 
def Kgt_g_12_7_s1new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	o = Bladex.GetEntity(inv.GetActiveWeapon())
	x,y,z = o.Position
	spark= Bladex.CreateSpark("Snow",x,y,z, 0,1,0, 1.1,400,100,10,10, 200,200,200, 0,0,20, 800,1.5,1.0/60.0,0)
	spark.RasterMode="BlendingAlpha"
	#
	if step==1:
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "WhiteTrail", 500, 5, 0, 0.9, 20, 2.0, 2000)
	elif step==3:
		GenFX.ModifyParticles(ComboFX_prtlsys, 600, 5, 0, 0.01, 20, 0.5)


#BARBARO
#"Bar_g2h_b6" CHAOSWORD

def Bar_g2h_b6_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 3000, 1, 0, 0.01, 10, 0.3)

#"Bar_g_axe211" ECLIPSE

def Bar_g_axe211_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 3000, 1, 0, 0.01, 10, 0.4)

#"Bar_g2h_b6low" DEATHSWORD

def Bar_g2h_b6low_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 3000, 2, 0, 0.01, 10, 0.4)

#"Bar_g_axe33" GUADANYA

def Bar_g_axe33_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 2, 0, 0.01, 10, 0.4)

#"Bar_g2h_13" LONGSWORD

def Bar_g2h_13_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 2, 0, 0.01, 10, 0.2)

#"Bar_g2h_s8" ALFANGE

def Bar_g2h_s8_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 2, 0, 0.01, 10, 0.2)

#"Bar_g_axe34" HACHA2HOJAS

def Bar_g_axe34_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		ComboFX_prtlsys=GenFX.AddParticles(pers.InvRight, "RedTrail", 500, 4, 0, 0.01, 10, 2.5)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 2000, 5, 0, 0.1, 10, 1.0)
	elif step==3:
		GenFX.ModifyParticles(ComboFX_prtlsys, 4000, 4, 0, 0.1, 10, 0.6)

#"Bar_g_axe30" ICEAXE

def Bar_g_axe30_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	o = Bladex.GetEntity(inv.GetActiveWeapon())
	x,y,z = o.Position
	spark= Bladex.CreateSpark("Snow",x,y,z, 0,1,0, 1.1,400,100,10,10, 200,200,200, 0,0,20, 800,1.5,1.0/60.0,0)
	spark.RasterMode="BlendingAlpha"
	#
	if step==1:
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "WhiteTrail", 600, 1, 0, 0.9, 20, 2.0, 2000)
	elif step==4:
		GenFX.ModifyParticles(ComboFX_prtlsys, 700, 5, 0, 0.01, 20, 0.5)

#"Bar_g2h_28" FLATSWORD

def Bar_g2h_28_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 4, 0, 0.01, 10, 0.4)

#"Bar_g2h_b29" BIGSWORD

def Bar_g2h_b29_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 2, 0, 0.01, 10, 0.4)

#"Bar_g_axe12" RHINOCLUB

def Bar_g_axe12_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 4000, 2, 0, 0.01, 10, 0.5)

#"Bar_g_axe32" HACHARRAJADA

def Bar_g_axe32_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 4000, 3, 0, 0.01, 10, 0.5)

#"Bar_g2h_21_7" SAWSWORD

def Bar_g2h_21_7_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 3, 0, 0.01, 10, 1.9)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 3000, 3, 0, 0.01, 10, 0.4)

#"Bar_g2h_earthpow" FIREBIGSWORD1

def Bar_g2h_earthpow_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 4000, 3, 0, 0.1, 30, 1.3)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 1000, 90, 0, 0.2, 25, 0.2)

#"Bar_g2h_21_2" FIREBIGSWORD2

def Bar_g2h_21_2_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2000, 3, 0, 0.1, 20, 1.3)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 5000, 3, 0, 0.1, 35, 0.3)

#"Bar_g_magic" BLADESWORD

def Bar_g_magic_FX(EntityName, EventName):
	global ComboFX_prtlsys1
	global ComboFX_prtlsys2
	global ComboFX_prtlsys3
	global ComboFX_prtlsys4
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	obj_name = inv.GetActiveWeapon()
	if step==1:
		ComboFX_prtlsys1=GenFX.AddParticles(pers.Name, "LittleEnergyDissip", 200, 1, 1, 0.05, 30, 2.5, -600)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys1, 800, 1, 1, 0.05, 30, 0.8)

		id_number = int(10.0*Bladex.GetTime())

		fx_ent1 = Bladex.CreateEntity("FX1%s" % (id_number,), "FXVert2", 0,0,0)
		fx_ent2 = Bladex.CreateEntity("FX2%s" % (id_number,), "FXVert2", 0,0,0)
		fx_ent3 = Bladex.CreateEntity("FX3%s" % (id_number,), "Entity Spot", 0,0,0)
		fx_ent3.CastShadows = 0
		fx_ent3.Flick = 0
		fx_ent3.Color = (190, 180, 255)
		fx_ent3.Intensity = 0.0
		fx_ent1.Scale = 1.5
		fx_ent1.Link(fx_ent2)
		prtlsys=GenFX.AddParticles(fx_ent1.Name, "LittleEnergyDissip", 350, 0, 0, 0.1, 17, 3.9+0.7) # FastEnergyConc
		prtlsys=GenFX.AddParticles(fx_ent2.Name, "BrillosBladeSword", 150, 5, 0, 0.01, 6, 3.9+0.7)

		TrackEntity = (AnimAux.TrackEntity, (obj_name, ("anchor", "1H_R", (0,0,0)), ("", "", (1,0,0,0)), ("anchor", "1H_R", (0,0,1))), {})
		animation = AnimAux.Animation(fx_ent1, 5.0, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(0, 1280, 1.3, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 1280, 0.7, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 0, 2.5, BeforeFrame=TrackEntity)
		
		channel = animation.AddChannel(Loop=-1)
		node = channel.AddNode(0, math.pi*2, 0.75, Handler=AnimAux.NODE_HANDLER.Rotation, BeforeFrame=TrackEntity)

		animation.run()
		#
		animation = AnimAux.Animation(fx_ent3, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(0, 1280, 0.8, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 1280, 2.0, BeforeFrame=TrackEntity)

		channel = animation.AddChannel()
		node = channel.AddNode(0.0, 8.0, 0.8, BeforeFrame=TrackEntity, Handler=AnimAux.NODE_HANDLER.Intensity)
		node = channel.AddNode(8.0, 0.0, 2.0, BeforeFrame=TrackEntity, Handler=AnimAux.NODE_HANDLER.Intensity)

		animation.run()

	elif step==4:
		prtlsys=GenFX.AddParticles(obj_name, "LittleEnergyDissip", 1000, 4, 0, 0.1, 20, 1.4)
	elif step==5:
		prtlsys=GenFX.AddParticles(obj_name, "BrillosBladeSword", 800, 60, 0, 0.1, 24, 0.15)
		# 残影
		obj = Bladex.CreateEntity(str(Bladex.GetTime()), "FXVert2", 0,0,0)

		animation = AnimAux.Animation(obj, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel(Loop=-1, Time2Live=0.28)
		node = channel.AddNode(Handler=AnimAux.NODE_HANDLER.AfterimageFX)
		node.Afterimage_Target = obj_name
		node.Afterimage_Interval = 0.019

		animation.run()

#"Bar_g_magic2" BLADESWORD

def Bar_g_magic2_FX(EntityName, EventName):
	global ComboFX_prtlsys1
	global ComboFX_prtlsys2
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	if step==1:
		ComboFX_prtlsys1=GenFX.AddParticles(pers.InvRight, "LittleEnergyDissip", 1000, 4, 0, 0.1, 30, 2.0)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys1, 1000, 4, 0, 0.1, 20, 1.75)
	elif step==3:
		ComboFX_prtlsys2=GenFX.AddParticles(pers.InvRight, "LittleEnergyDissip", 6000, 60, 0, 0.05, 20, 0.1)


#AMAZONA
#"Amz_g_spears8" BO

def Amz_g_spears8_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 4, 0, 0.01, 10, 0.3)

#"Amz_g_spear_2katab6low" BICHERO

def Amz_g_spear_2katab6low_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 4, 0, 0.01, 10, 0.3)

#"Amz_g_spear19" LANZA

def Amz_g_spear19_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 3, 0, 0.01, 10, 0.3)

#"Amz_g_spear22" NAGINATA

def Amz_g_spear22_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 6, 0, 0.1, 10, 0.27)

#"Amz_g_spear09" TRIDENTE

def Amz_g_spear09_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 4, 0, 0.1, 10, 0.2)

#"Amz_g_spear32kata_b2" AXPEAR

def Amz_g_spear32kata_b2_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2000, 4, 0, 0.1, 10, 1.4)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 3500, 3, 0, 0.01, 10, 0.3)

#"Amz_g_spear_kata23" DEATHBO

def Amz_g_spear_kata23_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2000, 5, 0, 0.1, 10, 1.4)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 3500, 3, 0, 0.01, 10, 0.4)

#"Amz_g_spear13" CROSSPEAR

def Amz_g_spear13_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 6000, 4, 0, 0.1, 10, 0.35)

#"Amz_g_spear3s2" HACHACUCHILLA

def Amz_g_spear3s2_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 4000, 6, 0, 0.1, 10, 0.3)

#"Amz_g_spear_21" CRUSHBO

def Amz_g_spear_21_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 4000, 3, 0, 0.1, 10, 0.4)

#"Amz_g_spear_b29" ARPON

def Amz_g_spear_b29_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 5200, 4, 0, 0.1, 10, 0.4)

#"Amz_g_spear33" NAGINATA2

def Amz_g_spear33_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 5, 0, 0.1, 10, 1.8)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 3000, 4, 0, 0.2, 10, 0.4)

#"Amz_g_spear_sb11" LANZAANCHA

def Amz_g_spear_sb11_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2000, 5, 0, 0.1, 10, 1.6)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 4000, 3, 0, 0.01, 10, 0.6)
	elif step==3:
		GenFX.ModifyParticles(ComboFX_prtlsys, 5000, 10, 0, 0.1, 10, 0.2)

# ICEWAND    
def Amz_g_spear16_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	o = Bladex.GetEntity(inv.GetActiveWeapon())
	x,y,z = o.Position
	#
	if step==1:
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "WhiteTrail", 500, 5, 0, 0.9, 20, 2.0, 2000)
	elif step==2:
		spark= Bladex.CreateSpark("Snow",x,y,z, 0,1,0, 1.1,400,100,10,10, 200,200,200, 0,0,20, 800,1.5,1.0/60.0,0)
		spark.RasterMode="BlendingAlpha"
		GenFX.ModifyParticles(ComboFX_prtlsys, 700, 5, 0, 0.01, 20, 0.4)

# STEELFEATHER
def Amz_g_spear19_bs1_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "GreenTrail", 800, 5, 0, 0.3, 18, 1.8)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 1600, 10, 0, 0.01, 24, 0.3)

# FIREBO
def Amz_g_spear_b6_26_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	obj_name = inv.GetActiveWeapon()

	if step==1:
		id_number = int(10.0*Bladex.GetTime())
		for i in (1,-1):
			fx_ent1 = Bladex.CreateEntity("FX%s_%s" % (id_number, i), "FXVert2", 0,0,0)
			fx_ent2 = Bladex.CreateEntity("FX%s_%s" % (id_number, i), "FXVert2", 0,0,0)
			fx_ent1.Link(fx_ent2)
			prtlsys=GenFX.AddParticles(fx_ent1.Name, "RedTrail", 400, 0, 0, 0.3, 17, 3.4)
			prtlsys=GenFX.AddParticles(fx_ent2.Name, "Llamita", 500, 10, 0, 0.3, 20, 3.4)

			animation = AnimAux.Animation(fx_ent1, 4.4, Destroy=AnimAux.DESTROY_METHOD_BIN)
			TrackEntity = (AnimAux.TrackEntity, (obj_name, ("", "", (0,0,0)), ("", "", (1,0,0,0)), ("anchor", "1H_R", (0,0,1))), {})

			channel = animation.AddChannel()
			node = channel.AddNode(0, 1085*i, 0.9, BeforeFrame=TrackEntity)
			node = channel.AddNode(1085*i, 0, 2.5, BeforeFrame=TrackEntity)
			
			channel = animation.AddChannel(Loop=-1)
			node = channel.AddNode(0, math.pi*2, 0.5, Handler=AnimAux.NODE_HANDLER.Rotation, BeforeFrame=TrackEntity)

			animation.run()
	elif step==2:
		ComboFX_prtlsys=GenFX.AddParticles(obj_name, "Llamita", 2000, 0, 20, 0.1, 20, 0.7, -3000)

#"Amz_g_magic" BLADESWORD

def Amz_g_magic_FX(EntityName, EventName):
	global ComboFX_prtlsys1
	global ComboFX_prtlsys2
	global ComboFX_prtlsys3
	global ComboFX_prtlsys4
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	obj_name = inv.GetActiveWeapon()
	if step==1:
		ComboFX_prtlsys1=GenFX.AddParticles(pers.Name, "LittleEnergyDissip", 200, 1, 1, 0.05, 30, 2.5, -600)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys1, 800, 1, 1, 0.05, 30, 0.8)

		id_number = int(10.0*Bladex.GetTime())

		fx_ent1 = Bladex.CreateEntity("FX1%s" % (id_number,), "FXVert2", 0,0,0)
		fx_ent2 = Bladex.CreateEntity("FX2%s" % (id_number,), "FXVert2", 0,0,0)
		fx_ent3 = Bladex.CreateEntity("FX3%s" % (id_number,), "Entity Spot", 0,0,0)
		fx_ent3.CastShadows = 0
		fx_ent3.Flick = 0
		fx_ent3.Color = (190, 180, 255)
		fx_ent3.Intensity = 0.0
		fx_ent1.Scale = 1.5
		fx_ent1.Link(fx_ent2)
		prtlsys=GenFX.AddParticles(fx_ent1.Name, "LittleEnergyDissip", 350, 0, 0, 0.1, 17, 3.9+0.7) # FastEnergyConc
		prtlsys=GenFX.AddParticles(fx_ent2.Name, "BrillosBladeSword", 150, 5, 0, 0.01, 6, 3.9+0.7)

		TrackEntity = (AnimAux.TrackEntity, (obj_name, ("anchor", "1H_R", (0,0,0)), ("", "", (1,0,0,0)), ("anchor", "1H_R", (0,0,1))), {})
		animation = AnimAux.Animation(fx_ent1, 5.0, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(0, 1280, 1.3, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 1280, 0.7, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 0, 2.5, BeforeFrame=TrackEntity)
		
		channel = animation.AddChannel(Loop=-1)
		node = channel.AddNode(0, math.pi*2, 0.75, Handler=AnimAux.NODE_HANDLER.Rotation, BeforeFrame=TrackEntity)

		animation.run()
		#
		animation = AnimAux.Animation(fx_ent3, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(0, 1280, 0.8, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 1280, 2.0, BeforeFrame=TrackEntity)

		channel = animation.AddChannel()
		node = channel.AddNode(0.0, 8.0, 0.8, BeforeFrame=TrackEntity, Handler=AnimAux.NODE_HANDLER.Intensity)
		node = channel.AddNode(8.0, 0.0, 2.0, BeforeFrame=TrackEntity, Handler=AnimAux.NODE_HANDLER.Intensity)

		animation.run()

	elif step==4:
		prtlsys=GenFX.AddParticles(obj_name, "LittleEnergyDissip", 1000, 4, 0, 0.1, 20, 1.4)
	elif step==5:
		prtlsys=GenFX.AddParticles(obj_name, "BrillosBladeSword", 800, 60, 0, 0.1, 24, 0.15)
		# 残影
		obj = Bladex.CreateEntity(str(Bladex.GetTime()), "FXVert2", 0,0,0)

		animation = AnimAux.Animation(obj, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel(Loop=-1, Time2Live=0.28)
		node = channel.AddNode(Handler=AnimAux.NODE_HANDLER.AfterimageFX)
		node.Afterimage_Target = obj_name
		node.Afterimage_Interval = 0.019

		animation.run()

#"Amz_g_magic2" BLADESWORD

def Amz_g_magic2_FX(EntityName, EventName):
	global ComboFX_prtlsys1
	global ComboFX_prtlsys2
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	if step==1:
		ComboFX_prtlsys1=GenFX.AddParticles(pers.InvRight, "LittleEnergyDissip", 1000, 4, 0, 0.1, 30, 2.0)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys1, 1000, 4, 0, 0.1, 20, 1.75)
	elif step==3:
		ComboFX_prtlsys2=GenFX.AddParticles(pers.InvRight, "LittleEnergyDissip", 6000, 60, 0, 0.05, 20, 0.1)


#ENANO
#"Dwf_g_14" GARROTE

def Dwf_g_14_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2000, 1, 0, 0.01, 10, 0.35)

#"Dwf_g_15" HACHA

def Dwf_g_15_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2000, 2, 0, 0.01, 10, 0.3)

#"Dwf_g_07" HACHA5

def Dwf_g_07_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2100, 1, 0, 0.01, 10, 0.4)

#"Dwf_g_11" GARROPIN

def Dwf_g_11_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2100, 2, 0, 0.01, 10, 0.4)

#"Dwf_g_16" HACHA4

def Dwf_g_16_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2500, 2, 0, 0.01, 10, 0.34)

#"Dwf_g_05" HACHA3

def Dwf_g_05_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 2500, 3, 0, 0.01, 10, 0.4)

#"Dwf_g_12" MARTILLO

def Dwf_g_12_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 2, 0, 0.01, 10, 0.4)

#"Dwf_g_18" MARTILLO2

def Dwf_g_18_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 2, 0, 0.01, 10, 0.4)

#"Dwf_g_13" GARROTE2

def Dwf_g_13_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 2, 0, 0.1, 10, 0.4)

#"Dwf_g_21" MAZADOBLE

def Dwf_g_21_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 4, 0, 0.01, 10, 0.4)

#"Dwf_g_s3_new" HACHA6

def Dwf_g_s3_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 4, 0, 0.01, 10, 0.4)

#"Dwf_g_17" HACHA2

def Dwf_g_17_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 2, 0, 0.1, 10, 0.35)

#"Dwf_g_31" MARTILLO3

def Dwf_g_31_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "RedTrail", 3000, 3, 0, 0.1, 10, 1.2)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 3000, 3, 0, 0.1, 10, 0.4)

#"Dwf_g_s22low_new" CRUSHHAMMER

def Dwf_g_s22low_new_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	if step==1:
		pers=Bladex.GetEntity(EntityName)
		inv=pers.GetInventory()
		ComboFX_prtlsys=GenFX.AddParticles(inv.GetActiveWeapon(), "GreenTrail", 1200, 5, 0, 0.1, 20, 0.9)

#"Dwf_g_s18_2h" ICEHAMMER

def Dwf_g_s18_2h_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	obj_name = inv.GetActiveWeapon()
	o = Bladex.GetEntity(obj_name)
	#
	if step==1:
		ComboFX_prtlsys=GenFX.AddParticles(obj_name, "WhiteTrail", 500, 5, 0, 0.5, 25, 2.0, 2000)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys, 1000, 35, 0, 0.01, 35, 0.25)
		x,y,z = o.Position
		spark= Bladex.CreateSpark("Snow",x,y,z, 0,1,0, 1.1,400,100,10,10, 200,200,200, 0,0,20, 800,1.5,1.0/60.0,0)
		spark.RasterMode="BlendingAlpha"
		#
		id_number = int(10.0*Bladex.GetTime())
		fx_ent1 = Bladex.CreateEntity("FX%s" % (id_number), "FXVert2", 0,0,0)
		fx_ent1.Scale=5
		fx_ent1.Position = pers.Rel2AbsPoint(0,-800,-700)
		prtlsys=GenFX.AddParticles(fx_ent1.Name, "WhiteTrail", 1000, 23, 0, 0.05, 35, 0.65, 3000)
		prtlsys.Velocity=0,-3000,0

		animation = AnimAux.Animation(fx_ent1, 2.0, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(fx_ent1.Scale, 28, 0.55, Handler=AnimAux.NODE_HANDLER.Scale)

		channel = animation.AddChannel(Loop=-1)
		node = channel.AddNode(0, AnimAux.two_pi, 0.4, Handler=AnimAux.NODE_HANDLER.Rotation)
		node.Direction = (0,-1,0)

		animation.run()


#"Dwf_g_22" FIREAXE

def Dwf_g_22_FX(EntityName, EventName):
	global ComboFX_prtlsys
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	obj_name = inv.GetActiveWeapon()

	if step==1:
		id_number = int(10.0*Bladex.GetTime())
		for i in (1,-1):
			fx_ent1 = Bladex.CreateEntity("FX%s_%s" % (id_number, i), "FXVert2", 0,0,0)
			fx_ent2 = Bladex.CreateEntity("FX%s_%s" % (id_number, i), "FXVert2", 0,0,0)
			fx_ent1.Link(fx_ent2)
			fx_ent1.Scale = fx_ent2.Scale = 4
			prtlsys=GenFX.AddParticles(fx_ent1.Name, "RedTrail", 400, 0, 0, 0.3, 17, 3.1)
			prtlsys=GenFX.AddParticles(fx_ent2.Name, "Llamita", 500, 10, 0, 0.3, 20, 3.1)

			animation = AnimAux.Animation(fx_ent1, 4.0, Destroy=AnimAux.DESTROY_METHOD_BIN)
			TrackEntity = (AnimAux.TrackEntity, (obj_name, ("anchor", "1H_R", (0,0,490)), ("", "", (1,0,0,0)), ("anchor", "1H_R", (0,0,1))), {})

			channel = animation.AddChannel(Loop=-1)
			node = channel.AddNode(-490*i, 490*i, 1.1, BeforeFrame=TrackEntity)
			node = channel.AddNode(490*i, -490*i, 1.1, BeforeFrame=TrackEntity)
			
			channel = animation.AddChannel(Loop=-1)
			node = channel.AddNode(0, AnimAux.two_pi, 0.9, Handler=AnimAux.NODE_HANDLER.Rotation, BeforeFrame=TrackEntity)

			animation.run()
	elif step==2:
		ComboFX_prtlsys=GenFX.AddParticles(obj_name, "Llamita", 1000, 0, 20, 0.1, 20, 0.7, -3000)
	elif step==3:
		id_number = int(10.0*Bladex.GetTime())
		fx_ent1 = Bladex.CreateEntity("FX%s" % (id_number), "FXVert2", 0,0,0)
		fx_ent1.Scale=5
		fx_ent1.Position = pers.Rel2AbsPoint(0,-800,-600)
		prtlsys=GenFX.AddParticles(fx_ent1.Name, "RedTrail", 1000, 25, 0, 0.05, 35, 0.65, -2000)
		prtlsys.Velocity=0,-1000,0

		animation = AnimAux.Animation(fx_ent1, 2.0, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(fx_ent1.Scale, 33, 0.6, Handler=AnimAux.NODE_HANDLER.Scale)

		channel = animation.AddChannel(Loop=-1)
		node = channel.AddNode(0, AnimAux.two_pi, 0.3, Handler=AnimAux.NODE_HANDLER.Rotation)
		node.Direction = (0,-1,0)

		animation.run()

#"Dwf_g_magic" BLADESWORD

def Dwf_g_magic_FX(EntityName, EventName):
	global ComboFX_prtlsys1
	global ComboFX_prtlsys2
	global ComboFX_prtlsys3
	global ComboFX_prtlsys4
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	inv=pers.GetInventory()
	obj_name = inv.GetActiveWeapon()
	if step==1:
		ComboFX_prtlsys1=GenFX.AddParticles(pers.Name, "LittleEnergyDissip", 200, 1, 1, 0.05, 30, 2.5, -600)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys1, 800, 1, 1, 0.05, 30, 0.8)

		id_number = int(10.0*Bladex.GetTime())

		fx_ent1 = Bladex.CreateEntity("FX1%s" % (id_number,), "FXVert2", 0,0,0)
		fx_ent2 = Bladex.CreateEntity("FX2%s" % (id_number,), "FXVert2", 0,0,0)
		fx_ent3 = Bladex.CreateEntity("FX3%s" % (id_number,), "Entity Spot", 0,0,0)
		fx_ent3.CastShadows = 0
		fx_ent3.Flick = 0
		fx_ent3.Color = (190, 180, 255)
		fx_ent3.Intensity = 0.0
		fx_ent1.Scale = 1.5
		fx_ent1.Link(fx_ent2)
		prtlsys=GenFX.AddParticles(fx_ent1.Name, "LittleEnergyDissip", 350, 0, 0, 0.1, 17, 3.9+0.7) # FastEnergyConc
		prtlsys=GenFX.AddParticles(fx_ent2.Name, "BrillosBladeSword", 150, 5, 0, 0.01, 6, 3.9+0.7)

		TrackEntity = (AnimAux.TrackEntity, (obj_name, ("anchor", "1H_R", (0,0,0)), ("", "", (1,0,0,0)), ("anchor", "1H_R", (0,0,1))), {})
		animation = AnimAux.Animation(fx_ent1, 5.0, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(0, 1280, 1.3, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 1280, 0.7, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 0, 2.5, BeforeFrame=TrackEntity)
		
		channel = animation.AddChannel(Loop=-1)
		node = channel.AddNode(0, math.pi*2, 0.75, Handler=AnimAux.NODE_HANDLER.Rotation, BeforeFrame=TrackEntity)

		animation.run()
		#
		animation = AnimAux.Animation(fx_ent3, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel()
		node = channel.AddNode(0, 1280, 0.8, BeforeFrame=TrackEntity)
		node = channel.AddNode(1280, 1280, 2.0, BeforeFrame=TrackEntity)

		channel = animation.AddChannel()
		node = channel.AddNode(0.0, 8.0, 0.8, BeforeFrame=TrackEntity, Handler=AnimAux.NODE_HANDLER.Intensity)
		node = channel.AddNode(8.0, 0.0, 2.0, BeforeFrame=TrackEntity, Handler=AnimAux.NODE_HANDLER.Intensity)

		animation.run()

	elif step==4:
		prtlsys=GenFX.AddParticles(obj_name, "LittleEnergyDissip", 1000, 4, 0, 0.1, 20, 1.4)
	elif step==5:
		prtlsys=GenFX.AddParticles(obj_name, "BrillosBladeSword", 800, 60, 0, 0.1, 24, 0.15)
		# 残影
		obj = Bladex.CreateEntity(str(Bladex.GetTime()), "FXVert2", 0,0,0)

		animation = AnimAux.Animation(obj, Destroy=AnimAux.DESTROY_METHOD_BIN)

		channel = animation.AddChannel(Loop=-1, Time2Live=0.28)
		node = channel.AddNode(Handler=AnimAux.NODE_HANDLER.AfterimageFX)
		node.Afterimage_Target = obj_name
		node.Afterimage_Interval = 0.019

		animation.run()

#"Dwf_g_magic2" BLADESWORD

def Dwf_g_magic2_FX(EntityName, EventName):
	global ComboFX_prtlsys1
	global ComboFX_prtlsys2
	step=int(EventName[len(EventName)-1:])
	pers=Bladex.GetEntity(EntityName)
	if step==1:
		ComboFX_prtlsys1=GenFX.AddParticles(pers.InvRight, "LittleEnergyDissip", 1000, 4, 0, 0.1, 30, 2.0)
	elif step==2:
		GenFX.ModifyParticles(ComboFX_prtlsys1, 1000, 4, 0, 0.1, 20, 1.75)
	elif step==3:
		ComboFX_prtlsys2=GenFX.AddParticles(pers.InvRight, "LittleEnergyDissip", 6000, 60, 0, 0.05, 20, 0.1)




#############################################
#     Asignacion de funciones a eventos     #
#############################################


def KgtCombosFX(pers_name):
	if netgame.GetNetState() == 1:
		return
	pers=Bladex.GetEntity(pers_name)
	pers.AddAnmEventFunc("Kgt_g_27kata_new_1", Kgt_g_27kata_new_FX)
	pers.AddAnmEventFunc("Kgt_g_27kata_new_2", Kgt_g_27kata_new_FX)
	pers.AddAnmEventFunc("Kgt_g_27kata_new_3", Kgt_g_27kata_new_FX)

	pers.AddAnmEventFunc("Kgt_g_28new_1", Kgt_g_28new_FX)
	pers.AddAnmEventFunc("Kgt_g_28new_2", Kgt_g_28new_FX)

	pers.AddAnmEventFunc("Kgt_g_01_new_1", Kgt_g_01_new_FX)

	pers.AddAnmEventFunc("Kgt_g_32_5_3new_1", Kgt_g_32_5_3new_FX)
	pers.AddAnmEventFunc("Kgt_g_32_5_3new_2", Kgt_g_32_5_3new_FX)
	pers.AddAnmEventFunc("Kgt_g_32_5_3new_3", Kgt_g_32_5_3new_FX)

	pers.AddAnmEventFunc("Kgt_g_21_6_s8new_1", Kgt_g_21_6_s8new_FX)
	pers.AddAnmEventFunc("Kgt_g_21_6_s8new_2", Kgt_g_21_6_s8new_FX)
	pers.AddAnmEventFunc("Kgt_g_21_6_s8new_3", Kgt_g_21_6_s8new_FX)

	pers.AddAnmEventFunc("Kgt_g_s22low_new_1", Kgt_g_s22low_new_FX)

	pers.AddAnmEventFunc("Kgt_g_sb25_new_1", Kgt_g_sb25_new_FX)
	pers.AddAnmEventFunc("Kgt_g_sb25_new_2", Kgt_g_sb25_new_FX)

	pers.AddAnmEventFunc("Kgt_g_s19_new_1", Kgt_g_s19_new_FX)

	pers.AddAnmEventFunc("Kgt_g_18_11_22_new_1", Kgt_g_18_11_22_new_FX)
	pers.AddAnmEventFunc("Kgt_g_18_11_22_new_2", Kgt_g_18_11_22_new_FX)
	pers.AddAnmEventFunc("Kgt_g_18_11_22_new_3", Kgt_g_18_11_22_new_FX)

	pers.AddAnmEventFunc("Kgt_g_b32kata_new_1", Kgt_g_b32kata_new_FX)
	pers.AddAnmEventFunc("Kgt_g_b32kata_new_2", Kgt_g_b32kata_new_FX)

	pers.AddAnmEventFunc("Kgt_g_22kata_23_new_1", Kgt_g_22kata_23_new_FX)
	pers.AddAnmEventFunc("Kgt_g_22kata_23_new_2", Kgt_g_22kata_23_new_FX)

	pers.AddAnmEventFunc("Kgt_g_09_07_s6low_new_1", Kgt_g_09_07_s6low_new_FX)

	pers.AddAnmEventFunc("Kgt_g_29_3new_1", Kgt_g_29_3new_FX)

	pers.AddAnmEventFunc("Kgt_g_magic_1", Kgt_g_magic_FX)
	pers.AddAnmEventFunc("Kgt_g_magic_2", Kgt_g_magic_FX)
	pers.AddAnmEventFunc("Kgt_g_magic_3", Kgt_g_magic_FX)
	pers.AddAnmEventFunc("Kgt_g_magic_4", Kgt_g_magic_FX)
	pers.AddAnmEventFunc("Kgt_g_magic_5", Kgt_g_magic_FX)

	pers.AddAnmEventFunc("Kgt_g_magic2_1", Kgt_g_magic2_FX)
	pers.AddAnmEventFunc("Kgt_g_magic2_2", Kgt_g_magic2_FX)
	pers.AddAnmEventFunc("Kgt_g_magic2_3", Kgt_g_magic2_FX)

	# Added
	pers.AddAnmEventFunc("Kgt_g_s28kata_new_1", Kgt_g_s28kata_new_FX)
	pers.AddAnmEventFunc("Kgt_g_s28kata_new_2", Kgt_g_s28kata_new_FX)
	
	pers.AddAnmEventFunc("Kgt_g_12_7_s1new_1", Kgt_g_12_7_s1new_FX)
	pers.AddAnmEventFunc("Kgt_g_12_7_s1new_2", Kgt_g_12_7_s1new_FX)
	pers.AddAnmEventFunc("Kgt_g_12_7_s1new_3", Kgt_g_12_7_s1new_FX)


def AmzCombosFX(pers_name):
	if netgame.GetNetState() == 1:
		return
	pers=Bladex.GetEntity(pers_name)
	pers.AddAnmEventFunc("Amz_g_spears8_1", Amz_g_spears8_FX)

	pers.AddAnmEventFunc("Amz_g_spear_2katab6low_1", Amz_g_spear_2katab6low_FX)

	pers.AddAnmEventFunc("Amz_g_spear19_1", Amz_g_spear19_FX)

	pers.AddAnmEventFunc("Amz_g_spear22_1", Amz_g_spear22_FX)

	pers.AddAnmEventFunc("Amz_g_spear09_1", Amz_g_spear09_FX)

	pers.AddAnmEventFunc("Amz_g_spear32kata_b2_1", Amz_g_spear32kata_b2_FX)
	pers.AddAnmEventFunc("Amz_g_spear32kata_b2_2", Amz_g_spear32kata_b2_FX)

	pers.AddAnmEventFunc("Amz_g_spear_kata23_1", Amz_g_spear_kata23_FX)
	pers.AddAnmEventFunc("Amz_g_spear_kata23_2", Amz_g_spear_kata23_FX)

	pers.AddAnmEventFunc("Amz_g_spear13_1", Amz_g_spear13_FX)

	pers.AddAnmEventFunc("Amz_g_spear3s2_1", Amz_g_spear3s2_FX)

	pers.AddAnmEventFunc("Amz_g_spear_21_1", Amz_g_spear_21_FX)

	pers.AddAnmEventFunc("Amz_g_spear_b29_1", Amz_g_spear_b29_FX)

	pers.AddAnmEventFunc("Amz_g_spear33_1", Amz_g_spear33_FX)
	pers.AddAnmEventFunc("Amz_g_spear33_2", Amz_g_spear33_FX)

	pers.AddAnmEventFunc("Amz_g_spear_sb11_1", Amz_g_spear_sb11_FX)
	pers.AddAnmEventFunc("Amz_g_spear_sb11_2", Amz_g_spear_sb11_FX)
	pers.AddAnmEventFunc("Amz_g_spear_sb11_3", Amz_g_spear_sb11_FX)

	pers.AddAnmEventFunc("Amz_g_magic_1", Amz_g_magic_FX)
	pers.AddAnmEventFunc("Amz_g_magic_2", Amz_g_magic_FX)
	pers.AddAnmEventFunc("Amz_g_magic_3", Amz_g_magic_FX)
	pers.AddAnmEventFunc("Amz_g_magic_4", Amz_g_magic_FX)
	pers.AddAnmEventFunc("Amz_g_magic_5", Amz_g_magic_FX)

	pers.AddAnmEventFunc("Amz_g_magic2_1", Amz_g_magic2_FX)
	pers.AddAnmEventFunc("Amz_g_magic2_2", Amz_g_magic2_FX)
	pers.AddAnmEventFunc("Amz_g_magic2_3", Amz_g_magic2_FX)
    
    # Added
	pers.AddAnmEventFunc("Amz_g_spear16_1", Amz_g_spear16_FX)
	pers.AddAnmEventFunc("Amz_g_spear16_2", Amz_g_spear16_FX)
    
	pers.AddAnmEventFunc("Amz_g_spear19_bs1_1", Amz_g_spear19_bs1_FX)
	pers.AddAnmEventFunc("Amz_g_spear19_bs1_2", Amz_g_spear19_bs1_FX)
	
	pers.AddAnmEventFunc("Amz_g_spear_b6_26_1", Amz_g_spear_b6_26_FX)
	pers.AddAnmEventFunc("Amz_g_spear_b6_26_2", Amz_g_spear_b6_26_FX)


def BarCombosFX(pers_name):
	if netgame.GetNetState() == 1:
		return
	pers=Bladex.GetEntity(pers_name)
	pers.AddAnmEventFunc("Bar_g2h_b6_1", Bar_g2h_b6_FX)

	pers.AddAnmEventFunc("Bar_g_axe211_1", Bar_g_axe211_FX)

	pers.AddAnmEventFunc("Bar_g2h_b6low_1", Bar_g2h_b6low_FX)

	pers.AddAnmEventFunc("Bar_g_axe33_1", Bar_g_axe33_FX)

	pers.AddAnmEventFunc("Bar_g2h_13_1", Bar_g2h_13_FX)

	pers.AddAnmEventFunc("Bar_g2h_s8_1", Bar_g2h_s8_FX)

	pers.AddAnmEventFunc("Bar_g_axe34_1", Bar_g_axe34_FX)
	pers.AddAnmEventFunc("Bar_g_axe34_2", Bar_g_axe34_FX)
	pers.AddAnmEventFunc("Bar_g_axe34_3", Bar_g_axe34_FX)
	
	# Added
	pers.AddAnmEventFunc("Bar_g_axe30_1", Bar_g_axe30_FX)
	pers.AddAnmEventFunc("Bar_g_axe30_2", Bar_g_axe30_FX)
	pers.AddAnmEventFunc("Bar_g_axe30_3", Bar_g_axe30_FX)
	pers.AddAnmEventFunc("Bar_g_axe30_4", Bar_g_axe30_FX)

	pers.AddAnmEventFunc("Bar_g2h_28_1", Bar_g2h_28_FX)

	pers.AddAnmEventFunc("Bar_g2h_b29_1", Bar_g2h_b29_FX)

	pers.AddAnmEventFunc("Bar_g_axe12_1", Bar_g_axe12_FX)

	pers.AddAnmEventFunc("Bar_g_axe32_1", Bar_g_axe32_FX)

	pers.AddAnmEventFunc("Bar_g2h_21_7_1", Bar_g2h_21_7_FX)
	pers.AddAnmEventFunc("Bar_g2h_21_7_2", Bar_g2h_21_7_FX)

	pers.AddAnmEventFunc("Bar_g2h_earthpow_1", Bar_g2h_earthpow_FX)
	pers.AddAnmEventFunc("Bar_g2h_earthpow_2", Bar_g2h_earthpow_FX)

	pers.AddAnmEventFunc("Bar_g2h_21_2_1", Bar_g2h_21_2_FX)
	pers.AddAnmEventFunc("Bar_g2h_21_2_2", Bar_g2h_21_2_FX)

	pers.AddAnmEventFunc("Bar_g_magic_1", Bar_g_magic_FX)
	pers.AddAnmEventFunc("Bar_g_magic_2", Bar_g_magic_FX)
	pers.AddAnmEventFunc("Bar_g_magic_3", Bar_g_magic_FX)
	pers.AddAnmEventFunc("Bar_g_magic_4", Bar_g_magic_FX)
	pers.AddAnmEventFunc("Bar_g_magic_5", Bar_g_magic_FX)

	pers.AddAnmEventFunc("Bar_g_magic2_1", Bar_g_magic2_FX)
	pers.AddAnmEventFunc("Bar_g_magic2_2", Bar_g_magic2_FX)
	pers.AddAnmEventFunc("Bar_g_magic2_3", Bar_g_magic2_FX)


def DwfCombosFX(pers_name):
	if netgame.GetNetState() == 1:
		return
	pers=Bladex.GetEntity(pers_name)
	pers.AddAnmEventFunc("Dwf_g_14_1", Dwf_g_14_FX)

	pers.AddAnmEventFunc("Dwf_g_15_1", Dwf_g_15_FX)

	pers.AddAnmEventFunc("Dwf_g_07_1", Dwf_g_07_FX)

	pers.AddAnmEventFunc("Dwf_g_11_1", Dwf_g_11_FX)

	pers.AddAnmEventFunc("Dwf_g_16_1", Dwf_g_16_FX)

	pers.AddAnmEventFunc("Dwf_g_05_1", Dwf_g_05_FX)

	pers.AddAnmEventFunc("Dwf_g_12_1", Dwf_g_12_FX)

	pers.AddAnmEventFunc("Dwf_g_18_1", Dwf_g_18_FX)

	pers.AddAnmEventFunc("Dwf_g_13_1", Dwf_g_13_FX)

	pers.AddAnmEventFunc("Dwf_g_21_1", Dwf_g_21_FX)

	pers.AddAnmEventFunc("Dwf_g_s3_new_1", Dwf_g_s3_new_FX)

	pers.AddAnmEventFunc("Dwf_g_17_1", Dwf_g_17_FX)

	pers.AddAnmEventFunc("Dwf_g_31_1", Dwf_g_31_FX)
	pers.AddAnmEventFunc("Dwf_g_31_2", Dwf_g_31_FX)

	pers.AddAnmEventFunc("Dwf_g_magic_1", Dwf_g_magic_FX)
	pers.AddAnmEventFunc("Dwf_g_magic_2", Dwf_g_magic_FX)
	pers.AddAnmEventFunc("Dwf_g_magic_3", Dwf_g_magic_FX)
	pers.AddAnmEventFunc("Dwf_g_magic_4", Dwf_g_magic_FX)
	pers.AddAnmEventFunc("Dwf_g_magic_5", Dwf_g_magic_FX)

	pers.AddAnmEventFunc("Dwf_g_magic2_1", Dwf_g_magic2_FX)
	pers.AddAnmEventFunc("Dwf_g_magic2_2", Dwf_g_magic2_FX)
	pers.AddAnmEventFunc("Dwf_g_magic2_3", Dwf_g_magic2_FX)

    # Added
	pers.AddAnmEventFunc("Dwf_g_s22low_new_1", Dwf_g_s22low_new_FX)

	pers.AddAnmEventFunc("Dwf_g_s18_2h_1", Dwf_g_s18_2h_FX)
	pers.AddAnmEventFunc("Dwf_g_s18_2h_2", Dwf_g_s18_2h_FX)

	pers.AddAnmEventFunc("Dwf_g_22_1", Dwf_g_22_FX)
	pers.AddAnmEventFunc("Dwf_g_22_2", Dwf_g_22_FX)
	pers.AddAnmEventFunc("Dwf_g_22_3", Dwf_g_22_FX)
