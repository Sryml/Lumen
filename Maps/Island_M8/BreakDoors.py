import EnmGenRnd
import ReadGSFile
import Actions
import darfuncs



cgateA1=Bladex.GetSector(-15750,1000,-6500)
cgateA1.InitBreak( (-200,0,0),(0,1800,0),(0,0,700),'madera pesada')
cgateA1.Active=0




darfuncs.EnterSecIdEvent("saledeposito",ActivaSectorEsqueletoMaloso)