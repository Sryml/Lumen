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
import InitDataField
import MenuText

import string
import types
import typing

from Lumenx import printx
from LumenLib.UtilsWidget import AdaptResolution

SndInventorySelect = Bladex.CreateSound(
    "../../Sounds/golpe-generico2.wav", "InventorySelect"
)
SndInventorySelect.Volume = 1.7

# -------------------------------
MAXWEAPONS = 16
MAXSHIELDS = 16
MAXQUIVERS = 16
MAXOBJECTS = 32

VIEW_PERIOD = 2.0
FADEIN_PERIOD = 0.3
FADEOUT_PERIOD = 0.3
BORDERANIM_PERIOD = 0.3

INVENTORY = None
MAX_PAGES = 7
INVENTORY_FADEOU_TNAME = "LumenInventoryFadeOut[NSAVE]"

ListenKeys = {}

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

CHANGE_ANIM = [
    "attack_chg_r_l",
    "chg_r_l",
    "attack_chg_r",
    "chg_r",
]


IManager = BInput.GetInputManager()

# -------------------------------
Reference.DefaultInvScaleData["BotellaSagrada"] = 2.9
Reference.DefaultInvScaleData["Fetiche"] = 2.9
Reference.DefaultInvScaleData["Pergamino2"] = 2.7
# -------------------------------


def HideInventory():
    if INVENTORY and INVENTORY.GetVisible() and not INVENTORY.IsFadingOut():
        INVENTORY.Hide()


def InvObjectUse(me, inv):
    # type: (Bladex._entity.B_Entity_Person, Bladex._inventory.B_PyInventory) -> int
    import Actions

    EntityName = me.Name
    object_name = inv.GetSelectedObject()
    if object_name:
        object = Bladex.GetEntity(object_name)
        if object and object.CanUse:
            me.Data.obj_used = object
            InitDataField.Initialise(object)
            object.Data.UsedBy = EntityName
            object.UseFunc(object_name, Actions.USE_FROM_INV)  # type: ignore
            return 1
    return 0


def InventoryUse(me):
    # type: (Bladex._entity.B_Entity_Person) -> int
    import Actions, ScorerActions

    EntityName = me.Name
    inv = me.GetInventory()
    if Lumenx.GetInventoryStyle() == "Original":
        if hasattr(me.Data, "InventoryActive") and me.Data.InventoryActive:
            return InvObjectUse(me, inv)
        return 0
    # -------------------------------
    if not INVENTORY:
        return 0

    focus = INVENTORY.current_focus
    if not INVENTORY.GetVisible() or focus == -1:
        return 0
    item_name = INVENTORY.child_frame[focus].slot_data[0]
    if item_name == "" or (not inv.CarringObject(item_name)):
        ShowInventory(init=0, next_page=0, update_focus=1)  # refresh
        return 0

    Bladex.RemoveScheduledFunc(INVENTORY_FADEOU_TNAME)
    INVENTORY.CancelFade()
    INVENTORY.main_frame.SetAlpha(1.0)
    SndInventorySelect.PlayStereo()
    Bladex.AddScheduledFunc(
        Bladex.GetTime() + VIEW_PERIOD,
        INVENTORY.FadeOut,
        (FADEOUT_PERIOD,),
        INVENTORY_FADEOU_TNAME,
    )
    #
    INVENTORY.BorderAnim(BORDERANIM_PERIOD)
    #
    if INVENTORY.selected_inventory == "Weapon":
        ScorerActions.CB_WeaponOutX(EntityName, cycle=0)
    elif INVENTORY.selected_inventory in ("Shield", "Quiver"):
        ScorerActions.CB_ShieldOutX(EntityName, cycle=0)
    else:
        return InvObjectUse(me, inv)
    #
    return 1


# -------------------------------
def InventorySelectLast():
    if Lumenx.GetInventoryStyle() == "Original" or not INVENTORY:
        return
    if not INVENTORY.GetVisible():
        INVENTORY.selected_inventory = Lumenx.InventoryActivatedByFocus()
        ShowInventory(init=1, next_page=0)
        return
    #
    ShowInventory(init=0, next_page=0, update_focus=0)  # refresh
    if not INVENTORY.PrevFocus():
        return
    # printx("Select Last Inventory")
    #
    Bladex.RemoveScheduledFunc(INVENTORY_FADEOU_TNAME)
    INVENTORY.CancelFade()
    INVENTORY.main_frame.SetAlpha(1.0)
    SndInventorySelect.PlayStereo()
    Bladex.AddScheduledFunc(
        Bladex.GetTime() + VIEW_PERIOD,
        INVENTORY.FadeOut,
        (FADEOUT_PERIOD,),
        INVENTORY_FADEOU_TNAME,
    )


def InventorySelectNext():
    if Lumenx.GetInventoryStyle() == "Original" or not INVENTORY:
        return
    if not INVENTORY.GetVisible():
        INVENTORY.selected_inventory = Lumenx.InventoryActivatedByFocus()
        ShowInventory(init=1, next_page=0)
        return
    #
    ShowInventory(init=0, next_page=0, update_focus=0)  # refresh
    if not INVENTORY.NextFocus():
        return
    # printx("Select Next Inventory")
    #
    Bladex.RemoveScheduledFunc(INVENTORY_FADEOU_TNAME)
    INVENTORY.CancelFade()
    INVENTORY.main_frame.SetAlpha(1.0)
    SndInventorySelect.PlayStereo()
    Bladex.AddScheduledFunc(
        Bladex.GetTime() + VIEW_PERIOD,
        INVENTORY.FadeOut,
        (FADEOUT_PERIOD,),
        INVENTORY_FADEOU_TNAME,
    )


def InventorySelectByNumber(index):
    import ScorerActions

    if Lumenx.GetInventoryStyle() == "Original" or not INVENTORY:
        return
    if not INVENTORY.GetVisible():
        INVENTORY.selected_inventory = Lumenx.InventoryActivatedByNumbers()
        ShowInventory(init=1, next_page=0)
        return
    #
    ShowInventory(init=0, next_page=0, update_focus=0)  # refresh
    if not INVENTORY.SetFocus(index):
        return
    # printx("Select Inventory by Number: %d" % index)
    InventoryUse(Lumenx.GetControlCharacter())


# -------------------------------

OldIASet = IManager.GetInputActionsSet()
IManager.SetInputActionsSet("Default")
#
Bladex.AddInputAction("Select Last Inventory", 0)
Bladex.AddInputAction("Select Next Inventory", 0)
Bladex.AddInputAction("Inventory 1", 0)
Bladex.AddInputAction("Inventory 2", 0)
Bladex.AddInputAction("Inventory 3", 0)
Bladex.AddInputAction("Inventory 4", 0)
Bladex.AddInputAction("Inventory 5", 0)
Bladex.AddInputAction("Inventory 6", 0)
Bladex.AddInputAction("Inventory 7", 0)
Bladex.AddInputAction("Inventory 8", 0)

# Bladex.AssocKey("Select Last Inventory", "Mouse", "WheelUp")
# Bladex.AssocKey("Select Next Inventory", "Mouse", "WheelDown")
# Bladex.AssocKey("Inventory 1", "Keyboard", "1")
# Bladex.AssocKey("Inventory 2", "Keyboard", "2")
# Bladex.AssocKey("Inventory 3", "Keyboard", "3")
# Bladex.AssocKey("Inventory 4", "Keyboard", "4")
# Bladex.AssocKey("Inventory 5", "Keyboard", "5")
# Bladex.AssocKey("Inventory 6", "Keyboard", "6")
# Bladex.AssocKey("Inventory 7", "Keyboard", "7")
# Bladex.AssocKey("Inventory 8", "Keyboard", "8")

Bladex.AddBoundFunc("Select Last Inventory", InventorySelectLast)
Bladex.AddBoundFunc("Select Next Inventory", InventorySelectNext)
Bladex.AddBoundFunc("Inventory 1", lambda: InventorySelectByNumber(0))
Bladex.AddBoundFunc("Inventory 2", lambda: InventorySelectByNumber(1))
Bladex.AddBoundFunc("Inventory 3", lambda: InventorySelectByNumber(2))
Bladex.AddBoundFunc("Inventory 4", lambda: InventorySelectByNumber(3))
Bladex.AddBoundFunc("Inventory 5", lambda: InventorySelectByNumber(4))
Bladex.AddBoundFunc("Inventory 6", lambda: InventorySelectByNumber(5))
Bladex.AddBoundFunc("Inventory 7", lambda: InventorySelectByNumber(6))
Bladex.AddBoundFunc("Inventory 8", lambda: InventorySelectByNumber(7))
#
IManager.SetInputActionsSet(OldIASet)


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
    if INVENTORY.GetVisible() and INVENTORY.selected_inventory == "Weapon":
        init = 0
        next_page = 1
    INVENTORY.selected_inventory = "Weapon"
    ShowInventory(init, next_page)


def ShowLeftInv():
    import Scorer, ScorerActions

    if Lumenx.GetInventoryStyle() == "Original":
        Scorer.ShieldsControl.CycleElements()
        return
    #
    if not INVENTORY:
        return

    init = 1
    next_page = 0
    #
    char = Lumenx.GetControlCharacter()
    inv = char.GetInventory()
    if inv.HasBowOnBack or inv.HoldingBow:
        # if ScorerActions.DealQuivers(inv):
        inventory = "Quiver"
    else:
        inventory = "Shield"
    #
    if INVENTORY.GetVisible() and INVENTORY.selected_inventory == inventory:
        init = 0
        next_page = 1
    INVENTORY.selected_inventory = inventory
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
    if INVENTORY.GetVisible() and INVENTORY.selected_inventory == "Object":
        init = 0
        next_page = 1
    INVENTORY.selected_inventory = "Object"
    ShowInventory(init, next_page)


def RefreshInventory():
    if not INVENTORY or INVENTORY.GetVisible() == 0 or INVENTORY.IsFadingOut():
        return
    ShowInventory(0, 0, 0)


def GetEmptySlot(InventorySlot, last_slot, max_items):
    while InventorySlot[last_slot][1] != "":
        last_slot = last_slot + 1
        if last_slot >= max_items:
            return None
    return last_slot


def SetInvSlot(
    inv,
    inv_idx,
    ent_name,
    selected_inventory,
    InventoryStar,
    InventorySlot,
    last_slot,
    max_items,
):
    # type: (Bladex._inventory.B_PyInventory, int, str, str, dict, list, int, int) -> int
    ent = Bladex.GetEntity(ent_name)
    if not ent:
        return -1
    kind = ent.Kind
    index = InventoryStar.get(kind)
    if index is None:
        index = GetEmptySlot(InventorySlot, last_slot, max_items)
        if index is None:
            return -1
        else:
            last_slot = index
    #
    InventorySlot[index][0] = ent_name
    InventorySlot[index][1] = kind
    if selected_inventory == "Quiver":
        InventorySlot[index][2] = ent.Data.NumberOfArrows()
        InventorySlot[index][3] = ent.Data.MaxArrows
    elif selected_inventory == "Object":
        InventorySlot[index][2] = inv.GetNumberObjectsAt(inv_idx)
        InventorySlot[index][3] = inv.GetMaxNumberObjectsAt(inv_idx)
    else:
        InventorySlot[index][2] = 1
    return last_slot


def ShowInventory(init=1, next_page=0, update_focus=1):
    import ScorerWidgets

    Bladex.RemoveScheduledFunc(INVENTORY_FADEOU_TNAME)

    if next_page != 0:
        SndInventorySelect.PlayStereo()

    if init:
        INVENTORY.current_page = 0
        INVENTORY.main_frame.SetAlpha(0.0)
        INVENTORY.main_frame.SetVisible(1)
    else:
        INVENTORY.CancelFade()
        INVENTORY.main_frame.SetAlpha(1.0)
        INVENTORY.main_frame.SetVisible(1)

    INVENTORY.screen_scale = Raster.GetUnscaledSize()[0] / float(Raster.GetSize()[0])
    INVENTORY.object_scale = 1.0
    char = Lumenx.GetControlCharacter()
    inv = char.GetInventory()

    # focus = 0

    if (
        inv.HasBowOnBack or inv.HoldingBow
    ) and INVENTORY.selected_inventory == "Shield":
        INVENTORY.selected_inventory = "Quiver"
    selected_inventory = INVENTORY.selected_inventory

    if selected_inventory == "Weapon":
        CycleItem = inv.CycleWeapons
        GetSelectedItem = inv.GetSelectedWeapon
        GetItem = inv.GetWeapon
        nItems = inv.nWeapons
        InventorySlot = BCopy.deepcopy(INVENTORY.InvWeaponSlotBase)
        InventoryStar = InvWeaponStar
        InventoryQueue = char.Data.InvWeaponQueue  # type: list[str]
        if inv.HasBowOnBack or inv.HoldingBow:
            focus_item = inv.GetBow()
        else:
            focus_item = char.InvRightBack or char.InvRight
    elif selected_inventory == "Shield":
        CycleItem = inv.CycleShields
        GetSelectedItem = inv.GetSelectedShield
        GetItem = inv.GetShield
        nItems = inv.nShields
        InventorySlot = BCopy.deepcopy(INVENTORY.InvShieldSlotBase)
        InventoryStar = InvShieldStar
        InventoryQueue = char.Data.InvShieldQueue
        focus_item = char.InvLeftBack or char.InvLeft
        #
        if inv.HasBowOnBack or inv.HoldingBow:
            focus_item_wp = inv.GetBow()
        else:
            focus_item_wp = char.InvRightBack or char.InvRight
        if (
            focus_item_wp
            and focus_item_wp != inv.GetSelectedWeapon()
            and string.lower(char.AnimName) not in CHANGE_ANIM
        ):
            for i in range(inv.nWeapons):
                if inv.GetWeapon(i) == focus_item_wp:
                    for _ in range(i):
                        inv.CycleWeapons()
                    break
    elif selected_inventory == "Quiver":
        CycleItem = inv.CycleQuivers
        GetSelectedItem = inv.GetSelectedQuiver
        GetItem = inv.GetQuiver
        nItems = inv.nQuivers
        InventorySlot = BCopy.deepcopy(INVENTORY.InvQuiverSlotBase)
        InventoryStar = InvQuiverStar
        InventoryQueue = char.Data.InvQuiverQueue
        focus_item = GetSelectedItem()
    elif selected_inventory == "Object":
        CycleItem = inv.CycleObjects
        GetSelectedItem = inv.GetSelectedObject
        GetItem = inv.GetObject
        nItems = inv.nKindObjects
        InventorySlot = BCopy.deepcopy(INVENTORY.InvObjectSlotBase)
        InventoryStar = InvObjectStar
        InventoryQueue = char.Data.InvObjectQueue
        focus_item = GetSelectedItem()
        #
        INVENTORY.object_scale = 3.2
    else:
        printx("Invalid Inventory: %s" % selected_inventory)
        return
    INVENTORY.inv_operations = [inv, CycleItem, GetSelectedItem, GetItem, nItems]

    # -------------------------------
    max_items = MAX_PAGES * 8
    last_slot = 0
    kind_flag = selected_inventory == "Object"
    for name in InventoryQueue[:]:
        ret = last_slot
        for i in range(nItems):
            ent_name = GetItem(i)
            ent = Bladex.GetEntity(ent_name)
            check_name = ""
            if kind_flag and ent:
                check_name = ent.Kind
            elif not kind_flag:
                check_name = ent_name
            if check_name == name:
                # fmt: off
                ret = SetInvSlot(inv,i,ent_name,selected_inventory,InventoryStar,InventorySlot,last_slot,max_items)
                # fmt: on
                break
        else:
            InventoryQueue.remove(name)
        if ret == -1:
            break
        last_slot = ret
    #
    for i in range(nItems):
        ent_name = GetItem(i)
        ent = Bladex.GetEntity(ent_name)
        check_name = ""
        if kind_flag and ent:
            check_name = ent.Kind
        elif not kind_flag:
            check_name = ent_name
        if check_name in InventoryQueue:
            continue
        # fmt: off
        ret = SetInvSlot(inv,i,ent_name,selected_inventory,InventoryStar,InventorySlot,last_slot,max_items)
        # fmt: on
        InventoryQueue.append(check_name)
        if ret == -1:
            break
        last_slot = ret

    # if current_item_name:
    #     for i in range(max_items):
    #         if InvWeaponSlot[i][0] == current_item_name:
    #             focus = i % 8
    #             page = int(i / 8)
    #             break

    # -------------------------------
    # if init or next_page:
    #     INVENTORY.SetFocus(-1)
    #
    if InventoryStar:
        k = list(InventoryStar.values())
        k.sort()
        max_index = max(k[-1], last_slot)
    else:
        max_index = last_slot
    nPages = min(int(max_index / 8) + 1, MAX_PAGES)
    if next_page != 0:
        INVENTORY.current_page = (INVENTORY.current_page + next_page) % nPages
    page = INVENTORY.current_page
    INVENTORY.page_label.SetText("%d/%d" % (page + 1, nPages))

    inv_range = page * 8, min((page + 1) * 8, max_items)
    has_valid_focus = 0
    for i in range(8):
        slot_idx = inv_range[0] + i
        ent_name, kind, number, max_stack, star_flag = InventorySlot[slot_idx]

        frame = INVENTORY.child_frame[i]
        frame.slot_data = [ent_name, kind, number, max_stack, star_flag]
        _, border, name_widget, _, _, star_label = frame.widgets
        # border.SetColor(200, 200, 200)
        #
        attack_label, defence_label, res_label, stack_label = border.widgets
        star_label.SetVisible(0)
        attack_label.SetVisible(0)
        defence_label.SetVisible(0)
        res_label.SetVisible(0)
        stack_label.SetVisible(0)
        stack_label.SetColor(180, 180, 180)
        #
        name_text = ""
        ent = None
        if kind:
            if star_flag:
                star_label.SetVisible(1)

            if ent_name:
                if update_focus and ent_name == focus_item:
                    has_valid_focus = INVENTORY.SetFocus(i)
                ent = Bladex.GetEntity(ent_name)
                name_text = Reference.GetFriendlyNameByEntName(ent_name)
                # name_widget.SetAlpha(1)
                if kind == "Llavero":
                    stack_label.SetVisible(1)
                    stack_label.SetText(str(ScorerWidgets.GetUnusedKeys(inv)))
                #
                if selected_inventory in ("Weapon", "Shield"):
                    power, defence, res, res_max = (
                        Reference.GiveObjectPowDefResResMaxData(ent_name)
                    )
                    if power:
                        prefix = power >= 0 and "+" or ""  # 浮点数的正负号
                        attack_label.SetVisible(1)
                        attack_label.SetText("%s%sA" % (prefix, power))
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

    # -------------------------------
    if update_focus and not has_valid_focus:
        INVENTORY.SetFocus(-1)
    if init:
        INVENTORY.FadeIn(FADEIN_PERIOD)
    else:
        Bladex.AddScheduledFunc(
            Bladex.GetTime() + VIEW_PERIOD,
            INVENTORY.FadeOut,
            (FADEOUT_PERIOD,),
            INVENTORY_FADEOU_TNAME,
        )
    # -------------------------------


# -------------------------------
def InvDrawBOD(this, x, y, time):
    # type: (BUIx.B_FrameWidget, float, float, float) -> None
    alpha = INVENTORY.main_frame.GetAlpha()
    if alpha == 0.0:
        return

    ent_name, kind, number, max_stack, star_flag = this.slot_data

    Raster.SetAlpha(alpha)
    screen_scale = INVENTORY.screen_scale
    obj_scale = Reference.DefaultInvScaleData.get(kind, INVENTORY.object_scale)
    size = INVENTORY.border_size
    Bladex.DrawBOD(
        "UIBorderA3",
        x * screen_scale,
        y * screen_scale,
        size[0] * screen_scale,
        size[1] * screen_scale,
        0.02214 * screen_scale,
        1,
    )
    if kind:
        if not ent_name:
            Raster.SetAlpha(alpha * 0.45)
        Bladex.DrawBOD(
            kind,
            x * screen_scale,
            y * screen_scale,
            size[0] * screen_scale,
            size[1] * screen_scale,
            0.02214 * screen_scale * obj_scale,
            1,
        )
        if kind == "Llavero":
            import darfuncs

            inv = INVENTORY.inv_operations[0]  # type: Bladex._inventory.B_PyInventory
            key_label = INVENTORY.key_label
            n = 0
            for i in range(inv.nKeys):
                key = Bladex.GetEntity(inv.GetKey(i))
                if type(key.Data) is types.IntType:
                    auxval = key.Data
                    key.Data = darfuncs.EmptyClass()
                    key.Data.Used = auxval
                if key.Data == None:
                    key.Data = darfuncs.EmptyClass()
                    key.Data.Used = 1

                if key.Data.Used > 0:
                    Bladex.DrawBOD(
                        key.Kind,
                        (x - 10) * screen_scale,
                        (y - n * 13 - 9) * screen_scale,
                        0,
                        0,
                        0.0369 * screen_scale,
                        1,
                    )
                    key_label.SetText(Reference.GetFriendlyNameByEntName(key.Name))
                    key_label.DefDraw(x, y - n * 13 - 14, time)
                    n = n + 1
        # -------------------------------
    this.DefDraw(x, y, time)
    #


class InventoryUI:
    inited = 0

    def __init__(self):
        Bladex.AddScheduledFunc(
            Bladex.GetTime() + 0.2,
            self.InitWidgets,
            (),
            "Inventory.InitWidgets[NSAVE]",
        )

    def InitWidgets(self):
        import Scorer, darfuncs, Actions

        if InventoryUI.inited:
            return

        ent_name = Lumenx.GetControlCharacter().Name + "KeyRing"
        if not Bladex.GetEntity(ent_name):
            KeyRing = Bladex.CreateEntity(ent_name, "Llavero", 0, 0, 0)
            darfuncs.SetHint(KeyRing, "Keys")
            Actions.TakeObject(Lumenx.GetControlCharacter().Name, ent_name)

        parent = Scorer.wFrame
        #
        self.parent = parent
        self.child_frame = []  # type: list[BUIx.B_FrameWidget]
        self.current_focus = -1
        self.current_page = 0
        self.inv_operations = []
        self.screen_scale = Raster.GetUnscaledSize()[0] / float(Raster.GetSize()[0])
        self.object_scale = 1.0
        # self.current_res = Bladex.GetResolution()
        #
        self.border_anim = Interpolator.LinearInt(1.0, 0.0)
        self.border_anim.current_action = None
        self.border_anim.Execute = self.ExecuteBorderAnim
        self.border_anim.EndExecute = self.EndExecuteBorderAnim

        self.fader = Interpolator.LinearInt(0.0, 1.0)
        self.fader.current_action = None
        self.fader.EndExecute = self.EndExecute

        self.interpolator = Interpolator.Interp("LumenInventory", 0)
        #
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
        scale = 0.82
        # bod_scale = scale * 1.2 # for InvDrawBOD
        main_frame_w, main_frame_h = AdaptResolution(
            (2560, 345), (2560, 1440), view_size
        )
        frame_w, frame_h = AdaptResolution((130 * scale, 345), (2560, 1440), view_size)
        self.border_size = border_w, border_h = frame_w, frame_w
        name_w, name_h = AdaptResolution((260 * scale, 33 * scale), (2560, 1440))
        number_w, number_h = AdaptResolution((37 * scale, 37 * scale), (2560, 1440))
        #
        UIScaleFactor = Bladex.GetUIScaleFactor()
        if UIScaleFactor != 0:
            f = (1.2, 1.316)[UIScaleFactor - 1]
            main_frame_w, main_frame_h = main_frame_w * f, main_frame_h * f
            frame_w, frame_h = frame_w * f, frame_h * f
            self.border_size = border_w, border_h = border_w * f, border_h * f
            name_w, name_h = name_w * f, name_h * f
            number_w, number_h = number_w * f, number_h * f
        #
        # gap = ((2560 - 130 * scale * 8) / 13.2 / 2560) * main_frame_w
        gap = border_w * 1.16
        #
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
        # 详情标签
        self.detail_label = detail_label = BUIx.B_TextWidget(
            main_frame,
            "InventoryDetailLabel",
            "",
            ScorerWidgets.font_server,
            Language.FontCommon,
        )
        detail_label.SetCanvas(view_size)
        detail_label.SetScale(Language.FontScale["M"] * 0.8)
        detail_label.SetAlpha(1)
        detail_label.SetAutoScale(auto_scale)
        detail_label.SetDrawFunc(self.DrawDetail)
        # 页数
        self.page_label = page_label = BUIx.B_TextWidget(
            main_frame,
            "InventoryPageLabel",
            "",
            ScorerWidgets.font_server,
            Language.FontCommon,
        )
        page_label.SetCanvas(view_size)
        page_label.SetScale(Language.FontScale["S"])
        page_label.SetColor(170, 170, 170)
        page_label.SetAlpha(1)
        page_label.SetAutoScale(auto_scale)
        # 钥匙标签
        self.key_label = key_label = BUIx.B_TextWidget(
            main_frame,
            "InventoryKeyLabel",
            "",
            ScorerWidgets.font_server,
            Language.FontCommon,
        )
        key_label.SetCanvas(view_size)
        key_label.SetScale(Language.FontScale["S"])
        key_label.SetColor(150, 150, 150)
        key_label.SetAlpha(1)
        key_label.SetAutoScale(auto_scale)
        key_label.SetDrawFunc(lambda x, y, t: None)
        #
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
            border1.SetColor(240, 240, 30)
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
            attack_label.SetColor(160, 160, 160)
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
            defence_label.SetColor(160, 160, 160)
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
            res_label.SetColor(160, 160, 160)
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
            star_label = BUIx.B_BitmapWidget(
                frame,
                "InventoryStar_%d" % i,
                number_w * 0.6,
                number_w * 0.6,
                "UIStar",
            )
            star_label.SetColor(180, 180, 180)
            star_label.SetAlpha(1)
            star_label.SetVisible(0)
            star_label.SetAutoScale(auto_scale)
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
            frame.AddWidget(
                star_label,
                0.5,
                0,
                BUIx.B_FrameWidget.B_FR_HRelative,
                BUIx.B_FrameWidget.B_FR_HCenter,
                BUIx.B_FrameWidget.B_FR_AbsoluteTop,
                BUIx.B_FrameWidget.B_FR_VCenter,
            )
            frame.AddWidget(
                border1,
                0.5,
                border_h * 0.5,
                BUIx.B_FrameWidget.B_FR_HRelative,
                BUIx.B_FrameWidget.B_FR_HCenter,
                BUIx.B_FrameWidget.B_FR_AbsoluteTop,
                BUIx.B_FrameWidget.B_FR_VCenter,
            )
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
            frame.widgets = (border1, border2, name, name_back, number, star_label)
            border2.widgets = (attack_label, defence_label, res_label, stack_label)
        #
        main_frame.AddLabel(
            page_label,
            0.5 + (gap * 4.5 + border_w * 4) / main_frame_w,
            border_h * 0.5 / main_frame_h,
            BUIx.B_Widget.B_LAB_HCenter,
            BUIx.B_Widget.B_LAB_VCenter,
            BUIx.B_Widget.B_FR_HRelative,
            BUIx.B_Widget.B_FR_HCenter,
            BUIx.B_Widget.B_FR_VRelative,
            BUIx.B_Widget.B_FR_VCenter,
        )
        main_frame.AddWidget(key_label, 0, 0)
        main_frame.AddWidget(
            detail_label,
            0.5,
            0,
            # BUIx.B_Widget.B_LAB_HCenter,
            # BUIx.B_Widget.B_LAB_VCenter,
            BUIx.B_Widget.B_FR_HRelative,
            BUIx.B_Widget.B_FR_HCenter,
            BUIx.B_Widget.B_FR_VRelative,
            BUIx.B_Widget.B_FR_Top,
        )
        #
        for i in range(8):
            n = i % 4
            # HIndicator = BUIx.B_FrameWidget.B_FR_HRelative
            HAnchor = BUIx.B_FrameWidget.B_FR_Left
            D = 1
            if i < 4:
                i = 3 - i
                HAnchor = BUIx.B_FrameWidget.B_FR_Right
                D = -1
            main_frame.AddWidget(
                self.child_frame[i],
                0.5 + ((n + 1) * gap + n * frame_w) / main_frame_w * D,
                0,
                BUIx.B_FrameWidget.B_FR_HRelative,
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

    def DrawDetail(self, x, y, time):
        selected_inventory = self.selected_inventory
        if selected_inventory not in ("Weapon", "Shield"):
            return
        focus = self.current_focus
        if focus == -1:
            return
        ent_name, kind, number, max_stack, star_flag = self.child_frame[focus].slot_data
        if not ent_name:
            return
        #
        label = self.detail_label
        name_text = Reference.GetFriendlyNameByEntName(ent_name)
        power, defence, res, res_max = Reference.GiveObjectPowDefResResMaxData(ent_name)
        n = 0
        offset_y = 13
        scale = Language.FontScale["M"] * 0.8
        # NAME
        width = Language.font_behaviour_common.GetTextWidth(name_text) * scale
        label.SetColor(170, 170, 170)
        label.SetText(name_text)
        label.DefDraw(x - width * 0.5, y, time)
        n = n + 1
        # DEF POW
        def_text = ""
        pow_text = ""
        if defence is not None:
            prefix = ""
            if defence < 0:
                def_color = Language.FontColor.Red
            else:
                def_color = Language.FontColor.LightBlue
                prefix = "+"
            def_text = "%s%s %s" % (prefix, defence, MenuText.GetMenuText("DEF"))
        if power is not None:
            prefix = ""
            if power < 0:
                pow_color = Language.FontColor.Red
            else:
                pow_color = Language.FontColor.LightBlue
                prefix = "+"
            pow_text = "%s%s %s" % (prefix, power, MenuText.GetMenuText("POW"))
        if def_text:
            width = Language.font_behaviour_common.GetTextWidth(def_text) * scale
            label.SetColor(def_color[0], def_color[1], def_color[2])
            label.SetText(def_text)
            label.DefDraw(x - width - 2, y + n * offset_y, time)

            width = Language.font_behaviour_common.GetTextWidth(pow_text) * scale
            label.SetColor(pow_color[0], pow_color[1], pow_color[2])
            label.SetText(pow_text)
            label.DefDraw(x + 2, y + n * offset_y, time)
        else:
            width = Language.font_behaviour_common.GetTextWidth(pow_text) * scale
            label.SetColor(pow_color[0], pow_color[1], pow_color[2])
            label.SetText(pow_text)
            label.DefDraw(x - width * 0.5, y + n * offset_y, time)
        n = n + 1
        # RES
        if (res is not None) and (res_max is not None):
            res_text = "%s: %s / %s" % (
                MenuText.GetMenuText("RES"),  # "RESISTANCE"
                res,
                res_max,
            )
            r, g, b = Language.FontColor.Cyan
            width = Language.font_behaviour_common.GetTextWidth(res_text) * scale
            label.SetColor(r, g, b)
            label.SetText(res_text)
            label.DefDraw(x - width * 0.5, y + n * offset_y, time)
            n = n + 1
        #
        # self.main_frame.RecalcLayout()

    # -------------------------------
    def ListenDevice(self, x, y, z):
        printx(x, y, z)

    # -------------------------------

    def Hide(self):
        Bladex.RemoveScheduledFunc(INVENTORY_FADEOU_TNAME)
        self.CancelFade()
        self.main_frame.SetVisible(0)

    def GetVisible(self):
        return self.main_frame.GetVisible()

    def IsFadingOut(self):
        return self.fader.Execute == self.ExecuteFadeOut

    def CancelFade(self):
        self.interpolator.RemoveAction(self.fader.current_action)
        self.fader.Execute = None

    def CancelBorderAnim(self):
        self.interpolator.RemoveAction(self.border_anim.current_action)
        if self.current_focus != -1:
            border = self.child_frame[self.current_focus].widgets[0]
            border.SetVisible(0)

    def SetFocus(self, index):
        char = Lumenx.GetControlCharacter()
        if (
            self.selected_inventory == "Weapon"
            and string.lower(char.AnimName) in CHANGE_ANIM
        ):
            return 0
        last_empty = 0
        # 如果上一个槽为空，重置颜色
        if self.current_focus != -1:
            last_frame = self.child_frame[self.current_focus]
            if last_frame.slot_data[0] == "":
                last_empty = 1
                last_frame.widgets[1].SetColor(200, 200, 200)
        # 如果目标槽不为-1且空，返回0
        if index != -1:
            slot_data = self.child_frame[index].slot_data
            item_name = slot_data[0]
            if item_name == "":
                if last_empty:
                    self.current_focus = -1
                return 0
        self.CancelBorderAnim()
        # 如果上一个槽不为-1且与目标槽不同，重置颜色
        if self.current_focus != index and self.current_focus != -1:
            border = self.child_frame[self.current_focus].widgets[1]
            border.SetColor(200, 200, 200)
        self.current_focus = index
        # 仅清除焦点，直接返回
        if index == -1:
            return 0

        border = self.child_frame[index].widgets[1]
        border.SetColor(240, 240, 30)
        _, CycleItem, GetSelectedItem, GetItem, nItems = self.inv_operations
        if item_name != GetSelectedItem():
            for i in range(nItems):
                if GetItem(i) == item_name:
                    for _ in range(i):
                        CycleItem()
                    break
        #
        return 1

    def MoveFocus(self, inc):
        current_focus = max((self.current_focus + inc), -1) % 8
        for i in range(8):
            if self.child_frame[current_focus].slot_data[0] != "":
                break
            current_focus = (current_focus + inc) % 8
        return self.SetFocus(current_focus)

    def PrevFocus(self):
        return self.MoveFocus(-1)

    def NextFocus(self):
        return self.MoveFocus(1)

    # -------------------------------
    def FadeIn(self, period):
        self.fader.Execute = self.ExecuteFadeIn
        self.interpolator.RemoveAction(self.fader.current_action)
        t = Bladex.GetTime()
        self.fader.current_action = self.interpolator.AddAction(
            t, t + period, self.fader
        )

    def ExecuteFadeIn(self, value):
        ret = Interpolator.LinearInt.Execute(self.fader, value)
        self.main_frame.SetAlpha(ret)

    def FadeOut(self, period):
        self.fader.Execute = self.ExecuteFadeOut
        self.interpolator.RemoveAction(self.fader.current_action)
        t = Bladex.GetTime()
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
                INVENTORY_FADEOU_TNAME,
            )
        elif self.fader.Execute == self.ExecuteFadeOut:
            self.main_frame.SetAlpha(0)
            self.main_frame.SetVisible(0)
            # printx("Inventory Fadeout End")
        self.fader.Execute = None
        # printx("Inventory Fader End")

    # -------------------------------
    def BorderAnim(self, period):
        self.interpolator.RemoveAction(self.border_anim.current_action)
        t = Bladex.GetTime()
        self.border_anim.current_action = self.interpolator.AddAction(
            t, t + period, self.border_anim
        )
        border = self.child_frame[self.current_focus].widgets[0]
        border.SetSize(self.border_size[0], self.border_size[1])
        border.SetVisible(1)
        border.SetAlpha(0.8)

    def ExecuteBorderAnim(self, value):
        ret = Interpolator.LinearInt.Execute(self.border_anim, value)
        border = self.child_frame[self.current_focus].widgets[0]
        border.SetAlpha(ret * 0.8)
        val = (1 - ret) * 0.4 + 1.0
        border.SetSize(self.border_size[0] * val, self.border_size[1] * val)
        self.child_frame[self.current_focus].RecalcLayout()

    def EndExecuteBorderAnim(self):
        self.border_anim.current_action = None
        border = self.child_frame[self.current_focus].widgets[0]
        border.SetVisible(0)


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
