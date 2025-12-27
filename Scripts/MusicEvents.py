import Bladex
import DMusic
import string




#
#   EXPLANATION:
#
#   AddCombatMusic("Knight_N","../../sounds/combate1.wav", 100 , 2.2 , 3.5 ,1.4)
#                   (1)             (2)                       (3)   (4)   (5)  (6)
#
#       (1)  Race name (as  given in the scripts\enemies.py)
#       (2)  File of the music (wav or mp3)
#       (3)  Priority
#       (4)  Fade in time - OPT
#       (5)  Fade out time - OPT
#       (6)  Volume - OPT
#
#       OPT means OPTIONAL (1 by default in all of them)
#
#
#   ExcludeMusicFor("8ORC")
#
#       For that _specific_ enemy no music will be played , even that one was assigned to its kind
#


#
# Add the data HERE.
#
#AddCombatMusic("Knight_N","../../sounds/combate1.wav",100)



####### Mounstros bobetes  #######
#DMusic.AddCombatMusic("Spidersmall",     "../../sounds/suspense-1.wav",       25,1)
#DMusic.AddCombatMusic("Cos",             "../../sounds/suspense-1.wav",       50,1)
#DMusic.AddCombatMusic("Lich",            "../../sounds/suspense-1.wav",       75,1)
#DMusic.AddCombatMusic("Knight_Zombie",   "../../sounds/suspense-1.wav",      100,1)

####### Mounstros comunachos  #######
DMusic.AddCombatMusic("Ork",             "../../sounds/suspense-1.wav",      125,1)
#AddCombatMusic("2ORC",             "../../sounds/test.mp3",      126)

#DMusic.AddCombatMusic("Knight_Traitor",  "../../sounds/suspense-1.wav",      150,1)
#DMusic.AddCombatMusic("Skeleton",        "../../sounds/suspense-1.wav",      175,1)
#DMusic.AddCombatMusic("Dark_Ork",        "../../sounds/suspense-1.wav",      200,1)
#DMusic.AddCombatMusic("Gold_Ork",        "../../sounds/suspense-1.wav",      225,1)
#DMusic.AddCombatMusic("Great_Ork",       "../../sounds/combate1.wav",        250,1)
#DMusic.AddCombatMusic("Salamander",      "../../sounds/suspense-1.wav",      275,1)
#DMusic.AddCombatMusic("Troll_Dark",      "../../sounds/suspense-1.wav",      300,1)
#DMusic.AddCombatMusic("Troll_snow",      "../../sounds/suspense-1.wav",      325,1)

####### Mounstros dignos respeto  #######
#DMusic.AddCombatMusic("Little_Demon",    "../../sounds/suspense-1.wav",      350,1)
#DMusic.AddCombatMusic("Golem_clay",      "../../sounds/suspense-1.wav",      375,1)
#DMusic.AddCombatMusic("Dark_Knight",     "../../sounds/suspense-1.wav",      400,1)
#DMusic.AddCombatMusic("Minotaur",        "../../sounds/suspense-1.wav",      425,1)
#DMusic.AddCombatMusic("Golem_stone",     "../../sounds/suspense-1.wav",      450,1)
#DMusic.AddCombatMusic("Golem_metal",     "../../sounds/suspense-1.wav",      475,1)
#DMusic.AddCombatMusic("ChaosKnight",     "../../sounds/suspense-1.wav",      500,1)

##### Jefazos #####
#DMusic.AddCombatMusic("Ragnar",          "../../sounds/suspense-1.wav",      525,1)
#DMusic.AddCombatMusic("Golem_lava",      "../../sounds/suspense-1.wav",      550,1)
#DMusic.AddCombatMusic("Vamp",            "../../sounds/suspense-1.wav",      575,1)
#DMusic.AddCombatMusic("Great_Demon",     "../../sounds/suspense-1.wav",      600,1)
#DMusic.AddCombatMusic("DalGurak",        "../../sounds/suspense-1.wav",      625,1)
#DMusic.AddCombatMusic("DarkLord",        "../../sounds/suspense-1.wav",      650,1)





print "MusicEvents.py executed"
