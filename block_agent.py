from coordinate import Coordinate
from mcpi.minecraft import Minecraft
import time


class BlockAgent:
	def __init__(self, coordinate, direction, mc):
		"""
		set position and direction of the agent
		coordinate::Coordinate
		direction::chr(n,s,e,w)
		mc::Minecraft
		"""
		self.position = coordinate
		self.direction = direction
		self.mc = mc

	def render_agent(self):
		self.add_block(self.position)

	def print_direction(self):
		"""
		prints the current facing direction of the agent
		"""
		print(self.direction)

	def update_pos(self, coordinate):
		"""
		updates agent grid position
		"""
		self.position = coordinate

	def remove_block(self, coordinate):
		"""
		wrapper takes a coordinate and clears that place
		"""
		self.mc.setBlock(coordinate.get_x(), coordinate.get_y(), coordinate.get_z(), 0)

	def add_block(self, coordinate):
		"""
		wrapper takes a coordinate and clears that place
		"""
		self.mc.setBlock(coordinate.get_x(), coordinate.get_y(), coordinate.get_z(), 1)

	def get_next_block_type(self):
		"""
		reads direction from the agent state to return next
		block-type in path
		"""
		if self.direction == 'n':
			return self.mc.getBlock(x, y, z - 1)
		elif self.direction == 's':
			return self.mc.getBlock(x, y, z + 1)
		elif self.direction == 'e':
			return self.mc.getBlock(x + 1, y, z)
		elif self.direction == 'w':
			return self.mc.getBlock(x - 1, y, z)
		else:
			print("error: can't get_next_block_type")
			
	def get_block_type(self, c):
		"""
		gets the block type given a coordinate
		"""
		return self.mc.getBlock(int(c.get_x()), int(c.get_y()), int(c.get_z()))
		

	def get_next_block_coordinate(self):
		"""
		reads direction from the agent state to return a coordinate for the next step
		"""
		if self.direction == 'n':
			return Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() - 1)
		if self.direction == 's':
			return Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1)
		if self.direction == 'e':
			return Coordinate(self.position.get_x() + 1, self.position.get_y(), self.position.get_z())
		if self.direction == 'w':
			return Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z())

	def move_forward(self):
		"""
		moves the block agent forward by one space according to its
		direction and current positio
		"""
		# get new block coordinate
		new_block = self.get_next_block_coordinate()
		new_block_type = self.get_block_type(new_block)
		print('---------------------------------')
		print("BEGIN MOVE")
		print("direction: {}".format(self.direction))
		print("next block type: {}".format(new_block_type))
		print("current coordinate: ({}, {}, {})".format(self.position.get_x(), self.position.get_y(), self.position.get_z()))
		print("next coordinate: ({}, {}, {})".format(new_block.get_x(), new_block.get_y(), new_block.get_z()))
		
		# render one step
		if new_block_type == 0:  # if path is clear
			# remove old block
			print("removing old block: ({}, {}, {})".format(self.position.get_x(), self.position.get_y(),
															self.position.get_z()))
			self.remove_block(self.position)
			# set new block
			print("setting new block: ({}, {}, {})".format(new_block.get_x(), new_block.get_y(), new_block.get_z()))
			self.add_block(new_block)
			print('updating agent position to: ({}, {}, {})'.format(new_block.get_x(), new_block.get_y(),
																	new_block.get_z()))
			self.update_pos(new_block)
			print('---------------------------------')
		else:
			print("***COLLISION DETECTED***")

	def get_distance(self, coordinate):
		"""
		returns agent's distance from the given coordinate
		"""

	def expand(self):
		"""
		uses agent position to expand the (forward, left, right) nodes
		and returns the associated coordinate objects
		return:: 3 Coordinates corresponding to front.left,right nodes
		"""
		if self.direction == 'n': # return e,n,w
			return 
			Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1)),
			Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() - 1)),
			Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z())
		if self.direction == 's':# return w,s,e
			return
			Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z()),
			Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1)),
			Coordinate(self.position.get_x() + 1, self.position.get_y(), self.position.get_z())
		if self.direction == 'e':# return n,e,s
			return
			Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() - 1)),
			Coordinate(self.position.get_x() + 1, self.position.get_y(), self.position.get_z()),
			Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1))
		if self.direction == 'w':# return s,w,n
			return
			Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1)),
			Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z()),
			Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() - 1))

	def dfs(self, goal):
		"""
		depth-first traversal
		"""
		

	def bfs(self, goal):
		"""
		breadth-first traversal
		"""

	def a_star(self, goal):
		"""
		a-star algorithm for finding shortest path
		"""

	def hillclimb(self):
		"""
		a literal hill-climbing algorithm for our agent
		"""

	def reactive_agent(self):
		"""
		agent percepts and reacts to objects according to their
		block-type
		"""


# setup driver for this class test
mc = Minecraft.create()  # instantiate api
x, y, z = mc.player.getPos()  # get initial position
ax, ay, az = int(x), int(y), int(z)  # get coordinate for agent
mc.player.setPos(int(x), int(y), int(z + 4))  # modify position to make way for the snake
print("agent start pos:\ne/w: {}\nn/s: {}\nalt: {}".format(x, z, y))
agent_smith = BlockAgent(Coordinate(ax, ay, az), 'n', mc)  # instantiate agent
agent_smith.render_agent()

# demonstrate crawl
time.sleep(1)
print("begin crawl")
for i in range(10):
	agent_smith.move_forward()
	time.sleep(.3)
