
#CUERVO-VOLANDO-SOBRE-EL-TEMPLO
cuervo11_sound=Bladex.CreateSound('../../Sounds/cuervo-graznido.wav', 'SonidoCuervo11')
cuervo11_sound.Volume=1.0
cuervo11_sound.MinDistance=3000
cuervo11_sound.MaxDistance=40000

crow11=Bladex.CreateEntity("Crow11","Pio",34000,-25000,-38000)
crow11.Orientation=0.7,0.7,0,0
crow11.Actor=1
crow11.Animation="Crw_fly"
crow11.FPS=20.0
crow11.SendSectorMsgs=0
crow11.TurnOn()



#CUERVO-VOLANDO-BAJO-EN-EL-ACANTILADO

EspantarCuervo11()

cuervo12_sound=Bladex.CreateSound('../../Sounds/cuervo-graznido.wav', 'SonidoCuervo11')
cuervo12_sound.Volume=1.0
cuervo12_sound.MinDistance=3000
cuervo12_sound.MaxDistance=40000

crow12=Bladex.CreateEntity("Crow12","Pio",73000,-3000,6000)
crow12.Orientation=0.7,0.7,0,0
crow12.Actor=1
crow12.Animation="Crw_fly"
crow12.FPS=20.0
crow12.SendSectorMsgs=0
crow12.TurnOn()



EspantarCuervo12()
