from gdpc import Editor, Block, geometry
import numpy as np
import math

def surfaceNormal(coordinates:tuple, neighbors:list):
    """Calculate the normal vector of a surface

    Args:
        coordinates (tuple): tuple of 3d coordinates
        neighbors (list): list of tuple of 3d coordinates, minimum two coordinates

    Returns:
        list: components of the normal vector
    """
    normal_average = [0, 0, 0]
    length = len(neighbors)-1
    for i in range(length):
        vector_1 = np.array(neighbors[i].coordinates) - np.array(coordinates)
        vector_2 = np.array(neighbors[i+1].coordinates) - np.array(coordinates)

        normal = np.cross(vector_1, vector_2)

        if normal[0] != 0:
            normal_average[0] += 1
            normal_average[1] += normal[1] / normal[0]
            normal_average[2] += normal[2] / normal[0]

        elif normal[1] != 0:
            normal_average[0] += normal[0] / normal[1]
            normal_average[1] += normal[1] / normal[1]
            normal_average[2] += normal[2] / normal[1]

        elif normal[2] != 0:
            normal_average[0] += normal[0] / normal[2]
            normal_average[1] += normal[1] / normal[2]
            normal_average[2] += normal[2] / normal[2]
        else:
            normal_average[0] += normal[0]
            normal_average[1] += normal[1]
            normal_average[2] += normal[2]

    if length != 0:
        normal_average[0] /= length
        normal_average[1] /= length
        normal_average[2] /= length

        return normal_average

def surfaceNormal2(coordinates:tuple, neighbors:list):
    """Calculate the normal vector of a surface

    Args:
        coordinates (tuple): tuple of 3d coordinates
        neighbors (list): list of tuple of 3d coordinates, minimum two coordinates

    Returns:
        list: components of the normal vector
    """
    normal_average = [0, 0, 0]
    length = len(neighbors)-1
    for i in range(length):
        vector_1 = np.array(neighbors[i]) - np.array(coordinates)
        vector_2 = np.array(neighbors[i+1]) - np.array(coordinates)

        normal = np.cross(vector_1, vector_2)

        if normal[0] != 0:
            normal_average[0] += 1
            normal_average[1] += normal[1] / normal[0]
            normal_average[2] += normal[2] / normal[0]

        elif normal[1] != 0:
            normal_average[0] += normal[0] / normal[1]
            normal_average[1] += normal[1] / normal[1]
            normal_average[2] += normal[2] / normal[1]

        elif normal[2] != 0:
            normal_average[0] += normal[0] / normal[2]
            normal_average[1] += normal[1] / normal[2]
            normal_average[2] += normal[2] / normal[2]
        else:
            normal_average[0] += normal[0]
            normal_average[1] += normal[1]
            normal_average[2] += normal[2]

    if length != 0:
        normal_average[0] /= length
        normal_average[1] /= length
        normal_average[2] /= length

        return normal_average

def unitVector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angleBetween(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'"""
    v1_u = unitVector(v1)
    v2_u = unitVector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def slope(v1:tuple, vertical=(0, -1, 0)):
    return angleBetween(v1, vertical)

class Point:
    def __init__(self, coordinates:tuple, block:str):
        self.coordinates = coordinates
        self.block = block
        self.slope = None 
        self.neighbors = []

    def getSlope(self, neighbors:list):
        if (len(neighbors) > 1 ):
            self.slope = slope(surfaceNormal(self.coordinates, neighbors))
            
    

class Volume:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def remove_point(self, point):
        self.points.remove(point)

    def get_points(self):
        return self.points


editor = Editor(buffering=True)

# Get a block
editor.getBlock((1997, 72, 674))

# Place a block
#editor.placeBlock((1621,93,650), Block("stone"))


ED = Editor(buffering=True)

# Here we read start and end coordinates of our build area
BUILD_AREA = ED.getBuildArea()  # BUILDAREA
STARTX, STARTY, STARTZ = BUILD_AREA.begin
LASTX, LASTY, LASTZ = BUILD_AREA.last

WORLDSLICE = ED.loadWorldSlice(BUILD_AREA.toRect(), cache=True)  # this takes a while

#print(WORLDSLICE.getBlockGlobal((1997, 72, 674)))

def basicScan(coordinates_1:tuple, coordinates_2:tuple):

    coordinates_min = [min(coordinates_1[i], coordinates_2[i]) for i in range(3)]
    coordinates_max = [max(coordinates_1[i], coordinates_2[i]) for i in range(3)]   

    length_x = coordinates_max[0] - coordinates_min[0] + 1
    length_y = coordinates_max[1] - coordinates_min[1] + 1
    length_z = coordinates_max[2] - coordinates_min[2] + 1

    volume = [[[None for _ in range(length_x)] for _ in range(length_y)] for _ in range(length_z)]
    i = 0
    for x in range(coordinates_min[0], coordinates_max[0]+1):
        j = 0
        for y in range(coordinates_min[1], coordinates_max[1]+1):
            k = 0
            for z in range(coordinates_min[2], coordinates_max[2]+1):
                volume[i][j][k] = Point((x, y, z), editor.getBlock((x, y, z)))
                k += 1
            j += 1
        i += 1

    return volume

def calculateSlope(volume):
    for i in range(len(volume)):
        for j in range(len(volume[i])):
            for k in range(len(volume[i][j])):
                volume[i][j][k].neighbors = [volume[l][m][n] for n in range(max(0, k-1), min(k+2, len(volume[i][j]))) for m in range(max(0, j-1), min(j+2, len(volume[i]))) for l in range(max(0, i-1), min(i+2, len(volume))) if (str(volume[l][m][n].block) != "minecraft:air" and volume[l][m][n] != volume[i][j][k])]
                print([volume[l][m][n].coordinates for n in range(max(0, k-1), min(k+2, len(volume[i][j]))) for m in range(max(0, j-1), min(j+2, len(volume[i]))) for l in range(max(0, i-1), min(i+2, len(volume))) if (str(volume[l][m][n].block) != "minecraft:air" and volume[l][m][n] != volume[i][j][k])])
                volume[i][j][k].slope = volume[i][j][k].getSlope(volume[i][j][k].neighbors)
    return volume

volume = basicScan((2009, 79, 676), (2011, 81, 678))

print("hel")
volume = calculateSlope(volume)
print(volume[1][1][1].slope)
print("hel")

l = [(2009, 81, 676), (2010, 81, 676), (2011, 81, 676), (2009, 80, 677), (2011, 80, 677), (2009, 79, 678), (2010, 79, 678), (2011, 79, 678)]

print(slope(surfaceNormal2((2010, 80, 677), l)))