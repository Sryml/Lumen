##########################################
##########################################
#### 
####	ExtraData.py
####
##########################################
##########################################

import ExtraDataSave

camspirit = []

def SaveExtraData(filename):
    data = (camspirit,0)
    print "camspirit ",camspirit
    print ("datos ",data)
    ExtraDataSave.SaveExtraData(filename,data)

    return 1

def LoadExtraData(filename):
    global camspirit
    data = ExtraDataSave.LoadExtraData(filename)
    print ("datos ",data)
    camspirit = data[0]








