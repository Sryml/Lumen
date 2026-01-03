import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import Button
import AbreCam
import AuxFuncs
import darfuncs
import Stars

#LIBROS QUE APARECEN

LIBROS_DELTA_X=11000

#LIBRO QUE SE MUEVE  (0,0,-400)

o=Bladex.CreateEntity("Libromov","LibroPulsador",-271747.264000+LIBROS_DELTA_X,-27481.577000,76489.124000)
#o=Bladex.CreateEntity("Libromov","Libro",-271647.264000+LIBROS_DELTA_X,-27481.577000,76489.124000)
o.Static=0
o.Scale=2.194768
o.Orientation=0.707107,0.707107,0.000000,0.000000

darfuncs.SetHint(o,"Fake Book")


sb1=Bladex.GetSector(-270750+LIBROS_DELTA_X, -27500, 76750)
sb1.Active=0



button=Button.CreateButtonCombination(0,Descubre,"")
xx = button.AddButton("Libromov",2,(1,0,0),400,0,0,1)
xx.sound = Bladex.CreateSound('../../Sounds/caida-libro.wav', 'Sound libro')
xx.sound.Volume=1.0
xx.sound.MinDistance=7000
xx.sound.MaxDistance=20000
