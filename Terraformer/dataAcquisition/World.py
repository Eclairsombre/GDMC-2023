from gdpc import Editor, geometry
from gdpc import Block as place
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

    def getBlockFromCoordinates(self, coordinates):
            editor = Editor(buffering=True)
            if self.volume[coordinates[0] - self.coordinates_min[0]][coordinates[1] - self.coordinates_min[1]][coordinates[2] - self.coordinates_min[2]] == None:
                self.volume[coordinates[0] - self.coordinates_min[0]][coordinates[1] - self.coordinates_min[1]][coordinates[2] - self.coordinates_min[2]] = Block((coordinates[0], coordinates[1], coordinates[2]), editor.getBlock((coordinates[0], coordinates[1], coordinates[2])).id)
            
            return self.volume[coordinates[0] - self.coordinates_min[0]][coordinates[1] - self.coordinates_min[1]][coordinates[2] - self.coordinates_min[2]]


    def getNeighbors(self, Block):
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if not (i == 0 and j == 0 and k == 0):
                        coordinates = (Block.coordinates[0]+i, Block.coordinates[1]+j, Block.coordinates[2]+k)
                        if self.isInVolume(coordinates):
                            Block.addNeighbors([self.getBlockFromCoordinates(coordinates)])
        
        # for j in range(-1, 2):
        #     if j != 0:
        #         coordinates = (Block.coordinates[0], Block.coordinates[1]+j, Block.coordinates[2])
        #         if self.isInVolume(coordinates):
        #             Block.addNeighbors([self.getBlockFromCoordinates(coordinates)])
        
        # for k in range(-1, 2):
        #     if k != 0:
        #         coordinates = (Block.coordinates[0], Block.coordinates[1], Block.coordinates[2]+k)
        #         if self.isInVolume(coordinates):
        #             Block.addNeighbors([self.getBlockFromCoordinates(coordinates)])


    def setVolume(self):
        editor = Editor(buffering=True)

        for x in range(self.coordinates_min[0], self.coordinates_max[0]+1):
            for y in range(self.coordinates_min[1], self.coordinates_max[1]+1):
                for z in range(self.coordinates_min[2], self.coordinates_max[2]+1):
                    #self.volume[i][j][k] = Block((x, y, z), editor.getBlock((x, y, z)))
                    print(x, y, z)
                    self.addBlocks([Block((x, y, z), editor.getBlock((x, y, z)).id)])

    def propagate(self, coordinates, scanned=[]):
        i = 0
        editor = Editor(buffering=True)
        if self.isInVolume(coordinates):
            Block = self.getBlockFromCoordinates(coordinates)
            self.getNeighbors(Block)
            for neighbor in Block.neighbors:
                if neighbor not in scanned:
                    scanned.append(neighbor)
                    self.getNeighbors(neighbor)
                    if neighbor.isSurface():
                        editor.placeBlock(neighbor.coordinates, place("minecraft:glass"))
                        print(neighbor.coordinates)
                        self.propagate(neighbor.coordinates, scanned)
    
    def binaryImage(self):
        binaryImage = []
        for x in range(self.length_x):
            binaryImage.append([])
            for y in range(self.length_y):
                binaryImage[x].append([])
                for z in range(self.length_z):
                    if (self.volume[x][y][z] != None):
                        binaryImage[x][y].append(True)
                    else:
                        binaryImage[x][y].append(False)

        return np.array(binaryImage)

                        

# w = World()
# editor = Editor(buffering=False)

# import sys
# sys.setrecursionlimit(w.length_x * w.length_y * w.length_z)

# w.propagate((2047, 70, 612))
# print("done")
# print(w.binaryImage())