from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

blocktype = [57, 43, 68, 94, 102]
block = random.choice(blocktype)

mc.setBlock(x - 1, y, z, blocktype)
