from gdpc import Editor, Block, geometry
import numpy as np
import math

class Block:
    def __init__(self, coordinates:tuple, name:str):
        self.coordinates = coordinates
        self.name = name
        self.neighbors = []
        self.surface = None


    def addNeighbors(self, neighbors:list[Block]):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)

    def isSurface(self):
        if str(self.name) != 'minecraft:air':
            for neighbor in self.neighbors:
                if str(neighbor.name) == 'minecraft:air':
                    self.surface = True
                    break
            if len(neighbor) != 0:
                self.surface = False

from gdpc.lookup import *

print(AIRS, FIRES, FLOWERS, GRASS_PLANTS, CROPS, SAPLINGS, FOLIAGE, )