# this code is unfinished. feel free to submit a pull request :)
from mcpi.minecraft import Minecraft
import time
        
class Snake:
    def __init__(head, direction, mc, block_type=1, length=5):
        directions = set(['n','s','e','w'])
        # check for proper params, set features
        if direction in directions:
            self.head = head # head Coordinate of snake
            self.direction = direction # initial direction
            self.block_type = block_type # body type
            self.body = [] # length of snake
            self.mc = mc # minecraft api
            
            # create snake body
            x = head.x
            y = head.y
            z = head.z
            for i in range(length):
                self.body.append(Coordinate(x,y,z))
                self.mc.setBlock(x, y, z, 1)
                x -= 1 if direction == 'e' else x
                x += 1 if direction == 'w' else x
                z += 1 if direction == 'n' else z
                z -= 1 if direction == 's' else z
        else:
            print("choose a direction n, s, e, or w")
            return None
     
# (x = east/west) (y = altitude) (z = north/south)
# get position
mc = Minecraft.create() # instantiate api
x, y, z = mc.player.getPos() # get initial position
mc.player.setPos(int(x+1), int(y), int(z)) # modify position to make way for the snake
print("player pos:\ne/w: {}\nn/s: {}\nalt: {}".format(x+1, z, y))

# make the snake
head = Coordinate(x,y,z) # head of the snake
direction = 'n' # facing this direction

snake = Snake(head, direction, mc) # make the snake

# run = True
# 
# i = 0
# while run:
#     next_block = mc.getBlock(x, y, z-i)
#     if next_block > 0:
#         print("snake hit wall {}".format(next_block))
#         run = False
#     else:
#         mc.setBlock(x, y, z - i, 1)
#         print("snake at ({}, {}, {})".format(x, y, z-i))
#     time.sleep(.2)
#     i += 1
