import Menu
import Bladex
import Scorer
import ScorerWidgets
import BUIx
import AuxFuncs
import BBLib
import ItemTypes
import Reference #Para demo_mode flag...
import GameText
import MenuText
import KeybWidget
import Language
import GameText

execfile ("../../data/text/"+Language.Current+"/casa.py")

Bladex.LoadSampledAnimation("../../Anm/Kgt_seleccion.BMV","Kgt_seleccion",1,"Knight_N")
#Bladex.LoadSampledAnimation("../../Anm/Gladius.BMV","Gladius",1,"GladiusSeleccion")
#Bladex.LoadSampledAnimation("../../Anm/Shield_Kgt_seleccion.BMV","Shield_kgt_seleccion",1,"Shield_Kgt_seleccion")

Bladex.LoadSampledAnimation("../../Anm/Amz_seleccion.BMV","Amz_seleccion",1,"Amazon_N")
#Bladex.LoadSampledAnimation("../../Anm/Arco_Amz_seleccion.BMV","Arco_amz_seleccion",1,"Arco_Amz_seleccion")
#Bladex.LoadSampledAnimation("../../Anm/Flecha_Amz_seleccion.BMV","Flecha_amz_seleccion",1,"Flecha_Amz_seleccion")
Bladex.LoadSampledAnimation("../../Anm/Carcaj_Amz_seleccion.BMV","Carcaj_amz_seleccion",1,"Carcaj_Amz_seleccion")

Bladex.SetAnimationFactor("Amz_seleccion",3)
#Bladex.SetAnimationFactor("Arco_amz_seleccion",3)
#Bladex.SetAnimationFactor("Flecha_amz_seleccion",3)
Bladex.SetAnimationFactor("Carcaj_amz_seleccion",3)

Bladex.LoadSampledAnimation("../../Anm/Dwf_seleccion.BMV","Dwf_seleccion",1,"Dwarf_N")
#Bladex.LoadSampledAnimation("../../Anm/Axe_Dwf_seleccion.BMV","Axe_dwf_seleccion",1,"Axe_Dwf_seleccion")
Bladex.LoadSampledAnimation("../../Anm/Jar_Dwf_seleccion.BMV","Jar_dwf_seleccion",1,"Jar_Dwf_seleccion")

Bladex.SetAnimationFactor("Dwf_seleccion",3)
Bladex.SetAnimationFactor("Jar_dwf_seleccion",3)
#Bladex.SetAnimationFactor("Axe_dwf_seleccion",3)

Bladex.LoadSampledAnimation("../../Anm/Bar_seleccion.BMV","Bar_seleccion",1,"Barbarian_N")
Bladex.LoadSampledAnimation("../../Anm/Piedra_bar_seleccion.BMV","Piedra_bar_seleccion",1,"Piedra_Bar_seleccion")
Bladex.LoadSampledAnimation("../../Anm/Espada_bar_seleccion.BMV","Espada_bar_seleccion",1,"Espada_Bar_seleccion")

Bladex.SetAnimationFactor("Bar_seleccion",3)
Bladex.SetAnimationFactor("Piedra_bar_seleccion",3)
Bladex.SetAnimationFactor("Espada_bar_seleccion",3)

def GraspString (EntityName,EventName):
    bow= Bladex.GetEntity("ArcoAmz")
    bow.Data.GraspString()

def UnGraspString (EntityName,EventName):
    me= Bladex.GetEntity(EntityName)
    bow= Bladex.GetEntity("ArcoAmz")
    bow.Data.UnGraspString()

    #release arrow
    arrow= Bladex.GetEntity("FlechaAmz")
    arrow.ExcludeHitFor(me)
    arrow.PutToWorld()
    me.Unlink(arrow)
    vx,vy,vz= arrow.Rel2AbsVector(0,0,-40000)
    arrow.Fly(vx,vy,vz)

def TakeArrow (EntityName,EventName):
    me= Bladex.GetEntity(EntityName)
    arrow= Bladex.GetEntity("FlechaAmz")
    arrow.Stop()
    me.LinkAnchors("R_Hand",arrow,"1H_R")

def PickUpBowToLeft (EntityName,EventName):
    me= Bladex.GetEntity(EntityName)
    bow= Bladex.GetEntity("ArcoAmz")
    me.LinkAnchors("L_Hand",bow,"1H_L")

def LeftDrop (EntityName,EventName):
    me= Bladex.GetEntity(EntityName)
    bow= Bladex.GetEntity("ArcoAmz")
    me.Unlink(bow)

def EndAnmAmz(name):
    time= Bladex.GetTime()
    PickUpBowToLeftTime= 336.0/60.0
    LeftDropTime= 768.0/60.0
    TakeArrowTime= 580.0/60.0
    GraspStringTime= 600.0/60.0
    UnGraspStringTime= 646.0/60.0
    Bladex.AddScheduledFunc(time+PickUpBowToLeftTime, PickUpBowToLeft,(name, "PickUpBowToLeft"),"PickUpBowToLeft")
    Bladex.AddScheduledFunc(time+LeftDropTime,        LeftDrop,       (name, "LeftDrop"),       "LeftDrop")
    Bladex.AddScheduledFunc(time+TakeArrowTime,       TakeArrow,      (name, "TakeArrow"),      "TakeArrow")
    Bladex.AddScheduledFunc(time+GraspStringTime,     GraspString,    (name, "GraspString"),    "GraspString")
    Bladex.AddScheduledFunc(time+UnGraspStringTime,   UnGraspString,  (name, "UnGraspString"),  "UnGraspString")


def SetCameraInicio():
    global CurrentPerson
    global FinishPerson

    CurrentPerson = 2
    FinishPerson = 2

    cam = Bladex.GetEntity("Camera")
    cam.SetMaxCamera("Seleccion_Camera_seleccion_caballero.cam",0,-1)
    AuxFuncs.FadeFrom(0.5, 0.5)

#Bladex.AddScheduledFunc(Bladex.GetTime(),SetCameraInicio,())
SetCameraInicio()

def LanzarAnimacionActor():
    SonidosDelKavayero()
    SonidosDelEnano()
    SonidosDelBarbaro()
    SonidosDeLaAmazona()

    cab = Bladex.GetEntity("Caballero")
    amz = Bladex.GetEntity("Amazona")
    ena = Bladex.GetEntity("Enano")
    bar = Bladex.GetEntity("Barbaro")

    glad = Bladex.GetEntity("WeaponActor1")
    escudo = Bladex.GetEntity("EscudoActor1")
    arco = Bladex.GetEntity("ArcoAmz")
    #flecha = Bladex.GetEntity("FlechaAmz")
    carcaj = Bladex.GetEntity("CarcajAmz")
    jarra = Bladex.GetEntity("JarraDwf")
    #hacha = Bladex.GetEntity("HachaDwf")
    piedra = Bladex.GetEntity("PiedraBar")
    espada = Bladex.GetEntity("EspadaBar")

    #glad.Position = 15751,-8338,-12536
    #glad.Actor = 1
    #glad.Animation = "Gladius"

    #escudo.Position = 16405,-8249,-12193
    #escudo.Actor = 1
    #escudo.Animation = "Shield_kgt_seleccion"

    #flecha.Position = 15238,-1318,22399
    #flecha.Position = 14793,-1379,22214
    #14789,1305,22220

    #flecha.Actor = 1
    #flecha.Animation = "Flecha_amz_seleccion"
    #flecha.Alpha = 0.0

    carcaj.Position = 14656,-801,22334
    carcaj.Actor = 1
    carcaj.Animation = "Carcaj_amz_seleccion"

    jarra.Position = 12077,-355,10356
    jarra.Actor = 1
    jarra.Animation = "Jar_dwf_seleccion"

    #hacha.Position = 11862,-691,9307
    #hacha.Position = 11976,-691,9307
    #hacha.Actor = 1
    #hacha.Animation = "Axe_dwf_seleccion"

    piedra.Position = -957,-149,-3251
    piedra.Actor = 1
    piedra.Animation = "Piedra_bar_seleccion"

    espada.Position = -630,-30,-3126
    espada.Actor = 1
    espada.Animation = "Espada_bar_seleccion"

    cab.Position = 16039, -8388,-11988
    cab.Actor = 1
    cab.Animation = "Kgt_seleccion"

    amz.Position = 14881, -1082,22235
    amz.Actor = 1
    #amz.AddAnmEventFunc("PickUpBowToLeft", PickUpBowToLeft)
    #amz.AddAnmEventFunc("LeftDrop", LeftDrop)
    #amz.AddAnmEventFunc("GraspString", GraspString)
    #amz.AddAnmEventFunc("UnGraspString", UnGraspString)
    amz.Animation="Amz_seleccion"
    EndAnmAmz (amz.Name)
    amz.OnAnimationEndFunc= EndAnmAmz

    ena.Position = 11563, -827,9813
    ena.Actor = 1
    ena.Animation = "Dwf_seleccion"

    bar.Position = -99, -616,-3233
    bar.Actor = 1
    bar.Animation = "Bar_seleccion"

    cab.LinkAnchors("R_Hand",glad,"1H_R")
    cab.LinkAnchors("Shield",escudo,"Shield")

    glad.TurnOn()
    escudo.TurnOn()
    #flecha.TurnOn()
    carcaj.TurnOn()
    jarra.TurnOn()
    #hacha.TurnOn()
    piedra.TurnOn()
    espada.TurnOn()
    cab.TurnOn()
    amz.TurnOn()
    ena.TurnOn()
    bar.TurnOn()


def CreateActor():
    char=Bladex.CreateEntity("Caballero","Knight_N",0,0,0)
    char.RotateRel(0,0,0,1,0,0,1.57)
    char.Static = 1

    glad=Bladex.CreateEntity("WeaponActor1","Gladius",0,0,0,"Weapon")
    #glad.RotateRel(0,0,0,1,0,0,1.57)
    #glad.Static = 1

    escudo=Bladex.CreateEntity("EscudoActor1","Escudo3",0,0,0,"Weapon")
    #escudo.RotateRel(0,0,0,1,0,0,1.57)
    #escudo.Static = 1

    arco=Bladex.CreateEntity("ArcoAmz","Arco2",16336,-671,22801,"Weapon")
    arco.Orientation=(0.499056011438, -0.50122833252, 0.49957087636, -0.500142157078)
    arco.Data= ItemTypes.Arco_Amz_seleccion(arco)


    flecha=Bladex.CreateEntity("FlechaAmz","Flecha",0,0,0,"Arrow")
    #flecha.RotateRel(0,0,0,1,0,0,1.57)
    #flecha.Static = 1

    carcaj=Bladex.CreateEntity("CarcajAmz","Carcaj_Amz_seleccion",0,0,0)
    carcaj.RotateRel(0,0,0,1,0,0,1.57)
    carcaj.Static = 1

    taburete=Bladex.CreateEntity("TabureteDwf","Taburete_Dwf_seleccion",11537,-430,9786)
    taburete.RotateRel(0,0,0,1,0,0,1.57)

    #hacha=Bladex.CreateEntity("HachaDwf","Axe_Dwf_seleccion",0,0,0)
    #hacha.RotateRel(0,0,0,1,0,0,1.57)
    #hacha.Static = 1

    jarra=Bladex.CreateEntity("JarraDwf","Jar_Dwf_seleccion",0,0,0)
    jarra.RotateRel(0,0,0,1,0,0,1.57)
    jarra.Static = 1

    piedra=Bladex.CreateEntity("PiedraBar","Piedra_Bar_seleccion",0,0,0)
    piedra.RotateRel(0,0,0,1,0,0,1.57)
    piedra.Static = 1

    espada=Bladex.CreateEntity("EspadaBar","Espada_Bar_seleccion",0,0,0)
    espada.RotateRel(0,0,0,1,0,0,1.57)
    espada.Static = 1

    pvarias=Bladex.CreateEntity("PiedrasVarias","PiedrasBarbaro",-684,103,-3346)
    pvarias.RotateRel(0,0,0,1,0,0,1.57)


    char=Bladex.CreateEntity("Amazona","Amazon_N",0,0,0)
    char.RotateRel(0,0,0,1,0,0,1.57)
    char.Static = 1

    char=Bladex.CreateEntity("Enano","Dwarf_N",0,0,0)
    char.RotateRel(0,0,0,1,0,0,1.57)
    char.Static = 1

    char=Bladex.CreateEntity("Barbaro","Barbarian_N",0,0,0)
    char.RotateRel(0,0,0,1,0,0,1.57)
    char.Static = 1

CreateActor()

Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, LanzarAnimacionActor,())

CurrentPerson = 2
FinishPerson = 2
Stoped = 1
StateArrow = 1

CameraPerson = ["Seleccion_Camera_seleccion_amazona.cam","Seleccion_Camera_seleccion_barbaro.cam","Seleccion_Camera_seleccion_caballero.cam","Seleccion_Camera_seleccion_enano.cam"]
CameraAvance = ["Seleccion_Camera_amazona_barbaro.cam","Seleccion_Camera_barbaro_caballero.cam","Seleccion_Camera_caballero_enano.cam","Seleccion_Camera_enano_amazona.cam"]
CameraRetroc = ["Seleccion_Camera_barbaro_amazona.cam","Seleccion_Camera_caballero_barbaro.cam","Seleccion_Camera_enano_caballero.cam","Seleccion_Camera_amazona_enano.cam"]
MapaPerson = ["Ruins_M4","Barb_M1","Ragnar_M2","Dwarf_M3"]

FrameCamera = [60,50,60,47]


def StopRecorridoCamera(Camera,Frame):
    global Stoped

    if CurrentPerson == FinishPerson:
        cam = Bladex.GetEntity("Camera")
        cam.SetMaxCamera(CameraPerson[CurrentPerson],0,-1)
        Stoped = 1
        FadeArrow(2)
        SelectCharacterWidget.SetVisible(1)
    else:
        ChangePersonCamera()


def ChangePersonCamera():
    global CurrentPerson
    global Stoped

    if Stoped:
        FadeArrow(1)
        SelectCharacterWidget.SetVisible(0)

    #FlechaIzqWidget.SetVisible(0)
    #FlechaDerWidget.SetVisible(0)

    Stoped = 0

    cam = Bladex.GetEntity("Camera")
    dist = FinishPerson - CurrentPerson

    if CurrentPerson < FinishPerson:
        if dist < 3:
            cam.SetMaxCamera(CameraAvance[CurrentPerson],0,FrameCamera[CurrentPerson])
            CurrentPerson = CurrentPerson + 1
        else:
            CurrentPerson = 3
            cam.SetMaxCamera(CameraRetroc[CurrentPerson],0,FrameCamera[CurrentPerson])
    else:
        if dist > -3:
            CurrentPerson = CurrentPerson - 1
            cam.SetMaxCamera(CameraRetroc[CurrentPerson],0,FrameCamera[CurrentPerson])
        else:
            cam.SetMaxCamera(CameraAvance[CurrentPerson],0,FrameCamera[CurrentPerson])
            CurrentPerson = 0

    cam.AddCameraEvent(-1,StopRecorridoCamera)

def PressKeyZ():
    global FinishPerson

    if (YesNoActivated):
        ActivateWidgetYesNo()
    elif Stoped:
        if FinishPerson == 0:
            FinishPerson = 3
        else:
            FinishPerson = FinishPerson - 1

        ChangePersonCamera()

def PressKeyX():
    global FinishPerson

    if (YesNoActivated):
        ActivateWidgetYesNo()
    elif Stoped:
        if FinishPerson == 3:
            FinishPerson = 0
        else:
            FinishPerson = FinishPerson + 1

        ChangePersonCamera()

#def LoadTheMap():
#   Bladex.LoadLevel(MapaPerson[CurrentPerson])

FlechaDerWidget = 0
FlechaIzqWidget = 0
SelectCharacterWidget = 0
AreYouSureWidget = 0
YesWidget = 0
NoWidget = 0
YesNoValue = 1
YesNoActivated = 0
InfoCharWidget1 = 0
InfoCharWidget2 = 0
InfoCharWidget3 = 0
InfoCharWidget4 = 0
fondo1 = 0
fondo2 = 0
fondo3 = 0




marco1 = 0
marco2 = 0
marco3 = 0
marco4 = 0
marco5 = 0
marco6 = 0

#Size_X = Scorer.wFrame.GetSize()[0]
#Size_Y = Scorer.wFrame.GetSize()[1]
#Size_X = 800.0
#Size_Y = 600.0
#import Raster

#Size_X = Raster.GetSize()[0]
#Size_Y = Raster.GetSize()[1]
##Size_X=640
Size_Y=480

#print "Resolucion Raster"
#print Raster.GetSize()

##Scorer.wFrame.SetAutoScale(0)

#ARX = Size_X / 640.0
#ARY = Size_Y / 480.0


MarcoAnchoTex = 256.0
MarcoAltoTex = 256.0


#RasterRes =

def SlideFrame(dir,time = 0):
    if time < 1.0:
        Bladex.AddScheduledFunc(Bladex.GetTime() + 0.025,SlideFrame,(dir,time + 0.05))
    else:
        time = 1.0

        if dir:
            marco1.SetVisible(0)
            marco2.SetVisible(0)
            marco3.SetVisible(0)
            marco4.SetVisible(0)
            marco5.SetVisible(0)
            marco6.SetVisible(0)

    if dir:
        Y_UP = -MarcoAltoTex * time
        Y_DOWN = (Size_Y - MarcoAltoTex) + MarcoAltoTex * time
    else:
        Y_UP = -MarcoAltoTex + MarcoAltoTex * time
        Y_DOWN = Size_Y - MarcoAltoTex * time

    Scorer.wFrame.MoveWidgetTo("Marco1",0,Y_UP)
    # Scorer.wFrame.MoveWidgetTo("Marco2",MarcoAnchoTex,Y_UP)
    # Scorer.wFrame.MoveWidgetTo("Marco3",MarcoAnchoTex * 2.0,Y_UP)
    Scorer.wFrame.MoveWidgetRightTo("Marco2", "Marco1" ,Y_UP)
    Scorer.wFrame.MoveWidgetRightTo("Marco3", "Marco2" ,Y_UP)

    Scorer.wFrame.MoveWidgetTo("Marco4",0,Y_DOWN)
    # Scorer.wFrame.MoveWidgetTo("Marco5",MarcoAnchoTex,Y_DOWN)
    # Scorer.wFrame.MoveWidgetTo("Marco6",MarcoAnchoTex * 2.0,Y_DOWN)
    Scorer.wFrame.MoveWidgetRightTo("Marco5","Marco4",Y_DOWN)
    Scorer.wFrame.MoveWidgetRightTo("Marco6","Marco5",Y_DOWN)


def CreateWidgetMarco():
    global marco1
    global marco2
    global marco3
    global marco4
    global marco5
    global marco6

    TamX = 256.0
    TamY = 256.0

    marco1=BUIx.B_BitmapWidget(Scorer.wFrame,"Marco1",256,256,"1","../../Data/seleccionpersonaje.mmp")
    marco1.SetColor(255,255,255)
    Scorer.wFrame.AddWidget(marco1,0,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    marco1.SetSize(TamX,TamY)
    marco1.SetAlpha(1.0)
    marco1.SetVisible(0)
    marco1.SetAutoScale(1)


    marco2=BUIx.B_BitmapWidget(Scorer.wFrame,"Marco2",256,256,"2","../../Data/seleccionpersonaje.mmp")
    marco2.SetColor(255,255,255)
    Scorer.wFrame.AddWidget(marco2,256,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    marco2.SetSize(TamX,TamY)
    marco2.SetAlpha(1.0)
    marco2.SetVisible(0)
    marco2.SetAutoScale(1)

    marco3=BUIx.B_BitmapWidget(Scorer.wFrame,"Marco3",256,256,"3","../../Data/seleccionpersonaje.mmp")
    marco3.SetColor(255,255,255)
    Scorer.wFrame.AddWidget(marco3,512,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    marco3.SetSize(TamX,TamY)
    marco3.SetAlpha(1.0)
    marco3.SetVisible(0)
    marco3.SetAutoScale(1)

    marco4=BUIx.B_BitmapWidget(Scorer.wFrame,"Marco4",256,256,"4","../../Data/seleccionpersonaje.mmp")
    marco4.SetColor(255,255,255)
    Scorer.wFrame.AddWidget(marco4,0,480-256,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    marco4.SetSize(TamX,TamY)
    marco4.SetAlpha(1.0)
    marco4.SetVisible(0)
    marco4.SetAutoScale(1)

    marco5=BUIx.B_BitmapWidget(Scorer.wFrame,"Marco5",256,256,"5","../../Data/seleccionpersonaje.mmp")
    marco5.SetColor(255,255,255)
    Scorer.wFrame.AddWidget(marco5,256,480-256,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    marco5.SetSize(TamX,TamY)
    marco5.SetAlpha(1.0)
    marco5.SetVisible(0)
    marco5.SetAutoScale(1)

    marco6=BUIx.B_BitmapWidget(Scorer.wFrame,"Marco6",256,256,"6","../../Data/seleccionpersonaje.mmp")
    marco6.SetColor(255,255,255)
    Scorer.wFrame.AddWidget(marco6,512,480-256,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    marco6.SetSize(TamX,TamY)
    marco6.SetAlpha(1.0)
    marco6.SetVisible(0)
    marco6.SetAutoScale(1)


def CreateWidgetInfoChar():
    global InfoCharWidget1
    global InfoCharWidget2
    global InfoCharWidget3
    global InfoCharWidget4
    global FlechaDerWidget
    global FlechaIzqWidget


    InfoCharWidget1=BUIx.B_TextWidget(Scorer.wFrame,"InfoChar1","",ScorerWidgets.font_server,Language.LetrasMenuBig)
    InfoCharWidget1.SetText(TextInfoCharAmz1)
    InfoCharWidget1.SetAlpha(1)
    InfoCharWidget1.SetColor(255,0,0)
    Scorer.wFrame.AddWidget(InfoCharWidget1,0.5,100.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    InfoCharWidget1.SetVisible(0)
    InfoCharWidget1.SetAutoScale(1)

    InfoCharWidget2=BUIx.B_TextWidget(Scorer.wFrame,"InfoChar2","",ScorerWidgets.font_server,Language.LetrasMenu)
    InfoCharWidget2.SetText(TextInfoCharAmz2)
    InfoCharWidget2.SetAlpha(1)
    InfoCharWidget2.SetColor(254,254,202)
    #Scorer.wFrame.AddWidget(InfoCharWidget2,0.475,140.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    Scorer.wFrame.AddWidget(InfoCharWidget2,0.5,140.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    InfoCharWidget2.SetVisible(0)
    InfoCharWidget2.SetAutoScale(1)

    InfoCharWidget3=BUIx.B_TextWidget(Scorer.wFrame,"InfoChar3","",ScorerWidgets.font_server,Language.LetrasMenu)
    InfoCharWidget3.SetText(TextInfoCharAmz3)
    InfoCharWidget3.SetAlpha(1)
    InfoCharWidget3.SetColor(254,116,4)
    #Scorer.wFrame.AddWidget(InfoCharWidget3,0.49,290.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    Scorer.wFrame.AddWidget(InfoCharWidget3,0.5,290.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    InfoCharWidget3.SetVisible(0)
    InfoCharWidget3.SetAutoScale(1)

    InfoCharWidget4=BUIx.B_TextWidget(Scorer.wFrame,"InfoChar4","",ScorerWidgets.font_server,Language.LetrasMenu)
    InfoCharWidget4.SetText(TextInfoCharAmz4)
    InfoCharWidget4.SetAlpha(1)
    InfoCharWidget4.SetColor(247,255,171)
    Scorer.wFrame.AddWidget(InfoCharWidget4,0.5,320.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    InfoCharWidget4.SetVisible(0)
    InfoCharWidget4.SetAutoScale(1)


    FlechaIzqWidget=BUIx.B_TextWidget(Scorer.wFrame,"FlechaIzqWidget","<",ScorerWidgets.font_server,Language.LetrasMenuBig)
    FlechaIzqWidget.SetAlpha(1)
    FlechaIzqWidget.SetColor(128,128,128)
    FlechaIzqWidget.SetText("<")
    Scorer.wFrame.AddWidget(FlechaIzqWidget,0.03,15,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
    FlechaIzqWidget.SetVisible(1)
    FlechaIzqWidget.SetAutoScale(1)

    FlechaDerWidget=BUIx.B_TextWidget(Scorer.wFrame,"FlechaDerWidget",">",ScorerWidgets.font_server,Language.LetrasMenuBig)
    FlechaDerWidget.SetAlpha(1)
    FlechaDerWidget.SetColor(128,128,128)
    FlechaDerWidget.SetText(">")
    Scorer.wFrame.AddWidget(FlechaDerWidget,0.97,15,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
    FlechaDerWidget.SetVisible(1)
    FlechaDerWidget.SetAutoScale(1)
    Scorer.wFrame.RecalcLayout()

def FadeTextInfo(time = 0.0):
    if time < 1.0:
        Bladex.AddScheduledFunc(Bladex.GetTime() + 0.02,FadeTextInfo,(time + 0.1,))
    else:
        time = 1.0

    InfoCharWidget1.SetAlpha(time)
    InfoCharWidget2.SetAlpha(time)
    InfoCharWidget3.SetAlpha(time)
    InfoCharWidget4.SetAlpha(time)


def FadeFondo(time = 0.0):
    if time < 0.3:
        Bladex.AddScheduledFunc(Bladex.GetTime() + 0.02,FadeFondo,(time + 0.02,))
    else:
        time = 0.3

    fondo1.SetAlpha(time * 3.33)
    fondo2.SetAlpha(time * 3.33)
    fondo3.SetAlpha(time * 3.33)

BBLib.ReadMMP("../../Data/seleccionamazona.mmp")
BBLib.ReadMMP("../../Data/seleccionbarbaro.mmp")
BBLib.ReadMMP("../../Data/seleccioncaballero.mmp")
BBLib.ReadMMP("../../Data/seleccionenano.mmp")

def PrecargaBackgroundCharacters():
    global fondo1
    global fondo2
    global fondo3

    if fondo1 == 0:
        TamX = 256.0
        TamY = 256.0

        fondo1=BUIx.B_BitmapWidget(Scorer.wFrame,"FondoInfoChar",256,256,"AMZ1","../../Data/seleccionamazona.mmp")
        fondo1.SetColor(255,255,255)
        Scorer.wFrame.AddWidget(fondo1,0,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
        fondo1.SetSize(TamX,TamY)
        fondo1.SetAutoScale(1)

        fondo2=BUIx.B_BitmapWidget(Scorer.wFrame,"FondoInfoChar",256,256,"AMZ2","../../Data/seleccionamazona.mmp")
        fondo2.SetColor(255,255,255)
        Scorer.wFrame.AddWidget(fondo2,256.0,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
        fondo2.SetSize(TamX,TamY)
        fondo2.SetAutoScale(1)

        fondo3=BUIx.B_BitmapWidget(Scorer.wFrame,"FondoInfoChar",256,256,"AMZ3","../../Data/seleccionamazona.mmp")
        fondo3.SetColor(255,255,255)
        Scorer.wFrame.AddWidget(fondo3,0,256.0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
        fondo3.SetSize(TamX,TamY)
        fondo3.SetAutoScale(1)

    fondo1.SetBitmap("AMZ1")
    fondo2.SetBitmap("AMZ2")
    fondo3.SetBitmap("AMZ3")

    fondo1.SetBitmap("BAR1")
    fondo2.SetBitmap("BAR2")
    fondo3.SetBitmap("BAR3")

    fondo1.SetBitmap("CAB1")
    fondo2.SetBitmap("CAB2")
    fondo3.SetBitmap("CAB3")

    fondo1.SetBitmap("ENA1")
    fondo2.SetBitmap("ENA2")
    fondo3.SetBitmap("ENA3")


def ActivateWiggetInfoChar():

    if CurrentPerson == 0:
        InfoCharWidget1.SetText(TextInfoCharAmz1)
        InfoCharWidget2.SetText(TextInfoCharAmz2)
        InfoCharWidget3.SetText(TextInfoCharAmz3)
        InfoCharWidget4.SetText(TextInfoCharAmz4)

        fondo1.SetBitmap("AMZ1")
        fondo2.SetBitmap("AMZ2")
        fondo3.SetBitmap("AMZ3")
    elif CurrentPerson == 1:
        InfoCharWidget1.SetText(TextInfoCharBar1)
        InfoCharWidget2.SetText(TextInfoCharBar2)
        InfoCharWidget3.SetText(TextInfoCharBar3)
        InfoCharWidget4.SetText(TextInfoCharBar4)

        fondo1.SetBitmap("BAR1")
        fondo2.SetBitmap("BAR2")
        fondo3.SetBitmap("BAR3")
    elif CurrentPerson == 2:
        InfoCharWidget1.SetText(TextInfoCharKgt1)
        InfoCharWidget2.SetText(TextInfoCharKgt2)
        InfoCharWidget3.SetText(TextInfoCharKgt3)
        InfoCharWidget4.SetText(TextInfoCharKgt4)

        fondo1.SetBitmap("CAB1")
        fondo2.SetBitmap("CAB2")
        fondo3.SetBitmap("CAB3")
    elif CurrentPerson == 3:
        InfoCharWidget1.SetText(TextInfoCharDwf1)
        InfoCharWidget2.SetText(TextInfoCharDwf2)
        InfoCharWidget3.SetText(TextInfoCharDwf3)
        InfoCharWidget4.SetText(TextInfoCharDwf4)

        fondo1.SetBitmap("ENA1")
        fondo2.SetBitmap("ENA2")
        fondo3.SetBitmap("ENA3")


    fondo1.SetVisible(1)
    fondo2.SetVisible(1)
    fondo3.SetVisible(1)
    FadeFondo()

    InfoCharWidget1.SetVisible(1)
    InfoCharWidget2.SetVisible(1)
    InfoCharWidget3.SetVisible(1)
    InfoCharWidget4.SetVisible(1)

    InfoCharWidget1.SetAlpha(0)
    InfoCharWidget2.SetAlpha(0)
    InfoCharWidget3.SetAlpha(0)
    InfoCharWidget4.SetAlpha(0)

    Bladex.AddScheduledFunc(Bladex.GetTime() + 0.3,FadeTextInfo,())
    Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,ScreenSelectionFinish,())

    ActivateWidgetYesNo()

    AreYouSureWidget.SetVisible(1)
    YesWidget.SetVisible(1)
    NoWidget.SetVisible(1)

    Scorer.wFrame.SetSize(10,10) # Fuerzo que recalcule.
    Scorer.wFrame.RecalcLayout()


ScreenSelectionFinished = 1

def ScreenSelectionFinish():
    global ScreenSelectionFinished

    ScreenSelectionFinished = 1


Bladex.AddScheduledFunc(Bladex.GetTime() + 0.3,FadeTextInfo,())



def ActivateWidgetYesNo():
    global YesNoValue

    if (YesNoValue):
        YesWidget.SetColor(128,128,128)
        NoWidget.SetColor(255,255,255)
        YesNoValue = 0
    else:
        YesWidget.SetColor(255,255,255)
        NoWidget.SetColor(128,128,128)
        YesNoValue = 1

def CreateWidgetAreYouSure():
    global SelectCharacterWidget
    global AreYouSureWidget
    global YesWidget
    global NoWidget

    SelectCharacterWidget=BUIx.B_TextWidget(Scorer.wFrame,"SelectCharacter","",ScorerWidgets.font_server,Language.LetrasMenu)
    SelectCharacterWidget.SetAlpha(1)
    SelectCharacterWidget.SetColor(128,128,128)
    SelectCharacterWidget.SetText(MenuText.GetMenuText("Press arrows to choose character. Press ${\"ENTER\":Accept} to select"))

    AreYouSureWidget=BUIx.B_TextWidget(Scorer.wFrame,"AreYouSure","",ScorerWidgets.font_server,Language.LetrasMenu)
    AreYouSureWidget.SetAlpha(1)
    AreYouSureWidget.SetColor(255,255,255)
    AreYouSureWidget.SetText(MenuText.GetMenuText("ARE YOU SURE?"))

    YesWidget=BUIx.B_TextWidget(Scorer.wFrame,"Yes","",ScorerWidgets.font_server,Language.LetrasMenu)
    YesWidget.SetAlpha(1)
    YesWidget.SetColor(128,128,128)
    YesWidget.SetText(MenuText.GetMenuText("Yes"))

    NoWidget=BUIx.B_TextWidget(Scorer.wFrame,"No","",ScorerWidgets.font_server,Language.LetrasMenu)
    NoWidget.SetAlpha(1)
    NoWidget.SetColor(128,128,128)
    NoWidget.SetText(MenuText.GetMenuText("No"))

    Scorer.wFrame.AddWidget(SelectCharacterWidget,0.50,22.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
    Scorer.wFrame.AddWidget(AreYouSureWidget,0.45,23.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
    Scorer.wFrame.AddWidget(YesWidget,0.56,23.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
    Scorer.wFrame.AddWidget(NoWidget,0.60,23.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

    SelectCharacterWidget.SetVisible(1)
    AreYouSureWidget.SetVisible(0)
    YesWidget.SetVisible(0)
    NoWidget.SetVisible(0)

last_start_time = 0
last_fade_time = 0
Forward_Arrow = 1

def FadeArrow(fade):
    global last_fade_time
    global StateArrow

    StateArrow = fade + 1
    last_fade_time = Bladex.GetTime()


def MoveArrow(entity,time):
    global last_start_time
    global Forward_Arrow
    global StateArrow

    if StateArrow:
        delta_time = time - last_start_time

        if delta_time >= 0.33:
            last_start_time = time
            delta_time = 0

            if Forward_Arrow:
                Forward_Arrow = 0
            else:
                Forward_Arrow = 1

        Disp = delta_time * 0.03

        Y = 15.0

        if Forward_Arrow:
            Scorer.wFrame.MoveWidgetTo("FlechaIzqWidget",0.03 - Disp,Y)
            Scorer.wFrame.MoveWidgetTo("FlechaDerWidget",0.97 + Disp,Y)
        else:
            Scorer.wFrame.MoveWidgetTo("FlechaIzqWidget",0.02 + Disp,Y)
            Scorer.wFrame.MoveWidgetTo("FlechaDerWidget",0.98 - Disp,Y)
    if StateArrow == 2:
        delta_time = time - last_fade_time
        delta_time = delta_time * 2.0

        if delta_time >= 1.0:
            delta_time = 1.0
            StateArrow = 0

        alpha = 1.0 - delta_time

        FlechaIzqWidget.SetAlpha(alpha)
        FlechaDerWidget.SetAlpha(alpha)
    elif StateArrow == 3:
        alpha = time - last_fade_time
        alpha = alpha * 2.0

        if alpha <= 0.0:
            delta_time = 0.0
            StateArrow = 1
            #FlechaIzqWidget.SetAlpha(alpha)
            #FlechaDerWidget.SetAlpha(alpha)

        FlechaIzqWidget.SetAlpha(alpha)
        FlechaDerWidget.SetAlpha(alpha)


char = Bladex.GetEntity("Player1")
char.TimerFunc = MoveArrow
char.SubscribeToList("Timer60")

#Scorer.wFrame.MoveWidgetTo("Yes",0.6,30)
#Scorer.wFrame.MoveWidgetTo("No",0.65,30)

def PressKeyEnter():
    global ScreenSelectionFinished
    global YesNoValue
    global YesNoActivated

    if YesNoActivated:
        print "YesNoActivated 1"
        if ScreenSelectionFinished:
            print "ScreenSelectionFinished 1"
            ScreenSelectionFinished = 0

            YesNoActivated = 0
            AreYouSureWidget.SetVisible(0)
            Bladex.AddScheduledFunc(Bladex.GetTime() + 0.6,SelectCharacterWidget.SetVisible,(1,))
            Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,ScreenSelectionFinish,())
            YesWidget.SetVisible(0)
            NoWidget.SetVisible(0)

            InfoCharWidget1.SetVisible(0)
            InfoCharWidget2.SetVisible(0)
            InfoCharWidget3.SetVisible(0)
            InfoCharWidget4.SetVisible(0)

            fondo1.SetVisible(0)
            fondo2.SetVisible(0)
            fondo3.SetVisible(0)
            FlechaIzqWidget.SetVisible(1)
            FlechaDerWidget.SetVisible(1)

            SlideFrame(1)

            if YesNoValue:
                print "YesNoValue 1"
                Menu.SwitchToCasaMenu()
                Menu.ActivateMenu()
                Menu.Character = CurrentPerson

                File = open("../2DMap/2dMapData.txt","w")
                if CurrentPerson == 0:
                    File.write("AM")
                if CurrentPerson == 1:
                    File.write("BR")
                if CurrentPerson == 2:
                    File.write("KN")
                if CurrentPerson == 3:
                    File.write("DW")
                File.close()
    elif Stoped:
        if ScreenSelectionFinished:
            if Reference.DEMO_MODE==1 and CurrentPerson == 0 and ("AM" not in Reference.DEMO_PLAYERS):
                print "Amazon not available in demo"
                GameText.WriteTextAux(MenuText.GetMenuText("Amazon not available in demo mode"),2.0,255,255,255,[])
                return
            if Reference.DEMO_MODE==1 and CurrentPerson == 1 and ("BR" not in Reference.DEMO_PLAYERS):
                print "Barbarian not available in demo"
                GameText.WriteTextAux(MenuText.GetMenuText("Barbarian not available in demo mode"),2.0,255,255,255,[])
                return
            if Reference.DEMO_MODE==1 and CurrentPerson == 2 and ("KN" not in Reference.DEMO_PLAYERS):
                print "Knight not available in demo"
                GameText.WriteTextAux(MenuText.GetMenuText("Knight not available in demo mode"),2.0,255,255,255,[])
                return
            if Reference.DEMO_MODE==1 and CurrentPerson == 3 and ("DW" not in Reference.DEMO_PLAYERS):
                print "Dwarf not available in demo"
                GameText.WriteTextAux(MenuText.GetMenuText("Dwarf not available in demo mode"),2.0,255,255,255,[])
                return

            ScreenSelectionFinished = 0
            YesNoActivated = 1
            YesNoValue = 1
            Bladex.AddScheduledFunc(Bladex.GetTime() + 0.6,ActivateWiggetInfoChar,())
            SelectCharacterWidget.SetVisible(0)
            FlechaIzqWidget.SetVisible(0)
            FlechaDerWidget.SetVisible(0)
            SlideFrame(0)
            marco1.SetVisible(1)
            marco2.SetVisible(1)
            marco3.SetVisible(1)
            marco4.SetVisible(1)
            marco5.SetVisible(1)
            marco6.SetVisible(1)

CreateWidgetAreYouSure()
CreateWidgetInfoChar()
CreateWidgetMarco()

def PressKeyEsc():
    global YesNoActivated
    global ScreenSelectionFinished

    if YesNoActivated:
        if ScreenSelectionFinished:
            ScreenSelectionFinished = 0
            YesNoActivated = 0
            AreYouSureWidget.SetVisible(0)
            Bladex.AddScheduledFunc(Bladex.GetTime() + 0.6,SelectCharacterWidget.SetVisible,(1,))
            Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,ScreenSelectionFinish,())
            YesWidget.SetVisible(0)
            NoWidget.SetVisible(0)

            InfoCharWidget1.SetVisible(0)
            InfoCharWidget2.SetVisible(0)
            InfoCharWidget3.SetVisible(0)
            InfoCharWidget4.SetVisible(0)

            fondo1.SetVisible(0)
            fondo2.SetVisible(0)
            fondo3.SetVisible(0)
            FlechaIzqWidget.SetVisible(1)
            FlechaDerWidget.SetVisible(1)
            SlideFrame(1)
    else:
        Menu.ActivateMenu()

import BInput

InputManager=BInput.GetInputManager()
LastOne = InputManager.GetInputActionsSet()
InputManager.SetInputActionsSet("Default")

Bladex.AddInputAction("Retrocede",0)
Bladex.AddInputAction("Avanza",0)
Bladex.AddInputAction("Selecciona",0)
Bladex.AddInputAction("Cancelar",0)

def RedefineKeys():
	import BInput

	InputManager=BInput.GetInputManager()
	LastOne = InputManager.GetInputActionsSet()
	InputManager.SetInputActionsSet("Default")

	Bladex.AssocKey("Retrocede","Keyboard","Right")
	Bladex.AssocKey("Avanza","Keyboard","Left")
	Bladex.AssocKey("Selecciona","Keyboard","Enter")
	Bladex.AssocKey("Cancelar","Keyboard","Esc")

	InputManager.SetInputActionsSet(LastOne)

KeybWidget.AdditionalKeysCallBack = RedefineKeys

RedefineKeys()

Bladex.AddBoundFunc("Retrocede",PressKeyX)
Bladex.AddBoundFunc("Avanza",PressKeyZ)
Bladex.AddBoundFunc("Selecciona",PressKeyEnter)
Bladex.AddBoundFunc("Cancelar",PressKeyEsc)
InputManager.SetInputActionsSet(LastOne)


HouseActive = 0

# funcion callback indica que El Usuario Presiona La Tecla Escape
def ElUsuarioPresionaLaTeclaEscape(Salio):
    global HouseActive
    if Salio:
        HouseActive = 1
    else:
        if HouseActive:
            Menu.SwitchToGlobalMenu()
        return not HouseActive



Menu.EscapeFunction = ElUsuarioPresionaLaTeclaEscape

def SetDefaultPerson():
    global CurrentPerson
    global FinishPerson

    CurrentPerson = 3
    FinishPerson = 3

    cam = Bladex.GetEntity("Camera")
    cam.SetMaxCamera("Seleccion_Camera_seleccion_enano.cam",0,-1)

def ActivateStartWidgets():
    SelectCharacterWidget.SetVisible(1)
    FlechaDerWidget.SetVisible(1)
    FlechaIzqWidget.SetVisible(1)

def DeactivateStartWidgets():
    SelectCharacterWidget.SetVisible(0)
    FlechaDerWidget.SetVisible(0)
    FlechaIzqWidget.SetVisible(0)

def OnEnterDemoCasa():
    DeactivateStartWidgets()

def OnLeaveDemoCasa():
    global CurrentPerson
    ActivateStartWidgets()
    cam = Bladex.GetEntity("Camera")
    cam.SetMaxCamera(CameraPerson[CurrentPerson],0,-1)
    #SetDefaultPerson()

PrecargaBackgroundCharacters()
