#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import Raster
import Bladex
import Lumenx
import BUIx
import BBLib
import Language
import ScorerWidgets
import BInput
import BCopy
import Interpolator
import Reference

from Lumenx import printx
from LumenLib.UtilsWidget import AdaptResolution

# -------------------------------
VIEW_PERIOD = 2.0
FADEIN_PERIOD = 0.3
FADEOUT_PERIOD = 0.3

MAX_PAGES = 7
INVENTORY = None
InventoryFadeOutName = "LumenInventoryFadeOut[NPersistent]"

InvWeaponStar = {}
InvShieldStar = {}
InvQuiverStar = {}
InvObjectStar = {
    "Pocima100": 0,
    "Pocima200": 1,
    "PocimaTodo": 2,
    "PowerPotion": 3,
    "Llavero": 7,
}


# -------------------------------
def ShowRightInv():
    import Scorer

    if Lumenx.GetInventoryStyle() == "Original":
        Scorer.WeaponsControl.CycleElements()
        return
    #
    if not INVENTORY:
        return
    init = 1
    next_page = 0
    if INVENTORY.main_frame.GetVisible() and INVENTORY.selected_inventory == "Weapon":
        init = 0
        next_page = 1
    INVENTORY.selected_inventory = "Weapon"
    ShowInventory(init, next_page)


def ShowLeftInv():
    import Scorer

    if Lumenx.GetInventoryStyle() == "Original":
        Scorer.ShieldsControl.CycleElements()
        return
    #
    if not INVENTORY:
        return
    init = 1
    next_page = 0
    if INVENTORY.main_frame.GetVisible() and INVENTORY.selected_inventory == "Shield":
        init = 0
        next_page = 1
    INVENTORY.selected_inventory = "Shield"
    ShowInventory(init, next_page)


def ShowObjectInv():
    import Scorer

    if Lumenx.GetInventoryStyle() == "Original":
        Scorer.CycleElements()
        return
    #
    if not INVENTORY:
        return
    init = 1
    next_page = 0
    if INVENTORY.main_frame.GetVisible() and INVENTORY.selected_inventory == "Object":
        init = 0
        next_page = 1
    INVENTORY.selected_inventory = "Object"
    ShowInventory(init, next_page)


def ShowInventory(init=1, next_page=0):
    Bladex.RemoveScheduledFunc(InventoryFadeOutName)
    if init:
        INVENTORY.main_frame.SetAlpha(0.0)
        INVENTORY.main_frame.SetVisible(1)
    else:
        INVENTORY.interpolator.RemoveAction(INVENTORY.fader.current_action)
        INVENTORY.main_frame.SetAlpha(1.0)
        # INVENTORY.main_frame.SetVisible(1)

    INVENTORY.screen_scale = Raster.GetUnscaledSize()[0] / float(Raster.GetSize()[0])
    char = Lumenx.GetControlCharacter()
    inv = char.GetInventory()
    # current_item_name = ""
    # if INVENTORY.selected_inventory == "Weapon":
    #     current_item_name = char.InvRightBack or char.InvRight
    focus = -1
    page = 0

    INVENTORY.object_scale = 1.0
    selected_inventory = INVENTORY.selected_inventory
    if selected_inventory == "Weapon":
        GetItem = inv.GetWeapon
        nItems = inv.nWeapons
        InventorySlot = BCopy.deepcopy(INVENTORY.InvWeaponSlotBase)
        InventoryStar = InvWeaponStar
    elif selected_inventory == "Shield":
        GetItem = inv.GetShield
        nItems = inv.nShields
        InventorySlot = BCopy.deepcopy(INVENTORY.InvShieldSlotBase)
        InventoryStar = InvShieldStar
    elif selected_inventory == "Quiver":
        GetItem = inv.GetQuiver
        nItems = inv.nQuivers
        InventorySlot = BCopy.deepcopy(INVENTORY.InvQuiverSlotBase)
        InventoryStar = InvQuiverStar
    elif selected_inventory == "Object":
        GetItem = inv.GetObject
        nItems = inv.nObjects
        InventorySlot = BCopy.deepcopy(INVENTORY.InvObjectSlotBase)
        InventoryStar = InvObjectStar
        INVENTORY.object_scale = 3.0
    else:
        printx("Invalid Inventory: %s" % selected_inventory)
        return
    #
    if InventoryStar:
        k = list(InventoryStar.values())
        k.sort()
        max_index = max(k[-1], nItems - 1)
    else:
        max_index = nItems - 1
    nPages = min(int(max_index / 8), MAX_PAGES - 1)

    slot_idx = 0
    max_items = MAX_PAGES * 8
    for i in range(nItems):
        ent_name = GetItem(i)
        ent = Bladex.GetEntity(ent_name)
        if not ent:
            continue
        kind = ent.Kind
        index = InventoryStar.get(kind)
        if index is None:
            while InventorySlot[slot_idx][1] != "":
                slot_idx = slot_idx + 1
                if slot_idx >= max_items:
                    break
            index = slot_idx
        #
        InventorySlot[index][0] = ent_name
        InventorySlot[index][1] = kind
        if selected_inventory == "Quiver":
            InventorySlot[index][2] = ent.Data.NumberOfArrows()
            InventorySlot[index][3] = ent.Data.MaxArrows
        elif selected_inventory == "Object":
            InventorySlot[index][2] = inv.GetNumberObjectsAt(i)
            InventorySlot[index][3] = inv.GetMaxNumberObjectsAt(i)
        else:
            InventorySlot[index][2] = 1

    # if current_item_name:
    #     for i in range(max_items):
    #         if InvWeaponSlot[i][0] == current_item_name:
    #             focus = i % 8
    #             page = int(i / 8)
    #             break
    #
    inv_range = page * 8, min((page + 1) * 8, max_items)
    for i in range(8):
        slot_idx = inv_range[0] + i
        ent_name, kind, number, max_stack, star_flag = InventorySlot[slot_idx]

        frame = INVENTORY.child_frame[i]
        _, border, name_widget, _, _ = frame.widgets
        #
        attack_label, defence_label, res_label, stack_label = border.widgets
        attack_label.SetVisible(0)
        defence_label.SetVisible(0)
        res_label.SetVisible(0)
        stack_label.SetVisible(0)
        stack_label.SetColor(180, 180, 180)
        #
        name_text = ""
        ent = None
        if kind:
            if ent_name:
                ent = Bladex.GetEntity(ent_name)
                name_text = Reference.GetFriendlyNameByEntName(ent_name)
                # name_widget.SetAlpha(1)
                #
                if selected_inventory in ("Weapon", "Shield"):
                    power, defence, res, res_max = (
                        Reference.GiveObjectPowDefResResMaxData(ent_name)
                    )
                    if power:
                        attack_label.SetVisible(1)
                        attack_label.SetText("%+dA" % power)
                    if selected_inventory == "Weapon":
                        if defence:
                            defence_label.SetVisible(1)
                            defence_label.SetText("%+dD" % defence)
                    else:
                        if res:
                            res_label.SetVisible(1)
                            res_label.SetText("%dR" % res)
            else:
                # 占位的情况
                # name_text = Reference.GetObjectFriendlyName(kind)
                # name_widget.SetAlpha(0.5) # 透明度不起作用，也许要使用SetDrawFunc?
                if selected_inventory == "Object":
                    max_stack = Reference.StackObjects.get(kind, 1)
            # 堆叠标签
            if max_stack > 1:
                stack_label.SetVisible(1)
                stack_label.SetText("%d/%d" % (number, max_stack))
                if number == 0:
                    stack_label.SetColor(160, 20, 20)

        name_widget.SetText(name_text)
        frame.RecalcLayout()
        #
        frame.slot_data = [ent_name, kind, number, max_stack, star_flag]
    #
    if init:
        INVENTORY.FadeIn(FADEIN_PERIOD)
    else:
        Bladex.AddScheduledFunc(
            Bladex.GetTime() + VIEW_PERIOD,
            INVENTORY.FadeOut,
            (FADEOUT_PERIOD,),
            InventoryFadeOutName,
        )


# -------------------------------
def InvDrawBOD(this, x, y, time):
    # type: (BUIx.B_FrameWidget, float, float, float) -> None
    alpha = INVENTORY.main_frame.GetAlpha()
    if alpha == 0.0:
        return

    ent_name, kind, number, max_stack, star_flag = this.slot_data

    Raster.SetAlpha(alpha)
    scale = INVENTORY.screen_scale
    obj_scale = INVENTORY.object_scale
    size = INVENTORY.border_size
    Bladex.DrawBOD(
        "UIBorderA3",
        x * scale,
        y * scale,
        size[0] * scale,
        size[1] * scale,
        0.0225 * scale,
        1,
    )
    if kind:
        if not ent_name:
            Raster.SetAlpha(alpha * 0.45)
        Bladex.DrawBOD(
            kind,
            x * scale,
            y * scale,
            size[0] * scale,
            size[1] * scale,
            0.0225 * scale * obj_scale,
            1,
        )
    this.DefDraw(x, y, time)
    #


class InventoryUI:
    inited = 0

    def __init__(self):
        Bladex.AddScheduledFunc(Bladex.GetTime() + 0.2, self.InitWidgets, ())

    def InitWidgets(self):
        import Scorer

        if InventoryUI.inited:
            return

        parent = Scorer.wFrame
        #
        self.parent = parent
        self.child_frame = []  # type: list[BUIx.B_FrameWidget]
        self.screen_scale = Raster.GetUnscaledSize()[0] / float(Raster.GetSize()[0])
        self.object_scale = 1.0
        # self.current_res = Bladex.GetResolution()
        #
        self.fader = Interpolator.LinearInt(0.0, 1.0)
        self.fader.current_action = None
        self.fader.EndExecute = self.EndExecute
        self.interpolator = Interpolator.Interp("LumenInventory", 0)

        max_items = MAX_PAGES * 8
        # (name, kind, number, max_stack, star_flag)
        self.InvWeaponSlotBase = []
        self.InvShieldSlotBase = []
        self.InvQuiverSlotBase = []
        self.InvObjectSlotBase = []
        for i in range(max_items):
            self.InvWeaponSlotBase.append(["", "", 0, 1, 0])
            self.InvShieldSlotBase.append(["", "", 0, 1, 0])
            self.InvQuiverSlotBase.append(["", "", 0, 1, 0])
            self.InvObjectSlotBase.append(["", "", 0, 1, 0])

        for star, base in (
            (InvWeaponStar, self.InvWeaponSlotBase),
            (InvShieldStar, self.InvShieldSlotBase),
            (InvQuiverStar, self.InvQuiverSlotBase),
            (InvObjectStar, self.InvObjectSlotBase),
        ):
            for k, v in star.items():
                if v >= max_items:
                    continue
                base[v][1] = k
                base[v][-1] = 1
        self.selected_inventory = "Weapon"
        #
        auto_scale = 0
        if Lumenx.GetGameVersion() == Lumenx.CLASSIC_VER:
            auto_scale = 1

        view_size = parent.GetSize()
        #
        main_frame_w, main_frame_h = AdaptResolution(
            (2560, 380), (2560, 1440), view_size
        )
        self.main_frame = main_frame = BUIx.B_FrameWidget(
            parent, "InventoryFrame", main_frame_w, main_frame_h
        )
        main_frame.SetAlpha(0.0)
        main_frame.SetVisible(0)
        main_frame.SetAutoScale(auto_scale)
        parent.AddWidget(
            main_frame,
            0.5,
            0,
            BUIx.B_FrameWidget.B_FR_HRelative,
            BUIx.B_FrameWidget.B_FR_HCenter,
            # BUIx.B_FrameWidget.B_FR_AbsoluteLeft,
            # BUIx.B_FrameWidget.B_FR_Left,
            BUIx.B_FrameWidget.B_FR_AbsoluteBottom,
            BUIx.B_FrameWidget.B_FR_Bottom,
        )
        #
        frame_w, frame_h = AdaptResolution((130, 380), (2560, 1440), view_size)
        self.border_size = border_w, border_h = AdaptResolution(
            (130, 130), (2560, 1440), view_size
        )
        name_w, name_h = AdaptResolution((260, 35), (2560, 1440))
        number_w, number_h = AdaptResolution((38, 38), (2560, 1440))
        gap = ((2560 - 130 * 8) / 10.0 / 2560) * main_frame_w
        for i in range(8):
            frame = BUIx.B_FrameWidget(
                main_frame, "InventoryChildFrame_%d" % i, frame_w, frame_h
            )
            frame.SetAlpha(1.0)
            frame.SetAutoScale(auto_scale)
            frame.SetDrawFunc(self.WrapDraw(frame))
            frame.slot_data = ["", "", 0, 1, 0]
            # 用于动画效果的叠加边框
            border1 = BUIx.B_BitmapWidget(
                frame,
                "InventoryBorder1_%d" % i,
                border_w,
                border_h,
                "UIBorderA1",
            )
            border1.SetColor(240, 240, 0)
            border1.SetAlpha(1.0)
            border1.SetVisible(0)
            border1.SetAutoScale(auto_scale)
            # 主体边框
            border2 = BUIx.B_BitmapWidget(
                frame,
                "InventoryBorder2_%d" % i,
                border_w,
                border_h,
                "UIBorderA2",
            )
            border2.SetColor(200, 200, 200)
            border2.SetAlpha(1.0)
            border2.SetAutoScale(auto_scale)
            # 攻击力标签
            attack_label = BUIx.B_TextWidget(
                border2,
                "InventoryAttackLabel_%d" % i,
                "",
                ScorerWidgets.font_server,
                Language.FontCommon,
            )
            attack_label.SetCanvas(view_size)
            attack_label.SetScale(Language.FontScale["S"])
            attack_label.SetColor(180, 180, 180)
            attack_label.SetAlpha(1)
            attack_label.SetAutoScale(auto_scale)
            # 防御力标签
            defence_label = BUIx.B_TextWidget(
                border2,
                "InventoryDefenceLabel_%d" % i,
                "",
                ScorerWidgets.font_server,
                Language.FontCommon,
            )
            defence_label.SetCanvas(view_size)
            defence_label.SetScale(Language.FontScale["S"])
            defence_label.SetColor(180, 180, 180)
            defence_label.SetAlpha(1)
            defence_label.SetAutoScale(auto_scale)
            # 抵抗力标签
            res_label = BUIx.B_TextWidget(
                border2,
                "InventoryResLabel_%d" % i,
                "",
                ScorerWidgets.font_server,
                Language.FontCommon,
            )
            res_label.SetCanvas(view_size)
            res_label.SetScale(Language.FontScale["S"])
            res_label.SetColor(180, 180, 180)
            res_label.SetAlpha(1)
            res_label.SetAutoScale(auto_scale)
            # 堆叠数标签
            stack_label = BUIx.B_TextWidget(
                border2,
                "InventoryStackLabel_%d" % i,
                "",
                ScorerWidgets.font_server,
                Language.FontCommon,
            )
            stack_label.SetCanvas(view_size)
            stack_label.SetScale(Language.FontScale["S"])
            stack_label.SetColor(180, 180, 180)
            stack_label.SetAlpha(1)
            stack_label.SetAutoScale(auto_scale)
            # 星标
            # star = BUIx.B_BitmapWidget(
            #     frame,
            #     "InventoryStar_%d" % i,
            #     30,
            #     30,
            #     "UIStar",
            # )
            #
            name = BUIx.B_TextWidget(
                frame,
                "InventoryName_%d" % i,
                "",  # "Cross-tipped Spear",
                ScorerWidgets.font_server,
                Language.FontCommon,
            )
            name.SetCanvas(view_size)
            name.SetColor(180, 180, 180)
            name.SetScale(Language.FontScale["S"])
            name.SetAlpha(1)
            name.SetAutoScale(auto_scale)

            name_back = BUIx.B_BitmapWidget(
                frame,
                "InventoryNameBack_%d" % i,
                name_w,
                name_h,
                "UINameBack",
            )
            name_back.SetColor(255, 255, 255)
            name_back.SetAlpha(0.8)
            name_back.SetAutoScale(auto_scale)

            number = BUIx.B_BitmapWidget(
                frame,
                "InventoryNumber_%d" % i,
                number_w,
                number_h,
                "UINum%d" % (i + 1),
            )
            number.SetColor(190, 190, 190)
            number.SetAlpha(1.0)
            number.SetAutoScale(auto_scale)
            #
            frame.AddWidget(border1, 0, 0)
            frame.AddWidget(border2, 0, 0)
            frame.AddWidget(
                name,
                0.5,
                border_h + name_h * 0.5,
                BUIx.B_FrameWidget.B_FR_HRelative,
                BUIx.B_FrameWidget.B_FR_HCenter,
                BUIx.B_FrameWidget.B_FR_AbsoluteTop,
                BUIx.B_FrameWidget.B_FR_VCenter,
            )
            frame.AddWidget(
                name_back,
                0.5,
                border_h,
                BUIx.B_FrameWidget.B_FR_HRelative,
                BUIx.B_FrameWidget.B_FR_HCenter,
                BUIx.B_FrameWidget.B_FR_AbsoluteTop,
                BUIx.B_FrameWidget.B_FR_Top,
            )
            frame.AddWidget(
                number,
                0.5,
                border_h + name_h,
                BUIx.B_FrameWidget.B_FR_HRelative,
                BUIx.B_FrameWidget.B_FR_HCenter,
                BUIx.B_FrameWidget.B_FR_AbsoluteTop,
                BUIx.B_FrameWidget.B_FR_Top,
            )
            #
            border2.AddLabel(
                attack_label,
                0.1,
                0.05,
                BUIx.B_Widget.B_LAB_HCenter,
                BUIx.B_Widget.B_LAB_VCenter,
                BUIx.B_Widget.B_FR_HRelative,
                BUIx.B_Widget.B_FR_Left,
                BUIx.B_Widget.B_FR_VRelative,
                BUIx.B_Widget.B_FR_Top,
            )
            border2.AddLabel(
                defence_label,
                1 - 0.1,
                1 - 0.05,
                BUIx.B_Widget.B_LAB_HCenter,
                BUIx.B_Widget.B_LAB_VCenter,
                BUIx.B_Widget.B_FR_HRelative,
                BUIx.B_Widget.B_FR_Right,
                BUIx.B_Widget.B_FR_VRelative,
                BUIx.B_Widget.B_FR_Bottom,
            )
            border2.AddLabel(
                res_label,
                1 - 0.1,
                1 - 0.05,
                BUIx.B_Widget.B_LAB_HCenter,
                BUIx.B_Widget.B_LAB_VCenter,
                BUIx.B_Widget.B_FR_HRelative,
                BUIx.B_Widget.B_FR_Right,
                BUIx.B_Widget.B_FR_VRelative,
                BUIx.B_Widget.B_FR_Bottom,
            )
            border2.AddLabel(
                stack_label,
                1 - 0.1,
                1 - 0.05,
                BUIx.B_Widget.B_LAB_HCenter,
                BUIx.B_Widget.B_LAB_VCenter,
                BUIx.B_Widget.B_FR_HRelative,
                BUIx.B_Widget.B_FR_Right,
                BUIx.B_Widget.B_FR_VRelative,
                BUIx.B_Widget.B_FR_Bottom,
            )
            #
            self.child_frame.append(frame)
            frame.widgets = (border1, border2, name, name_back, number)
            border2.widgets = (attack_label, defence_label, res_label, stack_label)

        for i in range(8):
            n = i % 4
            HIndicator = BUIx.B_FrameWidget.B_FR_AbsoluteLeft
            HAnchor = BUIx.B_FrameWidget.B_FR_Left
            if i > 3:
                i = 7 - n
                HIndicator = BUIx.B_FrameWidget.B_FR_AbsoluteRight
                HAnchor = BUIx.B_FrameWidget.B_FR_Right
            main_frame.AddWidget(
                self.child_frame[i],
                (n + 1) * gap + n * frame_w,
                0,
                HIndicator,
                HAnchor,
                BUIx.B_FrameWidget.B_FR_AbsoluteTop,
                BUIx.B_FrameWidget.B_FR_Top,
            )
        #
        global INVENTORY
        INVENTORY = self
        InventoryUI.inited = 1
        #
        self.Listener = BInput.B_InputListener("InventoryListener")
        self.Listener.SetPythonFunc(self.ListenDevice)

    def WrapDraw(self, this):
        def wrapped(x, y, time, this=this):
            InvDrawBOD(this, x, y, time)

        return wrapped

    # -------------------------------
    def ListenDevice(self, x, y, z):
        pass

    # -------------------------------
    def FadeIn(self, period):
        t = Bladex.GetTime()
        self.fader.Execute = self.ExecuteFadeIn
        self.interpolator.RemoveAction(self.fader.current_action)
        self.fader.current_action = self.interpolator.AddAction(
            t, t + period, self.fader
        )

    def ExecuteFadeIn(self, value):
        ret = Interpolator.LinearInt.Execute(self.fader, value)
        self.main_frame.SetAlpha(ret)

    def FadeOut(self, period):
        t = Bladex.GetTime()
        self.fader.Execute = self.ExecuteFadeOut
        self.interpolator.RemoveAction(self.fader.current_action)
        self.fader.current_action = self.interpolator.AddAction(
            t, t + period, self.fader
        )
        self.main_frame.SetAlpha(1.0)
        self.main_frame.SetVisible(1)

    def ExecuteFadeOut(self, value):
        ret = Interpolator.LinearInt.Execute(self.fader, 1.0 - value)
        self.main_frame.SetAlpha(ret)

    def EndExecute(self):
        self.fader.current_action = None
        if self.fader.Execute == self.ExecuteFadeIn:
            self.main_frame.SetAlpha(1)
            Bladex.AddScheduledFunc(
                Bladex.GetTime() + VIEW_PERIOD,
                self.FadeOut,
                (FADEOUT_PERIOD,),
                InventoryFadeOutName,
            )
        elif self.fader.Execute == self.ExecuteFadeOut:
            self.main_frame.SetAlpha(0)
            self.main_frame.SetVisible(0)
        # printx("Inventory Fader End")


"""
if 1:
    from LumenLib import Inventory
    # Inventory.INVENTORY.InvWeaponSlotBase
    # Inventory.INVENTORY.main_frame.SetVisible(0)
    # Inventory.INVENTORY.main_frame.SetAlpha(0.0)
    INVENTORY = Inventory.INVENTORY
    frame = INVENTORY.child_frame[0]
    frame.widgets[1].RecalcLabelLayout(BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter)
    attack_label, defence_label, res_label, stack_label = frame.widgets[1].widgets
    frame.widgets[2].SetAlpha(0.5)
"""
