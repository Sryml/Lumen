import GameText
import Bladex
import OnOff
import Torchs



HistoriaSec = Bladex.GetSector(-38352.7904858, 16835.2, 21096.4367189)
HistoriaSec.OnEnter = CuentaCuentos


o=Bladex.CreateEntity("lampegip2","Lamparaegipto",-38228.992000,16322.019000,28515.362000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 40 ]
o.Lights=[ (0.000000,0.090000,(216,95,14)) ]

OnOff.AddLightData("lampegip2",30.000000,0.090000,(216,95,14))
OnOff.LightSpeed     =   0.005


ApagalaSec = Bladex.GetSector(-38021.14, 17482.25, 6958.78)
ApagalaSec.OnEnter = Apagalahist
