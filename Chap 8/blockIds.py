from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    return 103
def water():
    return 9
def lava():
    return 11
def tnt():
    return 46
def flower():
    return 175
def diamondBlock():
    return 57

block = melon()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)


