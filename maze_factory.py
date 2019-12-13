from picraft import *
from mcpi.minecraft import Minecraft

def clear_space(mc, x1, x2, z1, z2):
	"""
	takes a coordinate and clears out a (X x Y)-dimeanion space for our 
	structures
	"""
	x, y, z = mc.player.getPos() # get initial position
	mc.setBlocks(x1, y, z1, x2, y+30, z2, 0)
		
def get_dimensions():
	"""
	calculates the dimensions relative to the player for maze
	construction 
	"""
	x, y, z = mc.player.getPos()
	x1, x2 = (x-50), (x+50)
	z1, z2 = (z-2), (z-120) 
	return x1, x2, z1, z2
	
def create_maze(mc, x1, x2, z1, z2):
	"""
	clears a space and makes a maze baby, just the way you like it
	"""
	
# init
mc = Minecraft.create()
x, y, z = mc.player.getPos() # get initial position
ax, ay, az = int(x), int(y), int(z+2)
mc.player.setPos(ax, ay, az)  

#get dimensions and clear space
x1,x2,z1,z2 = get_dimensions()
#clear_space(mc, x1, x2, z1, z2)
