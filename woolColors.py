from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blockState = 0

def getWoolState(color):

    if color == "Pink":
        blockState = 6
    elif color == "Black":
        blockState = 15
    elif color == "Blue":
        blockState = 11
    elif color == "Brown":
        blockState = 12
    elif color == "Cyan":
        blockState = 9
    elif color == "Gray":
        blockState = 7
    elif color == "Green":
        blockState = 13
    elif color == "Light Blue":
        blockState = 3
    elif color == "Light Grey":
        blockState = 8
    elif color == "Lime":
        blockState = 5
    elif color == "Magenta":
        blockState = 2
    elif color == "Orange":
        blockState = 1
    elif color == "Purple":
        blockState = 10
    elif color == "Red":
        blockState = 14
    elif color == "Yellow":
        blockState = 4
    else:
        blockState = 0
    return blockState

  
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)


    
