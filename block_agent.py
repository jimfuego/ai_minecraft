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
		'''prints the current facing direction of the agent'''
		print(self.direction)
		
	def remove_block(self,coordinate):
		'''wrapper takes a coordinate and clears that place'''
		self.mc.setBlock(coordinate.get_x(), coordinate.get_y(), coordinate.get_z(), 0)

	def remove_block(self,x,y,z):
		'''wrapper takes (x,y,z) values and clears that place'''
		self.mc.setBlock(x, y, z, 0)
	
	def add_block(self, coordinate):
		'''wrapper takes a coordinate and clears that place'''
		self.mc.setBlock(coordinate.get_x(), coordinate.get_y(), coordinate.get_z(), 1)

	def add_block(self,x,y,z):
		'''wrapper takes (x,y,z) values and clears that place'''
		self.mc.setBlock(x, y, z, 1)
	
	def get_next_block_type(self):
		'''reads direction from the agent state to return next block-type in path'''
		if self.direction == 'n':
			return self.mc.getBlock(x, y, z - 1)
		if self.direction == 's':
			return self.mc.getBlock(x, y, z + 1)
		if self.direction == 'e':
			return self.mc.getBlock(x + 1, y, z) 
		if self.direction == 'w':
			return self.mc.getBlock(x - 1, y, z)
		
	def get_next_block_coordinate(self):
		'''reads direction from the agent state to return a coordinate for the next step'''
		if self.direction == 'n':
			return Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() - 1)
		if self.direction == 's':
			return Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1)
		if self.direction == 'e':
			return Coordinate(self.position.get_x() + 1, self.position.get_y(), self.position.get_z())
		if self.direction == 'w':
			return Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z())
	
	def move_forward(self):
		if self.get_next_block_type() == 0: # if path is clear
			self.get_next_block_coordinate()
		
mc = Minecraft.create() # instantiate api
x, y, z = mc.player.getPos() # get initial position
mc.player.setPos(int(x+1), int(y), int(z)) # modify position to make way for the snake
print("player pos:\ne/w: {}\nn/s: {}\nalt: {}".format(x+1, z, y))

agent_smith = BlockAgent(Coordinate(x,y,z), 'n', mc) # instantiate agent
agent_smith.print_direction()
agent_smith.add_block(x,y,z) # print orientation
	
