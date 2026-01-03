import Bladex

Bladex.LoadSampledAnimation("../../Anm/Crw_act11.BMV","Crw_act11",1,"Crw")

def CreateCrow(pos,fps,orient):
	cuervovolando1=Bladex.CreateEntity("CuervoVolando1", "Crw",pos[0],pos[1],pos[2])
	cuervovolando1.Orientation=orient
	cuervovolando1.CastShadows=0
	cuervovolando1.Actor=1
	cuervovolando1.Animation="Crw_act11"
	cuervovolando1.FPS=fps
	cuervovolando1.SendSectorMsgs=0
	cuervovolando1.TurnOn()
posi = -28000,-19000,32000
Bladex.AddScheduledFunc(Bladex.GetTime()+ 0.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+ 2.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+ 4.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+ 6.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+ 8.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+10.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+12.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+14.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+16.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+18.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))
Bladex.AddScheduledFunc(Bladex.GetTime()+20.0,CreateCrow,(posi,25.0,(0.555685,0.555685,-0.437281,0.437281)))


