import sys




ObjectsStore={}

StoreIndex=0 # Que no se me olvide guardar este valor al guardar partida

# -Sryml
AutoStoreIndex=0

def GetAutoId():
    global AutoStoreIndex
    AutoStoreIndex = AutoStoreIndex + 1
    return str(AutoStoreIndex)
#

def GetNewId():
    global StoreIndex

    StoreIndex=StoreIndex+1
    key=str(StoreIndex)
    while ObjectsStore.has_key(key):
        StoreIndex=StoreIndex+1
        key=str(StoreIndex)

##    print "GetNewId()",key
    return key


def CheckStore():
    import Reference
##    # Recoleccion de basura
    for i in ObjectsStore.keys():
        if sys.getrefcount(ObjectsStore[i]) <= 2: # Thanks Tomash
            # garbage collection, if the only reference to the class is here, delete it
            Reference.debugprint("CheckStore(): %s deleted by garbage collection, index %s" % (ObjectsStore[i], repr(i))) # -Sryml
            del ObjectsStore[i]

    # Objetos que ya no son validos
    for i in ObjectsStore.keys():    
        try:
            obj=ObjectsStore[i]
            ret=obj.persistent_check()
            if not ret:
                del ObjectsStore[i]
        except AttributeError:
            pass
        except TypeError:
            pass
    
 