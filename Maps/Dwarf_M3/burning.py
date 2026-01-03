

import Bladex


#######################################################
# Define the talking knight class
#######################################################


# flame barriles
object_kind="Barril"
particle_type="LargeFire"
min_d=230.0
max_d=430.0
flame_h=4.0
flame_s=1.0
speed=1.5
time2live=1000000			# 10 Seconds


Bladex.AddCombustionDataFor(object_kind, particle_type, min_d, max_d, flame_h, flame_s, speed, time2live)

# flame CAJAS
object_kind="Cajon2"
particle_type="LargeFire"
min_d=600.0
max_d=400.0
flame_h=4.0
flame_s=1.0
speed=1.5
time2live=1000000			# 10 Seconds


Bladex.AddCombustionDataFor(object_kind, particle_type, min_d, max_d, flame_h, flame_s, speed, time2live)

