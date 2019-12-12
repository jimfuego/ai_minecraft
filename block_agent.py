from coordinate import Coordinate
from mcpi.minecraft import Minecraft
import time

class BlockAgent:
	def __init__(self, coordinate, direction, mc):
		'''
		set position and direction of the agent
		coordinate::Coordinate
		direction::chr(n,s,e,w)
		mc::Minecraft
		'''
		self.position = coordinate
		self.direction = direction
		self.mc = mc
		self.inject_agent()
		
	def inject_agent(self):
		self.add_block(self.position)
		
	def print_direction(self):
		'''prints the current facing direction of the agent'''
		print(self.direction)
		
	def update_pos(self, coordinate):
		'''updates agent grid position'''
		self.position = coordinate
		
	def remove_block(self,coordinate):
		'''
		wrapper takes a coordinate and clears that place
		'''
		self.mc.setBlock(coordinate.get_x(), coordinate.get_y(), coordinate.get_z(), 0)
	
	def add_block(self, coordinate):
		'''
		wrapper takes a coordinate and clears that place
		'''
		self.mc.setBlock(coordinate.get_x(), coordinate.get_y(), coordinate.get_z(), 1)
	
	def get_next_block_type(self):
		'''
		reads direction from the agent state to return next 
		block-type in path
		'''
		if self.direction == 'n':
			return self.mc.getBlock(x, y, z - 1)
		if self.direction == 's':
			return self.mc.getBlock(x, y, z + 1)
		if self.direction == 'e':
			return self.mc.getBlock(x + 1, y, z) 
		if self.direction == 'w':
			return self.mc.getBlock(x - 1, y, z)
		
	def get_next_block_coordinate(self):
		'''
		reads direction from the agent state to return a coordinate for the next step
		'''
		if self.direction == 'n':
			return Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() - 1)
		if self.direction == 's':
			return Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1)
		if self.direction == 'e':
			return Coordinate(self.position.get_x() + 1, self.position.get_y(), self.position.get_z())
		if self.direction == 'w':
			return Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z())
	
	def move_forward(self):
		'''
		moves the block agent forward by one space according to its 
		direction and current position
		'''
		#if path is clear
		print("direction: {}".format(self.direction))
		print("next block type: {}".format(self.get_next_block_type()))
		# get new block coordinate
		new_block = self.get_next_block_coordinate()
		print("current coordinate: ({}, {}, {})".format(self.position.get_x(),self.position.get_y(),self.position.get_z()))
		print("next coordinate: ({}, {}, {})".format(new_block.get_x(),new_block.get_y(),new_block.get_z()))
		if self.get_next_block_type() == 0: # if path is clear
			print('---------------------------------')
			# remove old block
			print("removing old block: ({}, {}, {})".format(self.position.get_x(),self.position.get_y(),self.position.get_z()))
			self.remove_block(self.position)
			# set new block
			print("setting new block: ({}, {}, {})".format(new_block.get_x(),new_block.get_y(),new_block.get_z()))
			self.add_block(new_block)
			print('updating agent position to: ({}, {}, {})'.format(new_block.get_x(),new_block.get_y(),new_block.get_z()))
			self.update_pos(new_block)
			print('---------------------------------')
		
 	def get_distance(coordinate):
		'''
		returns agent's distance from the given coordinate
		'''
	
	def expand():
		'''
		uses agent position to expand the (forward, left, right) nodes
		and returns the associated coordinate objects
		'''

	def dfs():
		'''
		depth-first traversal
		'''
		
	def bfs():
		'''
		breadth-first traversal
		'''
		
	def a_star():
		'''
		a-star algorithm for finding shortest path
		'''
		
	def hill-climb():
		'''
		a literal hill-climbing algorithm for our agent
		'''
		
	def reactive agent():
		'''
		agent percepts and reacts to objects according to their
		block-type
		'''		
		
# setup driver for this class test
mc = Minecraft.create() # instantiate api
x, y, z = mc.player.getPos() # get initial position
ax,ay,az = int(x), int(y), int(z) # get coordinate for agent
mc.player.setPos(int(x), int(y), int(z+4)) # modify position to make way for the snake
print("agent start pos:\ne/w: {}\nn/s: {}\nalt: {}".format(x, z, y))
agent_smith = BlockAgent(Coordinate(ax,ay,az), 'n', mc) # instantiate agent
agent_smith.inject_agent()

# demonstrate crawl
time.sleep(1)
print("begin crawl")
for i in range(10):
	agent_smith.move_forward()
	time.sleep(.3)
	
