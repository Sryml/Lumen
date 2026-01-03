import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import AuxFuncs
import darfuncs
import Stars
import Bladex
import OnOff

	
GrupoMuerte1         = darfuncs.E_Grup()
GrupoMuerte1.OnDeath = FinGrupoMuerte1
GrupoMuerte1.AddGuy("11HSKL")
GrupoMuerte1.AddGuy("12HSKL")
	
darfuncs. EnterSecEvent(-17000,-34000,26000,Sorpresa1)

###########


GrupoMuerte2         = darfuncs.E_Grup()
GrupoMuerte2.OnDeath = FinGrupoMuerte2
GrupoMuerte2.AddGuy("13HSKL")
GrupoMuerte2.AddGuy("14HSKL")

	
darfuncs. EnterSecEvent(-4000,-33000,26000,Sorpresa2)


###########


GrupoMuerte3         = darfuncs.E_Grup()
GrupoMuerte3.OnDeath = FinGrupoMuerte3
GrupoMuerte3.AddGuy("15HSKL")
GrupoMuerte3.AddGuy("16HSKL")

	
darfuncs. EnterSecEvent(7000,-34000,15000,Sorpresa3)

GrupoMuerte4         = darfuncs.E_Grup()
GrupoMuerte4.OnDeath = FinGrupoMuerte4
GrupoMuerte4.AddGuy("17HSKL")
