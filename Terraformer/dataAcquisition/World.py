from gdpc import Editor, Block, geometry
import numpy as np
import math

from Block import Block

class World:
    def __init__(self, buildArea=None):

        if buildArea == None:
            editor = Editor(buffering=True)
            buildArea = editor.getBuildArea()

        self.coordinates_min = [min(buildArea.begin[i], buildArea.last[i]) for i in range(3)]
        self.coordinates_max = [max(buildArea.begin[i], buildArea.last[i]) for i in range(3)]   

        self.length_x = self.coordinates_max[0] - self.coordinates_min[0] +1
        self.length_y = self.coordinates_max[1] - self.coordinates_min[1] +1
        self.length_z = self.coordinates_max[2] - self.coordinates_min[2] +1

        self.volume = [[[None for _ in range(self.length_z)] for _ in range(self.length_y)] for _ in range(self.length_x)]
        

    def isInVolume(self, coordinates):
        if (self.coordinates_min[0] <= coordinates[0] <= self.coordinates_max[0] and 
        self.coordinates_min[1] <= coordinates[1] <= self.coordinates_max[1] and 
        self.coordinates_min[2] <= coordinates[2] <= self.coordinates_max[2]):
            return True
        return False

    def addBlocks(self, blocks:list[Block]):
        for block in blocks:
            if self.isInVolume(block.coordinates):
                self.volume[block.coordinates[0] - self.coordinates_min[0]][block.coordinates[1] - self.coordinates_min[1]][block.coordinates[2] - self.coordinates_min[2]] = block
            else:
                raise "Block not in volume"

    def getBlockFromCoordinates(self, coordinates):
            return self.volume[coordinates[0] - self.coordinates_min[0]][coordinates[1] - self.coordinates_min[1]][coordinates[2] - self.coordinates_min[2]]


    def getNeighbors(self, Block):
        for i in range(-1, 2):
            if i != 0:
                coordinates = (Block.coordinates[0]+i, Block.coordinates[1], Block.coordinates[2])
                if self.isInVolume(coordinates):
                    Block.addNeighbors([self.getBlockFromCoordinates(coordinates)])
        
        for j in range(-1, 2):
            if j != 0:
                coordinates = (Block.coordinates[0], Block.coordinates[1]+j, Block.coordinates[2])
                if self.isInVolume(coordinates):
                    Block.addNeighbors([self.getBlockFromCoordinates(coordinates)])
        
        for k in range(-1, 2):
            if k != 0:
                coordinates = (Block.coordinates[0], Block.coordinates[1], Block.coordinates[2]+k)
                if self.isInVolume(coordinates):
                    Block.addNeighbors([self.getBlockFromCoordinates(coordinates)])


    def setVolume(self):
        editor = Editor(buffering=True)

        for x in range(self.coordinates_min[0], self.coordinates_max[0]+1):
            for y in range(self.coordinates_min[1], self.coordinates_max[1]+1):
                for z in range(self.coordinates_min[2], self.coordinates_max[2]+1):
                    #self.volume[i][j][k] = Block((x, y, z), editor.getBlock((x, y, z)))
                    print(x, y, z)
                    self.addBlocks([Block((x, y, z), editor.getBlock((x, y, z)))])

    def propagate(self, coordinates, scanned=[]):
        if self.isInVolume(coordinates):
            Block = self.getBlockFromCoordinates(coordinates)
            self.getNeighbors(Block)
            for neighbor in Block.neighbors:
                if neighbor not in scanned:
                    scanned.append(neighbor)
                    if str(neighbor.name) != 'minecraft:air':
                        self.propagate(neighbor.coordinates, scanned)

w = World()
print(len(w.volume))
w.setVolume()
print(w.volume[0][0][0].name)
print("done")

w.propagate(w.volume[0][0][0].coordinates)

for i in range(0, 6):
    print(w.volume[1][1][1].neighbors[i].name)