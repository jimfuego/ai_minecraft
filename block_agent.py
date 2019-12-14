from coordinate import Coordinate
from mcpi.minecraft import Minecraft
from collections import defaultdict
from random import randrange, shuffle
import random
import time
import math

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
        """
        renders agent at it's specified location
        """
        self.add_block(self.position)

    def print_direction(self):
        """
        prints the current facing direction of the agent
        """
        print(self.direction)

    def get_pos(self):
        """
        returns a coordinate object of agent's position
        """
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
        if coordinate is None:
            return False
        self.mc.setBlock(coordinate.get_x(), coordinate.get_y(), coordinate.get_z(), 0)
        return True
    
    def add_block(self, coordinate, block_type=1):
        """
        wrapper takes a coordinate and clears that place
        """
        bt = self.get_block_type(coordinate)
        if bt == 0:
            self.mc.setBlock(coordinate.get_x(), coordinate.get_y(), coordinate.get_z(), block_type)
        else:
            print("error setting block where type {} exists".format(bt))

    def move_agent(self, coordinate, block_type=1):
        """
        removes block from current location to parameterized location,
        and updates agent state
        """
        self.remove_block(self.position)
        self.update_pos(coordinate)
        self.add_block(coordinate, block_type)

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
        return None

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
        w = Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z())
        e = Coordinate(self.position.get_x() + 1, self.position.get_y(), self.position.get_z())
        empty_neighbors = set()
        if self.get_block_type(n) == 0:
            empty_neighbors.add(n)
        if self.get_block_type(s) == 0:
            empty_neighbors.add(s)
        if self.get_block_type(e) == 0:
            empty_neighbors.add(e)
        if self.get_block_type(w) == 0:
            empty_neighbors.add(w)
        return empty_neighbors
    
    def expand_ra(self):
        """
        uses agent position to expand the (n, s, e, w) nodes and returns
        the associated coordinate objects if the space is empty
        return:: the surrounding, traversible coordinates/nodes []
        """
        n = Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() - 1)
        s = Coordinate(self.position.get_x(), self.position.get_y(), self.position.get_z() + 1)
        w = Coordinate(self.position.get_x() - 1, self.position.get_y(), self.position.get_z())
        e = Coordinate(self.position.get_x() + 1, self.position.get_y(), self.position.get_z())
        #empty_neighbors = set()
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
            agent.remove_block(vertex)
            return True
        if vertex not in visited:  # if we have not visted this node yet
            visited.add(vertex)  # add this node to visited set
            neighbors = agent.expand()
            print("neighbors: {}".format(neighbors))
            stack.extend(neighbors - visited)  # add unvisited nodes stack
        time.sleep(.2)


def bfs(agent, goal):
    """
    breadth-first traversal
    """
    visited, q = set(), [agent.get_pos()]
    while q:
        vertex = q.pop(0)
        agent.move_agent(vertex)
        print("agent arrived at {}".format(vertex))
        if agent.get_pos() == goal:  # check for goal state
            print("GOAL REACHED")
            agent.remove_block(vertex)
            return True
        if vertex not in visited:  # if we have not visted this node yet
            visited.add(vertex)  # add this node to visited set
            neighbors = agent.expand()
            print("neighbors: {}".format(neighbors))
            q.extend(neighbors - visited)  # add unvisited nodes stack
        time.sleep(.2)


def a_star(agent, start, goal):
    """
    a-star algorithm for finding shortest path
    """

    def a_star_heuristic(node, start, goal):
        """calculates the distance (hypotenuse) between two 2D points"""
        if node is None or start is None or goal is None:
            return 0
        return \
            math.hypot(start.get_x() - node.get_x(), start.get_y() - node.get_y()) + \
            math.hypot(goal.get_x() - node.get_x(), goal.get_y() - node.get_y())

    def reconstruct_path(came_from, cur):
        """reconstructs the path found by a_star"""
        path = [cur]
        while cur in came_from:
            cur = came_from[cur]
            path.insert(0, cur)
        return path

    # init some guys
    frontier = set([start])
    came_from = {}
    g_scores = defaultdict(lambda: None, {start.__repr__(): 0})
    h_start = a_star_heuristic(start, start, goal)
    f_scores = defaultdict(lambda: None, {start.__repr__(): h_start})
    current = start
    while frontier:
        for node in frontier:  # get the node with the lowest f score
            c_f = a_star_heuristic(current, start, goal)
            n_f = a_star_heuristic(node, start, goal)
            if n_f <= c_f:
                current = current if node is None else node
        agent.move_agent(current)  # position agent
        if current == goal:
            agent.remove_block(current)
            return reconstruct_path(came_from, current)
        frontier.remove(current)
        for neighbor in agent.expand():
            temp_g = .5 + g_scores[current.__repr__()]  # 1 is a stand-in due to equal weights to neighbors
            neighbor_g = g_scores[neighbor.__repr__()]
            neighbor_g = 100 if neighbor_g is None else neighbor_g
            if temp_g <= neighbor_g:
                came_from[neighbor.__repr__()] = current
                g_scores[neighbor.__repr__()] = temp_g
                f_scores[neighbor.__repr__()] = g_scores[neighbor.__repr__()] + 1
                if neighbor not in frontier:
                    frontier.add(neighbor)
    print("Could not find shortest path!")
    agent.remove_block(start)
    return False  # failed to find shortest path


def hillclimb():
    """
    a literal hill-climbing algorithm for our agent
    """
    def random_hop(mc,n,s,l,a):
        """
        return a valid coordinate for a random hop
        """
        x = 8
        y = a
        z = randrange(n, s, 1)
        while True:
            if mc.getBlock(x,y,z) != 0:
                y += 1
            else:
                return Coordinate(x,y,z)
    
    def get_step_up(agent):
        """
        return a valid coordinate corresponding to the next step up (if any)
        """
        n = Coordinate(agent.position.get_x(), agent.position.get_y(), agent.position.get_z() - 1)
        s = Coordinate(agent.position.get_x(), agent.position.get_y(), agent.position.get_z() + 1) 
        nt = agent.get_block_type(n)
        st = agent.get_block_type(s)
        if nt + st == 0:  # local max found
            return None
        if agent.get_block_type(n) != 0:
            return Coordinate(agent.get_pos().get_x(), agent.get_pos().get_y() + 1, agent.get_pos().get_z() - 1)
        if agent.get_block_type(s) != 0:
            return Coordinate(agent.get_pos().get_x(), agent.get_pos().get_y() + 1, agent.get_pos().get_z() + 1) 
        
    north = 33
    south = 61
    lat = 7  
    alt = 10
    mc = Minecraft.create()
    start_point = random_hop(mc, north, south, lat, alt)
    print(start_point)
    agent = BlockAgent(start_point, 'n', mc)  # instantiate agent
    start_block = agent.get_block_type(start_point)
    max_y = 0
    running_max = None
    if start_block != 0:
        print("start point occupied by a block ID:{}".format(start_block))
        return False
    agent.render_agent()
    while True:  # keep walking until there are no more steps, then jump.
        time.sleep(1)
        next_step = get_step_up(agent)
        print(next_step)
        if next_step is None:
            agent.move_agent(random_hop(mc, north, south, lat, alt))
        else:
            agent.move_agent(next_step)
            if next_step.get_y() > max_y:  # reset max marker
                max_y = next_step.get_y()
                agent.remove_block(running_max)
                running_max = Coordinate(next_step.get_x() - 1, next_step.get_y(), next_step.get_z())
                agent.add_block(running_max)
        


def reactive_agent(start):
    """
    agent percepts and reacts to objects according to their
    block-type
    """
    def detect_ground(mc, node):
        return mc.getBlock(node.get_x(), node.get_y()-1, node.get_z())
        
    mc = Minecraft.create()
    agent = BlockAgent(start, 'n', mc)  # instantiate agent
    start_block = agent.get_block_type(start)  # starting point inside reaction zone!
    if start_block != 0:
        print("start point occupied by a block ID:{}".format(start_block))
        return False
    print("agent start pos DFS:\ne/w: {}\nn/s: {}\nalt: {}".format(start.get_x(), start.get_z(), start.get_y()))
    while True:  # main loop
        nodes = agent.expand_ra()
        node = random.choice(nodes)
        agent.move_agent(node, detect_ground(mc, node))
        time.sleep(.3)
        

def run_dfs(start, goal):
    # DFS
    mc = Minecraft.create()
    agent_smith = BlockAgent(start, 'n', mc)  # instantiate agent
    start_block = agent_smith.get_block_type(start)
    if start_block != 0:
        print("start point occupied by a block ID:{}".format(start_block))
        return False
    agent_smith.render_agent()
    print("agent start pos DFS:\ne/w: {}\nn/s: {}\nalt: {}".format(start.get_x(), start.get_z(), start.get_y()))
    dfs(agent_smith, goal)
    return True


def run_bfs(start, goal):
    # BFS
    mc = Minecraft.create()
    agent_smith = BlockAgent(start, 'n', mc)  # instantiate agent
    start_block = agent_smith.get_block_type(start)
    if start_block != 0:
        print("start point occupied by a block ID:{}".format(start_block))
        return False
    agent_smith.render_agent()
    print("agent start pos DFS:\ne/w: {}\nn/s: {}\nalt: {}".format(start.get_x(), start.get_z(), start.get_y()))
    bfs(agent_smith, goal)
    return True


def run_a_star(start, goal):
    mc = Minecraft.create()
    agent_smith = BlockAgent(start, 'n', mc)  # instantiate agent
    start_block = agent_smith.get_block_type(start)
    if start_block != 0:
        print("start point occupied by a block ID:{}".format(start_block))
        return False
    #agent_smith.render_agent()
    print("agent start pos A*:\ne/w: {}\nn/s: {}\nalt: {}".format(start.get_x(), start.get_z(), start.get_y()))
    a_star(agent_smith, start, goal)


maze_start = Coordinate(-13, 9, 56)  # starting point of our maze
maze_goal = Coordinate(-8, 9, 43)  # Goal point of our maze
react_start = Coordinate(-8, 9, 28)

# setup driver for this class test
#run_dfs(maze_start, maze_goal)
#run_bfs(maze_start, maze_goal)
#run_a_star(maze_start, maze_goal)
#hillclimb()
reactive_agent(react_start)
