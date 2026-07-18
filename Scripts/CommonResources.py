


def Init():
    import Bladex
    import BBLib

    BBLib.ReadMMP('../../3dChars/Kgt.mmp')
    BBLib.ReadMMP('../../3dChars/Amz.mmp')
    BBLib.ReadMMP('../../3dChars/Dwf.mmp')
    BBLib.ReadMMP('../../3dChars/Bar.mmp')
    BBLib.ReadMMP('../../3dobjs/weapons.mmp')
    BBLib.ReadMMP('../../3dobjs/genericos.mmp')

    BBLib.ReadMMP('../../3dChars/KgtSkin1.mmp')
    BBLib.ReadMMP('../../3dChars/KgtSkin2.mmp')
    BBLib.ReadMMP('../../3dChars/BarSkin1.mmp')
    BBLib.ReadMMP('../../3dChars/BarSkin2.mmp')
    BBLib.ReadMMP('../../3dChars/AmzSkin1.mmp')
    BBLib.ReadMMP('../../3dChars/AmzSkin2.mmp')
    BBLib.ReadMMP('../../3dChars/DwfSkin1.mmp')
    BBLib.ReadMMP('../../3dChars/DwfSkin2.mmp')
    
    BBLib.ReadMMP('../../3dobjs/weapons2.mmp')
    BBLib.ReadMMP("../../3dobjs/ArcheryTarget.mmp")
    BBLib.ReadMMP('../../Data/UIWidgets.mmp')
    #
    Bladex.ReadBitMap("../../Data/empty.bmp","empty")

    
    Bladex.BodInspector()
    BBLib.LoadBOD('Piedra_01')
    BBLib.LoadBOD('Llavero')


