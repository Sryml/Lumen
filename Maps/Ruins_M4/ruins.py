import Bladex





### Sol ###

Bladex.SetSun(1,200,180,-30)


### Luz lago subt. ###

luzlagosub=Bladex.CreateEntity("LuzLagoSub", "Entity Spot", -4552.0, 13500.0, -54890.0)
luzlagosub.Color=128, 250, 255
luzlagosub.Intensity=25
luzlagosub.Precission=0.03125
luzlagosub.Visible=0
luzlagosub.CastShadows=0


### Agua ###

agua_lagoext=Bladex.CreateEntity("agua_lagoext","Entity Water",62000,4000,56000) # 1150,56000)
agua_lagoext.Reflection=0
agua_lagoext.Color=0,10,10

agua_pozo=Bladex.CreateEntity("agua_pozo","Entity Water",48500,11000,-49000) # 9150,-49000)
agua_pozo.Reflection=-1
agua_pozo.Color=0,10,10

agua_lagoint=Bladex.CreateEntity("agua_lagoint","Entity Water",-5000,13500,-54000) # 9600,-54000)
agua_lagoint.Reflection=-1.5
agua_lagoint.Color=0,90,70

agua_dercercainic=Bladex.CreateEntity("agua_dercercainic","Entity Water",45500,11500,20500)
agua_dercercainic.Reflection=-1
agua_dercercainic.Color=0,10,10

agua_deropinic=Bladex.CreateEntity("agua_deropinic","Entity Water",-73500,11200,1500)
agua_deropinic.Reflection=-1
agua_deropinic.Color=0,10,10



### Sonidos para animaciones

ruinsesfcorto1amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz.wav', 'RuinsEsfuerzoCorto1Amz')
ruinsesfcorto1amz.MinDistance=1000
ruinsesfcorto1amz.MaxDistance=10000
ruinsesfcorto2amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz2.wav', 'RuinsEsfuerzoCorto2Amz')
ruinsesfcorto2amz.MinDistance=1000
ruinsesfcorto2amz.MaxDistance=10000
ruinspasopie1amz=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'RuinsPasoPie1Amz')
ruinspasopie1amz.MinDistance=1000
ruinspasopie1amz.MaxDistance=10000
ruinspasopie2amz=Bladex.CreateSound('../../sounds/paso-piedra-2.wav', 'RuinsPasoPie2Amz')
ruinspasopie2amz.MinDistance=1000
ruinspasopie2amz.MaxDistance=10000
ruinspasopie3amz=Bladex.CreateSound('../../sounds/paso-piedra-3.wav', 'RuinsPasoPie3Amz')
ruinspasopie3amz.MinDistance=1000
ruinspasopie3amz.MaxDistance=10000
ruinsesflargoamz=Bladex.CreateSound('../../sounds/esfuerzo-largo-amz.wav', 'RuinsEsfuerzoLargoAmz')
ruinsesflargoamz.MinDistance=1000
ruinsesflargoamz.MaxDistance=10000


### Sectores inclinados

Bladex.GetSector(55000, 1700, 49000).TooSteep=0
