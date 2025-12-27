





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

    BODPakloaded=BBLib.LoadBODData("Pak/BODPak.dat")
    if not BODPakloaded:
        Bladex.AddScheduledFunc(0,LoadBODPack,(),"LoadBODPack")
