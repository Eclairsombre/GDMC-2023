from gdpc import Block as place

import sys
sys.path.append("Terraformer/mapAnalysis/")
import Skeleton 

from gdpc import Editor

from math import sqrt

import roads

def get_distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)

def simplify_coordinates(coordinates, epsilon):
    if len(coordinates) < 3:
        return coordinates

    # Find the point with the maximum distance
    max_distance = 0
    max_index = 0
    end_index = len(coordinates) - 1

    for i in range(1, end_index):
        distance = get_distance(coordinates[i], coordinates[0])
        if distance > max_distance:
            max_distance = distance
            max_index = i

    simplified_coordinates = []

    # If the maximum distance is greater than epsilon, recursively simplify
    if max_distance > epsilon:
        rec_results1 = simplify_coordinates(coordinates[:max_index+1], epsilon)
        rec_results2 = simplify_coordinates(coordinates[max_index:], epsilon)

        # Combine the simplified sub-results
        simplified_coordinates.extend(rec_results1[:-1])
        simplified_coordinates.extend(rec_results2)
    else:
        # The maximum distance is less than epsilon, retain the endpoints
        simplified_coordinates.append(coordinates[0])
        simplified_coordinates.append(coordinates[end_index])

    return simplified_coordinates


def irlToMc(coordinates):

    print(coordinates, "coordinates")
    editor = Editor()
    buildArea = editor.getBuildArea()
    xMin = (editor.getBuildArea().begin).x
    yMin = (editor.getBuildArea().begin).y
    zMin = (editor.getBuildArea().begin).z

    print(xMin, yMin, zMin)

    coordinates_final = []

    coordinates_final.append(coordinates[0] + xMin)
    coordinates_final.append(coordinates[1] + yMin)
    coordinates_final.append(coordinates[2] + zMin)

    print(coordinates_final)

    return coordinates_final

def setRoads(skeleton):
    # Generation
    for i in range(len(skeleton.lines)):
        for j in range(len(skeleton.lines[i])):
            xyz = irlToMc(skeleton.coordinates[skeleton.lines[i][j]])
            skeleton.lines[i][j] = xyz
            print(skeleton.lines[i][j], "eee")

    # Simplification

    for i in range(len(skeleton.lines)):
        skeleton.lines[i] = simplify_coordinates(skeleton.lines[i], 10)


    for i in range(len(skeleton.lines)):  # HERE --------------------------------------
        print(skeleton.lines[i])
        road = roads.RoadCurve(roads.standard_modern_lane_agencement, skeleton.lines[i])
        road.setLanes()
        print(road.getLanes(), "LANES ***********")


# ### Execution ###


# from skimage.data import binary_blobs
# blobs = binary_blobs(16, volume_fraction=0.3, n_dim=3)

# # # # # # #

import sys
sys.path.append("Terraformer/dataAcquisition/")
import World

w = World.World()

import sys
sys.setrecursionlimit(w.length_x * w.length_y * w.length_z)

w.propagate((1671, 64, 622))
print("done")
print(w.binaryImage())

# # # # # #

skel = Skeleton.Skeleton()

skel.setSkeleton(w.binaryImage())

skel.parseGraph()
print(skel.centers)
print(skel.lines)
print(skel.intersections)
print(skel.coordinates)

setRoads(skel)

Skeleton.heightmap()