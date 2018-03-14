from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random


def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

brokenWall = []
height, width = 5, 10  

for i in range(height):
    for j in range(width):
        mc.setBlock(x, y, z, brokenBlock())
        x += 1
    y += 1
    x = pos.x
        
