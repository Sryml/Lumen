import Bladex



class CampoData:

	pass


def Initialise(*args, **kwargs):
	# -Sryml
	entity = args[0]
	if not entity.Data:
		entity.Data=CampoData()
	entity.Data.__dict__.update(kwargs)
