
#CUERVO-VOLANDO-SOBRE-EL-COMIENZO-DEL-RIO
cuervo1_sound=Bladex.CreateSound('../../Sounds/cuervo-graznido.wav', 'SonidoCuervo1')
cuervo1_sound.Volume=1.0
cuervo1_sound.MinDistance=3000
cuervo1_sound.MaxDistance=40000

crow1=Bladex.CreateEntity("Crow1","Crw",-84000,-5000,-114000)
crow1.Orientation=0.7,0.7,0,0
crow1.Actor=1
crow1.Animation="Crw_fly"
crow1.FPS=20.0
crow1.SendSectorMsgs=0
crow1.TurnOn()



EspantarCuervo1()


#CUERVO-VOLANDO-SOBRE-EL-ACANTILADO-DEL-POBLADO
cuervo2_sound=Bladex.CreateSound('../../Sounds/cuervo-graznido.wav', 'SonidoCuervo2')
cuervo2_sound.Volume=1.0
cuervo2_sound.MinDistance=3000
cuervo2_sound.MaxDistance=40000

crow2=Bladex.CreateEntity("Crow2","Crw",-126000,-16000,64000)
crow2.Orientation=0.7,0.7,0,0
crow2.Actor=1
crow2.Animation="Crw_fly"
crow2.FPS=20.0
crow2.SendSectorMsgs=0
crow2.TurnOn()



EspantarCuervo2()

#CUERVO-VOLANDO-SOBRE-EL-PRINCIPIO-DEL-ACANTILADO-DEL-POBLADO
cuervo3_sound=Bladex.CreateSound('../../Sounds/cuervo-graznido.wav', 'SonidoCuervo3')
cuervo3_sound.Volume=1.0
cuervo3_sound.MinDistance=3000
cuervo3_sound.MaxDistance=40000

crow3=Bladex.CreateEntity("Crow3","Crw",-128000,-24000,101000)
crow3.Orientation=0.7,0.7,0,0
crow3.Actor=1
crow3.Animation="Crw_fly"
crow3.FPS=20.0
crow3.SendSectorMsgs=0
crow3.TurnOn()

EspantarCuervo3()
