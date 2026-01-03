import darfuncs
import Bladex
import Scorer
import Reference
import darfuncs

demoniote=Bladex.CreateEntity("DemonioGigante", "Great_Demon", 582725,307446,183505)
demoniote.Position = char.Position
demoniote.Person   = 1
demoniote.Angle    = 3.1415
EnemyTypes.EnemyDefaultFuncs(demoniote)
demoniote.Data.EndPhase1(demoniote.Name)
darfuncs.HideBadGuy(demoniote.Name)
demoniote.ImDeadFunc = MuerteDemoniote


StartArena1SceneSector = Bladex.GetSector(558119, 301927, 180746)
StartArena1SceneSector.OnEnter = IniciaSecuenciaArena