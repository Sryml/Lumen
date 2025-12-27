


import Bladex
import cPickle


def Store(key,value):
    "Guarda en memoria un valor arbitrario de Python (que se pueda hacer pick)"

    s=cPickle.dumps(value)
    Bladex.SetStringValue(key,s)


def Get(key):
    "Recupera de memoria un valor arbitrario de Python previamente guardado"

    v=Bladex.GetStringValue(key)
    if v:
        return cPickle.loads(v)
    return None


def Delete(key):
    Bladex.DeleteStringValue(key)
