# 0..511  Reserved to the game mode (arena, combat, deadmatch, capture the flag, etc.)
NET_GAME_MODE = 0 

# 512..1023  Reserved to the engine based scripts (lava deaths, and misc FX)
NET_ENGINE = 512

# 1024...32000 Used to send map specifics values (as changes in the environment, or some visual FX)
NET_USER = 1024

# Please, put your values here....
################################## NET_GAME_MODE values ##################################

#-------------------------
NET_GAME_FRAGS		= NET_GAME_MODE+0 
NET_GAME_STATUS		= NET_GAME_MODE+1
NET_GAME_KOMBATERS	= NET_GAME_MODE+2

#                     . . .

NET_GAME_IN_COMBAT	= NET_GAME_MODE+201
NET_GAME_CHAT_STRING	= NET_GAME_MODE+202

# Please, put your values here....
################################## NET_ENGINE values ##################################

NET_GAME_FADE_DUE2BIGFALL = NET_ENGINE + 0
NET_GAME_THROW_WEAPON     = NET_ENGINE + 1
NET_GAME_START_TRAPS      = NET_ENGINE + 2


################################## NET_USER values ##################################

# arena 1 (volcano deathmatch)

NET_GAME_LAVAPOSITION	= NET_USER + 0