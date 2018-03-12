from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

totdepth = 50

for i in range(totdepth):
    block = mc.getBlock(x, y - i, z)
    if block == 56:
        mc.postToChat("A diamond ore is " + str(i) + " blocks below you.")
        break
else:
    mc.postToChat("There are no diamond ore blocks below you")
