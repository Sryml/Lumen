# This file was created automatically by SWIG.
import BUIxc
class B_FontPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def GetFirst(self):
        val = BUIxc.B_Font_GetFirst(self.this)
        return val
    def GetLast(self):
        val = BUIxc.B_Font_GetLast(self.this)
        return val
    def GetTextWidth(self,arg0):
        val = BUIxc.B_Font_GetTextWidth(self.this,arg0)
        return val
    def GetHeight(self,arg0):
        val = BUIxc.B_Font_GetHeight(self.this,arg0)
        return val
    def __str__(self):
        val = BUIxc.B_Font___str__(self.this)
        return val
    def GetPointer(self):
        val = BUIxc.B_Font_GetPointer(self.this)
        return val
    def __repr__(self):
        return "<C B_Font instance>"
class B_Font(B_FontPtr):
    def __init__(self,this):
        self.this = this




class B_FontServerPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_FontServer(self.this)
    def CreateBFont(self,arg0,*args):
        val = apply(BUIxc.B_FontServer_CreateBFont,(self.this,arg0,)+args)
        val = B_FontPtr(val)
        val.thisown = 1
        return val
    def GetBFont(self,arg0):
        val = BUIxc.B_FontServer_GetBFont(self.this,arg0)
        val = B_FontPtr(val)
        return val
    def DestroyBFont(self,arg0):
        val = BUIxc.B_FontServer_DestroyBFont(self.this,arg0.this)
        return val
    def __repr__(self):
        return "<C B_FontServer instance>"
class B_FontServer(B_FontServerPtr):
    def __init__(self) :
        self.this = BUIxc.new_B_FontServer()
        self.thisown = 1




class B_WidgetPtr :
    B_LAB_Left = BUIxc.B_Widget_B_LAB_Left
    B_LAB_Right = BUIxc.B_Widget_B_LAB_Right
    B_LAB_HCenter = BUIxc.B_Widget_B_LAB_HCenter
    B_LAB_Top = BUIxc.B_Widget_B_LAB_Top
    B_LAB_Bottom = BUIxc.B_Widget_B_LAB_Bottom
    B_LAB_VCenter = BUIxc.B_Widget_B_LAB_VCenter
    B_FR_AbsoluteLeft = BUIxc.B_Widget_B_FR_AbsoluteLeft
    B_FR_AbsoluteRight = BUIxc.B_Widget_B_FR_AbsoluteRight
    B_FR_HRelative = BUIxc.B_Widget_B_FR_HRelative
    B_FR_AbsoluteTop = BUIxc.B_Widget_B_FR_AbsoluteTop
    B_FR_AbsoluteBottom = BUIxc.B_Widget_B_FR_AbsoluteBottom
    B_FR_VRelative = BUIxc.B_Widget_B_FR_VRelative
    B_FR_Left = BUIxc.B_Widget_B_FR_Left
    B_FR_Right = BUIxc.B_Widget_B_FR_Right
    B_FR_HCenter = BUIxc.B_Widget_B_FR_HCenter
    B_FR_Top = BUIxc.B_Widget_B_FR_Top
    B_FR_Bottom = BUIxc.B_Widget_B_FR_Bottom
    B_FR_VCenter = BUIxc.B_Widget_B_FR_VCenter
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_Widget(self.this)
    def SetSize(self,arg0,arg1):
        val = BUIxc.B_Widget_SetSize(self.this,arg0,arg1)
        return val
    def GetSize(self):
        val = BUIxc.B_Widget_GetSize(self.this)
        return val
    def SetAutoScale(self,arg0):
        val = BUIxc.B_Widget_SetAutoScale(self.this,arg0)
        return val
    def SetScale(self,arg0):
        val = BUIxc.B_Widget_SetScale(self.this,arg0)
        return val
    def GetAutoScale(self):
        val = BUIxc.B_Widget_GetAutoScale(self.this)
        return val
    def __str__(self):
        val = BUIxc.B_Widget___str__(self.this)
        return val
    def Name(self):
        val = BUIxc.B_Widget_Name(self.this)
        return val
    def GetPosition(self):
        val = BUIxc.B_Widget_GetPosition(self.this)
        return val
    def SetDrawFunc(self,arg0):
        val = BUIxc.B_Widget_SetDrawFunc(self.this,arg0)
        return val
    def DefDraw(self,arg0,arg1,arg2):
        val = BUIxc.B_Widget_DefDraw(self.this,arg0,arg1,arg2)
        return val
    def SetSizeChangedFunc(self,arg0):
        val = BUIxc.B_Widget_SetSizeChangedFunc(self.this,arg0)
        return val
    def DefSizeChanged(self,arg0,arg1):
        val = BUIxc.B_Widget_DefSizeChanged(self.this,arg0,arg1)
        return val
    def SetData(self,arg0):
        val = BUIxc.B_Widget_SetData(self.this,arg0)
        return val
    def GetPointer(self):
        val = BUIxc.B_Widget_GetPointer(self.this)
        return val
    def SetColor(self,arg0,arg1,arg2):
        val = BUIxc.B_Widget_SetColor(self.this,arg0,arg1,arg2)
        return val
    def GetColor(self):
        val = BUIxc.B_Widget_GetColor(self.this)
        return val
    def SetAlpha(self,arg0):
        val = BUIxc.B_Widget_SetAlpha(self.this,arg0)
        return val
    def GetAlpha(self):
        val = BUIxc.B_Widget_GetAlpha(self.this)
        return val
    def MultiplyAlpha(self,arg0):
        val = BUIxc.B_Widget_MultiplyAlpha(self.this,arg0)
        return val
    def AddAlpha(self,arg0):
        val = BUIxc.B_Widget_AddAlpha(self.this,arg0)
        return val
    def AddLabel(self,arg0,arg1,arg2,*args):
        val = apply(BUIxc.B_Widget_AddLabel,(self.this,arg0.this,arg1,arg2,)+args)
        return val
    def RecalcLabelLayout(self,arg0,arg1):
        val = BUIxc.B_Widget_RecalcLabelLayout(self.this,arg0,arg1)
        return val
    def ProcessCommand(self,arg0):
        val = BUIxc.B_Widget_ProcessCommand(self.this,arg0)
        return val
    def SetVisible(self,arg0):
        val = BUIxc.B_Widget_SetVisible(self.this,arg0)
        return val
    def GetVisible(self):
        val = BUIxc.B_Widget_GetVisible(self.this)
        return val
    def SetClipDraw(self,arg0):
        val = BUIxc.B_Widget_SetClipDraw(self.this,arg0)
        return val
    def GetClipDraw(self):
        val = BUIxc.B_Widget_GetClipDraw(self.this)
        return val
    def SetClipChildren(self,arg0):
        val = BUIxc.B_Widget_SetClipChildren(self.this,arg0)
        return val
    def GetClipChildren(self):
        val = BUIxc.B_Widget_GetClipChildren(self.this)
        return val
    def GetHasFocus(self):
        val = BUIxc.B_Widget_GetHasFocus(self.this)
        return val
    def SetHasFocus(self,*args):
        val = apply(BUIxc.B_Widget_SetHasFocus,(self.this,)+args)
        return val
    def AcceptsFocus(self):
        val = BUIxc.B_Widget_AcceptsFocus(self.this)
        return val
    def __repr__(self):
        return "<C B_Widget instance>"
class B_Widget(B_WidgetPtr):
    def __init__(self,arg0,arg1,arg2,arg3) :
        self.this = BUIxc.new_B_Widget(arg0.this,arg1,arg2,arg3)
        self.thisown = 1




class B_RectWidgetPtr(B_WidgetPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_RectWidget(self.this)
    def SetSize(self,arg0,arg1):
        val = BUIxc.B_RectWidget_SetSize(self.this,arg0,arg1)
        return val
    def SetBitmap(self,arg0):
        val = BUIxc.B_RectWidget_SetBitmap(self.this,arg0)
        return val
    def SetBitmapIndex(self,arg0):
        val = BUIxc.B_RectWidget_SetBitmapIndex(self.this,arg0)
        return val
    def SetBitmapCoords(self,arg0,arg1,arg2,arg3):
        val = BUIxc.B_RectWidget_SetBitmapCoords(self.this,arg0,arg1,arg2,arg3)
        return val
    def SetBorderColor(self,arg0,arg1,arg2):
        val = BUIxc.B_RectWidget_SetBorderColor(self.this,arg0,arg1,arg2)
        return val
    def GetBorderColor(self):
        val = BUIxc.B_RectWidget_GetBorderColor(self.this)
        return val
    def SetBorder(self,arg0):
        val = BUIxc.B_RectWidget_SetBorder(self.this,arg0)
        return val
    def GetBorder(self):
        val = BUIxc.B_RectWidget_GetBorder(self.this)
        return val
    def SetSolid(self,arg0):
        val = BUIxc.B_RectWidget_SetSolid(self.this,arg0)
        return val
    def GetSolid(self):
        val = BUIxc.B_RectWidget_GetSolid(self.this)
        return val
    def __repr__(self):
        return "<C B_RectWidget instance>"
class B_RectWidget(B_RectWidgetPtr):
    def __init__(self,arg0,arg1,arg2,arg3) :
        self.this = BUIxc.new_B_RectWidget(arg0.this,arg1,arg2,arg3)
        self.thisown = 1




class B_FrameWidgetPtr(B_RectWidgetPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_FrameWidget(self.this)
    def SetSize(self,arg0,arg1):
        val = BUIxc.B_FrameWidget_SetSize(self.this,arg0,arg1)
        return val
    def AddWidget(self,arg0,arg1,arg2,*args):
        val = apply(BUIxc.B_FrameWidget_AddWidget,(self.this,arg0.this,arg1,arg2,)+args)
        return val
    def RemoveWidget(self,arg0,*args):
        val = apply(BUIxc.B_FrameWidget_RemoveWidget,(self.this,arg0,)+args)
        return val
    def RemoveWidget_Idx(self,arg0,*args):
        val = apply(BUIxc.B_FrameWidget_RemoveWidget_Idx,(self.this,arg0,)+args)
        return val
    def nWidgets(self):
        val = BUIxc.B_FrameWidget_nWidgets(self.this)
        return val
    def GetWidget(self,arg0):
        val = BUIxc.B_FrameWidget_GetWidget(self.this,arg0)
        val = B_WidgetPtr(val)
        return val
    def GetWidget_Idx(self,arg0):
        val = BUIxc.B_FrameWidget_GetWidget_Idx(self.this,arg0)
        val = B_WidgetPtr(val)
        return val
    def MoveWidgetTo(self,arg0,arg1,arg2):
        val = BUIxc.B_FrameWidget_MoveWidgetTo(self.this,arg0,arg1,arg2)
        return val
    def MoveWidgetRightTo(self,arg0,arg1,arg2):
        val = BUIxc.B_FrameWidget_MoveWidgetRightTo(self.this,arg0,arg1,arg2)
        return val
    def MoveWidgetTo_Idx(self,arg0,arg1,arg2):
        val = BUIxc.B_FrameWidget_MoveWidgetTo_Idx(self.this,arg0,arg1,arg2)
        return val
    def MoveWidgetRel(self,arg0,arg1,arg2):
        val = BUIxc.B_FrameWidget_MoveWidgetRel(self.this,arg0,arg1,arg2)
        return val
    def MoveWidgetRel_Idx(self,arg0,arg1,arg2):
        val = BUIxc.B_FrameWidget_MoveWidgetRel_Idx(self.this,arg0,arg1,arg2)
        return val
    def RecalcLayout(self):
        val = BUIxc.B_FrameWidget_RecalcLayout(self.this)
        return val
    def GetWidgetPosition(self,arg0):
        val = BUIxc.B_FrameWidget_GetWidgetPosition(self.this,arg0)
        return val
    def __repr__(self):
        return "<C B_FrameWidget instance>"
class B_FrameWidget(B_FrameWidgetPtr):
    def __init__(self,arg0,arg1,arg2,arg3) :
        self.this = BUIxc.new_B_FrameWidget(arg0.this,arg1,arg2,arg3)
        self.thisown = 1




class B_GridWidgetPtr(B_RectWidgetPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_GridWidget(self.this)
    def AddWidget(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8):
        val = BUIxc.B_GridWidget_AddWidget(self.this,arg0.this,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8)
        return val
    def GetWidget(self,arg0,arg1,arg2):
        val = BUIxc.B_GridWidget_GetWidget(self.this,arg0,arg1,arg2)
        val = B_WidgetPtr(val)
        return val
    def DefSizeChanged(self,arg0,arg1):
        val = BUIxc.B_GridWidget_DefSizeChanged(self.this,arg0,arg1)
        return val
    def __repr__(self):
        return "<C B_GridWidget instance>"
class B_GridWidget(B_GridWidgetPtr):
    def __init__(self,arg0,arg1,arg2,arg3,arg4,arg5) :
        self.this = BUIxc.new_B_GridWidget(arg0.this,arg1,arg2,arg3,arg4,arg5)
        self.thisown = 1




class B_TextWidgetPtr(B_RectWidgetPtr):
    B_TEXT_Horizontal = BUIxc.B_TextWidget_B_TEXT_Horizontal
    B_TEXT_Vertical = BUIxc.B_TextWidget_B_TEXT_Vertical
    B_TEXT_Left = BUIxc.B_TextWidget_B_TEXT_Left
    B_TEXT_HCenter = BUIxc.B_TextWidget_B_TEXT_HCenter
    B_TEXT_Right = BUIxc.B_TextWidget_B_TEXT_Right
    B_TEXT_Top = BUIxc.B_TextWidget_B_TEXT_Top
    B_TEXT_VCenter = BUIxc.B_TextWidget_B_TEXT_VCenter
    B_TEXT_Bottom = BUIxc.B_TextWidget_B_TEXT_Bottom
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_TextWidget(self.this)
    def SetText(self,arg0):
        val = BUIxc.B_TextWidget_SetText(self.this,arg0)
        return val
    def GetTextData(self):
        val = BUIxc.B_TextWidget_GetTextData(self.this)
        return val
    def SetFont(self,arg0):
        val = BUIxc.B_TextWidget_SetFont(self.this,arg0.this)
        val = B_FontPtr(val)
        return val
    def SetOrientation(self,arg0):
        val = BUIxc.B_TextWidget_SetOrientation(self.this,arg0)
        return val
    def GetOrientation(self):
        val = BUIxc.B_TextWidget_GetOrientation(self.this)
        return val
    def SetTextOriginX(self,arg0):
        val = BUIxc.B_TextWidget_SetTextOriginX(self.this,arg0)
        return val
    def GetTextOriginX(self):
        val = BUIxc.B_TextWidget_GetTextOriginX(self.this)
        return val
    def SetTextOriginY(self,arg0):
        val = BUIxc.B_TextWidget_SetTextOriginY(self.this,arg0)
        return val
    def GetTextOriginY(self):
        val = BUIxc.B_TextWidget_GetTextOriginY(self.this)
        return val
    def SetAutoSize(self,arg0):
        val = BUIxc.B_TextWidget_SetAutoSize(self.this,arg0)
        return val
    def GetAutoSize(self):
        val = BUIxc.B_TextWidget_GetAutoSize(self.this)
        return val
    def SetBackgroundColor(self,arg0,arg1,arg2):
        val = BUIxc.B_TextWidget_SetBackgroundColor(self.this,arg0,arg1,arg2)
        return val
    def GetBackgroundColor(self):
        val = BUIxc.B_TextWidget_GetBackgroundColor(self.this)
        return val
    def SetBackgroundAlpha(self,arg0):
        val = BUIxc.B_TextWidget_SetBackgroundAlpha(self.this,arg0)
        return val
    def GetBackgroundAlpha(self):
        val = BUIxc.B_TextWidget_GetBackgroundAlpha(self.this)
        return val
    def SetJustification(self,arg0):
        val = BUIxc.B_TextWidget_SetJustification(self.this,arg0)
        return val
    def GetJustification(self):
        val = BUIxc.B_TextWidget_GetJustification(self.this)
        return val
    def __str__(self):
        val = BUIxc.B_TextWidget___str__(self.this)
        return val
    def __repr__(self):
        return "<C B_TextWidget instance>"
class B_TextWidget(B_TextWidgetPtr):
    def __init__(self,arg0,arg1,arg2,arg3,arg4,*args) :
        self.this = apply(BUIxc.new_B_TextWidget,(arg0.this,arg1,arg2,arg3.this,arg4,)+args)
        self.thisown = 1




class B_BarWidgetPtr(B_RectWidgetPtr):
    B_BAR_Horizontal = BUIxc.B_BarWidget_B_BAR_Horizontal
    B_BAR_Vertical = BUIxc.B_BarWidget_B_BAR_Vertical
    B_BAR_Both = BUIxc.B_BarWidget_B_BAR_Both
    B_BAR_Fordward = BUIxc.B_BarWidget_B_BAR_Fordward
    B_BAR_Backward = BUIxc.B_BarWidget_B_BAR_Backward
    B_BAR_Expand = BUIxc.B_BarWidget_B_BAR_Expand
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_BarWidget(self.this)
    def SetLimits(self,arg0,arg1):
        val = BUIxc.B_BarWidget_SetLimits(self.this,arg0,arg1)
        return val
    def GetLimits(self):
        val = BUIxc.B_BarWidget_GetLimits(self.this)
        return val
    def SetValue(self,arg0):
        val = BUIxc.B_BarWidget_SetValue(self.this,arg0)
        return val
    def GetValue(self):
        val = BUIxc.B_BarWidget_GetValue(self.this)
        return val
    def SetPosition(self,arg0):
        val = BUIxc.B_BarWidget_SetPosition(self.this,arg0)
        return val
    def GetPosition(self):
        val = BUIxc.B_BarWidget_GetPosition(self.this)
        return val
    def SetPositionPercentage(self,arg0):
        val = BUIxc.B_BarWidget_SetPositionPercentage(self.this,arg0)
        return val
    def GetPositionPercentage(self):
        val = BUIxc.B_BarWidget_GetPositionPercentage(self.this)
        return val
    def SetBackgroundColor(self,arg0,arg1,arg2):
        val = BUIxc.B_BarWidget_SetBackgroundColor(self.this,arg0,arg1,arg2)
        return val
    def GetBackgroundColor(self):
        val = BUIxc.B_BarWidget_GetBackgroundColor(self.this)
        return val
    def SetBackgroundAlpha(self,arg0):
        val = BUIxc.B_BarWidget_SetBackgroundAlpha(self.this,arg0)
        return val
    def GetBackgroundAlpha(self):
        val = BUIxc.B_BarWidget_GetBackgroundAlpha(self.this)
        return val
    def SetOrientation(self,arg0):
        val = BUIxc.B_BarWidget_SetOrientation(self.this,arg0)
        return val
    def GetOrientation(self):
        val = BUIxc.B_BarWidget_GetOrientation(self.this)
        return val
    def SetMovementMode(self,arg0):
        val = BUIxc.B_BarWidget_SetMovementMode(self.this,arg0)
        return val
    def GetMovementMode(self):
        val = BUIxc.B_BarWidget_GetMovementMode(self.this)
        return val
    def __repr__(self):
        return "<C B_BarWidget instance>"
class B_BarWidget(B_BarWidgetPtr):
    def __init__(self,arg0,arg1,arg2,arg3) :
        self.this = BUIxc.new_B_BarWidget(arg0.this,arg1,arg2,arg3)
        self.thisown = 1




class B_BitmapWidgetPtr(B_WidgetPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_BitmapWidget(self.this)
    def SetSize(self,arg0,arg1):
        val = BUIxc.B_BitmapWidget_SetSize(self.this,arg0,arg1)
        return val
    def SetBitmap(self,arg0):
        val = BUIxc.B_BitmapWidget_SetBitmap(self.this,arg0)
        return val
    def __repr__(self):
        return "<C B_BitmapWidget instance>"
class B_BitmapWidget(B_BitmapWidgetPtr):
    def __init__(self,arg0,arg1,arg2,arg3,arg4,*args) :
        self.this = apply(BUIxc.new_B_BitmapWidget,(arg0.this,arg1,arg2,arg3,arg4,)+args)
        self.thisown = 1




class B_StackBarWidgetPtr(B_WidgetPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BUIxc.delete_B_StackBarWidget(self.this)
    def AddBar(self,arg0):
        val = BUIxc.B_StackBarWidget_AddBar(self.this,arg0.this)
        return val
    def GetBar(self,arg0):
        val = BUIxc.B_StackBarWidget_GetBar(self.this,arg0)
        val = B_BarWidgetPtr(val)
        return val
    def GetnBars(self):
        val = BUIxc.B_StackBarWidget_GetnBars(self.this)
        return val
    def SetPosition(self,arg0):
        val = BUIxc.B_StackBarWidget_SetPosition(self.this,arg0)
        return val
    def GetPosition(self):
        val = BUIxc.B_StackBarWidget_GetPosition(self.this)
        return val
    def SetPositionPercentage(self,arg0):
        val = BUIxc.B_StackBarWidget_SetPositionPercentage(self.this,arg0)
        return val
    def GetPositionPercentage(self):
        val = BUIxc.B_StackBarWidget_GetPositionPercentage(self.this)
        return val
    def AddValue(self,arg0):
        val = BUIxc.B_StackBarWidget_AddValue(self.this,arg0)
        return val
    def SetOrientation(self,arg0):
        val = BUIxc.B_StackBarWidget_SetOrientation(self.this,arg0)
        return val
    def GetOrientation(self):
        val = BUIxc.B_StackBarWidget_GetOrientation(self.this)
        return val
    def SetMovementMode(self,arg0):
        val = BUIxc.B_StackBarWidget_SetMovementMode(self.this,arg0)
        return val
    def GetMovementMode(self):
        val = BUIxc.B_StackBarWidget_GetMovementMode(self.this)
        return val
    def SetSize(self,arg0,arg1):
        val = BUIxc.B_StackBarWidget_SetSize(self.this,arg0,arg1)
        return val
    def Draw(self,arg0,arg1,arg2):
        val = BUIxc.B_StackBarWidget_Draw(self.this,arg0,arg1,arg2)
        return val
    def __repr__(self):
        return "<C B_StackBarWidget instance>"
class B_StackBarWidget(B_StackBarWidgetPtr):
    def __init__(self,arg0,arg1,arg2,arg3) :
        self.this = BUIxc.new_B_StackBarWidget(arg0.this,arg1,arg2,arg3)
        self.thisown = 1






#-------------- FUNCTION WRAPPERS ------------------

def Draw(arg0,arg1,arg2,arg3):
    val = BUIxc.Draw(arg0.this,arg1,arg2,arg3)
    return val

def CreateNULLWidget():
    val = BUIxc.CreateNULLWidget()
    val = B_WidgetPtr(val)
    val.thisown = 1
    return val

def CreateWidgetFromPtr(arg0):
    val = BUIxc.CreateWidgetFromPtr(arg0)
    val = B_WidgetPtr(val)
    val.thisown = 1
    return val

def CreateRectWidgetFromPtr(arg0):
    val = BUIxc.CreateRectWidgetFromPtr(arg0)
    val = B_RectWidgetPtr(val)
    val.thisown = 1
    return val

def CreateFrameWidgetFromPtr(arg0):
    val = BUIxc.CreateFrameWidgetFromPtr(arg0)
    val = B_FrameWidgetPtr(val)
    val.thisown = 1
    return val

def CreateTextWidgetFromPtr(arg0):
    val = BUIxc.CreateTextWidgetFromPtr(arg0)
    val = B_TextWidgetPtr(val)
    val.thisown = 1
    return val



#-------------- VARIABLE WRAPPERS ------------------

