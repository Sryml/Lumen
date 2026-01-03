import NetTraps

# Agrega una trampa de lava
lava = NetTraps.LavaFlood(-500,60000,60,30)	# <limite superior>,<limite inferior>,<maximo de tiempo>,<minimo de tiempo>
lava.Position = (26837, 74000, 4427)		# Posicion donde esta la lava
lava.TimeRound  = 4				# Tiempo de oscilacion
lava.DeltaRound = 3000				# Radio de oscilacion
lava.Quake      = 1				# asigna el evento de temblores a la oscilacion.

# Temblores
NetTraps.mQuakeTime     =   2			# Duracion minima del temblores
NetTraps.MQuakeTime     =   4			# Duracion maxima del temblores
NetTraps.mQuakeDelay    =   5			# Retardo minimo entre temblores
NetTraps.MQuakeDelay    =  10			# Retardo maximo entre temblores
NetTraps.QuakeIntensity = 100			# Intensidad del temblor