from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'place1': (-30.0, 1.0, -10.0), 'place2': (0.0, 30.0, 6.0), 'place3': (-50.0, 4.0, 75.0)}

choice = ""

while choice != 'exit':
    choice = input('Enter a location("exit" to close): ')
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)
