# Talk System - Custom parameters and setup
import Language

TSCustomVers = "1.0"  # Configuration File version

TSmmp = "../../Data/TSWidgets.mmp"  # widget image

TSFont = Language.FontCommon  # or bmp font
TSFontScale = 0.29  # font scale

AnimSpeed = 6.0  # Animation Speed
AnimFPS = 60  # Animation FPS

TSTalkRange = 5000
TSHideDelay = 10.0
SelectNPCArea = 10000

# Dialogue configuration
MaxLines = "auto"  # Maximum number of lines. Integer or string "auto"
TextVsep = "0em"  # Line spacing, 1em represents the height of a line of text.
TextMargin = {
    "top": 0.07, "right": 0.078, "bottom": 0.074, "left": 0.078
    } # text margins
# text color
ColorDlg = 255, 255, 255  # Dialogue text
ColorAns = 207, 144, 49  # Answer text
ColorAnsSelected = 252, 247, 167  # Selected answer
HUDBrightness = 1.0

# Journal configuration
jMaxLines = "auto"  # Maximum number of lines. Integer or string "auto"
jTextVsep = "0em"  # Line spacing, 1em represents the height of a line of text.
jTextMargin = {
    "top": 0.076, "right": 0.107, "bottom": 0.075, "left": 0.107
    } # text margins
# text color
ColorjTitle = 255, 204, 51  # Journal title
ColorjText = 252, 247, 167  # Journal text
ColorjTextSelected = 255, 204, 51  # Journal selected text
jHUDBrightness = 0.628
