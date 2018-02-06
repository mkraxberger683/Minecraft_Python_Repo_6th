from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 24
height = 10
levels = range(height)

pos = mc.player.getTilePos()
x, y, z = pos.x + height, pos.y, pos.z

for level in reversed(levels):
    mc.setBlocks(x - level, y, z - level, x + level, y, z + level, block)
    y += 1
