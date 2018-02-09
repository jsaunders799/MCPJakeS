from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def setMelon(x, y, z):
    mc.setBlock(x, y , z, 103)
    time.sleep(10)

setMelon (x + 2, y, z)
setMelon (x, y, z + 2)
setMelon (x + 2, y, z + 2)


