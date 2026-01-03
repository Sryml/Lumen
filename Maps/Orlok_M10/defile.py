import Bladex
import whrandom
import NetSounds




### Sol ###

#Bladex.SetSun(1,-75,75,-5)



### Sectores que resbalan

s=Bladex.GetSector(33250,-42150,65125)
s.TooSteep=1

s=Bladex.GetSector(33250,-42150,72875)
s.TooSteep=1

s=Bladex.GetSector(16750,-42150,65125)
s.TooSteep=1

s=Bladex.GetSector(16750,-42150,72875)
s.TooSteep=1




#######################################
### Pasos en animaciones scriptadas ###
#######################################


orlokpasonie1=Bladex.CreateSound('../../sounds/M-00-NIEVEL2.wav', 'OrlokPasoNie1')
orlokpasonie1.MinDistance=500
orlokpasonie1.MaxDistance=8000
orlokpasonie2=Bladex.CreateSound('../../sounds/M-00-NIEVER1.wav', 'OrlokPasoNie2')
orlokpasonie2.MinDistance=500
orlokpasonie2.MaxDistance=8000
orlokpasonie3=Bladex.CreateSound('../../sounds/M-00-NIEVER2.wav', 'OrlokPasoNie3')
orlokpasonie3.MinDistance=500
orlokpasonie3.MaxDistance=8000


# Animacion inicio
