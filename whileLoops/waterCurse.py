from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
count = 0
while count <= 100:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 38)
    time.sleep(.2)
