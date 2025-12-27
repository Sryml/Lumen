import netgame
import Bladex

SonidosDedicados = netgame.IsDedicated()

if SonidosDedicados:
	KindSound = {}
	def anifake(EntityName,EventName):
		index = KindSound[Bladex.GetEntity(EntityName).Kind].index(EventName)
		netgame.ChangeAnmSoundIndex(EntityName,index)

def AddAnimSound(per,aniname, sonido, time):
	if netgame.GetNetState() == 2:
		netgame.AddSoundToClient(per.Name,aniname,sonido)
	else:
		if SonidosDedicados:
			if not KindSound.has_key(per.Kind):
				KindSound[per.Kind] = []

			evname = aniname + "fake"
			
			if not (evname in KindSound[per.Kind]):
				Bladex.AddAnmEvent(aniname,evname,time)
				KindSound[per.Kind].append(evname)
				
			per.AddAnmEventFunc(evname, anifake)
		else:
			per.AddAnimSound(aniname, sonido, time)