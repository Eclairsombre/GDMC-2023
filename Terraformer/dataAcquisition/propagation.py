from gdpc import Editor, Block, geometry
import numpy as np
import math

from World import World


def propagate(coordinates, World):
    scanned = []
    if World.isInVolume(World, coordinates):
        Block = World.getBlockFromCoordinates(World, coordinates)
        World.getNeighbors(World, Block)
        for neighbor in Block.neighbors:
            if neighbor not in scanned:
                scanned.append(neighbor)
                propagate(neighbor.coodinates, World)

        

w = World()
print(len(w.volume))
w.setVolume()
print(w.volume[0][0][0].name)
print("done")

propagate(w.volume[0][0][0].coordinates, World)
print(w.volume[2][2][2].neighbors[0].coordinates)

