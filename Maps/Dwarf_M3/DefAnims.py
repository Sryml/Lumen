import Bladex


def qLoadAnims(biped_name, Animation, AnimationFileName, person):
    Bladex.LoadSampledAnimation(
        "../../Anm/" + AnimationFileName + ".BMV",
        AnimationFileName,
        0,
        person,
    )
    Bladex.AddBipedAction(biped_name, Animation, AnimationFileName, 0.0, 1.0, 0)


def _Player1(biped_name, Kind):
    qLoadAnims(biped_name, "final_dwarf", "Dwf_final_dwarf", Kind)
    qLoadAnims(biped_name, "masacre", "Dwf_masacre", Kind)
    qLoadAnims(biped_name, "entrada", "Dwf_entrada", Kind)


def Knight():
    _Player1("Knight", "Knight_N")


def Dwf():
    _Player1("Dwf", "Dwarf_N")


def Amz():
    _Player1("Amz", "Amazon_N")


def Bar():
    _Player1("Bar", "Barbarian_N")
