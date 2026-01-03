import Bladex
import Objects
import Sounds
import Levers
import AuxFuncs


###########################
#     Puente levadizo     #
###########################


puentelevadizo=Bladex.CreateEntity("PuenteLevadizo","PuenteFernando",-104478.986206,-5461.340888,-55254.571972)
puentelevadizo.Scale=1.000000
puentelevadizo.Orientation=1.000000,0.000000,0.000000,0.000000
puentelevadizo.ExclusionMask=2

puentelevadizomovil=Objects.CreateDinamicObject("PuenteLevadizo")

looppuentelevadizo=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopPuenteLevadizo")
looppuentelevadizo.Volume=1
#looppuentelevadizo.Scale=0.56
#looppuentelevadizo.MinDistance=500
looppuentelevadizo.MinDistance=10000
looppuentelevadizo.MaxDistance=90000

golpepuentelevadizo=Sounds.CreateEntitySound("../../Sounds/drawbridge-door-close.wav", "GolpePuenteLevadizo")
golpepuentelevadizo.Volume=1
#golpepuentelevadizo.Scale=0.56
#golpepuentelevadizo.MinDistance=500
golpepuentelevadizo.MinDistance=10000
golpepuentelevadizo.MaxDistance=90000

atranquepuentelevadizo=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "AtranquePuenteLevadizo")
atranquepuentelevadizo.Volume=1
#atranquepuentelevadizo.Scale=0.56
#atranquepuentelevadizo.MinDistance=500
atranquepuentelevadizo.MinDistance=10000
atranquepuentelevadizo.MaxDistance=90000

puentelevadizomovil.estado=0



puentelevadizoinv=Bladex.CreateEntity("PuenteLevadizoInv","PuenteFernando",-104478.986206,-5461.340888,-55254.571972)
puentelevadizoinv.Scale=1.000000
puentelevadizoinv.Orientation=1.000000,0.000000,0.000000,0.000000
puentelevadizoinv.Alpha=0.0



palanca1puentelev=Levers.PlaceLever("Palanca1PuenteLev", Levers.LeverType3, (-95225.475417,-9673.524137,-56605.334630), (0.006171,0.006171,-0.707080,0.707080), 1.0)
palanca1puentelev.mode=2

palanca2puentelev=Levers.PlaceLever("Palanca2PuenteLev", Levers.LeverType3, (-112923.146402,-9167.543743,-56615.794150), (0.000000,0.000000,0.707107,-0.707107), 1.0)
palanca2puentelev.mode=2

palanca1puentelev.OnTurnOnFunc=BajaPuente
palanca1puentelev.OnTurnOnArgs=()

palanca2puentelev.OnTurnOnFunc=BajaPuente
palanca2puentelev.OnTurnOnArgs=()
