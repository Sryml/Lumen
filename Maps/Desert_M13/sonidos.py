import Sounds
import ReadGSFile

ReadGSFile.ProcessGhostSectorFile("desert.sf")



#####--altar de fuego---######

saltarf=Bladex.CreateSound("../../Sounds/fuego-altar-loop.wav","saltarf")
saltarf.MaxDistance=30000
saltarf.MinDistance=2000
saltarf.Volume=1.0

encenf=Bladex.CreateSound("../../Sounds/encendido-fuego.wav","encenf")
encenf.MaxDistance=30000
encenf.MinDistance=2000
encenf.Volume=1.0

#saltarf.Play(-60000, -4500, 41600,-1)
