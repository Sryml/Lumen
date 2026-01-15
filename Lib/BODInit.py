#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#
# Change list:
# * Added cache disable feature
#

import Lumenx



def LoadBODPack():
    import BBLib
    print "Saving BOD Pak"
    try:
        import os
        os.mkdir("Pak")
    except:
        pass
    BBLib.SaveBODData("Pak/BODPak.dat")



def Init():
    import BBLib
    import Bladex

    if not Lumenx.IsCacheEnabled():
        return

    BODPakloaded=BBLib.LoadBODData("Pak/BODPak.dat")
    if not BODPakloaded:
        Bladex.AddScheduledFunc(0,LoadBODPack,(),"LoadBODPack")
