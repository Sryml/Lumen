import Bladex

Bladex.SetCallCheck(1)

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("arena7.lvl")

execfile("../../Scripts/BladeInit.py")

execfile("agua.py")
execfile("objs.py")

char.Angle=0
