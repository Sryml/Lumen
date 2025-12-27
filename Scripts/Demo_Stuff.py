####################################################################################
#
#
#
#    			dd ee mm oo !! !! !! !!
#
#
#
####################################################################################

import Bladex
import Reference
import Menu

import Raster

import BUIx
import BBLib
import BInput

import darfuncs
import GameText
import TutorialScorer

import Language

fading_start_time=0
logo_rebel = 0
logo_severance=0


last_demo_msg_time=0

demo_is_active=0
prev_was_menu=0



LOGOS_FULL=1

TutorialScorer.ActivateTutorialScorer(Language.LetrasMenuBig)
TutorialScorer.wMultiText.SetScale(0.5)
TutorialScorer.wMultiText.SetColor(255,0,0)

LastMessage = 0


OnEnterDemo=0
OnExitDemo=0

def StaticLogoRebel(time):
    global last_demo_msg_time
    global logo_rebel
    global logo_severance
    global fading_start_time
    global LastMessage

    alpha= (time-fading_start_time)*0.25
    if alpha>0.8:
        alpha=0.8
    if alpha<0:
        alpha=0

    if time-last_demo_msg_time>3.0:
        GameText.WriteTextAux("DEMO mode - press any key",2.0,255,255,255,[])
        last_demo_msg_time=time

    w, h = Raster.GetSize()

    Raster.SetPosition(w-136,h-90-10)
    Raster.SetAlpha(alpha)
    Raster.DrawBitmap(logo_rebel,128,90)

    Raster.SetPosition(w/2.0-128,-90)
    Raster.SetAlpha(alpha)
    Raster.DrawBitmap(logo_severance,256,256)



def FadeLogoRebel(time):
    global logo_rebel
    global fading_start_time

    """
    alpha= 1.0-(time-fading_start_time)*0.5
    if alpha>1:
        alpha=1
    elif alpha>0:
        Bladex.SetAfterFrameFunc("FadeLogoRebel", FadeLogoRebel)
    else:
        alpha=0
        Bladex.RemoveAfterFrameFunc("FadeLogoRebel")
        fading_start_time=Bladex.GetTime()+0.5
    """

    if (time-fading_start_time<2):
        alpha= (time-fading_start_time)*0.5
    else:
        alpha= 1.0-(time-fading_start_time-2)*0.5


    if alpha>1:
        alpha=1
    elif alpha<=0:
        alpha=0
        if (time-fading_start_time>1):
            Bladex.RemoveAfterFrameFunc("FadeLogoRebel")
            fading_start_time=Bladex.GetTime()+0.5


    #print "Alpha rebel is " + str(alpha)

    Raster.SetPenColor(255,255,255)
    Raster.SetAlpha(alpha)

    if LOGOS_FULL==1:
        Raster.SetPosition(0,0)
        Raster.DrawBitmap(logo_rebel,Raster.GetSize()[0],Raster.GetSize()[1])
    else:
        Raster.SetPosition(Raster.GetSize()[0]-256,Raster.GetSize()[1]-256)
        Raster.DrawBitmap(logo_rebel,255,255)



def LaunchDemoCamera2(a,b):
    global fading_start_time
    global LastMessage

    fading_start_time=Bladex.GetTime()+1
    Bladex.RemoveAfterFrameFunc("StaticLogoRebel")
    Bladex.SetAfterFrameFunc("FadeLogoRebel", FadeLogoRebel)
    darfuncs.LaunchMaxCamera("demo_travelling.cam",0,-1,LaunchDemoCamera)


def LaunchDemoCamera(a,b):

    """
    if Bladex.GetCurrentMap()=="Casa":
        Deactivate4Demo()
    """
    darfuncs.LaunchMaxCamera("demo_travelling.cam",0,-1,LaunchDemoCamera2)


import pdb
def FinishDemoFunc(x,y,z):
    global Listener

    print "Demo_Stuff.FinishDemoFunc called"

    BInput.GetInputManager().GetAttachedDevice("Keyboard").RemoveListener("EndDemo")
    Listener = None
    DemoLoop()


def DemoLoop():
    global fading_start_time
    global demo_is_active
    global prev_was_menu
    global Listener
    global LastMessage

    global CurrentPerson
    global FinishPerson

    AppMode=Bladex.GetAppMode()
    import Scorer

    if AppMode=="Menu":
        demo_is_active=1
        prev_was_menu=1
        print "DemoLoop-Menu2Demo"
        Menu.ActivateMenu()
        print "DemoLoop , activatemenu en menu2demo"
        Bladex.SetAppMode("Demo")

        if OnEnterDemo:
            OnEnterDemo()

        print "demo mode set up"
        #Bladex.KillMusic()
        Bladex.ExeMusicEvent( Bladex.GetMusicEvent("musica_loop_demo") )
        fading_start_time=Bladex.GetTime()+1
        Bladex.SetAfterFrameFunc("FadeLogoRebel", FadeLogoRebel)

        Listener=BInput.B_InputListener("EndDemo")
        Listener.SetPythonFunc(FinishDemoFunc)
        BInput.GetInputManager().GetAttachedDevice("Keyboard").AddListener(Listener)

        Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, LaunchDemoCamera,(0,0))
        Scorer.SetVisible(0)

    elif AppMode=="Demo":
        demo_is_active=0
        Bladex.ActivateInput() #la funcion launchMaxcamera la habia desactivado!
        print "DemoLoop-Demo2Menu"
        if prev_was_menu==1:
            Menu.ActivateMenu()
            print "set menu mode"
            Bladex.SetAppMode("Menu")
        else:
            print "NO set 2 menu mode"
            Bladex.SetAppMode("Game")

        if OnExitDemo:
            OnExitDemo()

        #Bladex.KillMusic()
        Bladex.ExeMusicEvent(-1)
        Bladex.RemoveAfterFrameFunc("FadeLogoRebel")
        Bladex.RemoveAfterFrameFunc("StaticLogoRebel")

        prev_was_menu=0

        cam=Bladex.GetEntity("Camera")

        if Bladex.GetCurrentMap()!="Casa":
            cam.SetPersonView("Player1")
            cam.Cut()
            Bladex.SetListenerPosition(1)
            Scorer.SetVisible(1)

    elif AppMode=="Game":
        prev_was_menu=0
        demo_is_active=1
        print "DemoLoop-Game2Demo"
        Bladex.SetAppMode("Demo")
        print "demo mode set up"
        #Bladex.KillMusic()
        Bladex.ExeMusicEvent( Bladex.GetMusicEvent("musica_loop_demo") )
        fading_start_time=Bladex.GetTime()+1
        Bladex.SetAfterFrameFunc("FadeLogoRebel", FadeLogoRebel)

        if OnEnterDemo:
            OnEnterDemo()

        Listener=BInput.B_InputListener("EndDemo")
        Listener.SetPythonFunc(FinishDemoFunc)
        BInput.GetInputManager().GetAttachedDevice("Keyboard").AddListener(Listener)

        LaunchDemoCamera(0,0)
        Scorer.SetVisible(0)










#
# Init
#
def Init():
    global logo_rebel
    global logo_severance


    #
    # FUNC itself
    #
    if Reference.DEMO_MODE==1:
        Bladex.SetMenuTgapFunc(DemoLoop)
    else:
        return



    #
    # LOGO REBELACT
    #
    BBLib.ReadMMP("../../Data/logorebel.mmp")
    logo_rebel=Raster.BmpHandle("LOGOREBELALFA")



    #
    # LOGO SEVERANCE
    #
    BBLib.ReadMMP("../../Data/logoseverance256.mmp")
    logo_severance=Raster.BmpHandle("LOGOSEVERANCE")



    #
    # MUSICAS
    #
    Bladex.AddMusicEventMP3  ( "musica_loop_demo",     "../../Sounds/tema.mp3",          0.1, 1.0, 1.0, 11000,     0, -1 )
    Bladex.AddMusicEventMP3  ( "emptyloquesea_demo",   "",                                  0.1, 0.1, 1.0, 11000,     0, 0 )
