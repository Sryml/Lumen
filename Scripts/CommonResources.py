


def Init():
    import Bladex
    import BBLib

    BBLib.ReadMMP('../../3dChars/Kgt.mmp')
    BBLib.ReadMMP('../../3dChars/Amz.mmp')
    BBLib.ReadMMP('../../3dChars/Dwf.mmp')
    BBLib.ReadMMP('../../3dChars/Bar.mmp')
    BBLib.ReadMMP('../../3dobjs/weapons.mmp')
    BBLib.ReadMMP('../../3dobjs/genericos.mmp')

    
    Bladex.BodInspector()
    BBLib.LoadBOD('Piedra_01')
    BBLib.LoadBOD('Llavero')


