# This file was created automatically by SWIG.
import BImagexc
class B_ImageFXPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BImagexc.delete_B_ImageFX(self.this)
    def SetSharedBuffer(self,arg0):
        val = BImagexc.B_ImageFX_SetSharedBuffer(self.this,arg0.this)
        return val
    def ClearBuffer(self):
        val = BImagexc.B_ImageFX_ClearBuffer(self.this)
        return val
    def GetDimension(self):
        val = BImagexc.B_ImageFX_GetDimension(self.this)
        return val
    def GetBufferSize(self):
        val = BImagexc.B_ImageFX_GetBufferSize(self.this)
        return val
    def Apply(self):
        val = BImagexc.B_ImageFX_Apply(self.this)
        return val
    def SetOwnsBuffer(self,arg0):
        val = BImagexc.B_ImageFX_SetOwnsBuffer(self.this,arg0)
        return val
    def GetOwnsBuffer(self):
        val = BImagexc.B_ImageFX_GetOwnsBuffer(self.this)
        return val
    def CopyToBuffer2(self):
        val = BImagexc.B_ImageFX_CopyToBuffer2(self.this)
        return val
    def GetFromBuffer2(self,arg0):
        val = BImagexc.B_ImageFX_GetFromBuffer2(self.this,arg0)
        return val
    def GetImageBuffer(self):
        val = BImagexc.B_ImageFX_GetImageBuffer(self.this)
        return val
    def SetImageBuffer(self,arg0,arg1,*args):
        val = apply(BImagexc.B_ImageFX_SetImageBuffer,(self.this,arg0,arg1,)+args)
        return val
    def CopyImageBuffer(self,arg0,arg1,arg2):
        val = BImagexc.B_ImageFX_CopyImageBuffer(self.this,arg0,arg1,arg2)
        return val
    def CopySubBuffer(self,arg0,arg1,arg2,arg3,arg4,*args):
        val = apply(BImagexc.B_ImageFX_CopySubBuffer,(self.this,arg0,arg1,arg2,arg3,arg4,)+args)
        return val
    def __repr__(self):
        return "<C B_ImageFX instance>"
class B_ImageFX(B_ImageFXPtr):
    def __init__(self) :
        self.this = BImagexc.new_B_ImageFX()
        self.thisown = 1




class B_BWFilterPtr(B_ImageFXPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BImagexc.delete_B_BWFilter(self.this)
    def Apply(self):
        val = BImagexc.B_BWFilter_Apply(self.this)
        return val
    def __repr__(self):
        return "<C B_BWFilter instance>"
class B_BWFilter(B_BWFilterPtr):
    def __init__(self) :
        self.this = BImagexc.new_B_BWFilter()
        self.thisown = 1




class B_GridFilterPtr(B_ImageFXPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BImagexc.delete_B_GridFilter(self.this)
    def SetCoefficient(self,arg0,arg1,arg2):
        val = BImagexc.B_GridFilter_SetCoefficient(self.this,arg0,arg1,arg2)
        return val
    def GetCoefficient(self,arg0,arg1):
        val = BImagexc.B_GridFilter_GetCoefficient(self.this,arg0,arg1)
        return val
    def SetCoefficients(self,arg0):
        val = BImagexc.B_GridFilter_SetCoefficients(self.this,arg0)
        return val
    def Apply(self):
        val = BImagexc.B_GridFilter_Apply(self.this)
        return val
    def __repr__(self):
        return "<C B_GridFilter instance>"
class B_GridFilter(B_GridFilterPtr):
    def __init__(self) :
        self.this = BImagexc.new_B_GridFilter()
        self.thisown = 1




class B_GridSubFilterPtr(B_GridFilterPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BImagexc.delete_B_GridSubFilter(self.this)
    def __repr__(self):
        return "<C B_GridSubFilter instance>"
class B_GridSubFilter(B_GridSubFilterPtr):
    def __init__(self) :
        self.this = BImagexc.new_B_GridSubFilter()
        self.thisown = 1




class B_SideDistortFilterPtr(B_ImageFXPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BImagexc.delete_B_SideDistortFilter(self.this)
    def SetDistance(self,arg0):
        val = BImagexc.B_SideDistortFilter_SetDistance(self.this,arg0)
        return val
    def GetDistance(self):
        val = BImagexc.B_SideDistortFilter_GetDistance(self.this)
        return val
    def __repr__(self):
        return "<C B_SideDistortFilter instance>"
class B_SideDistortFilter(B_SideDistortFilterPtr):
    def __init__(self) :
        self.this = BImagexc.new_B_SideDistortFilter()
        self.thisown = 1






#-------------- FUNCTION WRAPPERS ------------------



#-------------- VARIABLE WRAPPERS ------------------

