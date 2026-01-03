import Bladex

def qLoadAnims(Kind,Animation,person):
	Bladex.LoadSampledAnimation("../../Anm/"+Kind+"_"+Animation+".BMV",Kind+"_"+Animation,0,person)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)

def Dwf():
	qLoadAnims("Dwf","final_dwarf","Dwarf_N")
	qLoadAnims("Dwf","masacre",    "Dwarf_N")
	qLoadAnims("Dwf","entrada",    "Dwarf_N")