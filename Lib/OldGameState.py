


import Bladex
import BBLib
import time
import types
import cPickle
import marshal
import os
import shutil
import string
import GameStateAux

DefaultValues={}


##cPickle.persistent_id=GameStateAux.persistent_id
##cPickle.persistent_load=GameStateAux.persistent_load


DefaultValues["SendSectorMsgs"]=0
DefaultValues["SendTriggerSectorMsgs"]=0
DefaultValues["FiresIntensity"]=[]
DefaultValues["Lights"]=[]
DefaultValues["CanUse"]=0
DefaultValues["AngVel"]=0.0
DefaultValues["FlickPeriod"]=1.0
DefaultValues["SizeFactor"]=1.0
DefaultValues["Flick"]=1
DefaultValues["RasterModeZ"]="Full"
DefaultValues["FireParticleType"]=None
DefaultValues["RasterModeAlpha"]="BlendingAlpha"
DefaultValues["Alpha"]=1.0
DefaultValues["Scale"]=1.0
DefaultValues["Velocity"]=(0.0, 0.0, 0.0)
DefaultValues["Slash"]=0.0
DefaultValues["Gravity"]=(0.0, 9800.0, 0.0)
DefaultValues["ContinuousDamage"]=0
DefaultValues["TestHit"]=1
DefaultValues["AngularVelocity"]=(0.0, 0.0, 0.0)
DefaultValues["CastShadows"]=1
DefaultValues["Orientation"]=(1.0, 0.0, 0.0, 0.0)
DefaultValues["MaxAmplitude"]=400.0
DefaultValues["MinSectorLength"]=1000000.0
DefaultValues["UseFunc"]=None
DefaultValues["SubscribedLists"]=[]
DefaultValues["InternalState"]=None
DefaultValues["CombatGroup"]=None
#DefaultValues["BlockingPropensity"]=0.0
DefaultValues["Wuea"]=0.0
DefaultValues["PartialLevel"]=0
DefaultValues["Sneak"]=0
DefaultValues["Run"]=0
DefaultValues["Blind"]=0
DefaultValues["GoToSneaking"]=0
DefaultValues["Tl"]=0
DefaultValues["Aim"]=0
DefaultValues["Gob"]=0
DefaultValues["Tr"]=0
DefaultValues["Gof"]=0
DefaultValues["ContinuousBlock"]=0
DefaultValues["TrailMode"]=0
DefaultValues["WeaponMode"]=0
DefaultValues["StaticWeaponMode"]=0
DefaultValues["ExclusionMask"]=-1
DefaultValues["ObjectName"]=None
DefaultValues["PersonNodeName"]=None
DefaultValues["PersonName"]=None

##NotSave=["Entity Sound","Entity Person"]
#NotSave=["Entity Sound"]
NotSave=[]




def SavePickDataAux(file,aux_dir,data,assign):
    if type(data)==types.MethodType:
        print "SavePickDataAux() -> Skipping method"
        return

    if(data):
        try:
##            if data.has_key(ObjId):
            if GameStateAux.LoadedPickledData.has_key(data.ObjId):
##                print "SavePickDataAux() -> Found ",data.ObjId,"in GameStateAux.LoadedPickledData"
                return
        except:
            pass

        filename="%s/%s.dat"%(aux_dir,id(data))
        if os.path.exists(filename):
##            print "SavePickDataAux() -> Found",filename,"for object",data
            return

##        print "SavePickDataAux() -> Saving",data,"in",filename
        funcfile=open(filename,"wt")
        p=cPickle.Pickler(funcfile)
        p.persistent_id=GameStateAux.persistent_id
        p.dump(data)
        funcfile.close()

        restorestring='GameStateAux.GetPickledData("%s")'%(filename,)
        file.write(assign%(restorestring,))


def SavePickledObjects(file,aux_dir):
    import ObjStore
    filename="%s/%s.dat"%(aux_dir,"DinObjs")

##    print "SavePickledObjects() -> Saving in",filename
    funcfile=open(filename,"wt")
    p=cPickle.Pickler(funcfile)
    p.dump(ObjStore.ObjectsStore)
    funcfile.close()

    file.write('GameStateAux.GetPickledObjects("%s")\n'%(filename,))




class EntityState:
    def __init__(self,entity):
        self.CreationProps={}
        self.Props={}
        self.SpecialProps={}

        self.CreationProps["Name"]=entity.Name
        self.CreationProps["Kind"]=entity.Kind
        self.CreationProps["Position"]=entity.Position
        self.Props["SendSectorMsgs"]=entity.SendSectorMsgs
        self.Props["SendTriggerSectorMsgs"]=entity.SendTriggerSectorMsgs
        self.Props["Mass"]=entity.Mass

        self.SpecialProps["InternalState"]=entity.InternalState

        self.SpecialProps["SubscribedLists"]=entity.SubscribedLists
        self.SpecialProps["CanUse"]=entity.CanUse
        self.SpecialProps["Parent"]=entity.Parent     #Sólo Lectura
        self.SpecialProps["Data"]=entity.Data
        self.SpecialProps["CanUse"]=entity.CanUse

        self.SpecialProps["FrameFunc"]=entity.FrameFunc
        self.SpecialProps["HitFunc"]=entity.HitFunc
        self.SpecialProps["InflictHitFunc"]=entity.InflictHitFunc
        self.SpecialProps["DamageFunc"]=entity.DamageFunc
        self.SpecialProps["TimerFunc"]=entity.TimerFunc
        self.SpecialProps["HearFunc"]=entity.HearFunc
        self.SpecialProps["UseFunc"]=entity.UseFunc
        self.SpecialProps["SeeFunc"]=entity.SeeFunc
        self.SpecialProps["StickFunc"]=entity.StickFunc
        #self.SpecialProps["ChangeNodeFunc"]=entity.ChangeNodeFunc

        # Esta la trato como caso especial.
        self.InWorld=entity.InWorld

    def SaveCreation(self,file,aux_dir):
        file.write('\n\n\n')
        file.write('o=Bladex.CreateEntity("%s","%s",%f,%f,%f)\n' %
                    (self.CreationProps["Name"],
                     self.CreationProps["Kind"],
                     self.CreationProps["Position"][0],
                     self.CreationProps["Position"][1],
                     self.CreationProps["Position"][2]
                    )
                  )


    def SaveProperties(self,file,aux_dir):
        SpecialNames=self.SpecialProps.keys()
        for i in self.Props.keys():
            if i not in SpecialNames:
                value=self.Props[i]
                if not (DefaultValues.has_key(i) and DefaultValues[i]==value):
                    if type(value) is types.StringType:
                        file.write('o.%s="%s"\n'%(i,value))
                    else:
                        file.write('o.%s=%s\n'%(i,value))
        if not self.InWorld:
            file.write('o.RemoveFromWorld()\n')
        file.write('\n')


##    def __SaveCallbackFunction(self,filename,function):
##        funcfile=open(filename,"wt")
##        p=cPickle.Pickler(funcfile)
##        p.dump(function)
##        funcfile.close()
##        print "Saving Function for ",self.CreationProps["Name"],"in",funcfile

    def SaveSpecialProperties(self,file,aux_dir):
        name=self.CreationProps["Name"]

        funcs=( ("UseFunc","usefnc"),
                ("FrameFunc","frmfnc"),
                ("HitFunc","hitfnc"),
                ("InflictHitFunc","ihitfnc"),
                ("DamageFunc","dmgfnc"),
                ("TimerFunc","tmrfnc"),
                ("HearFunc","hearfnc"),
                ("SeeFunc","seefnc"),
                ("StickFunc","stkfnc")
              )

        for i in funcs:
            curr_func=self.SpecialProps[i[0]]
            f_rest_string="o.%s="%(i[0])
            SavePickDataAux(file,aux_dir,curr_func,f_rest_string+'%s\n')

        if self.SpecialProps["SubscribedLists"]:
            file.write('GameStateAux.SetSubscribedLists(o,%s)\n'%self.SpecialProps["SubscribedLists"])

        if self.SpecialProps["InternalState"]:
            value=self.SpecialProps["InternalState"]
            if not (DefaultValues.has_key("InternalState") and DefaultValues["InternalState"]==value):
                if type(value) is types.StringType:
                    file.write('o.InternalState="%s"\n'%(value))
                else:
                   file.write('o.InternalState=%s\n'%(str(value)))
            file.write('\n')

    def SaveState(self,file,aux_dir):
        self.SaveCreation(file,aux_dir)
        self.SaveProperties(file,aux_dir)


    def SaveStatePass2(self,file,aux_dir):
##        print "SaveStatePass2",self.CreationProps["Name"]
        file.write('o=Bladex.GetEntity("%s")\n'%(self.CreationProps["Name"]))
        self.SaveSpecialProperties(file,aux_dir)
        data=self.SpecialProps["Data"]
        SavePickDataAux(file,aux_dir,data,'o.Data=%s\n\n\n\n')


class EntitySpotState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["Flick"]=entity.Flick
        self.Props["Visible"]=entity.Visible
        self.Props["CastShadows"]=entity.CastShadows
        #self.Props["GlowTexture"]=entity.CastShadows #Sólo Escritura
        #self.Props["GlowTestZ"]=entity.CastShadows   #Sólo Escritura
        self.Props["Intensity"]=entity.Intensity
        self.Props["Precission"]=entity.Precission
        self.Props["AngVel"]=entity.AngVel
        self.Props["SizeFactor"]=entity.SizeFactor
        self.Props["Intensity2"]=entity.Intensity2
        self.Props["FlickPeriod"]=entity.FlickPeriod
        self.Props["Color"]=entity.Color


    def SaveCreation(self,file,aux_dir):
        if not self.SpecialProps["Parent"]:
            EntityState.SaveCreation(self,file,aux_dir)
        else:
            parent=Bladex.GetEntity(self.SpecialProps["Parent"])
            if parent.Person:
                EntityState.SaveCreation(self,file,aux_dir)


    def SaveProperties(self,file,aux_dir):
        if not self.SpecialProps["Parent"]:
            EntityState.SaveProperties(self,file,aux_dir)
        else:
            parent=Bladex.GetEntity(self.SpecialProps["Parent"])
            if parent.Person:
                EntityState.SaveProperties(self,file,aux_dir)


class EntityObjectState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        #self.Props["nLights"]=entity.nLights
        #self.Props["LightGlow"]=entity.LightGlow
        self.Props["CastShadows"]=entity.CastShadows
        self.Props["Scale"]=entity.Scale
        self.Props["FiresIntensity"]=entity.FiresIntensity
        self.Props["Lights"]=entity.Lights
        #self.Props["nFires"]=entity.nFires
        #self.Props["Solids"]=entity.Solids
        #self.Props["LightIntensity"]=entity.LightIntensity
        #self.Props["LightPrecission"]=entity.LightPrecission
        #self.Props["LightColor"]=entity.LightColor
        self.Props["Alpha"]=entity.Alpha
        self.Props["FireParticleType"]=entity.FireParticleType
##        self.Props["RasterModeZ"]=entity.RasterModeZ #Chapuza de Jose y Manuel
##        self.Props["RasterModeAlpha"]=entity.RasterModeAlpha #Chapuza de Jose y Manuel
        self.Props["Orientation"]=entity.Orientation        
        self.Props["ExclusionMask"]=entity.ExclusionMask



class EntityPhysicState(EntityObjectState):
    def __init__(self,entity):
        EntityObjectState.__init__(self,entity)
        self.Props["Velocity"]=entity.Velocity
        self.Props["Gravity"]=entity.Gravity
        self.Props["AngularVelocity"]=entity.AngularVelocity
#       self.SpecialProps["OnStopFunc"]=entity.OnStopFunc
##        self.SpecialProps["TestHit"]=entity.TestHit

    def SaveCreation(self,file,aux_dir):
        file.write('\n\n\n')
        try:
            file.write('o=Bladex.CreateEntity("%s","%s",%f,%f,%f,"Physic")\n' %
                    (self.CreationProps["Name"],
                     self.CreationProps["Kind"],
                     self.CreationProps["Position"][0],
                     self.CreationProps["Position"][1],
                     self.CreationProps["Position"][2]
                    )
                  )
        except Exception,exc:
            print "Warning: Saving Physic entity failed"
            print self.CreationProps["Name"],exc

#    def SaveSpecialProperties(self,file,aux_dir):
#        EntityObjectState.SaveSpecialProperties(self,file,aux_dir)
#        SavePickDataAux(file,aux_dir,self.SpecialProps["OnStopFunc"],'o.OnStopFunc=%s\n')
#        SavePickDataAux(file,aux_dir,self.SpecialProps["TestHit"],'o.TestHit=%s\n')


class EntityWeaponState(EntityPhysicState):
    def __init__(self,entity):
        EntityPhysicState.__init__(self,entity)
        self.Props["ContinuousDamage"]=entity.ContinuousDamage
        self.Props["Radius"]=entity.Radius
        self.Props["Height"]=entity.Height
        self.Props["Cone"]=entity.Cone
        self.Props["TrailColor"]=entity.TrailColor
        self.Props["TrailLifeTime"]=entity.TrailLifeTime
        self.Props["TrailMode"]=entity.TrailMode
        self.Props["WeaponMode"]=entity.WeaponMode
        self.Props["StaticWeaponMode"]=entity.StaticWeaponMode

    def SaveCreation(self,file,aux_dir):
        file.write('\n\n\n')
        try:
            file.write('o=Bladex.CreateEntity("%s","%s",%f,%f,%f,"Weapon")\n' %
                    (self.CreationProps["Name"],
                     self.CreationProps["Kind"],
                     self.CreationProps["Position"][0],
                     self.CreationProps["Position"][1],
                     self.CreationProps["Position"][2]
                    )
                  )
        except Exception,exc:
            print "Warning: Saving Weapon entity failed"
            print self.CreationProps["Name"],exc


class EntityActorState(EntityObjectState):
    def __init__(self,entity):
        EntityObjectState.__init__(self,entity)
        self.Props["Frame"]=entity.Frame
        self.Props["Animation"]=entity.Animation
        self.Props["OnAnimationEndFunc"]=entity.OnAnimationEndFunc
        self.Props["OnPathNodeFunc"]=entity.OnPathNodeFunc
        #self.Props["FPS"]=entity.FPS  #Sólo Escritura



class EntityArrowState(EntityWeaponState):
    def __init__(self,entity):
        EntityWeaponState.__init__(self,entity)

    def SaveCreation(self,file,aux_dir):
        file.write('\n\n\n')
        try:
            file.write('o=Bladex.CreateEntity("%s","%s",%f,%f,%f,"Arrow")\n' %
                    (self.CreationProps["Name"],
                     self.CreationProps["Kind"],
                     self.CreationProps["Position"][0],
                     self.CreationProps["Position"][1],
                     self.CreationProps["Position"][2]
                    )
                  )
        except Exception,exc:
            print "Warning: Saving Arrow entity failed"
            print self.CreationProps["Name"],exc



class EntityParticleSystemState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["YGravity"]=entity.YGravity
        self.Props["Friction"]=entity.Friction
        self.Props["Friction"]=entity.Friction
        self.Props["Friction2"]=entity.Friction2
        self.Props["PPS"]=entity.PPS
        self.Props["DeathTime"]=entity.DeathTime
        self.Props["FollowFactor"]=entity.FollowFactor
        self.Props["NormalVelocity"]=entity.NormalVelocity
        self.Props["RandomVelocity"]=entity.RandomVelocity
        self.Props["RandomVelocity_V"]=entity.RandomVelocity_V
        self.Props["Time2Live"]=entity.Time2Live
        self.Props["Time2Live_V"]=entity.Time2Live_V
        self.Props["ParticleType"]=entity.ParticleType
        self.Props["ObjectName"]=entity.ObjectName
        self.Props["PersonNodeName"]=entity.PersonNodeName
        self.Props["PersonName"]=entity.PersonName
        self.Props["Velocity"]=entity.Velocity
        self.Props["D"]=entity.D
        self.Props["D1"]=entity.D1
        self.Props["D2"]=entity.D2




class EntityFireState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["Intensity"]=entity.Intensity
        self.Props["FireParticleType"]=entity.FireParticleType


    def SaveCreation(self,file,aux_dir):
        if not self.SpecialProps["Parent"]:
            EntityState.SaveCreation(self,file,aux_dir)
        else:
            parent=Bladex.GetEntity(self.SpecialProps["Parent"])
            if parent.Person:
                EntityState.SaveCreation(self,file,aux_dir)


    def SaveProperties(self,file,aux_dir):
        if not self.SpecialProps["Parent"]:
            EntityState.SaveProperties(self,file,aux_dir)
        else:
            parent=Bladex.GetEntity(self.SpecialProps["Parent"])
            if parent.Person:
                EntityState.SaveProperties(self,file,aux_dir)





class EntityCameraState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["PViewType"]=entity.PViewType
##        self.Props["Returns"]=entity.Returns
        #self.Props["LookAtTime"]=entity.LookAtTime
        self.Props["Dist"]=entity.Dist
        #self.Props["EarthQuake"]=entity.EarthQuake  # Falta Lectura
        self.Props["EarthQuakeFactor"]=entity.EarthQuakeFactor
        self.Props["TPos"]=entity.TPos
        self.Props["TAng"]=entity.TAng
        self.Props["TType"]=entity.TType
        self.Props["SType"]=entity.SType
        #self.Props["ChangeNodeFunc"]=entity.ChangeNodeFunc #REVISAR

        # La cámara es un caso especial, no la destruyo, pero guardo su estado interno.
    def SaveCreation(self,file,aux_dir):
        file.write('\n\n\n')
        file.write('o=Bladex.GetEntity("Camera")\n')
        file.write('if o is None:\n\to=Bladex.CreateEntity("%s","Entity Camera",%f,%f,%f)' %
                       (self.CreationProps["Name"],
                        self.CreationProps["Position"][0],
                        self.CreationProps["Position"][1],
                        self.CreationProps["Position"][2]
                       )
                   )
        file.write('\n\n\n')





class EntitySlidingAreaState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["SlidingSurface"]=entity.SlidingSurface 
        self.Displacement=entity.Displacement 
        self.SpecialProps["OnStopFunc"]=entity.OnStopFunc

        self.Limit = entity.DisplacementLimit
        self.V_D = entity.V_D
        self.A_D = entity.A_D
        self.IsStopped = entity.IsStopped

    def SaveProperties(self,file,aux_dir):        
        EntityState.SaveProperties(self,file,aux_dir)
        file.write('o.Displacement=%s\n'%( str(self.Displacement)))

    def SaveSpecialProperties(self,file,aux_dir):
        EntityState.SaveSpecialProperties(self,file,aux_dir)
        SavePickDataAux(file,aux_dir,self.SpecialProps["OnStopFunc"],'o.OnStopFunc=%s\n')
        if not self.IsStopped:
            file.write('o.SlideTo(%s,%s,%s)\n'%( str(self.Limit),str(self.V_D),str(self.A_D)))


class EntityWaterState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["Color"]=entity.Color
        self.SpecialProps["TouchFluidFunc"]=entity.TouchFluidFunc
        #self.Props["Reflection"]=entity.Reflection  #Sólo Escritura
        #self.Props["Transparency"]=entity.Transparency  #Sólo Escritura

    def SaveSpecialProperties(self,file,aux_dir):
        EntityState.SaveSpecialProperties(self,file,aux_dir)
        SavePickDataAux(file,aux_dir,self.SpecialProps["TouchFluidFunc"],'o.TouchFluidFunc=%s\n')



class EntitySoundState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["SendNotify"]=entity.SendNotify
        self.Props["MinDistance"]=entity.MinDistance
        self.Props["MaxDistance"]=entity.MaxDistance
        self.Props["Volume"]=entity.Volume
        self.Props["BaseVolume"]=entity.BaseVolume

    def SaveCreation(self,file,aux_dir):
        EntityState.SaveCreation(self,file,aux_dir)
        file.write('o.SetObjectSound("%s")\n'%self.CreationProps["Name"])

class EntityMagicMissileState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["Flick"]=entity.Flick
        self.Props["CastShadows"]=entity.CastShadows
        self.Props["Intensity"]=entity.Intensity
        self.Props["Precission"]=entity.Precission
        self.Props["Intensity2"]=entity.Intensity2
        self.Props["Color"]=entity.Color


class EntityElectricBoltState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["Active"]=entity.Active
        self.Props["Damage"]=entity.Damage
        self.Props["MinSectorLength"]=entity.MinSectorLength
        self.Props["MaxAmplitude"]=entity.MaxAmplitude
        self.Props["Target"]=entity.Target
        self.Props["OuterGlowColor"]=entity.OuterGlowColor
        self.Props["InnerGlowColor"]=entity.InnerGlowColor
        self.Props["CoreGlowColor"]=entity.CoreGlowColor


class EntityPoolState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["DeepColor"]=entity.DeepColor
        self.Props["Color"]=entity.Color




class EntityParticleState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["ObjCTest"]=entity.ObjCTest
        self.Props["Friction"]=entity.Friction
        self.Props["Friction2"]=entity.Friction2
        self.Props["DeathTime"]=entity.DeathTime
        self.Props["Velocity"]=entity.Velocity
        self.Props["Gravity"]=entity.Gravity





class EntityDecalState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["Alpha"]=entity.Alpha
        self.Props["ZoomS"]=entity.ZoomS
        self.Props["ZoomT"]=entity.ZoomT
        self.Props["OriginS"]=entity.OriginS
        self.Props["OriginT"]=entity.OriginT
        self.Props["Angle"]=entity.Angle
        self.Props["BlendMode"]=entity.BlendMode
        self.Props["Texture"]=entity.Texture
        self.Props["Color"]=entity.Color




class EntityLavaState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Props["TextureName"]=entity.TextureName
        self.Props["Zoom"]=entity.Zoom
        self.SpecialProps["TouchFluidFunc"]=entity.TouchFluidFunc

    def SaveSpecialProperties(self,file,aux_dir):
        EntityState.SaveSpecialProperties(self,file,aux_dir)
        SavePickDataAux(file,aux_dir,self.SpecialProps["TouchFluidFunc"],'o.TouchFluidFunc=%s\n')



class EntityBipedState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        #self.Props["LastSound"]=entity.LastSound #Solo lectura
        #self.Props["LastSoundPosition"]=entity.LastSoundPosition #Solo lectura






class EntityPersonState(EntityBipedState):
    def __init__(self,entity):
        EntityBipedState.__init__(self,entity)
        self.Props["CombatDistFlag"]=entity.CombatDistFlag
        #self.Props["Mask"]=entity.Mask
        #self.Props["MutilationsMask"]=entity.MutilationsMask #Sólo Escritura
        #self.Props["EnemyARange"]=entity.EnemyARange
        self.Props["Level"]=entity.Level
        self.Props["Gof"]=entity.Gof
        self.Props["Gob"]=entity.Gob
        self.Props["Aim"]=entity.Aim
        self.Props["Tr"]=entity.Tr
        self.Props["Tl"]=entity.Tl
        self.Props["Run"]=entity.Run
        self.Props["Sneak"]=entity.Sneak
        #self.Props["ShortStep"]=entity.ShortStep
        #self.Props["Attack"]=entity.Attack #Solo lectura
        #self.Props["Block"]=entity.Block #Solo lectura
        self.Props["ContinuousBlock"]=entity.ContinuousBlock
        self.Props["Blind"]=entity.Blind
        self.Props["Deaf"]=entity.Deaf
        self.Props["GoToSneaking"]=entity.GoToSneaking
        self.Props["GoToJogging"]=entity.GoToJogging
        #self.Props["InDestructorAttack"]=entity.InDestructorAttack
        #self.Props["Heard"]=entity.Heard
        #self.Props["Seen"]=entity.Seen
        self.Props["PartialLevel"]=entity.PartialLevel
        self.Props["Angle"]=entity.Angle
        self.Props["Life"]=entity.Life
        self.Props["Energy"]=entity.Energy
        self.Props["Wuea"]=entity.Wuea
        self.Props["BlockingPropensity"]=entity.BlockingPropensity
        #self.Props["LastTimeSeen"]=entity.LastTimeSeen
        self.Props["Alpha"]=entity.Alpha
        #self.Props["Inventory"]=entity.Inventory
        self.Props["CombatGroup"]=entity.CombatGroup
##        self.Props["RasterModeZ"]=entity.RasterModeZ #Chapuza de Jose y Manuel
##        self.Props["RasterModeAlpha"]=entity.RasterModeAlpha #Chapuza de Jose y Manuel
        #self.Props["EnemyLastSeen"]=entity.EnemyLastSeen #Solo lectura
        #self.Props["InitPos"]=entity.InitPos #Solo lectura
        #self.Props["AttackList"]=entity.AttackList
        self.Props["MeshName"]=entity.MeshName
        self.SpecialProps["EnterPrimaryAAFunc"]=entity.EnterPrimaryAAFunc
        self.SpecialProps["EnterSecondaryAAFunc"]=entity.EnterSecondaryAAFunc
        self.SpecialProps["EnterCloseFunc"]=entity.EnterCloseFunc
        self.SpecialProps["EnterLargeFunc"]=entity.EnterLargeFunc
        self.SpecialProps["AnmEndedFunc"]=entity.AnmEndedFunc
        self.SpecialProps["DelayNoSeenFunc"]=entity.DelayNoSeenFunc
        self.SpecialProps["RouteEndedFunc"]=entity.RouteEndedFunc
        self.SpecialProps["ImHurtFunc"]=entity.ImHurtFunc
        self.SpecialProps["ImDeadFunc"]=entity.ImDeadFunc
        self.SpecialProps["EnemyDeadFunc"]=entity.EnemyDeadFunc
        self.SpecialProps["NoAllowedAreaFunc"]=entity.NoAllowedAreaFunc
        self.SpecialProps["EnemyNoAllowedAreaFunc"]=entity.EnemyNoAllowedAreaFunc
        #self.Props["OnHit"]=entity.OnHit
        self.SpecialProps["CharSeeingEnemyFunc"]=entity.CharSeeingEnemyFunc
        self.SpecialProps["AnmTranFunc"]=entity.AnmTranFunc
        self.SpecialProps["TakeFunc"]=entity.TakeFunc
        self.SpecialProps["ThrowFunc"]=entity.ThrowFunc
        self.SpecialProps["MutilateFunc"]=entity.MutilateFunc
        self.SpecialProps["CombatDistFlag"]=entity.CombatDistFlag

        #self.Props["WillCrashInFloor"]=entity.WillCrashInFloor #Sólo Escritura
        #self.Props["CurrentAreas"]=entity.CurrentAreas #Sólo Escritura
        #self.Props["Will1aaTo2aa"]=entity.Will1aaTo2aa    #Sólo Escritura
        #self.Props["OnFloor"]=entity.OnFloor              #Sólo Escritura
        #self.Props["InCombat"]=entity.InCombat            #Sólo Escritura
        #self.Props["DefenceNeeded"]=entity.DefenceNeeded  #Sólo Escritura
        #self.Props["AstarState"]=entity.AstarState         #Sólo Escritura
        #self.Props["RouteType"]=entity.RouteType           #Sólo Escritura
        #self.Props["BayRoute"]=entity.BayRoute             #Sólo Escritura
        #self.Props["CharType"]=entity.CharType             #Sólo Escritura
        #self.Props["CharTypeExt"]=entity.CharTypeExt       #Sólo Escritura
        #self.Props["AnimFullName"]=entity.AnimFullName     #Sólo Escritura
        #self.Props["AnimName"]=entity.AnimName             #Sólo Escritura
        #self.Props["InvRightBack"]=entity.InvRightBack     #Sólo Lectura
        #self.Props["InvLeftBack"]=entity.InvLeftBack       #Sólo Lectura
        #self.Props["ActiveEnemy"]=entity.ActiveEnemy       #Sólo Escritura
        #self.Props["InvRight"]=entity.InvRight             #Sólo Lectura
        #self.Props["InvLeft"]=entity.InvLeft               #Sólo Lectura
        #self.Props["InvLeft2"]=entity.InvLeft2             #Sólo Lectura
        #self.Props["Dist2Floor"]=entity.Dist2Floor          #Sólo Escritura

        self.InitInventory(entity)


    def SaveSpecialProperties(self,file,aux_dir):
##        EntityState.SaveSpecialProperties(self,file,aux_dir)
        name=self.CreationProps["Name"]
        # Es lo mismo que el general excepto las funciones
        if self.SpecialProps["SubscribedLists"]:
            file.write('GameStateAux.SetSubscribedLists(o,%s)\n'%self.SpecialProps["SubscribedLists"])

        if self.SpecialProps["InternalState"]:
            value=self.SpecialProps["InternalState"]
            if not (DefaultValues.has_key("InternalState") and DefaultValues["InternalState"]==value):
                if type(value) is types.StringType:
                    file.write('o.InternalState="%s"\n'%(value))
                else:
                   file.write('o.InternalState=%s\n'%(str(value)))
            file.write('\n')

        if not self.InWorld:
            file.write('darfuncs.HideBadGuy("%s")\n'%(self.CreationProps["Name"],))
        file.write('\n\n')

    def InitInventory(self,entity):
        inv=entity.GetInventory()
        self.Inventory={}
        self.Inventory["Objects"]=[]
        for i in range(inv.nObjects):
            self.Inventory["Objects"].append(inv.GetObject(i))

        self.Inventory["Weapons"]=[]
        for i in range(inv.nWeapons):
            self.Inventory["Weapons"].append(inv.GetWeapon(i))

        self.Inventory["Shields"]=[]
        for i in range(inv.nShields):
            self.Inventory["Shields"].append(inv.GetShield(i))

        self.Inventory["Quivers"]=[]
        for i in range(inv.nQuivers):
            self.Inventory["Quivers"].append(inv.GetQuiver(i))

        self.Inventory["Keys"]=[]
        for i in range(inv.nKeys):
            self.Inventory["Keys"].append(inv.GetKey(i))

        self.Inventory["SpecialKeys"]=[]
        for i in range(inv.nSpecialKeys):
            self.Inventory["SpecialKeys"].append(inv.GetSpecialKey(i))

        self.Inventory["Tablets"]=[]
        for i in range(inv.nTablets):
            self.Inventory["Tablets"].append(inv.GetTablet(i))

        self.Inventory["InvLeft"]=entity.InvLeft
        self.Inventory["InvLeft2"]=entity.InvLeft2
        self.Inventory["InvRight"]=entity.InvRight
        self.Inventory["InvLeftBack"]=entity.InvLeftBack
        self.Inventory["InvRightBack"]=entity.InvRightBack



    def SaveStatePass2(self,file,aux_dir):
        #print "begin PersonEntity.SaveStatePass2() "
        EntityBipedState.SaveStatePass2(self,file,aux_dir)

        file.write('\no=Bladex.GetEntity("%s")\n'%(self.CreationProps["Name"]))
        file.write('inv=o.GetInventory()\n')
        for i in self.Inventory["Objects"]:
            #inv.AddObject(i)
            file.write('inv.AddObject("%s")\n'%(i,))

        for i in self.Inventory["Weapons"]:
            file.write('GameStateAux.AddWeaponToInventory(inv,"%s")\n'%(i,))

        for i in self.Inventory["Shields"]:
            #inv.AddShield(i)
            #Breakings.SetBreakableWS(i)
            file.write('inv.AddShield("%s")\n'%(i,))
            real_ent=Bladex.GetEntity(i)
            try:
                a=real_ent.Data.brkobjdata
                file.write('Breakings.SetBreakableWS("%s")\n'%(i,))
                #print weapon_name,"is breakable."
            except:
                pass

        for i in self.Inventory["Quivers"]:
            #obj=CreateEntAux(i,"Weapon")
            #ItemTypes.ItemDefaultFuncs(obj)
            #inv.AddQuiver(i)
            file.write('GameStateAux.AddQuiverToInventory(inv,"%s")\n'%(i,))

        for i in self.Inventory["Keys"]:
            #inv.AddKey(i)
            file.write('inv.AddKey("%s")\n'%(i,))

        for i in self.Inventory["SpecialKeys"]:
            #inv.AddSpecialKey(i)
            file.write('inv.AddSpecialKey("%s")\n'%(i,))

        for i in self.Inventory["Tablets"]:
            #inv.AddTablet(i)
            file.write('inv.AddTablet("%s")\n'%(i,))

        if self.Inventory["InvLeft"]:
            #inv.LinkLeftHand(Inventory["InvLeft"])
            file.write('inv.LinkLeftHand("%s")\n'%(self.Inventory["InvLeft"],))
            # SetBreakable?

        if self.Inventory["InvLeft2"]:
            #inv.LinkLeftHand2(Inventory["InvLeft2"])
            file.write('inv.LinkLeftHand2("%s")\n'%(self.Inventory["InvLeft2"],))
            # SetBreakable?

        if self.Inventory["InvRight"]:
            #inv.LinkRightHand(Inventory["InvRight"])
            file.write('inv.LinkRightHand("%s")\n'%(self.Inventory["InvRight"],))
            # SetBreakable?

        if self.Inventory["InvRightBack"]:
            #inv.LinkBack(Inventory["InvRightBack"])
            file.write('inv.LinkBack("%s")\n'%(self.Inventory["InvRightBack"],))
            # SetBreakable?

        if self.Inventory["InvLeftBack"]:
            #inv.LinkBack(Inventory["InvLeftBack"])
            file.write('inv.LinkBack("%s")\n'%(self.Inventory["InvLeftBack"],))
            # SetBreakable?
            
            
        #print "end PersonEntity.SaveStatePass2() "



    def SaveCreation(self,file,aux_dir):
        file.write('\n\n\n')
        try:
            file.write('o=Bladex.CreateEntity("%s","%s",%f,%f,%f,"Person")\n' %
                    (self.CreationProps["Name"],
                     self.CreationProps["Kind"],
                     self.CreationProps["Position"][0],
                     self.CreationProps["Position"][1],
                     self.CreationProps["Position"][2]
                    )
                  )
        except Exception,exc:
            print "Warning: Saving Person entity failed"
            print self.CreationProps["Name"],exc



class EntitiesStateAux:
    def __init__(self,EntClass):
        self.EntClass=EntClass
        self.Entities=[]

    def AddEntityState(self,entity):
        self.Entities.append(self.EntClass(entity))

    def SaveStates(self,file,aux_dir):
        file.write('# There are %d entities\n\n'%(len(self.Entities),))
        for i in self.Entities:
            i.SaveState(file,aux_dir)

    def SaveStatesPass2(self,file,aux_dir):
        for i in self.Entities:
            i.SaveStatePass2(file,aux_dir)

    def DestroyEntities(self):
        for i in self.Entities:
            if i.CreationProps["Name"]!="Camera":
                realent=Bladex.GetEntity(i.CreationProps["Name"])
                realent.SubscribeToList("Pin")
        self.Entities=[]




##class PersonEntitiesStateAux:
##    def DestroyEntities(self):
##        for i in self.Entities:
##            realent=Bladex.GetEntity(i.CreationProps["Name"])
##            inv=realent.GetInventory()
##            realent.SubscribeToList("Pin")
##        self.Entities=[]



class EntitiesState:
    def __init__(self):
        self.State={}
        #self.State["Entity"]=EntitiesStateAux(EntityState)
        self.State["Entity Object"]=EntitiesStateAux(EntityObjectState)
        self.State["Entity PhysicObject"]=EntitiesStateAux(EntityPhysicState)
        self.State["Entity Weapon"]=EntitiesStateAux(EntityWeaponState)
        self.State["Entity Arrow"]=EntitiesStateAux(EntityArrowState)
        self.State["Entity Actor"]=EntitiesStateAux(EntityActorState)
        self.State["Entity Biped"]=EntitiesStateAux(EntityBipedState)
        self.State["Entity Person"]=EntitiesStateAux(EntityPersonState)
        self.State["Entity Spot"]=EntitiesStateAux(EntitySpotState)
        self.State["Entity PrtclSys"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System D1"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System D2"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System D3"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System Dobj"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System Dperson"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Fire"]=EntitiesStateAux(EntityFireState)
        #self.State["Entity Dynamic Fire"]=EntitiesStateAux(EntityDynamicFireState)
        self.State["Entity Camera"]=EntitiesStateAux(EntityCameraState)
        self.State["Entity Water"]=EntitiesStateAux(EntityWaterState)
        #self.State["Entity Trail"]=EntitiesStateAux(EntityTrailState)
        self.State["Entity Sound"]=EntitiesStateAux(EntitySoundState)
        self.State["Entity Magic Missile"]=EntitiesStateAux(EntityMagicMissileState)
        self.State["Entity ElectricBolt"]=EntitiesStateAux(EntityElectricBoltState)
        self.State["Entity Pool"]=EntitiesStateAux(EntityPoolState)
        self.State["Entity Particle"]=EntitiesStateAux(EntityParticleState)
        self.State["Entity Decal"]=EntitiesStateAux(EntityDecalState)
        self.State["Entity Lava"]=EntitiesStateAux(EntityLavaState)
        self.State["Entity Sliding Area"]=EntitiesStateAux(EntitySlidingAreaState)
        #self.State["Sparks"]=EntitiesStateAux(EntityObjectState)
        #self.State["Clients"]=EntitiesStateAux(EntityObjectState)
        #self.State["Auras"]=EntitiesStateAux(EntityObjectState)

    def GetState(self):
        for i in range(Bladex.nEntities()):
            entity=Bladex.GetEntity(i)
            kind=entity.Kind
            state=None

            if kind in self.State.keys():
                self.State[kind].AddEntityState(entity)
            else: # Estamos con una entidad con BOD
                if entity.Static:
                    self.State["Entity Object"].AddEntityState(entity)
                elif entity.Person:
                    self.State["Entity Person"].AddEntityState(entity)
                elif entity.Weapon:
                    self.State["Entity Weapon"].AddEntityState(entity)
                elif entity.Arrow:
                    self.State["Entity Arrow"].AddEntityState(entity)
                elif entity.Physic:
                    self.State["Entity PhysicObject"].AddEntityState(entity)
##                elif entity.Actor:
##                    self.State["Entity Actor"].AddEntityState(entity)


    def SaveStatePass1(self,file,aux_dir):
        for i in self.State.keys():
            file.write('############################################################\n')
            file.write('# Entities %s\n'%(i,))
            if i not in NotSave:
                self.State[i].SaveStates(file,aux_dir)
            file.write('\n\n')

    def SaveStatePass2(self,file,aux_dir):
        for i in self.State.keys():
            if i not in NotSave:
                self.State[i].SaveStatesPass2(file,aux_dir)
            file.write('\n\n')


    def DestroyEntities(self):
        for i in self.State.keys():
            if i not in NotSave:
                self.State[i].DestroyEntities()











class MainCharState(EntityPersonState):
    "Clase para grabar el estado del jugador. Temporal"
    def __init__(self,entity):
        if not entity:
            return
        EntityPersonState.__init__(self,entity)
        inv=entity.GetInventory()
        self.Inventory={}
        self.Inventory["Objects"]=[]
        for i in range(inv.nObjects):
            self.Inventory["Objects"].append(self.__GetObjAux(inv.GetObject(i)))

        self.Inventory["Weapons"]=[]
        for i in range(inv.nWeapons):
            self.Inventory["Weapons"].append(self.__GetObjAux(inv.GetWeapon(i)))

        self.Inventory["Shields"]=[]
        for i in range(inv.nShields):
            self.Inventory["Shields"].append(self.__GetObjAux(inv.GetShield(i)))

        self.Inventory["Quivers"]=[]
        for i in range(inv.nQuivers):
            self.Inventory["Quivers"].append(self.__GetObjAux(inv.GetQuiver(i)))

        self.Inventory["Keys"]=[]
        for i in range(inv.nKeys):
            self.Inventory["Keys"].append(self.__GetObjAux(inv.GetKey(i)))

        self.Inventory["SpecialKeys"]=[]
        for i in range(inv.nSpecialKeys):
            self.Inventory["SpecialKeys"].append(self.__GetObjAux(inv.GetSpecialKey(i)))

        self.Inventory["Tablets"]=[]
        for i in range(inv.nTablets):
            self.Inventory["Tablets"].append(self.__GetObjAux(inv.GetTablet(i)))

        self.Inventory["InvLeft"]=self.__GetObjAux(entity.InvLeft)
        self.Inventory["InvLeft2"]=self.__GetObjAux(entity.InvLeft2)
        self.Inventory["InvRight"]=self.__GetObjAux(entity.InvRight)
        self.Inventory["InvLeftBack"]=self.__GetObjAux(entity.InvLeftBack)
        self.Inventory["InvRightBack"]=self.__GetObjAux(entity.InvRightBack)


    def __GetBOD(self,ent_kind):
        RM=BBLib.GetResourceManager()
        for i in range(RM.NResources(BBLib.B_CID_OBJDSCR)):
            if RM.IsResourceLoaded(BBLib.B_CID_OBJDSCR,i):
                if RM.GetResourceName(BBLib.B_CID_OBJDSCR,i)==ent_kind:
                    return RM.GetResourceFile(BBLib.B_CID_OBJDSCR,i)
        return None

    def __GetObjAux(self,obj):
        if not obj:
            return None
        objKind=Bladex.GetEntity(obj).Kind
        return (obj,objKind,self.__GetBOD(objKind))


    def SaveCreation(self,file):
        file.write('\n\n\n')
        file.write('o=Bladex.CreateEntity("%s","%s",%f,%f,%f,"Person")\n' %
                    (self.CreationProps["Name"],
                     self.CreationProps["Kind"],
                     self.CreationProps["Position"][0],
                     self.CreationProps["Position"][1],
                     self.CreationProps["Position"][2]
                    )
                  )


    def SaveInventory(self,file_name):
        f=open('../../Save/'+file_name,'wt')
        p=cPickle.Pickler(f)
        temp={}
        temp["Life"]=self.Props["Life"]
        temp["Level"]=self.Props["Level"]
        temp["PartialLevel"]=self.Props["PartialLevel"]
        
        p.dump((self.CreationProps,temp,self.Inventory))
        f.close()






def CreateEntAux(obj_tuple,obj_kind):
	obj=Bladex.GetEntity(obj_tuple[0])
	if not obj:
			BBLib.ReadBOD(obj_tuple[2])
			obj=Bladex.CreateEntity(obj_tuple[0],obj_tuple[1],0,0,0,obj_kind)
	return obj






def CreateMainCharWithProps(props):
	CreationProps=props[0]
	Props=props[1]
	Inventory=props[2]

	import Basic_Funcs
	import AniSound
	import Reference
	import Breakings
	import ItemTypes

	char=Bladex.CreateEntity("Player1",CreationProps["Kind"],0,0,0,"Person")
	char.Data=Basic_Funcs.PlayerPerson(char)
	inv=char.GetInventory()
	AniSound.AsignarSonidosCaballero('Player1')

	char.Level=Props["Level"]
	char.PartialLevel=Props["PartialLevel"]
	char.Life=Props["Life"]
	char.Energy=Props["Energy"]

	for i in Inventory["Objects"]:
		CreateEntAux(i,"Physic")
		inv.AddObject(i[0])

	for i in Inventory["Weapons"]:
		obj=CreateEntAux(i,"Weapon")
		object_flag=Reference.GiveObjectFlag(i[0])
		if object_flag == Reference.OBJ_BOW:
			inv.AddBow(i[0])
		else:
			flag=Reference.GiveWeaponFlag(i[0])
			#inv.AddWeapon(i[0],flag)
			inv.AddWeapon(i[0])
		Breakings.SetBreakableWS(i[0])

	for i in Inventory["Shields"]:
		CreateEntAux(i,"Weapon")
		inv.AddShield(i[0])
		Breakings.SetBreakableWS(i[0])

	for i in Inventory["Quivers"]:
		obj=CreateEntAux(i,"Weapon")
		ItemTypes.ItemDefaultFuncs(obj)
		inv.AddQuiver(i[0])

	for i in Inventory["Keys"]:
		CreateEntAux(i,"Physic")
		inv.AddKey(i[0])

	for i in Inventory["SpecialKeys"]:
		CreateEntAux(i,"Physic")
		inv.AddSpecialKey(i[0])

	for i in Inventory["Tablets"]:
		CreateEntAux(i,"Physic")
		inv.AddTablet(i[0])

	if Inventory["InvLeft"]:
		CreateEntAux(Inventory["InvLeft"],"Physic")
		inv.LinkLeftHand(Inventory["InvLeft"][0])

	if Inventory["InvLeft2"]:
		CreateEntAux(Inventory["InvLeft2"],"Physic")
		inv.LinkLeftHand2(Inventory["InvLeft2"][0])

	if Inventory["InvRight"]:
		CreateEntAux(Inventory["InvRight"],"Physic")
		inv.LinkRightHand(Inventory["InvRight"][0])

	if Inventory["InvLeftBack"]:
		CreateEntAux(Inventory["InvLeftBack"],"Physic")
		inv.LinkBack(Inventory["InvLeftBack"][0])

	if Inventory["InvRightBack"]:
		CreateEntAux(Inventory["InvRightBack"],"Physic")
		inv.LinkBack(Inventory["InvRightBack"][0])


def RestoreMainCharState(filename):
  f=open('../../Save/'+filename,'rt')
  u=cPickle.Unpickler(f)
  props=u.load()
  CreateMainCharWithProps(props)
  print "Main char created from file",filename
  f.close()

def SaveMainCharState(filename):
  ent=Bladex.GetEntity('Player1')
  ent_state=MainCharState(ent)
  ent_state.SaveInventory(filename)



class SectorState:
    def __init__(self):
        self.Index=-1
        self.OnEnter=None
        self.OnLeave=None
        self.OnHit=None
        self.OnWalkOn=None
        self.OnWalkOut=None
        self.Active=None
        self.ActiveSurface=None
        self.Save=0
        self.BreakInfo=None

    def GetState(self,idx):
        s=Bladex.GetSector(idx)
        if s:
            self.Index=s.Index
            self.OnEnter=s.OnEnter
            self.OnLeave=s.OnLeave
            self.OnHit=s.OnHit
            self.OnWalkOn=s.OnWalkOn
            self.OnWalkOut=s.OnWalkOut
            self.Active=s.Active
            self.ActiveSurface=s.ActiveSurface
            self.BreakInfo=s.BreakInfo
            if s.Active!=1 or s.BreakInfo or s.OnEnter or s.OnLeave or s.OnWalkOn or s.OnWalkOut: #s.OnHit
                self.Save=1

    def SaveState(self,file,aux_dir):
        if(self.Save):
            file.write('s=Bladex.GetSector(%d)\n'%(self.Index))
            self.__SaveCallbackFunction(file,"OnEnter",aux_dir,self.OnEnter)
            self.__SaveCallbackFunction(file,"OnLeave",aux_dir,self.OnLeave)
##            self.__SaveCallbackFunction(file,"OnHit",aux_dir,self.OnHit)
            self.__SaveCallbackFunction(file,"OnWalkOn",aux_dir,self.OnWalkOn)
            self.__SaveCallbackFunction(file,"OnWalkOut",aux_dir,self.OnWalkOut)
            file.write('s.Active=%d\n'%(self.Active))
            if self.BreakInfo:
                file.write('s.BreakInfo=%s\n'%(str(self.BreakInfo)))
##            file.write('s.ActiveSurface=%d'%(self.ActiveSurface))
            file.write('\n\n')


    def __SaveCallbackFunction(self,file,cbname,aux_dir,function):
        r_cb_str='s.%s='%(cbname,)
        SavePickDataAux(file,aux_dir,function,r_cb_str+'%s\n')


class MapState:
    def __init__(self):
        self.SectorsState=[]

    def GetState(self):
        nSectors=Bladex.nSectors()
        for i in range(nSectors):
            s=SectorState()
            s.GetState(i)
            if s.Save:
                self.SectorsState.append(s)

    def SaveState(self,file,aux_dir):
        for i in self.SectorsState:
            i.SaveState(file,aux_dir)


class TriggerSectorState:
    def __init__(self):
        self.Index=-1
        self.OnEnter=None
        self.OnLeave=None
        self.Data=None
        self.Name=None

    def GetState(self,idx):
        self.Name=Bladex.GetTriggerSectorName(idx)
        self.Index=idx
        self.OnEnter=Bladex.GetTriggerSectorFunc(self.Name,"OnEnter")
        self.OnLeave=Bladex.GetTriggerSectorFunc(self.Name,"OnLeave")
        self.Data=Bladex.GetTriggerSectorData(self.Name)

    def SaveState(self,file,aux_dir):

##        self.__SaveCallbackFunction(file,"OnEnter",aux_dir,self.OnEnter)
##        self.__SaveCallbackFunction(file,"OnLeave",aux_dir,self.OnLeave)
##        self.__SavePickledData(file,aux_dir,self.Data)
        SavePickDataAux(file,aux_dir,self.OnEnter,"Bladex.SetTriggerSectorFunc('"+self.Name,"','OnEnter','%s')")
        SavePickDataAux(file,aux_dir,self.OnLeave,"Bladex.SetTriggerSectorFunc('"+self.Name,"','OnLeave','%s')")
        SavePickDataAux(file,aux_dir,self.Data,"Bladex.SetTriggerSectorData('"+self.Name,"','%s')")
        file.write('\n\n')


##    def __SaveCallbackFunction(self,file,cbname,aux_dir,function):
##        if(function):
##            filename="%s/%s.dat"%(aux_dir,id(function))
##            funcfile=open(filename,"wt")
##            p=cPickle.Pickler(funcfile)
##            p.dump(function)
##            funcfile.close()
##
##            file.write('Bladex.SetTriggerSectorFunc("%s","%s",GameStateAux.GetPickledData("%s"))\n'%(self.Name,cbname,filename))
##
##    def __SavePickledData(self,file,aux_dir,data):
##        if(data):
##            filename="%s/%s.dat"%(aux_dir,id(data))
##            funcfile=open(filename,"wt")
##            p=cPickle.Pickler(funcfile)
##            p.dump(data)
##            funcfile.close()
##
##            file.write('Bladex.SetTriggerSectorData("%s",GameStateAux.GetPickledData("%s"))\n'%(self.Name,filename))



class TriggersState:
    def __init__(self):
        self.SectorsState=[]

    def GetState(self):
        nSectors=Bladex.nTriggerSectors()
        for i in range(nSectors):
            s=SectorState()
            s.GetState(i)
            self.SectorsState.append(s)

    def SaveState(self,file,aux_dir):
        for i in self.SectorsState:
            i.SaveState(file,aux_dir)



class WorldState:
    def __init__(self):
        self.EntitiesState=EntitiesState()
        self.MapState=MapState()
        self.TriggersState=TriggersState()
        #print "__name__",__name__

    def GetState(self):
        self.EntitiesState.GetState()
        self.MapState.GetState()

    def SaveState(self,filename):
        import os
        aux_dir=(os.path.splitext(filename)[0])+"_files"
        if os.path.exists(aux_dir):
            shutil.rmtree(aux_dir)
        os.mkdir(aux_dir)

        self.SaveAutoBODs(aux_dir)
##        self.SaveFunctions(aux_dir)


        # Ahora genero el script que al ejecutarse regenera el mundo
        file=open(filename,"wt")
        file.write('############################################################\n')
        file.write('#   Blade Game State %s\n'%(filename,))
        file.write('#   Do not modify\n')
        file.write('#   File created %s \n'%(time.asctime(time.gmtime(time.time())),))
        file.write('############################################################\n\n\n\n')
        file.write('import cPickle\n')
        file.write('import GameStateAux\n')
        file.write('import Breakings\n')
        file.write('import darfuncs\n')
        file.write('import Bladex\n\n\n\n')
        file.write('############################################################\n')
        file.write('#\n\n\n')

        file.write('Bladex.BeginLoadGame()\n')
        file.write('GameStateAux.aux_dir="%s"\n'%(aux_dir,))
        file.write('Bladex.SetCurrentMap(\"%s\")\n'%(Bladex.GetCurrentMap(),))
        file.write('Bladex.SetSaveInfo(%s)\n'%(str(Bladex.GetSaveInfo(),)))

        ResFiles=self.GetMMPFiles()
        file.write('print "About to load MMPs"\n')
        file.write('GameStateAux.LoadMMPs(%s)\n'%(str(ResFiles),))

        ResFiles=self.GetBMPFiles()
        file.write('print "About to load BMPs"\n')
        #file.write('GameStateAux.LoadBMPs(%s)\n'%(str(ResFiles),))
        self.SaveList('GameStateAux.LoadBMPs(%s)\n',ResFiles,file)

        ResFiles=self.GetAlphaBMPFiles()
        file.write('print "About to load Alpha BMPs"\n')
        #file.write('GameStateAux.LoadAlphaBMPs(%s)\n'%(str(ResFiles),))
        self.SaveList('GameStateAux.LoadAlphaBMPs(%s)\n',ResFiles,file)

        file.write('print "About to load Sounds"\n')
        file.write('Bladex.LoadSoundDataBase("%s/Sounds.sdb")\n'%(aux_dir,))
        Bladex.SaveSoundDataBase('%s/Sounds.sdb'%(aux_dir,))

##        ResFiles=self.GetBODFiles()
##        file.write('print "About to load BODs"\n')
##        #file.write('GameStateAux.LoadBODs(%s)\n'%(str(ResFiles),))
##        self.SaveList('GameStateAux.LoadBODs(%s)\n',ResFiles,file)

        file.write('print "About to load AutoBODs"\n')
        file.write('GameStateAux.LoadAutoBODs("%s")\n\n\n'%(aux_dir,))
        file.write('print "End AutoBODs ----------------------------"\n')

##        self.SaveParticleSystems(file)
        psys_data_file=aux_dir+'/psys_data.dat'
        Bladex.SaveParticleSystemsData(psys_data_file)
        file.write('Bladex.LoadParticleSystemsData("%s")\n'%(psys_data_file,))

        self.SaveTimers(file)

        file.write('print "End Timers ----------------------------"\n')
        file.write('import PickInit\n')
        file.write('PickInit.Init()\n\n')
        file.write( 'execfile("../../Scripts/SolidMask.py")\n')
        file.write( 'execfile("../../Scripts/material.py")\n')
        file.write( 'execfile("../../Scripts/anisound.py")\n')
        file.write( 'execfile("../../Scripts/anm_def.py")\n')
        file.write( 'execfile("../../Scripts/StepSounds.py")\n')
        file.write( 'execfile("../../Scripts/enemies.py")\n')
        file.write( 'execfile("../../Scripts/Biped/Biped.py")\n')
        file.write( 'execfile("../../Scripts/anm_conv.py")\n')
        file.write( 'execfile("../../Scripts/anm_mdf.py")\n')
        file.write( 'execfile("../../Scripts/CommonResources.py")\n')
##        file.write( 'execfile("../../Scripts/InitParticleSystems.py")\n')
        file.write( 'execfile("../../Scripts/AutoGenTextures.py")\n')

        file.write('Bladex.LoadWorld(\"%s")\n'%(Bladex.GetWorldFileName(),))

##        file.write( '#\n')
##        file.write( '# Timers\n')
##        file.write( '#\n')
##        file.write( 'Bladex.CreateTimer("Timer60",1.0/60.0)\n')
##        file.write( 'Bladex.CreateTimer("Timer30",1.0/30.0)\n')
##        file.write( 'Bladex.CreateTimer("Timer15",1.0/15.0)\n\n\n\n')


##        self.EntitiesState.SaveStatePass1(file,aux_dir)
        ent_data_file=aux_dir+'/ent_data.dat'
        Bladex.SaveEntitiesData(ent_data_file)
        file.write('Bladex.LoadEntitiesData("%s")\n'%(ent_data_file,))

        import os
        import sys
        file.write('import sys\n')
        file.write('import os\n')
        file.write('sys.path.append("%s")\n\n'%(os.getcwd(),))

##        print os.getcwd()
        file.write('try:\n')
        file.write('  execfile("DefFuncs.py")\n')
        file.write('except IOError:\n')
        file.write('  print "Can´t find DefFuncs.py"\n\n\n')

        file.write('try:\n')
        file.write('  execfile("MusicEvents.py")\n')
        file.write('except IOError:\n')
        file.write('  print "CanÕ´ find MusicEvents.py"\n\n\n')

        file.write('try:\n')
        file.write('  execfile("TextureMaterials.py")\n')
        file.write('except IOError:\n')
        file.write('  print "CanÕ´ find TextureMaterials.py"\n\n\n')

        # Grabar las variables, funciones, ...
        self.SaveModules(file)
        self.SaveVars(file)
        self.SaveSounds(file)
        self.SaveSectors(file)
        self.SaveEntities(file)

        SavePickledObjects(file,aux_dir)

        self.SaveObjects(file,aux_dir)
        file.write( '\n')
        file.write('GameStateAux.InitGameState()\n')


##        import PickInit
##        PickInit.Init()

        self.MapState.SaveState(file,aux_dir)
        self.TriggersState.SaveState(file,aux_dir)
        self.EntitiesState.SaveStatePass2(file,aux_dir)


        file.write( '\n')
        file.write('# Scorer Data init\n')
        file.write('#\n')
        file.write('import Scorer\n')
        file.write('Scorer.ActivateScorer()\n\n')
        file.write('import CharStats\n')
##        file.write('import PowDefWidgets\n')
##        file.write('PowDefWidgets.CreateWidgest()\n')
##        file.write('PowDefWidgets.Activate()\n')
##        file.write('import GameTex\n')
##        file.write('GameText.SetLanguage("Spanish")\n')
        file.write('execfile("../../Scripts/DefaultScorerData.py")\n\n')

        file.write('# Inicio del personaje y sus marcadores\n')
        file.write('char=Bladex.GetEntity("Player1")\n')
        file.write('Scorer.SetLevelLimits(0,CharStats.GetCharExperienceCost(char.CharType,0))\n')
        file.write('#Scorer.SetLevelBarValue(0)\n')
        file.write('#Scorer.SetLevelValue(0)\n')
        file.write('#\n')
        file.write('# Controls ( keyboard,mouse...) stuff\n')
        file.write('#\n')
        file.write('execfile("../../Scripts/InputInit.py")\n')
        file.write('import acts\n')
        file.write('acts.InitBindings("Player1")\n')
        file.write('try:\n')
        file.write('  execfile("../../Scripts/Control.py")\n')
        file.write('  print "BladeInit -> Executed Control.py"\n')
        file.write('except:\n')
        file.write('  execfile("../../Scripts/DefControl.py")\n')
        file.write('  print "BladeInit -> Executed DefControl.py"\n\n')
        file.write('#\n')
        file.write('# Menu\n')
        file.write('#\n')
        file.write('#execfile("../../Scripts/Menu.py")\n')
        file.write('import Menu\n')
        file.write('Menu.InitMenuKeys()\n')        
        file.write('print "About to load global functions"\n')
        file.write('GameStateAux.LoadGlobalFuncs("%s")\n\n\n'%(aux_dir,))
        file.write('Bladex.SetTime(%d)\n'%(Bladex.GetTime(),))
        file.write('Bladex.DoneLoadGame()\n\n\n')
        file.write('#   Good Bye! (Enjoy The Silence)\n')
        file.close()


    def SaveVars(self,file):
        "Saves variables in the global scope."

        global_vars=self.GetGlobalsAux(types.IntType)
        file.write('\n# Integer variables\n')
        for i in global_vars:
            file.write('%s=%s\n'%(str(i[0]),str(i[1])))

        global_vars=self.GetGlobalsAux(types.FloatType)
        file.write('\n# Float variables\n')
        for i in global_vars:
            file.write('%s=%s\n'%(str(i[0]),str(i[1])))

        global_vars=self.GetGlobalsAux(types.StringType)
        file.write('\n# String variables\n')
        for i in global_vars:
            file.write('%s="%s"\n'%(str(i[0]),str(i[1])))


    def SaveSounds(self,file):
        "Saves sound objects in the global scope."

        gmadlig=Bladex.CreateSound('../../sounds/golpe_maderamed.wav', 'GolpeMaderaMediana')
        snd_vars=self.GetGlobalsAux(type(gmadlig))

        file.write('\n# Sound objects\n')
        snd_vars_names=[]
        for i in snd_vars:
            snd_vars_names.append((str(i[0]),i[1].Name))

        for i in snd_vars_names:
            file.write('%s=Bladex.GetSound("%s")\n'%(i[0],i[1]))


    def SaveEntities(self,file):
        "Saves entity objects in the global scope."

        ent=Bladex.GetEntity(0)
        ent_vars=self.GetGlobalsAux(type(ent))

        file.write('\n# Entity objects\n')
        ent_vars_names=[]
        for i in ent_vars:
            ent_vars_names.append((str(i[0]),i[1].Name))

        for i in ent_vars_names:
            file.write('%s=Bladex.GetEntity("%s")\n'%(i[0],i[1]))
        file.write('\n\n')

    def SaveObjects(self,file,aux_dir):
        "Saves objects (from Lib/Object.py) in the global scope."

        import Objects
        obj=Objects.DinObj()
        obj_vars=self.GetGlobalsAux(type(obj))

        file.write('\n# Object objects\n')
        obj_vars_names=[]
        omit_objs=["__main__.Flecha"]
        for i in obj_vars:
            print i
            if i is not self and str(i[1].__class__):
                if str(i[0])!="state":
                    obj_vars_names.append((str(i[0]),i[1]))
##                print "WorldState.SaveObjects() Added"
                else:
                    print "Omited state"

        for i in obj_vars_names:
            try:
##                filename="%s/%s.dat"%(aux_dir,id(i[1]))
##                funcfile=open(filename,"wt")
##                p=cPickle.Pickler(funcfile)
##                p.dump(i[1])
##                funcfile.close()

##                file.write('%s=GameStateAux.GetPickledData("%s")\n'%(i[0],filename))

                SavePickDataAux(file,aux_dir,i[1],i[0]+"=%s\n")
            except Exception,exc:
                print "Failed saving of",i
                print exc

        file.write('\n\n')


    def SaveSectors(self,file):
        "Saves sector objects in the global scope."

        sec=Bladex.GetSector(0)
        sec_vars=self.GetGlobalsAux(type(sec))

        file.write('\n\n# Sector objects\n')
        sec_vars_names=[]
        for i in sec_vars:
            sec_vars_names.append((str(i[0]),i[1].Index))

        for i in sec_vars_names:
            file.write('%s=Bladex.GetSector(%d)\n'%(i[0],i[1]))
        file.write('\n\n')



    def SaveModules(self,file):
        "Saves modules in the global scope."

        import string
        OmitModules=["__builtins__","Scorer","Menu","GameText","GameState","GameStateAux"]
        global_mods=self.GetGlobalsAux(types.ModuleType)
        file.write('\n# Modules\n')
        for i in global_mods:
            if i[0] not in OmitModules and string.find(i[0],"AnimationSet")==-1 and string.find(i[0],"Widget")==-1:
                file.write('import %s\n'%(i[0],))


    def GetGlobalsAux(self,req_type):
        g=GetGlobals()
        elems=[]
        for i in g.items():
            if type(i[1])==req_type:
                elems.append(i)
        return elems

##    def SaveFunctions(self,aux_dir):
##        import types
##        funcs=self.GetGlobalsAux(types.FunctionType)
##        for i in funcs:
##            #print i
##            fn=i[1]
##            filename="%s/%s.dat"%(aux_dir,id(fn))
##            funcfile=open(filename,"wt")
##            code=marshal.dumps(fn.func_code)
##            p=cPickle.Pickler(funcfile)
##            p.dump((fn.func_name,code,fn.func_defaults,fn.func_doc))
##            funcfile.close()


    def SaveAutoBODs(self,path):
        # Primero voy a guardar los BODs que se generan automáticamente
        B_CID_AUTO_OBJDSCR=BBLib.B_CID_AUTO_OBJDSCR
        RM=BBLib.GetResourceManager()
        nAutoBODs=RM.NResources(B_CID_AUTO_OBJDSCR)
        for i in range(nAutoBODs):
            name="%s/%s.BOD"%(path,RM.GetResourceName(B_CID_AUTO_OBJDSCR,i))
            RM.SaveResource(B_CID_AUTO_OBJDSCR,i,name)

    def SaveList(self,command,lista,file):
        nchunks=len(lista)/5
        for i in range(nchunks):
            lolimit=5*i
            l=lista[lolimit:lolimit+5]
            file.write(command%(str(l),))

    def __AuxGetResFiles(self,kind):
        RM=BBLib.GetResourceManager()
        nRes=RM.NResources(kind)
        ResFiles=[]
        for i in range(nRes):
            res_file=RM.GetResourceFile(kind,i)
            if res_file not in ResFiles:
                ResFiles.append(res_file)
        return ResFiles

    def __AuxGetResFilesAndNames(self,kind):
        RM=BBLib.GetResourceManager()
        nRes=RM.NResources(kind)
        ResFiles=[]
        for i in range(nRes):
            res_file=RM.GetResourceFile(kind,i)
            res_name=RM.GetResourceName(kind,i)
            if res_file not in ResFiles:
                ResFiles.append((res_file,res_name))
        return ResFiles


##    def SaveParticleSystems(self,file):
##
##        file.write('\n# Particle Systems\n')
##        nParts=Bladex.GetnParticleGType()
##        for i in range(nParts):
##            PSystem=Bladex.GetParticleGType(i)
##            PSystemName=PSystem[0]
##            if PSystemName=="Energia2":
##                print "Warning, omiting particle system Energia2"
##                continue
##            
##            file.write('Bladex.AddParticleGType("%s","%s",%i,%i)\n\n'%(PSystem))
##
##            RedValues=[]
##            GreenValues=[]
##            BlueValues=[]
##            AlphaValues=[]
##            SizeValues=[]
##            for j in range(PSystem[3]):
##                PSValues=Bladex.GetParticleGVal(PSystemName,j)
##                RedValues.append(PSValues[0])
##                GreenValues.append(PSValues[1])
##                BlueValues.append(PSValues[2])
##                AlphaValues.append(PSValues[3])
##                SizeValues.append(PSValues[4])
##
##            file.write('RedValues=%s\n'%str(RedValues))
##            file.write('GreenValues=%s\n'%str(GreenValues))
##            file.write('BlueValues=%s\n'%str(BlueValues))
##            file.write('AlphaValues=%s\n'%str(AlphaValues))
##            file.write('SizeValues=%s\n'%str(SizeValues))
##            file.write('\n')
##
##            file.write('for i in range(%d):\n'%(PSystem[3]))
##            file.write('  Bladex.SetParticleGVal("%s",i,RedValues[i],GreenValues[i],BlueValues[i],AlphaValues[i],SizeValues[i])\n\n\n'%(PSystemName,))
  
    def SaveTimers(self,file):

        file.write('\n# Timers\n')
        nTimers=Bladex.GetnTimers()
        for i in range(nTimers):
            cTimer=Bladex.GetTimerInfo(i)
            file.write('Bladex.CreateTimer("%s",%f)\n\n'%(cTimer[0],cTimer[1]))
        file.write('\n')


    def GetMMPFiles(self):
        return self.__AuxGetResFiles(BBLib.B_CID_BITMAP)

    def GetBODFiles(self):
        return self.__AuxGetResFiles(BBLib.B_CID_OBJDSCR)

    def GetBMPFiles(self):
        return self.__AuxGetResFilesAndNames(BBLib.B_CID_BMP)

    def GetAlphaBMPFiles(self):
        return self.__AuxGetResFilesAndNames(BBLib.B_CID_ALPHABMP)


def GetGlobals():
    import sys
    try:
        1 + ''
    except:
        frame = sys.exc_info()[2].tb_frame.f_back

    while frame:
        globs=frame.f_globals
        frame=frame.f_back

    return globs
