from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'insidehouse': (72, 11, 88), 'ontophouse' : (72, 14, 88.2)}

choice = ''
while choice != 'exit':
    choice = input('Enter a location ("exit" to close): ')
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)
