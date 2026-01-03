import AniSound
import Sparks
import Actions
import pocimac
import ItemTypes
import Breakings



##########ARCO Y FLECHAS EN ZONA ARANIAS

bow=Bladex.CreateEntity("bararco1","Arco",8329.191980,-9765.342934,-93910.769477,"Weapon")
bow.Scale=1.000000
bow.Orientation=0.724387,0.145711,0.123904,0.662329
ItemTypes.ItemDefaultFuncs(bow)


o=Bladex.CreateEntity("barcarcaj1","Carcaj",9733.588995,-9899.648841,-93378.082146)
o.Scale=1.000000
o.Orientation=0.043847,0.324645,-0.154387,0.932120
ItemTypes.ItemDefaultFuncs (o)
o.Data.ArrowsLeft=10

o=Bladex.CreateEntity("barchaos1","Chaosword",-42238.841135,-19135.330038,63591.795890,"Weapon")
o.Scale=1.000000
o.Orientation=0.663021,0.652331,-0.262221,0.257113
ItemTypes.ItemDefaultFuncs (o)


##########	ECLIPSE

o=Bladex.CreateEntity("bareclipse","Eclipse",29014.249950,-46583.725026,159283.161832,"Weapon")
o.Scale=1.000000
o.Orientation=0.992717,0.015636,0.000177,-0.119450
ItemTypes.ItemDefaultFuncs (o)



o=Bladex.CreateEntity("bardeathsword","DeathSword",-197309.984000,-10033.175000,175969.054000,"Weapon")
o.Scale=1.000000
o.Orientation=0.993292,-0.009411,0.114937,0.008486
ItemTypes.ItemDefaultFuncs (o)



o=Bladex.CreateEntity("NoName1","Skull",-196426.082000,-10091.167000,175847.557000,"Physic")
o.Scale=1.000000
o.Orientation=0.825159,0.553577,-0.078992,-0.080157



o=Bladex.CreateEntity("NoName2","EsqueletoPieza1",-195934.926000,-10135.590000,175907.199000,"Physic")
o.Scale=1.000000
o.Orientation=0.883977,0.147699,-0.392551,-0.206574



####bo
o=Bladex.CreateEntity("barbo","Bo",-55495.837000,-13140.449000,39962.215000,"Weapon")
o.Scale=1.000000
o.Orientation=0.915217,0.179416,0.209322,0.293891
ItemTypes.ItemDefaultFuncs (o)



o=Bladex.CreateEntity("barescudo1","Escudo1",-124457.081137,-23408.838585,147432.837867,"Weapon")
o.Scale=1.000000
o.Orientation=0.967276,0.188131,0.008445,-0.170034
ItemTypes.ItemDefaultFuncs (o)



o=Bladex.CreateEntity("NoName2","EsqueletoPieza1",-121227.494463,-23311.202945,145322.804977,"Physic")
o.Scale=1.000000
o.Orientation=0.340719,0.029809,-0.936117,0.081900



o=Bladex.CreateEntity("NoName3","EsqueletoPieza2",-122362.153967,-23300.877955,144522.513034,"Physic")
o.Scale=1.000000
o.Orientation=0.664432,0.356802,-0.559159,0.344331



o=Bladex.CreateEntity("NoName5","EsqueletoPieza4",-121346.572929,-23246.006455,144268.729699,"Physic")
o.Scale=1.000000
o.Orientation=0.004153,0.654042,-0.755979,-0.026586



o=Bladex.CreateEntity("NoName6","EsqueletoPieza4",-122448.360149,-23253.969412,147436.857403,"Physic")
o.Scale=1.000000
o.Orientation=0.179098,-0.802794,0.478795,-0.306921



o=Bladex.CreateEntity("NoName7","EsqueletoPieza4",-122828.137445,-23232.421754,145977.518527,"Physic")
o.Scale=1.000000
o.Orientation=0.687791,0.331192,0.577559,0.289278



o=Bladex.CreateEntity("NoName8","GladiusPieza1",-124187.934957,-23218.468309,145470.644807,"Physic")
o.Scale=1.000000
o.Orientation=0.830205,-0.006262,0.557336,0.009816



o=Bladex.CreateEntity("NoName9","GladiusPieza2",-124447.162625,-23230.898016,146162.954700,"Physic")
o.Scale=1.000000
o.Orientation=0.016172,0.974166,0.157113,0.161413



o=Bladex.CreateEntity("NoName10","EsqueletoPieza2",-121197.073485,-23307.237922,147553.284822,"Physic")
o.Scale=1.000000
o.Orientation=0.538581,0.369127,0.653747,-0.382479



o=Bladex.CreateEntity("NoName11","EsqueletoPieza2",-172659.994598,-10851.819411,140810.647332,"Physic")
o.Scale=1.000000
o.Orientation=0.869726,0.475929,0.110553,0.069616



o=Bladex.CreateEntity("NoName12","EsqueletoPieza1",-173813.515570,-10778.341956,139970.564043,"Physic")
o.Scale=1.000000
o.Orientation=0.886296,0.034982,0.461180,-0.023850



o=Bladex.CreateEntity("NoName13","EsqueletoPieza4",-172774.744792,-10794.650786,139161.161868,"Physic")
o.Scale=1.000000
o.Orientation=0.159554,0.831580,-0.380607,-0.371693



o=Bladex.CreateEntity("NoName14","EsqueletoPieza4",-173764.288735,-10788.859373,141874.146239,"Physic")
o.Scale=1.000000
o.Orientation=0.453483,-0.359938,-0.763023,0.287391



o=Bladex.CreateEntity("NoName16","EsqueletoPieza2",-173019.383826,-10844.339859,138460.185376,"Physic")
o.Scale=1.000000
o.Orientation=0.615977,-0.250994,-0.504043,0.550922



o=Bladex.CreateEntity("NoName17","GladiusPieza1",-170634.951299,-10768.451721,140103.534494,"Physic")
o.Scale=1.000000
o.Orientation=0.999597,-0.015770,-0.004257,0.023227



o=Bladex.CreateEntity("NoName18","GladiusPieza2",-170744.383958,-10788.131453,141040.530411,"Physic")
o.Scale=1.000000
o.Orientation=0.023822,0.986247,0.161100,0.028206



o=Bladex.CreateEntity("barmaza","Maza",-172171.164558,-10844.292690,142612.419807,"Weapon")
o.Scale=1.000000
o.Orientation=0.082675,0.961510,0.081370,0.249081
ItemTypes.ItemDefaultFuncs (o)



o=Bladex.CreateEntity("NoName20","Hoguera",-172040.476709,-10944.081054,139961.936688,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 63 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName22","Tabla_rota",-171201.198745,-10797.808589,138476.594090,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName23","Tabla_rota",-173672.120980,-10803.268747,135769.664236,"Physic")
o.Scale=1.308209
o.Orientation=0.449775,0.449775,0.545621,-0.545621



o=Bladex.CreateEntity("NoName24","Tabla_rota",-169830.672187,-11456.299429,140953.608364,"Physic")
o.Scale=1.160969
o.Orientation=0.641024,0.161534,0.301676,0.687012



o=Bladex.CreateEntity("barescudo2","Escudo2",-168921.876080,-25852.529636,208776.079751,"Weapon")
o.Scale=1.000000
o.Orientation=0.965467,-0.178088,-0.124070,-0.144098
ItemTypes.ItemDefaultFuncs (o)



o=Bladex.CreateEntity("NoName26","EsqueletoPieza1",-167407.401906,-25686.928059,209458.033546,"Physic")
o.Scale=1.000000
o.Orientation=0.963667,0.144021,-0.222480,0.033250



o=Bladex.CreateEntity("NoName27","EsqueletoPieza2",-168752.743422,-25700.162107,209918.473824,"Physic")
o.Scale=1.000000
o.Orientation=0.744060,0.436202,-0.498926,0.084709



o=Bladex.CreateEntity("NoName28","EsqueletoPieza4",-167574.863229,-25634.230065,208130.777928,"Physic")
o.Scale=1.000000
o.Orientation=0.311412,-0.368092,-0.851934,0.204301
