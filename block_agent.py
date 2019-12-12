from coordinate import Coordinate
from mcpi.minecraft import Minecraft
import time

class BlockAgent:
	def __init__(self, position, direction, mc):
		'''
		set position and direction of the agent
		position::Coordinate
		direction::chr(n,s,e,w)
		mc::Minecraft
		'''
		self.position = position
		self.direction = direction
		self.mc = mc
		
	def print_direction(self):
		print(self.direction)
		
	def move_forward(self):
		x,y,z = self.mc.player.getPos()
		prev_pos = self.position
		if self.direction == 'n':
			print("moving north")
			self.position = Coordinate(x,y,z-1) if 0 == self.mc.getBlock(x, y, z-1) else self.position
		elif self.direction == 's':
			print("moving south")
			self.position = Coordinate(x,y,z+1) if 0 == self.mc.getBlock(x, y, z+1) else self.position
		elif self.direction == 'e':
			print("moving east")
			self.position = Coordinate(x+1,y,z) if 0 == self.mc.getBlock(x+1, y, z) else self.position
		elif self.direction == 'w':
			print("moving west")		
			self.position = Coordinate(x-1,y,z)	if 0 == self.mc.getBlock(x-1, y, z) else self.position
		print("removing block from ({}, {}, {})".format(x,y,z))
		print("placing new block   ({}, {}, {})".format(self.position.get_x(), self.position.get_y(), self.position.get_z()))
		self.mc.setBlock(x, y, z, 0) # remove previous block
		self.mc.setBlock(
			self.position.get_x(),
			self.position.get_x(),
			self.position.get_x(),
			1) # set new block
	
		
mc = Minecraft.create() # instantiate api
x, y, z = mc.player.getPos() # get initial position
mc.player.setPos(int(x+1), int(y), int(z)) # modify position to make way for the snake
print("player pos:\ne/w: {}\nn/s: {}\nalt: {}".format(x+1, z, y))

agent_smith = BlockAgent(Coordinate(x,y,z), 'n', mc) # instantiate agent
agent_smith.print_direction() # print orientation

for i in range(10):
	agent_smith.move_forward()
	time.sleep(.5)
	
