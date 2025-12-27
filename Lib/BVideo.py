# This file was created automatically by SWIG.
import BVideoc
class B_VideoPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BVideoc.delete_B_Video(self.this)
    def SetVideo(self,arg0):
        val = BVideoc.B_Video_SetVideo(self.this,arg0)
        return val
    def CloseVideo(self):
        val = BVideoc.B_Video_CloseVideo(self.this)
        return val
    def GetDimension(self):
        val = BVideoc.B_Video_GetDimension(self.this)
        return val
    def GetLength(self):
        val = BVideoc.B_Video_GetLength(self.this)
        return val
    def GetData(self,arg0):
        val = BVideoc.B_Video_GetData(self.this,arg0)
        return val
    def GetName(self):
        val = BVideoc.B_Video_GetName(self.this)
        return val
    def __repr__(self):
        return "<C B_Video instance>"
class B_Video(B_VideoPtr):
    def __init__(self) :
        self.this = BVideoc.new_B_Video()
        self.thisown = 1






#-------------- FUNCTION WRAPPERS ------------------



#-------------- VARIABLE WRAPPERS ------------------

