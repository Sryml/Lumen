# This file was created automatically by SWIG.
import BBLibc
class B_BitMap24Ptr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BBLibc.delete_B_BitMap24(self.this)
    def GetDimension(self):
        val = BBLibc.B_BitMap24_GetDimension(self.this)
        return val
    def GetData(self):
        val = BBLibc.B_BitMap24_GetData(self.this)
        return val
    def Clear(self):
        #:TODO:
        #val = BBLibc.B_BitMap24_Clear(self.this)
        #return val
        return 0
    def SaveToBMP(self,arg0):
        val = BBLibc.B_BitMap24_SaveToBMP(self.this,arg0)
        return val
    def ReadFromBMP(self,arg0):
        val = BBLibc.B_BitMap24_ReadFromBMP(self.this,arg0)
        return val
    def SaveToJPEG(self,arg0,*args):
        val = apply(BBLibc.B_BitMap24_SaveToJPEG,(self.this,arg0,)+args)
        return val
    def ReadFromJPEG(self,arg0):
        val = BBLibc.B_BitMap24_ReadFromJPEG(self.this,arg0)
        return val
    def ReadFromFile(self,arg0):
        val = BBLibc.B_BitMap24_ReadFromFile(self.this,arg0)
        return val
    def SaveToFile(self,arg0,*args):
        val = apply(BBLibc.B_BitMap24_SaveToFile,(self.this,arg0,)+args)
        return val
    def ChangeRGBOrder(self):
        val = BBLibc.B_BitMap24_ChangeRGBOrder(self.this)
        return val
    def __repr__(self):
        return "<C B_BitMap24 instance>"
class B_BitMap24(B_BitMap24Ptr):
    def __init__(self,*args) :
        self.this = apply(BBLibc.new_B_BitMap24,()+args)
        self.thisown = 1




class B_ResourceManagerPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def NResources(self,arg0):
        val = BBLibc.B_ResourceManager_NResources(self.this,arg0)
        return val
    def GetResourceName(self,arg0,arg1):
        val = BBLibc.B_ResourceManager_GetResourceName(self.this,arg0,arg1)
        return val
    def GetResourceFile(self,arg0,arg1):
        val = BBLibc.B_ResourceManager_GetResourceFile(self.this,arg0,arg1)
        return val
    def IsResourceLoaded(self,arg0,arg1):
        val = BBLibc.B_ResourceManager_IsResourceLoaded(self.this,arg0,arg1)
        return val
    def SaveResource(self,arg0,arg1,arg2):
        val = BBLibc.B_ResourceManager_SaveResource(self.this,arg0,arg1,arg2)
        return val
    def LoadResourceToMemory(self,arg0,arg1):
        val = BBLibc.B_ResourceManager_LoadResourceToMemory(self.this,arg0,arg1)
        return val
    def GetnFiles(self):
        val = BBLibc.B_ResourceManager_GetnFiles(self.this)
        return val
    def GetFile(self,arg0):
        val = BBLibc.B_ResourceManager_GetFile(self.this,arg0)
        return val
    def __repr__(self):
        return "<C B_ResourceManager instance>"
class B_ResourceManager(B_ResourceManagerPtr):
    def __init__(self,this):
        self.this = this






#-------------- FUNCTION WRAPPERS ------------------

GetnOpenedInputFiles = BBLibc.GetnOpenedInputFiles

GetnOpenInputFiles = BBLibc.GetnOpenInputFiles

ResetnOpenedInputFiles = BBLibc.ResetnOpenedInputFiles

SetOnOpenInputFileFunc = BBLibc.SetOnOpenInputFileFunc

RemoveOnOpenInputFileFunc = BBLibc.RemoveOnOpenInputFileFunc

ReadBOD = BBLibc.ReadBOD

LoadBOD = BBLibc.LoadBOD

ReadAutoBOD = BBLibc.ReadAutoBOD

ReadMMP = BBLibc.ReadMMP

SaveBODData = BBLibc.SaveBODData

LoadBODData = BBLibc.LoadBODData

SaveAutoBODData = BBLibc.SaveAutoBODData

LoadAutoBODData = BBLibc.LoadAutoBODData

LoadResourceToMemory = BBLibc.LoadResourceToMemory

GetCurrentLanguage = BBLibc.GetCurrentLanguage

GetConfigDirectory = BBLibc.GetConfigDirectory

def GetResourceManager():
    val = BBLibc.GetResourceManager()
    val = B_ResourceManagerPtr(val)
    return val



#-------------- VARIABLE WRAPPERS ------------------

B_CID_OBJDSCR = BBLibc.B_CID_OBJDSCR
B_CID_BITMAP = BBLibc.B_CID_BITMAP
B_CID_BMP = BBLibc.B_CID_BMP
B_CID_ALPHABMP = BBLibc.B_CID_ALPHABMP
B_CID_AUTO_OBJDSCR = BBLibc.B_CID_AUTO_OBJDSCR
