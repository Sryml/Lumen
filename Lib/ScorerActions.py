
import Actions
import Enm_Def
import Reference
import pdb
import Bladex




#
#
#



def IncCallBack():
  Reference.debugprint ("IncCallBack: Hola")


############

def InvChangeLeft(EntityName):
  me=Bladex.GetEntity(EntityName)
  if me.ActiveEnemy:
      me.AddAnmEventFunc("ChangeLEvent",ChangeLEventHandler)
      if me.Wuea==Reference.WUEA_WAIT:
          me.Wuea= Reference.WUEA_ENDED
      me.LaunchAnmType("Attack_Chg_l")
  else:
      me.AddAnmEventFunc("ChangeLEvent",ChangeLEventHandler)
      if me.Wuea==Reference.WUEA_WAIT:
          me.Wuea= Reference.WUEA_ENDED
      me.LaunchAnmType("Chg_l")


#PEPET

def InvChangeRight(EntityName):
  me=Bladex.GetEntity(EntityName)
  
  #des_weapon_name=inv.GetSelectedWeapon()
  #if Reference.GiveWeaponFlag(des_weapon_name)<>Reference.W_FLAG_1H and me.InvLeft<>"":

  if me.ActiveEnemy:
      me.AddAnmEventFunc("ChangeREvent",ChangeREventHandler)
      if me.Wuea==Reference.WUEA_WAIT:
          me.Wuea= Reference.WUEA_ENDED
      me.LaunchAnmType("Attack_Chg_r")
  else:
      me.AddAnmEventFunc("ChangeREvent",ChangeREventHandler)
      if me.Wuea==Reference.WUEA_WAIT:
          me.Wuea= Reference.WUEA_ENDED
      me.LaunchAnmType("Chg_r")


def InvChangeRightLeft(EntityName):
  me=Bladex.GetEntity(EntityName)
  if me.ActiveEnemy:
      me.AddAnmEventFunc("ChangeRLEvent",ChangeRLEventHandler)
      if me.Wuea==Reference.WUEA_WAIT:
          me.Wuea= Reference.WUEA_ENDED
      me.LaunchAnmType("Attack_Chg_r_l")
  else:
      me.AddAnmEventFunc("ChangeRLEvent",ChangeRLEventHandler)
      if me.Wuea==Reference.WUEA_WAIT:
          me.Wuea= Reference.WUEA_ENDED
      me.LaunchAnmType("Chg_r_l")



def ChangeLEventHandler(pj_name,event):
  me=Bladex.GetEntity(pj_name)
  me.DelAnmEventFunc("ChangeLEvent")
  inv=me.GetInventory()
  tmp_lback=me.InvLeftBack
  #print "ChangeLEventHandler"
  des_shield=inv.GetSelectedShield()
  if des_shield:
      if tmp_lback:
          inv.LinkLeftHand("None")
          inv.LinkLeftBack("None")
          inv.LinkLeftHand(des_shield)
      else:
          inv.LinkLeftHand(des_shield)


def ChangeQuiverHandler(pj_name,event):
    me=Bladex.GetEntity(pj_name)
    me.DelAnmEventFunc("ChangeREvent")
    inv=me.GetInventory()
    # Put back the arrow
    des_quiver_name=inv.GetSelectedQuiver()
    if me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:
        Actions.SheatheArrow(inv, me.InvRight)
    
    # Change the quiver
    inv.SetCurrentQuiver(des_quiver_name)
    inv.LinkRightBack("None")
    inv.LinkRightBack(des_quiver_name)
    
    # and get a new arrow, if you are carrying the bow...
    if inv.HoldingBow:
        Actions.UnSheatheArrow(inv)

def DealQuivers(inv):
  if (not inv.HoldingShield) and (not inv.HasShieldOnBack):
      des_weapon_name=inv.GetSelectedWeapon()
      if des_weapon_name:
          des_weapon=Bladex.GetEntity(des_weapon_name)
          if Reference.GiveObjectFlag(des_weapon_name)==Reference.OBJ_BOW:
              return 1
  return 0


def CB_SO_AnmEnd(EntityName):
  me=Bladex.GetEntity(EntityName)
  inv=me.GetInventory()
  deal_quivers= DealQuivers(inv)
  if deal_quivers:
      if inv.GetSelectedQuiver() != inv.GetActiveQuiver():
          me.AddAnmEventFunc("ChangeREvent",ChangeQuiverHandler)
          if me.Wuea==Reference.WUEA_WAIT:
            me.Wuea= Reference.WUEA_ENDED
          me.LaunchAnmType("Chg_r")
  else:
      des_shield=inv.GetSelectedShield()
      if des_shield:
          if des_shield==me.InvLeft:
              return
          if Actions.SthOnBack(EntityName)==1 and me.InvRightBack and not me.InvRight:
              InvChangeRightLeft(EntityName)
          else:
              InvChangeLeft(EntityName)
      else:
          Reference.debugprint("no des_shield")




############

def ChangeRLEventHandler(pj_name,event):    
    me=Bladex.GetEntity(pj_name)        
    me.DelAnmEventFunc("ChangeRLEvent")
    inv=me.GetInventory()
    des_weapon_name=inv.GetSelectedWeapon()
    if des_weapon_name: des_weapon=Bladex.GetEntity(des_weapon_name)
    if (me.InvLeft and Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW) or (me.InvLeftBack and Reference.GiveObjectFlag(me.InvLeftBack)==Reference.OBJ_BOW):
        if me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:
            Actions.SheatheArrow(inv, me.InvRight)
    
    if des_weapon_name:
        inv.LinkBack("None")
    
    if des_weapon_name and Reference.GiveObjectFlag(des_weapon_name)==Reference.OBJ_BOW:
        if Actions.StatL(me.Name) == Actions.LA_SHIELD:
            inv.LinkBack("None")
        inv.LinkLeftHand("None")
        inv.LinkLeftHand(des_weapon_name)
        Actions.UnSheatheArrow(inv)
    else:
        tmp_r_flag=Reference.W_FLAG_1H
        if des_weapon_name:
            tmp_r_flag=Reference.GiveWeaponFlag(des_weapon_name)

        if tmp_r_flag<>Reference.W_FLAG_1H:
            inv.LinkLeftHand("None")
            inv.LinkRightHand(des_weapon_name)
            return
        else:
            curr_left_name=inv.GetSelectedShield() 
            if curr_left_name:
                inv.LinkLeftHand(curr_left_name)
            else:
                inv.LinkLeftHand("None")
            if des_weapon_name:
                inv.LinkRightHand(des_weapon_name)
            else:
                inv.LinkRightHand("None")



def ChangeREventHandler(pj_name,event):
    me=Bladex.GetEntity(pj_name)
    me.DelAnmEventFunc("ChangeREvent")
    inv=me.GetInventory()
    tmp_rback=me.InvRightBack
    des_weapon_name=inv.GetSelectedWeapon()
    if des_weapon_name:
        des_weapon=Bladex.GetEntity(des_weapon_name)
        if tmp_rback:
            inv.LinkRightBack("None")
        if Reference.GiveObjectFlag(des_weapon_name)==Reference.OBJ_BOW:
            inv.LinkLeftHand(des_weapon_name)
            des_quiver_name=inv.GetSelectedQuiver()
            if des_quiver_name:
                inv.LinkRightHand(des_quiver_name)
            else:
                inv.LinkRightHand("None")
        else:
            inv.LinkRightHand(des_weapon_name)
    inv.LinkBack("None")



def CB_ShieldOutX(EntityName,cycle):
    me=Bladex.GetEntity(EntityName)
    if me.Wuea==Reference.WUEA_WAIT:
        return

    if me.Life <= 0:
        print "dth x2 fixed!"
        return

    
    tmp_r_flag=Reference.W_FLAG_1H
    if me.InvRight:
        tmp_r_flag=Reference.GiveWeaponFlag(me.InvRight)
    
    if tmp_r_flag==Reference.W_FLAG_2W or tmp_r_flag==Reference.W_FLAG_AXE or tmp_r_flag==Reference.W_FLAG_SP:
        return 
    
    inv=me.GetInventory()
    deal_quiver= DealQuivers(inv)
    
    if cycle :
        if deal_quiver:
            inv.CycleQuivers()
        else:
            inv.CycleShields()
    
    if deal_quiver:
        des_quiver=inv.GetSelectedQuiver() 
        if not des_quiver:
            return	
        CB_SO_AnmEnd(EntityName)
    else:
        des_shield=inv.GetSelectedShield()
        if not des_shield:
            return
        
        if Actions.StatL(me.Name) <> Actions.LA_NO_WEAPON and Actions.StatL(me.Name) <> Actions.LA_SHIELD:
            object= Bladex.GetEntity(me.InvLeft)
            if Actions.StatL(me.Name) <> Actions.LA_NO_WEAPON:
                if Actions.TryDropLeft(EntityName):
                    Reference.debugprint("CB_ShieldOut. I can	drop it")
                    me.AnmEndedFunc=CB_SO_AnmEnd
        else:
            CB_SO_AnmEnd(EntityName)



def CB_ShieldOut(): 
    CB_ShieldOutX("Player1",0)

############



def CB_WO_AnmEnd(EntityName):
  me=Bladex.GetEntity(EntityName)
  inv=me.GetInventory()
  des_weapon_name=inv.GetSelectedWeapon()
  left_bow=0
  curr_left_name=me.InvLeft
  if curr_left_name:
      curr_left=Bladex.GetEntity(curr_left_name)
      if Reference.GiveObjectFlag(curr_left_name)==Reference.OBJ_BOW:
        left_bow=1
  if des_weapon_name:
      des_weapon=Bladex.GetEntity(des_weapon_name)
      if Reference.GiveObjectFlag(des_weapon_name)==Reference.OBJ_BOW or left_bow:
        if des_weapon_name==me.InvLeft:
            return
        Actions.UnGraspString (EntityName,"UnGraspString")
        InvChangeRightLeft(EntityName)
      else:
        if des_weapon_name==me.InvRight:
            return
        if Actions.SthOnBack(EntityName)==1 and me.InvLeftBack:
            InvChangeRightLeft(EntityName)
        else:
            if Reference.GiveWeaponFlag(des_weapon_name)<>Reference.W_FLAG_1H and me.InvLeft<>"":
                InvChangeRightLeft(EntityName)
            else:
                InvChangeRight(EntityName)
  else:
      Reference.debugprint("no des_weapon")


def CB_WeaponOutX(EntityName,cycle=0):
  me=Bladex.GetEntity(EntityName)  

  if me.Wuea==Reference.WUEA_WAIT:
      Reference.debugprint("Wait is on . Returning...")
      return 0

  if me.Life <= 0:
      print "dth x2 fixed!"
      return 0


  inv=me.GetInventory()
  if cycle :
      inv.CycleWeapons()
      
  des_w=inv.GetSelectedWeapon()
  if not des_w:
      return 1
  
  curr_right_name=me.InvRight
  if des_w==curr_right_name:
      return 1

  #Do I	have to	drop it	?  
  if Actions.IsRightHandStandardObject(EntityName):
      if Actions.TryDropRight(EntityName):
          Actions.DropReleaseEventHandler(EntityName, "DropRightEvent")
          #maybe that didn't work, report the problem
          if me.InvRight:
              Actions.ReportMsg ("Cannot be dropped")
              return
          CB_WO_AnmEnd(EntityName)
  else:
      CB_WO_AnmEnd(EntityName)
  return 1
  
def CB_WeaponOut():
  CB_WeaponOutX("Player1",0)
#
#
#