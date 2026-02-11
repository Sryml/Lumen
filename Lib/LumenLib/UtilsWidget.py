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
import BInput
import Language
import MenuWidget
import MenuText
import GameText

import string
import math

from Lumenx import printx

# ----------------------------------
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None


# ----------------------------------
B_Widget = BUIx.B_Widget
IManager = BInput.GetInputManager()


# ----------------------------------
def ResizeImage(img_size, target_size):
    img_width, img_height = float(img_size[0]), float(img_size[1])
    target_width, target_height = float(target_size[0]), float(target_size[1])
    img_ratio = img_width / img_height
    target_ratio = target_width / target_height

    resize_width, resize_height = target_size
    if img_ratio > target_ratio:
        resize_width = target_width
        resize_height = resize_width / img_width * img_height
    elif img_ratio < target_ratio:
        resize_height = target_height
        resize_width = resize_height / img_height * img_width

    return (resize_width, resize_height)


def AdaptResolution(img_size, canvas, view_size=(), keep_h=1, min_scale=None):
    # type: (tuple, tuple, tuple, int, float|None) -> tuple[int, int]
    import Scorer

    if not view_size:
        view_size = Scorer.wFrame.GetSize()
    vw, vh = float(view_size[0]), float(view_size[1])
    if min_scale is None:
        if Lumenx.GetGameVersion() == Lumenx.CLASSIC_VER:
            min_scale = 0.5
        else:
            min_scale = 0.5 / (Raster.GetUnscaledSize()[1] / vh)

    f = max(float(view_size[keep_h]) / canvas[keep_h], min_scale)
    w, h = int(img_size[0] * f), int(img_size[1] * f)

    if w > vw and h > vh:
        f = min(vw / w, vh / h)
        w = int(w * f)
        h = int(h * f)
    elif w > vw:
        f = vw / w
        w = int(vw)
        h = int(h * f)
    elif h > vh:
        f = vh / h
        h = int(vh)
        w = int(w * f)
    return w, h


# ----------------------------------
def WrapWord(Word, CurrentWidth, MaxWidth, FontScale, font_behaviour):
    lines = []
    current_line = ""
    current_width = CurrentWidth
    for c in Word:
        width = font_behaviour.GetTextWidth(c) * FontScale
        if Lumenx.GetGameVersion() == Lumenx.CLASSIC_VER:
            width = int(width)
        if current_width + width > MaxWidth:
            lines.append(current_line)
            current_line = c
            current_width = width
        else:
            current_line = current_line + c
            current_width = current_width + width
    return lines, current_line, current_width


def WrapText(Text, MaxWidth, FontScale, font_behaviour):
    space_w = font_behaviour.GetTextWidth(" ") * FontScale
    if Lumenx.GetGameVersion() == Lumenx.CLASSIC_VER:
        space_w = int(space_w)

    ret_lines = []
    for text in string.split(Text, "\n"):  # type: ignore
        lines = []
        current_line = ""
        current_width = 0
        for word in string.split(text, " "):  # type: ignore
            if word == "":
                width = space_w
            else:
                if Lumenx.GetGameVersion() == Lumenx.CLASSIC_VER:
                    width = 0
                    for c in word:
                        width = width + int(font_behaviour.GetTextWidth(c) * FontScale)
                else:
                    width = font_behaviour.GetTextWidth(word) * FontScale

            if width > MaxWidth:
                wrap_word, current_line_new, current_width_new = WrapWord(
                    word, current_width, MaxWidth, FontScale, font_behaviour
                )
                if wrap_word:
                    lines.append(current_line + wrap_word[0])
                    lines = lines + wrap_word[1:]
                    current_line = current_line_new + " "
                    current_width = current_width_new + space_w
                else:
                    current_line = current_line + current_line_new + " "
                    current_width = current_width + current_width_new + space_w
            elif current_width + width > MaxWidth:
                lines.append(current_line)
                current_line = word + " "
                current_width = width + (word == "" and 0 or space_w)
            else:
                current_line = current_line + word + " "
                current_width = current_width + width + (word == "" and 0 or space_w)
        lines.append(current_line[:-1])
        ret_lines = ret_lines + lines

    return ret_lines


# ----------------------------------
class B_BackColor(BUIx.B_RectWidget):
    def __init__(self, Parent, MenuDescr, StackMenu):
        BUIx.B_RectWidget.__init__(self, Parent, MenuDescr["Name"], 1, 1)
        ViewSize = Raster.GetSize()
        self.Rectangle = MenuDescr.get("Rectangle", (0, 0, ViewSize[0], ViewSize[1]))
        self.Color = MenuDescr.get("Color", (0, 0, 0))
        self.Alpha = MenuDescr.get("Alpha", 1.0)
        self.SetDrawFunc(self.Draw)

    def Draw(self, x, y, time):
        r, g, b = self.Color
        Raster.SetFillColor(r, g, b)
        Raster.SetAlpha(self.Alpha)
        Raster.SolidRectangle(
            self.Rectangle[0], self.Rectangle[1], self.Rectangle[2], self.Rectangle[3]
        )
        self.DefDraw(x, y, time)

    def AcceptsFocus(self):
        return 0


# ----------------------------------
class ModGridItem(MenuWidget.B_MenuTreeItem, BUIx.B_FrameWidget):
    def __init__(self, Parent, MenuDescr, StackMenu):
        from LumenLib import BODLoader

        desc_margin = BODLoader.DESC_MARGIN

        self.border_scale = Parent.border_scale
        border_size = Parent.border_size
        BUIx.B_FrameWidget.__init__(
            self,
            Parent,
            "ModGridItem" + MenuDescr["Name"],
            border_size[0],
            border_size[1],
        )
        MenuWidget.B_MenuTreeItem.__init__(self, MenuDescr, StackMenu)
        self.SetDrawFunc(self.Draw)
        #
        self.wTitle = BUIx.B_TextWidget(
            self,
            "Title" + MenuDescr["Name"],
            MenuText.GetMenuText(MenuDescr["Name"]),
            Language.font_server,
            Language.FontCommon,
        )
        r, g, b = Language.FontColor.LightBlue
        self.wTitle.SetScale(Language.MFontScale["S"] * 0.92)
        self.wTitle.SetAlpha(1)
        self.wTitle.SetColor(r, g, b)

        self.wVers = BUIx.B_TextWidget(
            self,
            "Vers" + MenuDescr["Name"],
            "v" + MenuDescr["Version"],
            Language.font_server,
            Language.FontCommon,
        )
        r, g, b = Language.FontColor.White
        self.wVers.SetScale(Language.MFontScale["S"] * 0.66)
        self.wVers.SetAlpha(1)
        self.wVers.SetColor(r, g, b)

        self.wAuthor = BUIx.B_TextWidget(
            self,
            "Author" + MenuDescr["Name"],
            MenuText.GetMenuText(MenuDescr["Author"]),
            Language.font_server,
            Language.FontCommon,
        )
        r, g, b = Language.FontColor.White
        self.wAuthor.SetScale(Language.MFontScale["S"] * 0.66)
        self.wAuthor.SetAlpha(1)
        self.wAuthor.SetColor(r, g, b)

        self.wDesc = BUIx.B_TextWidget(
            self,
            "Desc" + MenuDescr["Name"],
            MenuDescr["Desc"],
            Language.font_server,
            Language.FontCommon,
        )
        r, g, b = Language.FontColor.White
        self.wDesc.SetScale(Language.MFontScale["S"] * 0.73)
        self.wDesc.SetAlpha(1)
        self.wDesc.SetColor(r, g, b)
        self.wDesc.SetJustification(BUIx.B_TextWidget.B_TEXT_Left)

        #
        self.wBorder = BUIx.B_BitmapWidget(
            self,
            "Border" + MenuDescr["Name"],
            border_size[0],
            border_size[1],
            "ModBorder",
        )
        self.wBorder.SetAlpha(1.0)
        self.wBorder.SetColor(255, 255, 255)
        #
        self.AddWidget(
            self.wTitle,
            0.5,
            0.0516,
            B_Widget.B_FR_HRelative,
            B_Widget.B_FR_HCenter,
            B_Widget.B_FR_VRelative,
            B_Widget.B_FR_VCenter,
        )
        self.AddWidget(
            self.wVers,
            desc_margin,
            0.6567,
            B_Widget.B_FR_HRelative,
            B_Widget.B_FR_Left,
            B_Widget.B_FR_VRelative,
            B_Widget.B_FR_VCenter,
        )
        self.AddWidget(
            self.wAuthor,
            1 - desc_margin,
            0.6567,
            B_Widget.B_FR_HRelative,
            B_Widget.B_FR_Right,
            B_Widget.B_FR_VRelative,
            B_Widget.B_FR_VCenter,
        )
        self.AddWidget(
            self.wDesc,
            desc_margin,
            0.694,
            B_Widget.B_FR_HRelative,
            B_Widget.B_FR_Left,
            B_Widget.B_FR_VRelative,
            B_Widget.B_FR_Top,
        )
        self.AddWidget(self.wBorder, 0, 0)

    def Draw(self, x, y, time):
        if self.GetHasFocus():
            r, g, b = Language.FontColor.Focused
        else:
            r, g, b = Language.FontColor.LightBlue
        self.wTitle.SetColor(r, g, b)
        #
        self.DefDraw(x, y, time)
        #
        img, w, h = self.MenuDescr["Show"]
        if img is not None:
            rw, rh = img.GetDimension()
            w, h = w * self.border_scale, h * self.border_scale
            border_w, border_h = self.GetSize()
            Raster.SetPosition(
                x + (border_w - w) * 0.5,
                y + border_h * 0.1091 + (261 * self.border_scale - h) * 0.5,
            )
            if Lumenx.GetGameVersion() == Lumenx.CLASSIC_VER:
                Raster.DrawImage(rw, rh, "RGB", "Normal", img.GetData())
            else:
                Raster.DrawResizeImage(rw, rh, "RGB", "Normal", img.GetData(), w, h)


class B_GridWidget(MenuWidget.B_MenuTree):
    GridSize = (1, 1)
    MaxPages = 1
    MaxItems = 0
    nItems = 0

    def __init__(self, Parent, Menudesc, StackMenu, VertPos=0):
        MenuWidget.B_MenuTree.__init__(self, Parent, Menudesc, StackMenu, VertPos)
        self.FocusPage = 0
        self.FocusRow = 0
        self.FocusCol = 0

    def ActivateItem(self, activate):
        import Menu

        if activate == 0:
            StackMenu = Menu._MainMenu.MenuStack
            w = StackMenu.Top()
            try:
                w.FinalRelease()
            except:
                pass
            StackMenu.Pop()

    #
    def SetFocus_Idx(self, index, update_page=0):
        if update_page:
            self.FocusPage = int(index / self.MaxItems)
            start = self.FocusPage * self.MaxItems
            end = (self.FocusPage + 1) * self.MaxItems
            for i in self.MenuItems[:start]:
                i.SetVisible(0)
            for i in self.MenuItems[start:end]:
                i.SetVisible(1)
            for i in self.MenuItems[end:]:
                i.SetVisible(0)
        MenuWidget.B_MenuTree.SetFocus_Idx(self, index)

    #
    def CalcIndex(self):
        return int(
            self.FocusPage * self.MaxItems
            + self.FocusRow * self.GridSize[0]
            + self.FocusCol
        )

    def ChangeRow(self, val):
        self.FocusRow = (self.FocusRow + val) % self.GridSize[1]
        index = self.CalcIndex()
        if index >= self.nItems:
            if val == 1:
                self.FocusRow = 0
            else:
                self.FocusRow = (
                    int((self.nItems - 1) / self.GridSize[0]) % self.GridSize[1]
                )
            index = self.CalcIndex()
        self.SetFocus_Idx(index)

    def ChangeCol(self, val):
        self.FocusCol = (self.FocusCol + val) % self.GridSize[0]
        index = self.CalcIndex()
        if index >= self.nItems:
            if val == 1:
                self.FocusCol = 0
            else:
                self.FocusCol = (self.nItems - 1) % self.GridSize[0]
            index = self.CalcIndex()
        self.SetFocus_Idx(index)

    def ChangePage(self, val):
        self.FocusPage = (self.FocusPage + val) % self.MaxPages
        index = self.CalcIndex()
        if index >= self.nItems:
            idx = self.nItems - 1
            self.FocusRow = int(idx / self.GridSize[0]) % self.GridSize[1]
            self.FocusCol = idx % self.GridSize[0]
            index = self.CalcIndex()
        self.SetFocus_Idx(index, update_page=1)
        self.page_lable.SetText(
            "%s/%s %s"
            % (self.FocusPage + 1, self.MaxPages, MenuText.GetMenuText("Pages"))
        )

    def PrevFocus(self):
        action = IManager.GetInputActions().Find("Menu_Control")
        ctrl = action.this != "NULL" and action.CurrentlyActivated() or 0
        if ctrl:
            self.ChangePage(-1)
        else:
            self.ChangeRow(-1)

    def NextFocus(self):
        action = IManager.GetInputActions().Find("Menu_Control")
        ctrl = action.this != "NULL" and action.CurrentlyActivated() or 0
        if ctrl:
            self.ChangePage(1)
        else:
            self.ChangeRow(1)

    def DecMenuItem(self):
        self.ChangeCol(-1)

    def IncMenuItem(self):
        self.ChangeCol(1)

    #

    # def AcceptsFocus(self):
    #     return len(self.MenuItems) != 0


class B_ModGridWidget(B_GridWidget):
    def __init__(self, Parent, Menudesc, StackMenu, VertPos=0):
        from LumenLib import BODLoader

        self.GridSize = GridSize = BODLoader.GRID_SIZE
        self.MaxItems = GridSize[0] * GridSize[1]
        self.border_size = border_size = AdaptResolution(
            BODLoader.BORDER_SIZE, (3840, 2160), Parent.GetSize()
        )
        self.border_scale = border_size[0] / float(BODLoader.BORDER_SIZE[0])
        self.gap = gap = AdaptResolution(
            (BODLoader.BORDER_GAP, BODLoader.BORDER_GAP), (3840, 2160), Parent.GetSize()
        )[0]
        size = (
            GridSize[0] * border_size[0] + (GridSize[0] - 1) * gap,
            GridSize[1] * border_size[1] + (GridSize[1] - 1) * gap,
        )
        Menudesc["Size"] = size
        #
        B_GridWidget.__init__(self, Parent, Menudesc, StackMenu, VertPos)
        # self.SetBorder(1)
        # self.SetBorderColor(200, 200, 0)
        self.nItems = len(self.MenuItems)
        if self.nItems:
            self.SetFocus_Idx(0)
        self.MaxPages = int((self.nItems - 1) / float(self.MaxItems)) + 1
        #
        self.page_lable = BUIx.B_TextWidget(
            self,
            Menudesc["Name"] + "PageLable",
            "1/%s %s" % (self.MaxPages, MenuText.GetMenuText("Pages")),
            Language.font_server,
            Language.FontCommon,
        )
        r, g, b = Language.FontColor.Unfocusable
        self.page_lable.SetScale(Language.MFontScale["S"] * 0.8)
        self.page_lable.SetAlpha(1)
        self.page_lable.SetColor(r, g, b)
        self.AddLabel(
            self.page_lable,
            0,
            8,
            B_Widget.B_LAB_Right,
            B_Widget.B_LAB_Bottom,
            B_Widget.B_FR_AbsoluteLeft,
            B_Widget.B_FR_Right,
            B_Widget.B_FR_AbsoluteTop,
            B_Widget.B_FR_Top,
        )

    def CreateMenuElements(self, Parent, Menudesc, StackMenu):
        from LumenLib import BODLoader

        gap = self.gap
        border_w, border_h = self.border_size
        ModList = BODLoader.GetModList()
        for index in range(len(ModList)):
            mod_dir = ModList[index]
            menu_element = ModGridItem(self, BODLoader.GetModInfo(mod_dir), StackMenu)
            MenuWidget.B_MenuFocusManager.AddMenuElement(self, menu_element)
            col = index % self.GridSize[0]
            row = int(index / self.GridSize[0]) % self.GridSize[1]
            self.AddWidget(menu_element, (border_w + gap) * col, (border_h + gap) * row)


# ----------------------------------
