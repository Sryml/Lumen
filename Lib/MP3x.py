# This file was created automatically by SWIG.
import MP3xc
class B_MP3PlayerPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            MP3xc.delete_B_MP3Player(self.this)
    def Load(self,arg0):
        val = MP3xc.B_MP3Player_Load(self.this,arg0)
        return val
    def Play(self):
        val = MP3xc.B_MP3Player_Play(self.this)
        return val
    def Stop(self):
        val = MP3xc.B_MP3Player_Stop(self.this)
        return val
    def SetVolume(self,arg0):
        val = MP3xc.B_MP3Player_SetVolume(self.this,arg0)
        return val
    def SetPCMVolume(self,arg0):
        val = MP3xc.B_MP3Player_SetPCMVolume(self.this,arg0)
        return val
    def SetBalance(self,arg0):
        val = MP3xc.B_MP3Player_SetBalance(self.this,arg0)
        return val
    def GetDuration(self):
        val = MP3xc.B_MP3Player_GetDuration(self.this)
        return val
    def GetMP3Type(self):
        val = MP3xc.B_MP3Player_GetMP3Type(self.this)
        return val
    def GetPlayerState(self):
        val = MP3xc.B_MP3Player_GetPlayerState(self.this)
        return val
    def GetLastError(self):
        val = MP3xc.B_MP3Player_GetLastError(self.this)
        return val
    def GetFileName(self):
        val = MP3xc.B_MP3Player_GetFileName(self.this)
        return val
    def __repr__(self):
        return "<C B_MP3Player instance>"
class B_MP3Player(B_MP3PlayerPtr):
    def __init__(self,arg0,*args) :
        self.this = apply(MP3xc.new_B_MP3Player,(arg0,)+args)
        self.thisown = 1






#-------------- FUNCTION WRAPPERS ------------------



#-------------- VARIABLE WRAPPERS ------------------

