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
        """renders agent at it's specified location"""
        self.add_block(self.position)

    def print_direction(self):
        """
        prints the current facing direction of the agent
        """
        print(self.direction)

    def get_pos(self):
        """returns a coordinate object of agent's position"""
        return self.position

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

    def move_agent(self, coordinate):
        """
        removes block from current location to parameterized location,
        and updates agent state
        """
        self.remove_block(self.position)
        self.update_pos(coordinate)
        self.add_block(coordinate)

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
        print("current coordinate: ({}, {}, {})".format(self.position.get_x(),
                                                        self.position.get_y(),
                                                        self.position.get_z()))
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

    def expand(self):
        """
        uses agent position to expand the (n, s, e, w) nodes and returns
        the associated coordinate objects if the space is empty
        return:: the surrounding, traversible coordinates/nodes []
        """
        n = Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() - 1)
        s = Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1)
        e = Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z())
        w = Coordinate(self.position.get_x() + 1, self.position.get_y(), self.position.get_z())
        empty_neighbors = []
        if self.get_block_type(n) == 0:
            empty_neighbors.append(n)
        if self.get_block_type(s) == 0:
            empty_neighbors.append(s)
        if self.get_block_type(e) == 0:
            empty_neighbors.append(e)
        if self.get_block_type(w) == 0:
            empty_neighbors.append(w)
        return empty_neighbors


def dfs(agent, goal):
    """
    depth-first traversal
    """
    visited, stack = set(), [agent.get_pos()]
    while stack:  # while there are nodes to visit
        vertex = stack.pop()  # get vertex (Coordinate)
        agent.move_agent(vertex)
        print("agent arrived at {}".format(vertex))
        if agent.get_pos() == goal:  # check for goal state
            print("GOAL REACHED")
            return True
        if vertex not in visited:  # if we have not visted this node yet
            visited.add(vertex)  # add this node to visited set
            stack.extend(agent.expand() - visited)  # add unvisited nodes stack


def bfs(agent, goal):
    """
    breadth-first traversal
    """


def a_star(agent, goal):
    """
    a-star algorithm for finding shortest path
    """
    start_point = Coordinate(12, 9, 56)  # starting point of our maze
    end_point = Coordinate(7, 9, 43)


def hillclimb(agent):
    """
    a literal hill-climbing algorithm for our agent
    """
    max_north = 34
    min_south = 61
    min_height = 10
    x = 8


def reactive_agent():
    """
    agent percepts and reacts to objects according to their
    block-type
    """
    start_point = Coordinate(7, 9, 28)  # starting point inside reaction zone!


def run_dfs():
    # DFS
    start = Coordinate(12, 9, 56)  # starting point of our maze
    goal = Coordinate(7, 9, 43)  # Goal point of our maze
    mc = Minecraft.create()
    agent_smith = BlockAgent(start, 'n', mc)  # instantiate agent
    agent_smith.render_agent()
    print("agent start pos DFS:\ne/w: {}\nn/s: {}\nalt: {}".format(start.get_x(), start.get_z(), start.get_y()))
    dfs(agent_smith, goal)


def run_bfs():
    # BFS
    start = Coordinate(12, 9, 56)  # starting point of our maze
    goal = Coordinate(7, 9, 43)  # Goal point of our maze
    mc = Minecraft.create()
    agent_smith = BlockAgent(start, 'n', mc)  # instantiate agent
    agent_smith.render_agent()
    print("agent start pos DFS:\ne/w: {}\nn/s: {}\nalt: {}".format(start.get_x(), start.get_z(), start.get_y()))


# setup driver for this class test
run_dfs()
