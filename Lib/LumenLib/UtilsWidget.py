#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import Raster
import Bladex
import Lumenx


from Lumenx import printx


def AdaptResolution(img_size, canvas, view_size=(), keep_h=1):
    # type: (tuple, tuple, tuple, int) -> tuple[int, int]
    import Scorer

    if not view_size:
        view_size = Scorer.wFrame.GetSize()
    vw, vh = float(view_size[0]), float(view_size[1])
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
