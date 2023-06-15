from gdpc import Block as place
from gdpc import Editor
import maths


USE_BATCHING = True
editor = Editor()


def setBlock(block, xyz):
    x, y, z = xyz
    editor.placeBlock((x, y, z), place(block))


def getBlock(xyz):
    print("You used getBlock in a deprecated manner.")
    # x, y, z = xyz
    # return minecraft.getBlock(x, y, z)


def fillBlock(block, xyz):
    xDistance = max(xyz[0], xyz[3]) - min(xyz[0], xyz[3])
    yDistance = max(xyz[1], xyz[4]) - min(xyz[1], xyz[4])
    zDistance = max(xyz[2], xyz[5]) - min(xyz[2], xyz[5])

    for i in range(min(xyz[0], xyz[3], max(xyz[0], xyz[3]))):
        for j in range(min(xyz[1], xyz[4]), max(xyz[1], xyz[4])):
            for k in range(min(xyz[2], xyz[5]), max(xyz[2], xyz[5])):
                setBlock(block, (i, j, k))


def setLine(block, xyz0, xyz1, pixelPerfect=True):
    points = maths.line(xyz0, xyz1, pixelPerfect)
    for i in points:
        setBlock(block, (i[0], i[1], i[2]))


if __name__ == "__main__":
    print("Please run construct.py instead.")